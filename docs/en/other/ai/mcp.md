# 是什么:
deepseek给的:

>**A stateful, context-aware orchestration framework** that optimizes interactions between users, LLMs, and external tools while balancing token limits, accuracy, and safety.

似乎是ReAct的高级版本?但却是在协议层动手脚,可以当做是一个stateful HTTP+function calling + 全局调控

# 创建简易的mcp server

## 1.装uv
如果要curl或者wget看官方给的url
```cmd
pip install uv
```

## 2.新建项目:
```cmd
uv init <name>
cd <name>
```

## 3.虚拟环境
(也许可以直接用conda,但算了,保持一致)
```cmd
uv venv
# uv venv --python 3.12
```
虚拟环境的文件在当前项目的根目录下.venv文件夹,ls -a就能看到
```cmd
# 激活
source .venv/Scripts/activate

# or, windows

.venv/Scripts/activate
```

## 4.装库:
```cmd
uv add "mcp[cli]"
```

## 5.随便写个server
根目录下创建一个python文件,比如touch server.py
```python
# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```
在这个示例里面,创建了一个tool和一个resource

主要语法:
### tool类:
写一个函数,在上面加上mcp.tool修饰,就是注册了一个tool,mcp server会自动读取参数,然后在访问模型的时候传递给模型

官方示例:

```python
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")

@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters"""
    return weight_kg / (height_m**2)

@mcp.tool()
async def fetch_weather(city: str) -> str:
    """Fetch current weather for a city"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.weather.com/{city}")
        return response.text
```

### resource类:

类似http的get请求,决定数据最终以什么样子被传入模型,多数情况下不应该有副作用或者耗时很长(sql?)

TODO: 查明resource参数

```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("My App")

@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"


@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Dynamic user data"""
    return f"Profile data for user {user_id}"
```

### prompt类:
这个很好理解,回应下最后扔到模型里的是什么提示词,似乎返回值可以是str或者base.Message

```python
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("My App")

@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"

@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]
```

## 6.运行:
```cmd
mcp dev server.py

# Add dependencies
mcp dev server.py --with pandas --with numpy

# Mount local code
mcp dev server.py --with-editable .
```

或者直接在python里mcp.run()
## 7.进入控制面板
```cmd
mcp dev server.py
```
在浏览器里打开给的url

分成几个面板: resource, prompt, tool, 以及其他(比如ping一下server看看server活着不)
## 8. 和LLM连接:
