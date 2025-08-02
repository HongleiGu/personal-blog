
::::::: tabbed-content
:::: tabbed-block
```    const fs = require('fs')
```::::

:::: tabbed-block
```    fs.writeFile("文件路径", "写入内容", err => {
        // 写入后的回调函数
    })
```::::
:::::::
:::::::::

=== 读取文件内容

```    fs.readFile("文件路径", (err, data) => {
        // 读取后的回调函数
        // data是文件内容的Buffer数据流
    })
```
:::::: {.tabbed-set .tabbed-alternate tabs="2:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
请自行查看[examples/nodejs/jss/fs.js](https://github.com/everythingfades/html/blob/main/examples/nodejs/jss/fs.js)
:::
::::
::::::
:::::::::::::::

## 8.2 URL端口:

端口号可以是0-65535之间的任意整数

http协议默认访问80端口

但是基本上0-1023都被系统程序占用

## 8.3 创建Web服务

- 加载http模块
- 监听request请求事件
- 设置端口,启动web服务
- 访问localhost:3000

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="3:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
请自行查看[examples/nodejs/jss/web.js](https://github.com/everythingfades/html/blob/main/examples/nodejs/jss/web.js)以及[examples/nodejs/jss/webhtml.js](https://github.com/everythingfades/html/blob/main/examples/nodejs/jss/webhtml.js)
:::
::::
::::::
:::::::

## 8.4 模块化:

### 8.4.1 Commonjs:

在js中,每个文件都被视为一个单独的模块,需要使用标准语法导入导出进行使用

::::::::: {.admonition .example}
Example

:::::: {.tabbed-set .tabbed-alternate tabs="4:1"}
::: tabbed-labels
导出
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

```    //设置module.exports属性
    moduel.exports = {
        属性名:暴露的值或者方法
    }
```
=== 导入:require模块名或者路径

```    require("js")
    require("./exports.js")
```:::::::::

### 8.4.2 ECMAScript

多数情况下,这个更为常用

#### 8.4.2.1 默认导入导出

:::::::::::: {.admonition .example}
Example

::::::::::: {.tabbed-set .tabbed-alternate tabs="5:4"}
::: tabbed-labels
导出导出示例导入导入示例
:::

::::::::: tabbed-content
:::: tabbed-block
```    export default {}
```::::

::: tabbed-block
请自行查看[examples/nodejs/jss/export.js](https://github.com/everythingfades/html/blob/main/examples/nodejs/jss/export.js)
:::

:::: tabbed-block
```    import obj from "模块名或者路径"
```::::

::: tabbed-block
请自行查看[examples/nodejs/jss/useexports.js](https://github.com/everythingfades/html/blob/main/examples/nodejs/jss/useexports.js)
:::
:::::::::
:::::::::::
::::::::::::

nodejs默认是支持commonjs的,如果需要ECMA需要再所在文件夹新建package.json文件夹,设置{\"type\":\"module\"}

#### 8.4.2.2 命名导入导出

- 导出 直接在变量前加export

- 导入:

```      import {something, something} from "模块名或者路径"
```
::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="6:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
整个[examples/nodejs/jss/EMCA](https://github.com/everythingfades/html/tree/main/examples/nodejs/jss/ECMA)都是示例
:::
::::
::::::
:::::::

### 8.4.3 包:

这个和python的概念一样,把init.py换成package.json,一般是如下形式:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="7:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    {
        "name": "包的名字",
        "version": "版本号",
        "description": "描述"
        "main": "软件包入口",
        "author": "作者",
        "license": "许可,没猜错的话就是apache那些github上的license"
    }
```::::
:::::
:::::::
::::::::

会默认去找index.js然后找main指定的模块文件

## 8.5 npm:

专属js的pip,也会自动检测依赖,但个人更喜欢pnpm(速度快)以及yarn,不过那些后面再说

### 8.5.1 命令

#### 8.5.1.1 自动生成package.json

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="8:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    npm init -y
```::::
:::::
:::::::
::::::::

#### 8.5.1.2 下载软件包:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="9:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    npm i 软件包名称
```::::
:::::
:::::::
::::::::

下载的包会在./node_modules文件夹里,自动记录到package.json里

#### 8.5.1.3 安装所有依赖:

npm下比直接拷贝node_modules快得多

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="10:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    npm i
```::::
:::::
:::::::
::::::::

### 8.5.2 全局软件包 nodemon

- 本地软件包: 当前项目内使用,封装属性和方法,存在与node_modules

- 全局软件包: 本机所有项目使用,封装命令和工具,在系统设置的位置

- 使用:

- 安装:

```      npm i nodemon -g
       # -g表示安装到全局
```
- 使用

```      nodemon 目标js
      # 在wsl2里需要加上 CHOKIDAR_USEPOLLING=true
      # CHOKIDAR_USEPOLLING=true nodemon 目标js
```:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
