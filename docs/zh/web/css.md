
::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="1:2"}
::: tabbed-labels
代码效果
```
:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>网页</title>
            <style>
                h1 {
                    color: blue;
                    font-size: 12px;
                    font-family: SimSun;
                    background-color: red;
                }
            </style>
        </head>
        <body>
            某个网页
            <h1 align = "center">标题1</h1>
            <h2 align = "left">标题2</h2>
            <h3 align = "right">标题3</h3>
            <h4>标题4</h4>
            <h5>标题5</h5>
            <h6>标题6</h6>
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/css_involved/html/basic.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/basic.html),并确保阅读首页须知
:::
::::::
::::::::
:::::::::

## 2.2 css的引入方式:

### 2.2.1 行内(不建议)

通过style通用html标签属性直接写在标签里(不建议使用)

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="2:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <p style="text-indent:30px;color:red">行内css</p>
            <p>不用css</p>
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/css_involved/html/inline_css.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/inline_css.html),并确保阅读首页须知
:::
::::::
::::::::
:::::::::

### 2.2.2 \< style\>\< /style\>

可以直接在\< head\>\< /head\>中添加\< style\>\<
/style\>来定义整个html的css

注意:如果通过\< a\>跳转到其他页面\< style\>\< /style\>里的格式不会生效

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="3:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>网页</title>
            <style>
                h1 {
                    color: blue;
                    font-size: 12px;
                    font-family: SimSun;
                    background-color: red;
                }
            </style>
        </head>
        <body>
            某个网页
            <h1 align = "center">标题1</h1>
            <h2 align = "left">标题2</h2>
            <h3 align = "right">标题3</h3>
            <h4>标题4</h4>
            <h5>标题5</h5>
            <h6>标题6</h6>
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/css_involved/html/style_tag_css.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/style_tag_css.html),并确保阅读首页须知
:::
::::::
::::::::
:::::::::

### 2.2.3 \< link\>

通过\< link\>引入外部css文件

同样,跳转到其他页面不会生效

注意,虽然是外部文件,但是这里加载依然会改变整个jupyter
notebook的css,不建议直接在jupyter里运行

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="4:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" type="text/css" href="./examples/css_involved/css/example.css">
            <title>网页</title>
        </head>
        <body>
            <p>某个网页</p>
            <h1 align = "center">标题1</h1>
            <h2 align = "left">标题2</h2>
            <h3 align = "right">标题3</h3>
            <h4>标题4</h4>
            <h5>标题5</h5>
            <h6>标题6</h6>
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/css_involved/html/link.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/link.html),并确保阅读首页须知
:::
::::::
::::::::
:::::::::

## 2.3 css选择器

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="5:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
这部分所有代码效果可请自行查看[examples/css_involved/html/selectors.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/selectors.html),并确保阅读首页须知
:::
::::
::::::
:::::::

### 2.3.1 全局选择器:

应用到所有元素上,优先级最低,一般是样式初始化

:::: {.admonition .example}
代码

```        *{
            font-family: SimSun;
        }
```::::

### 2.3.2 元素选择器:

标签名 {属性:值;}

可以是任何html文档中的标签,但是只能同时改变所有这种标签的样式

之前已经有很多这种例子了

:::: {.admonition .example}
代码

```    p{
        font-size:14px;
        color:red;
    }
```::::

### 2.3.3 类选择器:

需要现在要改样式的标签里定义class属性,然后根据class名写css

- 可以对多种标签使用
- 类名不能以数字开头
- 同一个标签可以用多个类选择器,加上空格隔开的多个class属性就行,如果属性冲突,会优先使用第一个可适用的属性定义

:::: {.admonition .example}
代码

```    # 假设我们有一个class叫example
    .example{
        color:purple;
    }
    # 会应用到如下tag上,注:something这个标签不存在,可以是任意标签
    <something class="example">...</something>
    <something class="example" class="example1">...</something>
```::::

### 2.3.4 id选择器

针对一个特定的标签使用,只能使用一次,css中用#定义

- id是唯一的(规范上不能重复,语法上可行)
- id不能以数字开头

:::: {.admonition .example}
代码

```    #something{
        border:3px dashed green;
    }
```::::

### 2.3.5 合并选择器

提取相同的样式,减少重复代码

选择器1,选择器2{}

:::: {.admonition .example}
代码

```    .h1.p{
        color:green;
    }
```::::

### 2.3.6 其他选择器

#### 2.3.7 后代选择器

选择所有被符合选择器1的标签包含的选择器2类标签

:::: {.admonition .example}
代码

```    ul li{
        color:green
    }
```::::

#### 2.3.8 \>选择器：

只选择直接作为选择器1的标签的选择器2类标签应用css,不对更深的标签起作用

可以和上面的选择器一起用

:::: {.admonition .example}
代码

```    ul>li{
        color:green;
    }
```::::

#### 2.3.9 +选择器:

选择跟在符合选择器1条件的标签之后的选择器2类标签应用css

可以和上面的选择器一起用

:::: {.admonition .example}
代码

```    .example+p{
        color:red;
    }
```::::

#### 2.3.10 \~选择器:

选择跟在符合选择器1条件的标签之后的所有选择器2元素,和后代选择器不同的是这个不在选择器1标签里

:::: {.admonition .example}
代码

```    .example~p{
        color:red;
    }
```::::

### 2.3.11 伪对象选择器:

给元素追加一个虚拟标签,可以节省html的资源开销

- ::after在后面添加一个对象,虚拟对象,装饰作用
- ::before在前面添加一个对象,虚拟对象,装饰作用
- :nth-chlid(n),选择的n个子元素
- :first-chlid,选择第一个子元素
- :last-child,选择最后一个子元素
- content(必须有,否则伪对象无效)

其他查表:https://www.w3schools.com/cssref/css_selectors.php

### 2.3.12 优先级

行内样式\>ID选择器\>类选择器\>元素选择器

## 2.4 css特性

- 继承性: 子级默认继承父级的字体特性
- 一般把文字写到body标签,然后特定元素单独设置
- 层叠性
- 相同的属性会覆盖,后面的css覆盖前面的css属性
- 不同是属性会叠加,不同的css属性都生效
- 优先级:但一个标签用了多种选择器的时候
- 选择器优先级高的样式神效
- 通配符选择器(\*)\< 标签选择器(p,div\...) \< 类选择器(.class) \<
  id选择器(#id) \< 行内样式 \< !important
  (除了!important以外,选中标签的范围越大,优先级越低)
- 如果涉及复合选择器,则需要叠加计算
  - 按照行内样式,id选择器个数,类选择器个数,标签选择器个数,(从左到右比较)

## 2.5 字体属性:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="6:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
这部分所有效果可自行查看[examples/css_involved/html/font.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/font.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

### 2.5.1 color:

- color
  - 各种颜色: 查表https://www.w3schools.com/colors/colors_names.asp
  - 色值:(茴香豆有4种写法,色值主要有3种写法)
  - RGB值:rgb(255,99,71),三个值分别对应rgb三个值,取值范围0-255
    - \< p style=\"background-color:rgb(255, 99, 71)\"\>html\< /p\>:

      rgb(255,99,71)
  - HEX值:#ff6347,和上面差不多,每两位表示RGB中的一个值,前面加上井号
    - \< p style=\"background-color:#ff6347\"\>html\< /p\>:

      #ff6347
  - RGBA值:rgba(255,99,71,1),rgba加上透明度(这个应该是可以的,但是jupyter不知道为什么会把style吞掉,如果%%html没问题,直接markdown不显示颜色)
    - \< p style=\"background-color:rgba(255, 99, 71, 0.5)\"\>\< /p\>:

      rgba(9, 100%, 64%, 0.5)

:::: {.admonition .example}
代码

```    div{color:red;}
    div{color:#ff0000;}
    div{color:rgb(255,0,0)}
    div{color:rgba(255.0,0,.5)}
```::::

### 2.5.2 font-size

某些浏览器有最小字体大小

:::: {.admonition .example}
代码

```    div{font-size:10px;}
```::::

### 2.5.3 font-weight:

设置文本的粗细

- bold:加粗
- bolder:更粗
- lighter:更细
- 100-900:默认400,bold700

注: 其实如果自己引入字体的话,可以自定义,@font-face

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="7:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    #5 {font-weight:normal}
    #6 {font-weight:bold}
    #7 {font-weight:bolder}
    #8 {font-weight:lighter}
    #9 {font-weight:360}
```::::
:::::
:::::::
::::::::

### 2.5.4 font-style:

设置文本的字体样式

- normal:默认
- italic:斜体字

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="8:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    #10 {font-style:normal}
    #11 {font-style:italic}
```::::
:::::
:::::::
::::::::

### 2.5.5 font-family:

用来指定一个元素的字体,如果字体名称包含空格,则必须用引号包裹

### 2.5.6 line-height:

设置文本间距,单倍间距或者双倍间距等

- 数字px
- 数据(几倍行距)

### 2.5.7 font:

把上面所有font属性写到一起

字号和字体值必须写,不然不生效

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="9:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
text部分所有效果可自行查看[examples/css_involved/html/text.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/text.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

### 2.5.8 text-indent:

文本缩进

- 数字px
- 数字em(1em是当前标签的字号大小)

### 2.5.9 text-align:

内容对齐,默认是left,居中的是文字,不是标签

### 2.5.10 text-decoration:

加上修饰线

- none;
- underline
- line-through
- overline

:::: {.admonition .example}
代码

```    div {
        # font-style, font-weight font-size line-height font-family
        font: italic 700 30px/2 楷体;
    }
```::::

## 2.6 背景

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="10:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
这部分所有效果可自行查看[examples/css_involved/html/background.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/background.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

### 2.6.1 background-color

和color一样,但是color是文字的颜色,bgc是背景的颜色

### 2.6.2 background-image

那个url()里面可以填本地地址,直接从本地访问图片,也可以直接url,

:::: {.admonition .example}
代码

```    .box{
        width: 600px;
        height: 600px;
        background-image: url("some url")
    }
```::::

### 2.6.3 background-repeat:

设置图片如何重复:

- repeat:默认属性,在分配的空间大于图片大小的时候会像两个方向重复图片
- repeat-x:只在x方向上重复图片
- repeat-y:只在y方向上重复图片
- no-repeat:不重复图片

:::: {.admonition .example}
代码

```    .box{
        background-image:url("something");
        background-repeat:no-repeat;
    }
```::::

### 2.6.4 background-size:

设置背景图片的大小

- length:设置背景图片的宽度和高度,可以只设置一个值,另一个会默认成auto
- percentage:设置图片占相对区域面积的百分比,可以只设置一个值,另一个会默认成auto
- cover:将图片设置成能完全覆盖背景区域的最大大小
- contain:保持图片和总比并且放缩成适合背景定位的最大大小

:::: {.admonition .example}
代码

```    .box{
        background-image: url("something");
        background-size 100% 100%;
    }
```::::

### 2.6.5 background-position:

以下都是第一个位置为水平位置,第二个为垂直位置,英文字面意思,不要多想

- left top
- left center
- left bottom
- right center
- right bottom
- center top
- center center
- center bottom
- x% y%
- xpos ypos

:::: {.admonition .example}
代码

```    .box{
        background-image: url("something");
        background-position: left top;
    }
```::::

### 2.6.6 background-attachment

使背景不会跟着元素移动

### 2.6.7 background复合:

把上面所有属性写到一起,空格隔开,不区分顺序

## 2.7文本属性

感觉好像font里也写了一遍,不过不管了

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="11:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
text部分所有效果可自行查看[examples/css_involved/html/text.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/text.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

### 2.7.1 text-align

文本对齐方式,英文字面意思

- left
- right
- center

:::: {.admonition .example}
代码

```    h1 {
        text-align:center
    }
```::::

### 2.7.2 text-decoration:

添加到文本的修饰,下划线,上划线,删除线等,英文字面意思

- underline
- overline
- line-through

:::: {.admonition .example}
代码

```    h1 {
        text-decoration:underline;
    }
```::::

### 2.7.3 text-transform

还是英文字面意思

- captialize
- uppercase
- lowercase

:::: {.admonition .example}
代码

```    h1 {
        text-transform:uppercase;
    }
```::::

### 2.7.4 text-indent:

定义缩进,直接是x px

:::: {.admonition .example}
代码

```    h1 {
        text-indent:30px;
    }
```::::

## 2.8 表格/边界属性

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="12:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
text部分所有效果可自行查看[examples/css_involved/html/table.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/table.html),并确保阅读首页须知,本来想分开的,但是没了边界属性之外感觉表格就没东西了
:::
::::
::::::
:::::::

### 2.8.1 border：

定义表格边框：

- 边框距离
- 边框样式
- 边框颜色

:::: {.admonition .example}
代码

```    table,td{
        border: 1px solid black;
    }
```::::

### 2.8.2 border-collapse:

设置边框是折叠成一个单一的边框还是隔开

:::: {.admonition .example}
代码

```    table{
        border-collapse:collapse;
    }
```::::

### 2.8.3 border-radius(这个一般不在表格中用)

创建圆角

- 设置一个值:四个角圆角相同
- 设置两个值:第一个为左上角和右下角,第二个值为右上角和左下角
- 设置三个值:第一个为左上角,第二个为右上角和左下角,第三个是右下角
- 设置四个值:第一个为左上角,第二个为右上角,第三个为左下角,第四个是右下角

```    #border-radius1{
                width:200px;
                height:200px;
                background:violet;
                border-radius:20px;
            }
```
## 2.9 css盒子模型:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="13:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
盒子部分所有效果可自行查看[examples/css_involved/html/box_model.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/box_model.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

封装周围的html元素的整体框架

- margin 外边距,透明的
- border 边框
- padding 内边距,透明的
- content 实际内容,编辑weight和height的时候实际编辑的是content部分的大小

针对这几个有一堆的css属性,具体自己查https://www.w3schools.com/cssref/index.php

一般border属性都以border开头

常用的对于以上四个都适用的,英文字面意思

- margin-top
- margin-bottom
- margin-left
- margin-right
- border-top
- border-bottom
- border-left
- border-right
- padding-top
- padding-bottom
- padding-left
- padding-right

盒子大小

- 默认:盒子大小= 内容尺寸 + border尺寸 + 内边距尺寸

margin不算进盒子

![css盒子](../assets/盒子模型.png)

- border和padding会撑大盒子
- 解决:
- 手动做减法
- 内减模式: box-sizing:border-box

### 2.9.1 外边距问题:

子级添加margin会导致父元素塌陷

解决办法:

- 取消自己margin,父级设置padding
- 父级设置overflow:hidden
- 父级设置border-top

### 2.9.2 行内元素内外边距问题:

行内元素添加margin和padding无法改变垂直位置

解决问题: 加line-height

### 2.9.3 清除默认样式:

比如p标签的空白,这里用全局选择器

:::: {.admonition .example}
代码

```    * {
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
    }
```::::

### 2.9.4 元素溢出:

用overflow控制,或者overflow-x,overflow-y

- scroll : 无论是否溢出都有滚动条
- hidden: 隐藏溢出部分
- auto: 自动识别,溢出就加scroll

### 2.9.5 box-shadow

一共四个值:

- h-shadow(必选):水平阴影的位置
- v-shadow(必选):垂直阴影的位置
- blur(可选):模糊距离
- color(可选):阴影的颜色

:::: {.admonition .example}
代码

```    #box-shadow1{
                width:200px;
                height:200px;
                background:aqua;
                box-shadow: 10px 20px
            }
```::::

## 2.10 css弹性盒子

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="14:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
弹性盒子部分所有效果可自行查看

examples/css_involved/html/flex-box.html,并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

弹性元素由弹性容器和弹性子元素组成,通过设置display的属性将其定义为弹性容器

弹性盒子默认横向摆放

- display:flex 启用弹性盒子,默认为水平排列

这种子元素可以自动基岩或拉伸

组成部分: - 弹性容器 - 弹性盒子 - 主轴: 默认在水平方向 - 侧轴:
默认在垂直方向

### 2.10.1 justify-content:

- flex-start: 默认值,从七点开始依次排列
- flex-end: 弹性盒子从终点开始依次排列
- center: 主轴居中
- space-between: 均匀排列,空白在盒子中间
- space-around: 均匀排列,空白在盒子两侧
- space-evenly: 弹性盒子和容器之间间距相等

### 2.10.2 flex-direction:

- row 横向从左到右摆放
- row-reverse 横向从右到左摆放
- column 纵向从上到下排列
- column-reverse 纵向从下到上排列

### 2.10.3 align-items:

- flex-start
- flex-end
- center

### 2.10.4 align-self:

单独控制某个弹性盒子的侧轴排列方式 - stretch: 沿着测轴拉伸至铺满容器 -
center: 居中 - flex-start: 起点开始排列 - flex-end:
弹性盒子从终点开始依次排列

### 2.10.5 flex:

控制弹性盒子在主轴方向的尺寸

属性值: 政治素质,表示占用父级元素剩余尺寸的分数,默认是1

### 2.10.6 flex-grow:

设置扩展因子,会根据弹性盒子的扩展因子分配剩余空间

可以设置扩展因子让各个元素大小自动按比例分配

各个元素的比例=扩展因子+1

### 2.10.7 flex-wrap:

弹性盒子可以自动挤压或者拉伸,默认情况下,所有天哪星河在一行显示

- wrap: 换行
- no-wrap: 不换行(默认)

### 2.10.8 align-content

这个是不会对单行生效的,和align-itmes似乎是一个东西

- flex-start: 默认值,从七点开始依次排列
- flex-end: 弹性盒子从终点开始依次排列
- center: 主轴居中
- space-between: 均匀排列,空白在盒子中间
- space-around: 均匀排列,空白在盒子两侧
- space-evenly: 弹性盒子和容器之间间距相等

## 2.11 文档流:

### 2.11.1 问题:

#### 2.11.2.1 空格折叠

无论放多少个空格都会被折叠成一个空格

#### 2.11.2.2 元素无间隙:

如果有两个并排的图片一起放置,中间是没有间隙的

### 2.11.2 解决:

脱离文档流:

- 浮动
- 绝对定位
- 固定定位

#### 浮动:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="15:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
浮动部分所有效果可自行查看[examples/css_involved/html/float.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/float.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="16:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
清除浮动部分所有效果可自行查看[examples/css_involved/html/disable-float.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/disable-float.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

float属性:(只有左右浮动,没有上下浮动),可以是元素拖了文档流

- left(向左浮动)
- right(向右浮动)

元素同时向一方向浮动的时候,会变成水平摆放,向左或者向右

当容器大小不足的时候会在下一行摆放

#### 2.11.2.1 清除浮动:

清除浮动会导致某些元素的位置发生变化,后续元素会收到影响

比如如果父级元素没有高度,子级元素无法撑开父级高度

- 父元素设置相应属性
- 增加clear属性, clear:both
- overflow清除浮动
- 伪对象方式, 在父级对象加上一个::after或者::before选择器,设置clear:both

##### 2.11.2.1.1 clear

- left(清除左浮动)
- right(清除右浮动)
- both(清除左右浮动,如果有的话)

##### 2.11.2.1.2 overflow:

如果父元素出了问题,同级元素受到影响,可以用overflow清除浮动,这种情况下不能设置父元素的高度

- visible(全部铺在页面上)
- hidden(隐藏)
- clip(把多的部分隐藏)
- scroll(增加一个可滚动的轴,大小不调整)
- auto(自适应)

## 2.12 定位:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="17:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
position部分所有效果可自行查看[examples/css_involved/html/position.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/position.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

position属性

- relative
- absolute(脱离文档流)
- fixed(脱离文档流)

可以使用left,top,right,bottom四个属性调整位置

对于absolute可以理解成每一个absolute的元素都在一个新的图层上(子绝父相)

fixed一般来说不会有这个问题,因为fixed元素会跟着页面滚动

设置定位后定位随着能定位的父元素决定,直到顶层文档

  定位方式   属性值     是否脱离标准流(文档流)   显示模式               参照物
  ---------- ---------- ------------------------ ---------------------- ------------------------------------
  相对定位   relative   否                       保持标签原有显示模式   自己原来的位置
  绝对定位   absolute   是                       行内块特点             已经定位的祖先元素或者浏览器可视区
  固定定位   fixed      是                       行内块特点             浏览器窗口

### 2.12.1 z-index:

解决图层问题,后来者居上,取值越大越靠上

## 2.13 transition:

和@keyframes 差不多, 语法上也差不多

- 可以在一个元素不同状态之间切换的时候添加过渡效果
- transition: 过渡属性,花费时间
- 注意:
- 过渡属性可以是具体的css属性
- 也可以设置为all,所有不同的属性值都产生过渡效果
- transition设置给元素本身
- 一般和伪对象选择器一起使用,设置不同状态

## 2.14 opacity:

设置整的元素的透明度,0-1

## 2.15 SEO:

尽量让网页在搜索引擎里靠前,一般企业里会用

方法:

- 氪金
- 网页后缀设置为html
- 标签语义化(在合适的地方使用合适的标签)

网页SEO标签

- title: 网页标题标签 \< head\>里的\< title\>
- description:网页描述 \< head\>里的\< meta name=\"description\"\>
- keywords: 网页关键词 \< head\>里的\< meta name=\"keywords\"\>

## 2.16 Favicon图标:

出现在浏览器标题栏的图标

:::: {.admonition .example}
代码

```    <link rel="shortcut icon" href="文件名" type="image/x-icon">
```::::

## 2.17 各种效果:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="18:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
tranlates部分所有效果可自行查看[examples/css_involved/html/translates.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/translates.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

### 2.17.1 二维

#### 2.17.1.1 平移:

transition和translate实现

#### 2.17.1.2 旋转效果:

:::: {.admonition .example}
代码

```    transform: rotate(角度)
```::::

https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform-function/rotate

#### 2.17.1.3 转换原点:

:::: {.admonition .example}
代码

```    transform-origin: 水平位置 垂直位置
```::::

#### 2.17.1.4 复合效果:

:::: {.admonition .example}
代码

```    transform: translate() rotate() 
```::::

transform属性有层叠性,不能一个一个写,必须写进一个transform属性里

#### 2.17.1.5 缩放:

:::: {.admonition .example}
代码

```    transform: scale(缩放倍数)
```::::

或者

:::: {.admonition .example}
代码

```    transform: scale(X缩放倍数,Y缩放倍数)
```::::

#### 2.17.1.6 倾斜:

transform: skew(角度);

#### 2.17.1.7 背景渐变:

##### 2.17.1.7.1 线性:

:::: {.admonition .example}
代码

```    background-image linear-gradient(
        渐变方向(角度或者to),
        颜色1, 终点位置(可不写)
        颜色2, 终点位置(可不写)
    )
```::::

https://developer.mozilla.org/zh-CN/docs/Web/CSS/gradient/linear-gradient

##### 2.17.1.7.2 径向

:::: {.admonition .example}
代码

```    background-image radial-gradient(
        半径 at 圆形位置(x位置 y位置),
        颜色1, 终点位置(可不写)
        颜色2, 终点位置(可不写)
    )
```::::

半径可以是两条,这种情况会变成椭圆

### 2.17.2 空间转换:

#### 2.17.2.1 平移:

:::: {.admonition .example}
代码

```    transform: translate3d(x,y,z); /*这里必须逗号隔开*/
    transform: translateX();
    transform: translateY();
    transform: translateZ();
```::::

默认z是没有效果的,但是可以给父级元素设置视距

#### 2.17.2.2 视距

perspective: 视距

添加给直接父级元素

#### 2.17.2.3 旋转

:::: {.admonition .example}
代码

```    transform: rotateX(值);
    transform: rotateY(值);
    transform: rotateZ(值);
```::::

或者

:::: {.admonition .example}
代码

```    transform: rotate3d(x,y,z,角度); /*x,y,z是0-1之间的数字*/
```::::

#### 2.17.2.4 立体呈现:

:::: {.admonition .example}
代码

```    transform-style: 属性
```::::

- flat: 子级处于平面中
- preserve-3d: 自己处于3D空间

#### 2.17.2.5 空间缩放:

:::: {.admonition .example}
代码

```    transform: scale3d(x,y,z);
```::::

## 2.18 动画:

用@keyframes创建动画,这个会一直重复播放

属性太多了,建议自己查表https://www.w3schools.com/css/css3_animations.asp

同时要在对应的元素上加animation属性

:::: {.admonition .example}
代码

```    animation: 动画名称 动画时长 速度曲线 延迟时间 重复次数 动画方向 执行完毕时状态
```::::

比如

:::: {.admonition .example}
代码

```    #breath:hover{
        animation: breath 2700ms ease-in-out 0s infinite alternate running;
    }
```::::

或者拆成多个属性值去写 - animation-name - animation-duration -
animation-delay - animation-fill-mode - forwards: 最后一帧状态 -
backwards: 第一帧状态 - animation-timing-function - linear -
ease-in-out - step() - \... - animation-iteration-count - infinite -
数字 - animation-direction - alternate为反向 - animation-play-state -
paused为暂停

:::: {.admonition .example}
代码

```    @keyframes rainbow{
                    0%{
                        height:25px;
                        width:25px;
                        background-color:red;
                    }
                    16%{
                        height:50px;
                        width:50px;
                        background-color:orange;
                    }
                    33%{
                        height:75px;
                        width:75px;
                        background-color:yellow
                    }
                    50%{
                        height:100px;
                        width:100px;
                        background-color:green
                    }
                    67%{
                        height:125px;
                        width:125px;
                        background-color:aquamarine;
                    }
                    83%{
                        height:150px;
                        width:150px;
                        background-color:blue
                    }
                    100%{
                        height:175px;
                        width:175px;
                        background-color:purple;
                    }
                }
```::::

## 2.19 兼容不同设备:

- 分辨率:
- 物理分辨率: 出厂设置,电脑显示屏分辨率
- 逻辑分辨率: 调节之后的的分辨率

其实一般来说我更倾向写个scss,里面封装一下vh和vw函数,不过这个是在vue里

### 2.19.1 视口:

:::: {.admonition .example}
代码

```    <meta name="viewport" content="width=device-width, initial-scale=1.0">
```::::

这个大概率不用动,vscode自动生成

上述代码表示

- 视口宽度=设备宽度
- 缩放一倍(不缩放)

### 2.19.2 二倍图:

- 移动端参考iPhone6/7/8,设备宽度375px产出设计稿
- 二倍图设计稿尺寸: 宽750px

### 2.19.3 适配方案:

- 宽度适配:宽度自适应,pc端网页
- 百分比布局
- flex布局
- 注意:这两个不能高度自适应
- 等比适配:宽高等比缩放,移动端网页
- rem
- vw

#### 2.19.4 rem:

rem是个相对单位,表示1HTML字号大小,是相对HTML标签字号计算出的单位

#### 2.19.5 vw vh

也是相对单位,相对试图的尺寸的计算结果,50vw表示50%视图宽

#### 2.19.6 媒体查询:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="19:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
自行查看[examples/css_involved/html/media-search.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/media-search.html),并确保阅读首页须知
:::
::::
::::::
:::::::

检测视口的宽度,编写差异化的css, 如果用rem调整大小,只需要固定html字号即可

先设置\< meta\>

用@media创建媒体查询,在不同屏幕大小下设置不同比例

:::: {.admonition .example}
代码

```    @media screen and (max-width:768px) and (min-width:996px){
                    #box{
                        background-color:aqua;
                    }
                    #p{
                        display:none;
                    }
                }
```::::

#### 2.19.7 rem-flexible.js

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="20:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
可自行查看[examples/css_involved/html/flexible.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/flexible.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

我个人觉得能不用别的插件就不用别的插件,不然你的项目还得跟着他的更新来,除非太好用了,这个插件我个人没在项目中用过,vue里直接用别的适配方式(自定义vw,vh)

##### 2.19.7.1 px转rem

一般设计稿是375px视口,

所以[\\(rem = \\frac{px}{根字号}\\)]{.arithmatex}

### 2.19.8 雪碧图/精灵图

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="21:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
text部分所有效果可自行查看[examples/css_involved/html/sprite.html](https://github.com/everythingfades/html/blob/main/examples/css_involved/html/sprite.html),并确保阅读首页须知,不然太乱了
:::
::::
::::::
:::::::

减少图片大小,减少http请求,提高性能

通过把图片设置到background-image里调整位置可以把一堆图片整合进一张,需要用哪个就调整到哪个的位置

```    #icon{
                    display: block; 
                    width: 45px;
                    height: 70px;
                    background-image: url(https://prts.wiki/images/ak.png?8efd0);
                    border: 3px solid red;
                }
```
### 2.19.9 字体图标:

相当于把图标通过unicode编码变成字体,省内存

## 2.20 less

css的扩展,使css具备一定的逻辑性计算能力

存放在 .less文件中,网页要引入对应的css,因为浏览器不支持less

VScode的插件Easy less,应该也有别的插件能做到,不过先用这个

### 2.20.1 注释:

单行注释: //

多行注释和css一样

记什么记,ctrl+/

### 2.20.2 支持运算:

加减乘除直接写计算表达式

除法要么用括号括起来,要么用 ./

如果运算中出现多个单位值,最后只会以一个单位为准

### 2.20.3 嵌套

可以生成后代选择器

:::: {.admonition .example}
代码

```    .father{
        color: red;
        .son{
            color: green;
        }
    }
```::::

用&表示当前元素,相当于this

同时可以写&:hover实现伪对象选择器

### 2.20.4 变量:

- 定义变量: \@变量名:数据;
- 使用变量: CSS属性: 变量名;

### 2.20.5 导入:

:::: {.admonition .example}
代码

```    @import '文件路径';
```::::

如果是less文件可以省略后缀

### 2.20.6 导出:

文件第一行写

:::: {.admonition .example}
代码

```    // out 路径
```::::

#### 2.20.6.1 禁止导出:

对于某些通用属性,我们不希望他们生成css

:::: {.admonition .example}
代码

```    // out:false
```::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
