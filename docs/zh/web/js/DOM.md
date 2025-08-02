
:::: tabbed-content
::: tabbed-block
请自行查看[examples/js_involved/html/js_select.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/js_select.html)
```::::
::::::
:::::::

### 5.1.1 获取DOM元素:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="2:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    document.querySelector('css选择器') // 这个只选择一个,如果有多个符合条件的只会返回第一个
    document.querySelectorAll('css选择器') // 这个选择所有,以伪数组形式返回,有长度有索引,但是没有pop(),push()等方法

    // 返回的对象可以直接更改属性

    // 其他:
    // 根据id获取一个元素
    document.getElementById("id")
    // 根据标签获取一个元素
    document.getElementByTagName("div")
    // 根据类名获取所有符合条件的元素
    document.getElementsByClassName("w")
```::::
:::::
:::::::
::::::::

### 5.1.2 操作元素内容:

.innerText属性可以获取文字内容

.innerHTML属性可以获取HTML文本

### 5.1.3 更改属性:

直接赋值就行,以下是几个常用的

如果属性名称用连字符连接,改写成驼峰命名法的格式, obj.style.fontFamily =
\"SimHei\" - obj.style.(相当于更改这个标签的css,更改样式) - eg.
obj.style.color = \"red\" - obj.src
(更改标签的src属性,可以换图片之类的) - obj.href
(更改标签的href属性,可以换链接之类的)

对于document,由于一个html只会有一个body,可以通过document.body直接获取页面的body标签,然后进行修改

#### 5.1.3.1 className

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="3:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/className.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/className.html)
:::::::

如果修改的样式很多,直接通过style属性修改会比较麻烦,于是可以通过借助css类名的形式改属性

其实就是修改一个标签的class属性,把他变成某个class从而应用那个类的css

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="4:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    元素.className = "active"
```::::
:::::
:::::::
::::::::

可以用css的选择器使得改完类名之后应用css不会覆盖原先的样式而是应用新类的新增样式

#### 5.1.3.2 classList:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="5:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/classList.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/classList.html)
:::::::

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="6:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    元素.classList.add('类名') //增加类名

    元素.classList.remove('类名') //删除类名

    元素.classList.toggle('类名') // 切换类名,存在就删,没有就加
```::::
:::::
:::::::
::::::::

如果classlist里的css有重复的,则会显示最有一个可用的属性

#### 5.1.3.3 表单类

::::::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="7:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/form.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/form.html)

:::::: {.tabbed-set .tabbed-alternate tabs="8:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/exampleForm.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/exampleForm.html)
:::::::::::

如果获取innerHTML是空,需要通过表单名称.value获取所有的值

### 5.1.4 自定义属性:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="9:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/self-defined-attr.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/self-define-attr.html)
:::::::

自定义属性名称以data-开头

## 5.2 间歇函数/计时器:

:::::::::::: {.admonition .example}
Example

:::::: {.tabbed-set .tabbed-alternate tabs="10:1"}
::: tabbed-labels
代码
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

```    setInterval(函数,间隔时间)
```
:::::: {.tabbed-set .tabbed-alternate tabs="11:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/timer.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/timer.html)
::::::::::::

- 间隔时间是毫秒,表示每过间隔时间执行一次函数,一旦开启就一直执行,注意函数的位置写的是函数名,也就是不加参数

- setInteval函数会返回一个id

- 用clearInterval(id)暂停执行

## 5.3 事件监听

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="12:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/eventListener.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/eventListener.html)
:::::::

```    元素对象.addEventListener('事件类型',执行函数)
```
\- 事件类型要加引号 - 每次按按钮触发一次函数

### 5.3.1 事件类型:

::::::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="13:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/otherEvent.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/otherEvent.html)

:::::: {.tabbed-set .tabbed-alternate tabs="14:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/mouseEvent.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/mouseEvent.html)
:::::::::::

- 鼠标
- click 鼠标点击
- mouseenter 鼠标经过
- mouseleave 鼠标离开
- 焦点
- focus 获得焦点
- blur 失去焦点
- 键盘事件
- Keydown 键盘按下触发
- Keyup 键盘抬起触发
- 文本事件:
- input 用户输入事件

### 5.3.2 事件对象:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="15:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/eventobject.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/eventobject.html)
:::::::

一个存储时间执行是的相关参数的一个对象,是事件监听绑定函数传入的参数,差不多就是一个json -
type: - 获取当前的时间类型 - clientX/clientY -
获取光标相对于浏览器课件窗口左上角的位置 - offsetX/offsetY -
获取光标相对当前DOM元素左上角的位置 - key - 用户按下键的数值 -
(keyCode已经废弃)

### 5.3.3 环境对象：

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="16:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/this.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/this.html)
:::::::

this, java的this

普通事件里this指的是window

如果是addEventListener返回调用的元素

可以用this.style之类的改参数

### 5.3.4 回调函数:

就是把一个A函数传给另一个B函数,此时A是回调函数

常见的回调函数:

- setInterval
- addEventListener

## 5.4 事件流:

分成两个阶段,捕获和冒泡

捕获阶段冲大往小,冒泡反着来

### 5.4.1 事件捕获:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="17:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/eventCapture.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/eventCapture.html)
:::::::

- 在addEventListener里传入第三个参数,true为使用捕获机制,false为不使用捕获机制
- 如果是用onclick绑定的则没有捕获阶段

### 5.4.2 事件冒泡

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="18:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/mouseEvent.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/mouseEvent.html)
:::::::

- 相当于子类父类继承,如果点击的部分在子类里,他也在父类里,这个时候绑定的同名函数将会按照冒泡阶段从小向大依次执行

### 5.4.3 阻止冒泡:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="19:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    事件对象.stopPropagation()
```::::
:::::
:::::::
::::::::

这个是阻断事件流传播, 同时阻止冒泡和捕获

### 5.4.4 解绑事件:

- 如果是onclick,直接把onclick属性赋值成null即可
- addEventListener使用removeEventListener(事件,函数名),(匿名函数无法被解绑)

### 5.4.5 特殊事件:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="20:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/mouseEvent.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/mouseEvent.html)
:::::::

- mouseover和mouseout有冒泡效果
- mouseenter和mouseleave没有冒泡效果

### 5.4.6 事件委托

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

请自行查看[examples/js_involved/html/eventCommission.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/eventCommission.html)
:::::::

同时给多个元素注册事件

就是定义一个父对象,触发子对象的时候会通过冒泡触发父对象的事件

### 5.4.7 阻止事件默认行为:

:::::::::::: {.admonition .example}
Example

:::::: {.tabbed-set .tabbed-alternate tabs="22:1"}
::: tabbed-labels
代码
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

```    e.pre1ventDefault()
```
:::::: {.tabbed-set .tabbed-alternate tabs="23:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/preventDefault.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/preventDefault.html)
::::::::::::

### 5.4.8 其他事件:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="24:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/otherEvent.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/otherEvent.html)
:::::::

#### 5.4.8.1 页面加载事件

##### 5.4.8.1.1 load

加载外部资源的加载完毕的时候触发的事件 - 等资源加载完处理事情 -
老代码script放在head中,直接找dom找不到

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="25:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    window.addEventListener("load", function(){
        // 等页面加载完在处理回调函数
    })
```::::
:::::
:::::::
::::::::

window是document的更上一级

也可以对元素加load,等这个文件加载完的时候在处理回调函数

##### 5.4.8.1.2 DOMContentLoaded:

当初是的html被加载,就触发,不需要等待所有的元素都完全加载

这会是给document加这个事件

#### 5.4.8.2 元素滚动事件

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="26:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/scrollExample.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/scrollExample.html)
:::::::

##### 5.4.8.2.1 scroll

滚动到某个区域的时候会触发的东西

还是给window加scroll事件

##### 5.4.8.2.2 scroll获取滚动位置:

- scorllLeft
- scorllTop

##### 5.4.8.2.3 scrollTo

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="27:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    windows.scrollTo(x坐标,y坐标)
```::::
:::::
:::::::
::::::::

#### 5.4.8.3 resize事件

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="28:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/resizeEvent.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/resizeEvent.html)
:::::::

当浏览器窗口大小发生变化的时候触发

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="29:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    window.addEventListener('resize',function)
```::::
:::::
:::::::
::::::::

##### 5.4.8.3.1 clientWidth clientHeight

获取元素的课件的宽和高(不包含border和margin等,但是包含padding)

##### 5.4.8.3.2 offsetLeft offsetTop

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="30:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/offset.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/offset.html)
:::::::

获取元素距离自己定位父级元素的左,上距离,这个会包含border很margin等

这个父级元素是有position属性的最近的父元素,直到document

## 5.5 日期对象:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="31:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/date.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/date.html)
:::::::

### 5.5.1 实例化:

java里的new关键字仙剑一个对象(js这么久居然没有新建过对象)

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="32:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    const date = new Date()
```::::
:::::
:::::::
::::::::

也可以

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="33:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    const data = new Date("2022-5-1 8:30:00")
```::::
:::::
:::::::
::::::::

### 5.5.2 日期对象方法:

- getFullYear() 获得四位年份
- getMonth() 获得月份 0-11
- getDate() 获得约分钟的某一天
- getDay() 获得星期 0-6
- getHours() 获得小时 0-23
- getMinutes() 获得分钟 0-59
- getSeconds() 获得秒 0-59

### 5.5.3 时间戳:

::::::::::::: {.admonition .example}
Example

:::::::::::: {.tabbed-set .tabbed-alternate tabs="34:4"}
::: tabbed-labels
代码1代码2代码3示例
:::

:::::::::: tabbed-content
:::: tabbed-block
```    const date = new Date()
    date.getTime()
```::::

:::: tabbed-block
```    +new Date()
```::::

:::: tabbed-block
```    Date.now()
```::::

::: tabbed-block
:::
::::::::::
::::::::::::

请自行查看[examples/js_involved/html/timestamp.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/timestamp.html)
:::::::::::::

是指从1970年01月01日00分00秒开始到现在的毫秒数

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="35:2"}
::: tabbed-labels
时间戳转时间输出
:::

:::::: tabbed-content
:::: tabbed-block
```    function timestampToTime(timestamp) {
            var date = new Date(timestamp);//时间戳为10位需*1000，时间戳为13位的话不需乘1000
            var Y = date.getFullYear() + '-';
            var M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1):date.getMonth()+1) + '-';
            var D = (date.getDate()< 10 ? '0'+date.getDate():date.getDate())+ ' ';
            var h = (date.getHours() < 10 ? '0'+date.getHours():date.getHours())+ ':';
            var m = (date.getMinutes() < 10 ? '0'+date.getMinutes():date.getMinutes()) + ':';
            var s = date.getSeconds() < 10 ? '0'+date.getSeconds():date.getSeconds();
            return Y+M+D+h+m+s;
        }
    timestampToTime(Date.now())
```::::

::: tabbed-block
\'2024-03-19 00:53:28\'
:::
::::::
::::::::
:::::::::

## 5.6 节点操作:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="36:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/modifyDOM.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/modifyDOM.html)
:::::::

### 5.6.1 DOM 节点

- 元素节点
- 所有的标签, body, div
- html是根节点
- 属性节点
- href等
- 文本节点:
- 标签里的字
- 其他类

主要操作元素节点

### 5.6.2 查找节点:

根据关系找

#### 5.6.2.1 父节点:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="37:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    e.parentNode
```::::
:::::
:::::::
::::::::

#### 5.6.2.2 子节点:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="38:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    e.children
```::::
:::::
:::::::
::::::::

#### 5.6.2.3 兄弟节点:

##### 5.6.2.3.1 下一个兄弟节点:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="39:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    e.nextElementSibling
```::::
:::::
:::::::
::::::::

##### 5.6.2.3.2 上一个兄弟节点:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="40:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    e.previousElementSibling
```::::
:::::
:::::::
::::::::

### 5.6.3 添加节点

::::::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="41:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/createElement.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/createElement.html)

:::::: {.tabbed-set .tabbed-alternate tabs="42:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/createInsertElement.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/createInsertElement.html)
:::::::::::

- 先新建一个新的节点,

- ::: highlight
      ```
      document.createElement()
      ```
  :::

- 然后在放到文档之中

- 插入到父元素中作为最后一个子元素

```      父元素.appenChild()
```
- 插入到某个元素之前

```      父元素.insertBefore(要插入的元素, 在哪个元素前面)
```
### 5.6.4 克隆节点:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="43:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    元素.cloneNode(Bool)
```::::
:::::
:::::::
::::::::

如果参数是True,则会和后代一起克隆

如果是False,则不克隆后代节点

默认是False

注意克隆之后还需要追加节点

### 5.6.5 删除节点

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="44:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    父元素.deleteNode(要删除的元素)
```::::
:::::
:::::::
::::::::

## 5.7 M端事件:

移动端特殊事件:

touch事件:

- touchstart
- touchmove
- touchend

## 5.8 JS插件:

swiper:移动端插件 具体的建议去查api文档

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="45:1"}
::: tabbed-labels
示例
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

请自行查看[examples/js_involved/html/swiper.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/swiper.html)
:::::::

ctrl cv全栈工程师上线
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
