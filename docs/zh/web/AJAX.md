
::::: tabbed-content
:::: tabbed-block
```    axios([
        url:"目标资源地址"
    ]).then((result) => 
        // 对服务器返回的数据做后续处理
          )
```::::
:::::
:::::::
::::::::

### 7.1.2 params

可以在URL后直接加参数,但params更不容易出错

相当于直接访问url

### 7.1.3 data

往服务器发送的数据

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="2:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
请自行查看[examples/ajax/axios.html](https://github.com/everythingfades/html/blob/main/examples/ajax/axios.html)
:::
::::
::::::
:::::::

### 7.1.3 常用方法:

  请求方法   操作
  ---------- ----------------
  GET        获取数据
  POST       提交数据
  PUT        修改数据(全部)
  DELETE     删除数据
  PATCH      修改数据(部分)

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="3:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    axios({
        url: "目标资源地址",
        method: "请求方法",
        data:{
            参数名:值
        }
    }).then(result => {
        // 后续处理
    })
```::::
:::::
:::::::
::::::::

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="4:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
请自行查看[examples/ajax/otherMethods.html](https://github.com/everythingfades/html/blob/main/examples/ajax/otherMethods.html)
:::
::::
::::::
:::::::

### 7.1.4 报错

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="5:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    axios({
        //请求选项
    }).then(result =>{
        //处理数据
    }).catch(error=>{
        //处理错误
    })
```::::
:::::
:::::::
::::::::

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="6:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
请自行查看[examples/ajax/error.html](https://github.com/everythingfades/html/blob/main/examples/ajax/error.html)
:::
::::
::::::
:::::::

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="7:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
axios相关应用请自行查看[examples/ajax/books.html](https://github.com/everythingfades/html/blob/main/examples/ajax/books.html),
[examples/ajax/citySearch.html](https://github.com/everythingfades/html/blob/main/examples/ajax/citySearch.html),
[examples/ajax/fastapi.html](https://github.com/everythingfades/html/blob/main/examples/ajax/fastapi.html)
:::
::::
::::::
:::::::

### 7.1.5 请求报文:

规定了服务器返回内容的格式

请求报文的组成部分有: - 请求行:请求方法, URL, 协议 -
请求头:以键值对的格式携带的附加信息,比如Content-type - 空行:空行 -
请求体: 发送的资源

#### 7.1.5.1 400:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="8:1"}
::: tabbed-labels
示例
:::

::::: tabbed-content
:::: tabbed-block
```    HTTP/1.1 400 Bad Request
    Date: Mon, 18 Mar 2024 16:09:31 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 54
    Connection: keep-alive
    Set-Cookie: acw_tc=76b20fe317107781711178538e045440fa72a6e24e552de06c572c4e423278;path=/;HttpOnly;Max-Age=1800
    Server: nginx
    Vary: Origin
    Access-Control-Allow-Origin: null
    Access-Control-Allow-Credentials: true
    Accept-Ranges: bytes
    x-frame-options: SAMEORIGIN
    x-xss-protection: 1; mode=block
    x-content-type-options: nosniff
    x-download-options: noopen
    x-readtime: 9
```::::
:::::
:::::::
::::::::

#### 7.1.5.2 200:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="9:1"}
::: tabbed-labels
示例
:::

::::: tabbed-content
:::: tabbed-block
```    HTTP/1.1 200 OK
    Date: Mon, 18 Mar 2024 16:11:21 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 82
    Connection: keep-alive
    Set-Cookie: acw_tc=76b20fe317107782811077982e0454238bafd4b2bcf33c854fbce26fc4744a;path=/;HttpOnly;Max-Age=1800
    Server: nginx
    Vary: Origin
    Access-Control-Allow-Origin: null
    Access-Control-Allow-Credentials: true
    Accept-Ranges: bytes
    x-frame-options: SAMEORIGIN
    x-xss-protection: 1; mode=block
    x-content-type-options: nosniff
    x-download-options: noopen
    x-readtime: 13
    X-Download-Options: noopen
    Referrer-Policy: no-referrer-when-downgrade
    X-Content-Type-Options: nosniff
    X-Permitted-Cross-Domain-Policies: none
```::::
:::::
:::::::
::::::::

### 7.1.6 响应报文:

和上面那个差不多

- 响应行(状态行): 协议, HTTP响应状态码,状态信息
- 响应头: 一键值对的格式携带的附加信息,比如:Content-Type
- 空行:空行
- 响应体:返回的资源

#### 7.1.6.1 响应状态码:

  状态码   说明
  -------- ------------
  1xx      信息
  2xx      成功
  3xx      重定向
  4xx      客户端错误
  5xx      服务端错误

## 7.2 bootstrap 弹框:

bootstrap.css和bootstrap.js

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="10:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
请自行查看[examples/ajax/bootstrap.html](https://github.com/everythingfades/html/blob/main/examples/ajax/bootstrap.html)
:::
::::
::::::
:::::::

其余建议看官方文档,虽然做到后面感觉这个不是很必要

## 7.3 XMLHttpRequest:

AJAX内部用XMLHttpRequest与服务器通信

### 7.3.1 使用:

- 创建XMLHttpRequest对象
- 配置请求方法和url
- 监听lodend时间，接受响应结果
- 发起请求\'

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="11:2"}
::: tabbed-labels
代码示例
:::

:::::: tabbed-content
:::: tabbed-block
```    const xhr = new XMLHttpsRequest()
    xhr.open("请求方法"，"url")
    xhr.addEventListener("loadend",()=>{
        console.log(xhr.response)
    })
    xhr,send()
```::::

::: tabbed-block
请自行查看[examples/ajax/provinceXML.html](https://github.com/everythingfades/html/blob/main/examples/ajax/provinceXML.html)
:::
::::::
::::::::
:::::::::

### 7.3.2 URLSearchParams:

用于把对象转成查询字符串

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="12:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
请自行查看[examples/ajax/URLSearchParams.html](https://github.com/everythingfades/html/blob/main/examples/ajax/URLSearchParams.html)
:::
::::
::::::
:::::::

### 7.3.3 发送post:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="13:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
请自行查看[examples/ajax/provinceXML.html](https://github.com/everythingfades/html/blob/main/examples/ajax/provinceXML.html)
:::
::::
::::::
:::::::

#### 7.3.3.1 设置请求头:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="14:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    xhr.setRequestHeader("Content-Type","application/json")
```::::
:::::
:::::::
::::::::

这个可以表示你上传的数据是一个json

https://juejin.cn/post/6844904094340120584

## 7.4 Promise:

Promise对象用于表示一个异步操作的最终完成或失败机器结果值

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="15:2"}
::: tabbed-labels
代码示例
:::

:::::: tabbed-content
:::: tabbed-block
```    const p = new Promise((resolve, reject)=>{
        // 执行异步任务
    })

    p.then(result => {
        // 成功后的代码
    }).catch(error => {
        // 失败后的代码
    })
```::::

::: tabbed-block
请自行查看[examples/ajax/Promise.html](https://github.com/everythingfades/html/blob/main/examples/ajax/Promise.html)
:::
::::::
::::::::
:::::::::

好处: - 逻辑更清晰 - 解决回调函数地狱问题

resolve表示成功,reject表示throw an error

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="16:2"}
::: tabbed-labels
代码示例
:::

:::::: tabbed-content
:::: tabbed-block
```    const p = new Promise((resolve, reject) => {
      setTimeout(() => {
            // resolve("succeed")
            reject(new Error("就是不让你过"))
        }, 2000)
    })

    p.then(result => {
        console.log(result)
    }).catch(error => {
        console.log(error)
    })
```::::

::: tabbed-block
请自行查看[examples/ajax/error.html](https://github.com/everythingfades/html/blob/main/examples/ajax/error.html)
:::
::::::
::::::::
:::::::::

### 7.4.1 三种状态:

创建对象的时候会处于pending状态

resolve执行后变成fullfilled状态,直接进入then回调函数

reject执行后状态变成rejected,直接进入catch回调函数

Promise对象一旦被兑现/拒绝就是好已经敲定了,状态无法再被改变

## 7.5 同步异步:

同步代码:需要等上一个执行完在执行下一个

异步代码:可以同时执行

异步: - 回调函数 - setInterval - \...

### 7.5.1 回调函数地狱:

回调函数来回嵌套,虽然是syntactic sugar

#### 7.5.1.1 Promise链式调用:

new
Promise执行then的时候可以新创建一个Promise对象,然后可以接着调用then的函数

在避免了来回形式调用的同时保证逻辑嵌套

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="17:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
请自行查看[examples/ajax/primiseChain.html](https://github.com/everythingfades/html/blob/main/examples/ajax/primiseChain.html)
:::
::::
::::::
:::::::

```    new Promise((resolve, reject) => {
        setTimeout(() => {
            reject("1")
        }, 1000)
    }).then(result =>{
        console.log(result)
        return Promise.reject("2")
    }).catch(error =>{
        console.log(error)
        return Promise.reject("3")
    }).then(result => {
        console.log(result)
        return Promise.reject("4")
    }).catch(error =>{
        console.log(error)
        return Promise.reject("5")
    }).then(result => {
        console.log(result)
    }).catch(error =>{
        console.log(error)
    })
```
### 7.5.2 async await

async作为函数的修饰关键字

await在async函数内部取代then函数,等待Promise对象成功状态的结果值

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="18:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
请自行查看[examples/ajax/asyncAwait.html](https://github.com/everythingfades/html/blob/main/examples/ajax/asyncAwait.html)
:::
::::
::::::
:::::::

### 7.5.3 事件循环:

之前有,就不写了

### 7.5.4 宏任务和微任务:

- 宏任务: 浏览器执行的异步代码
- 微任务: JS引擎执行的异步代码

  任务(代码)               执行所在环境
  ------------------------ --------------
  JS脚本执行(script)       浏览器
  setTimeout/setInterval   浏览器
  AJAX                     浏览器
  用户交互                 浏览器

  任务(代码)           执行所在环境
  -------------------- --------------
  Promise对象.then()   JS引擎

Promise语句本身是同步代码,所以会先执行Promise里面的代码然后等

会优先执行微任务队列里的任务,然后执行宏任务队列

:::::::::::: {.admonition .example}
Example

:::::: {.tabbed-set .tabbed-alternate tabs="19:1"}
::: tabbed-labels
代码
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

```    <script>
    console.log(1) // 同步代码,立即执行
    setTimeout(()=>{ // 异步代码,进入队列
        console.log(2) // 同步代码执行完之后,虽然延时是0,但是进入宏任务队列
    },0)
    const p = new Promise((resolve, reject) => { // Promise里是同步代码,这部分立即执行
        console.log(3)
        resolve(4) // 标记状态,但不直接执行then
    })
    p.then(result => { // 这个进入微任务队列,比宏任务队列里的任务优先执行,会先清空微任务队列,然后执行宏任务队列中的任务
        console.log(result)
    })
    console.log(5) // 同步代码,立即执行
    </script>
```
:::::: {.tabbed-set .tabbed-alternate tabs="20:1"}
::: tabbed-labels
输出
:::

:::: tabbed-content
::: tabbed-block
最后输出1 3 5 4 2
:::
::::
::::::
::::::::::::

### 7.5.5 Promise.all

合并多个Promise对象,这个Promise的then是所有Promise成功,如果一个失败就进catch

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="21:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/ajax/PromiseAll.html](https://github.com/everythingfades/html/blob/main/examples/ajax/PromiseAll.html)
:::::::

```    const p = Promise.all([Promise1, Promise2, Promise3.......])
    p.then(result => {

    }).catch(error => {

    })
```::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
