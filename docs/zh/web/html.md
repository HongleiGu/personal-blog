
:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>网页</title>
        </head>
        <body>
            某个网页
        </body>
    </html>
```::::

::: tabbed-block
请自行查看
[examples/basic_html_stuff/basic_skeleton.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/basic_skeleton.html),
并确保阅读首页须知
:::
::::::
::::::::
:::::::::

## 1.2 标签

主要分为单标签和双标签 - 双标签\< html\>\< /html\> - 单标签\< img\>

### 1.2.1 html基本骨架:

#### \<!DOCTYPE html\>声明(必须有且只有第一行是这个)

声明这个文档是一个html

#### 1.2.1.1 \< html\>\< /html\>(必须有且仅有一个)

定义html文档

#### 1.2.1.2 \< head\>\< /head\>(必须有且仅有一个)

定义头文件,定义超参数

#### 1.2.1.3 \< body\>\< /body\>(必须有且仅有一个)

定义元素的主体,是直接能在网页里看到的东西

#### 1.2.1.4 \< title\>\< /title\>(必须在\< head\>中出现)

定义这个网页的名称,

#### 1.2.1.5 \< meta\>(可以没有)

描述一个html的属性,关键词等,比如\< meta charset = \"UTF-8\"\>

具体参数看这里:https://www.w3schools.com/tags/tag_meta.asp

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="2:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    %%html
    <!DOCTYPE html>
    <html>
        <head>
            <title>网页</title>
            <meta charset = "UTF-8">
        </head>
        <body>
            某个网页
        </body>
    </html>
```::::

::: tabbed-block
请自行查看
[examples/basic_html_stuff/meta.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/meta.html),
并确保阅读首页须知
:::
::::::
::::::::
:::::::::

### 1.2.2 其他标签:

#### 1.2.2.1 \< h\>\< /h\>

用于定义标题,从h1到h6

- 选择位置: 增加align属性, align = \"left\"\|\"center\"\|\"right\"

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="3:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    %%html
    <!DOCTYPE html>
    <html>
        <head>
            <title>网页</title>
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
请自行查看
[examples/basic_html_stuff/h.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/h.html),
并确保阅读首页须知
:::
::::::
::::::::
:::::::::

#### 1.2.2.2 \< p\>\< /p\>

定义段落

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
            <title>网页</title>
        </head>
        <body>
            某个网页

            <!--这里空再多空格也换不了行-->
            something
            <p>标题1</p>
            <p>标题2</p>
            <p>标题3</p>
            <p>标题4</p>
            <p>标题5</p>
            <p>标题6</p>
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/basic_html_stuff/p.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/p.html),并确保阅读首页须知
:::
::::::
::::::::
:::::::::

#### 1.2.2.3 \< br\>

换行,也可以写成\< br/\>

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="5:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>网页</title>
        </head>
        <body>
            某个网页
            <!--这里空再多空格也换不了行-->
            something
            <p>标<br>题1</p>
            <p>标题2</p>
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/basic_html_stuff/br.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/br.html),并确保阅读首页须知
:::
::::::
::::::::
:::::::::

#### 1.2.2.4 \< hr\>

水平线

属性(其实都是通用属性)

- color:设置水平线的颜色
- width:设置水平新的长度
- size: 设置水平线的高度
- align: 对齐方式

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="6:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>网页</title>
        </head>
        <body>
            某个网页

            <!--这里空再多空格也换不了行-->
            something
            <p>标题1</p>
            <hr color="red">
            <p>标题2</p>
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/basic_html_stuff/hr.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/hr.html),并确保阅读首页须知,
:::
::::::
::::::::
:::::::::

#### 1.2.2.6 \< img\>

用来显示图片

属性:

- src:图片地址,可以是网址
- alt:在图片加载不出来的时候现实的文字
- title:图片标题,鼠标位于图片上是会显示的文字
- height:图片高度
- width:图片宽度

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="7:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    %%html
    <!DOCTYPE html>
    <html>
        <head>
            <title>网页</title>
        </head>
        <body>
            <img src="https://prts.wiki/images/ak.png?8efd0" alt="测试图片" width="100" height="100" style="color:red;background-color:powderblue">
            <img src="https://prts.wi_ki/images/ak.png?8efd0" alt="测试图片" width="100" height="100" style="color:red">
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/basic_html_stuff/img.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/img.html),并确保阅读首页须知,
:::
::::::
::::::::
:::::::::

#### 1.2.2.7 \< a\>

用来实现链接

属性

- href: 跳转的网页链接，如果不定义这个和文字没有区别

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="8:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        </head>
        <body>
            <a href="https://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88" style="color:red;background-color:powderblue">
                <img src="https://prts.wiki/images/ak.png?8efd0" alt="测试图片" width="100" height="100" style="color:red;background-color:powderblue">
            </a>
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/basic_html_stuff/a.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/a.html),并确保阅读首页须知,
:::
::::::
::::::::
:::::::::

#### 1.2.2.8 文本标签类:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="9:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
这部分整合在[examples/basic_html_stuff/text.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/text.html)中,需要请自行查看,并确保阅读首页须知
:::
::::
::::::
:::::::

##### 1.2.2.8.1 \< b\>

加粗

:::: {.admonition .example}
代码

```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <b style="text-align:center" title="example">段落1</b>
            <p style="text-indent:30px;color:red">段落2</p>
            <div>这是不用p的样式</div>
        </body>
    </html>
```::::

##### 1.2.2.8.2 \< em\>

表强调

:::: {.admonition .example}
代码

```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <em style="text-align:center" title="example">段落1</em>
            <p style="text-indent:30px;color:red">段落2</p>
            <div>这是不用p的样式</div>
        </body>
    </html>
```::::

##### 1.2.2.8.3 \< del\>

划掉

:::: {.admonition .example}
代码

```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <del title="example">段落1</del>
            <p style="text-indent:30px;color:red">段<mark>落</mark>2</p>
            <div>这是不用p的样式</div>
        </body>
    </html>
```::::

##### 1.2.2.8.4 \< i\>

斜体

:::: {.admonition .example}
代码

```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <i style="text-align:center" title="example">段落1</i>
            <p style="text-indent:30px;color:red">段落2</p>
            <div>这是不用p的样式</div>
        </body>
    </html>
```::::

##### 1.2.2.8.5 \< span\>

元素没有特定的含义,如果不加样式的话(其实多数html都只是相当于封装了一个类让css可以选择而已)

:::: {.admonition .example}
代码

```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <span style="text-align:center" title="example">段落1</span>
            <p style="text-indent:30px;color:red">段落2</p>
            <div>这是不用p的样式</div>
        </body>
    </html>
```::::

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="10:1"}
::: tabbed-labels
代码整合
:::

::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <p>p:段落1</p>
            <br>
            <b>b:段落1</b>
            <br>
            <span>span:段落1</span>
            <br>
            <em>em:段落1</em>
            <br>
            <i>i:段落1</i>
            <br>
            <del>段落1</del>
            <br>
            <strong>段落1</strong>
        </body>
    </html>
```::::
:::::
:::::::
::::::::

#### 1.2.2.9 \< audio\>\< /audio\>

- src: 通过设置src属性设置播放的音频
- controls: 默认是controls,显示控制面板
- loop: 循环播放
- autoplay: 自动播放,但是浏览器会禁用

=== warning \"\" 这部分还没有示例代码,单纯忘了写以及懒得找实例音频

#### 1.2.2.10 \< video\> \< /video\>

- src: 设置视频路径
- controls: 默认是controls,显示控制面板
- loop: 循环播放
- autoplay: 自动播放,静音状态下才能autoplay
- muted: 静音播放

=== warning \"\" 这部分还没有示例代码,单纯忘了写以及懒得找实例视频

#### 1.2.2.11 \< ol\>\< /ol\>(jupyter里显示可能有问题)

有序(ordered list),中间的元素用\< li\>\< /li\>标签表示

属性:

- type:
  - 1(数字标号)
  - a(小写字母标号)
  - A(大写字母标号)
  - i(小写罗马字母标号)
  - I(大写罗马数字标号)

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="11:2"}
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
            <ol type = "1">
                <li>
                    <ol type="1">
                        <li>popcat</li>
                        <li>happycat</li>
                    </ol>
                </li>
                <li>
                    <ol type="a">
                        <li>popcat</li>
                        <li>happycat</li>
                    </ol>
                </li>
                <li>
                    <ol type="A">
                        <li>popcat</li>
                        <li>happycat</li>
                    </ol>
                </li>
                <li>
                    <ol type="i">
                        <li>popcat</li>
                        <li>happycat</li>
                    </ol>
                </li>
                <li>
                    <ol type="I">
                        <li>popcat</li>
                        <li>happycat</li>
                    </ol>
                </li>
            </ol>
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/basic_html_stuff/ol.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/ol.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.12 \< li\>\< /li\>

用来表示列表中的元素,ol里有

#### 1.2.2.13 \< ul\>\< /ul\>

unordered list, 无序列表,不过\< li\>\< /li\>没有改变

ul里面只能有li标签,多数情况下其实感觉没必要用这个,直接css设置flex然后div就行,毕竟单个组件里二级列表目前感觉都是很稀少的情况

属性:

- type:
  - disc:实心圆
  - circle:空心圆
  - square:小方块
  - none:不显示

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="12:2"}
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
            <ul type="disc">
                <li>
                    <ul type="circle">
                        <li>popcat</li>
                        <li>happycat</li>
                    </ul>
                </li>
                <li>
                    <ul type="circle">
                        <li>popcat</li>
                        <li>happycat</li>
                    </ul>
                </li>
                <li>
                    <ul type="circle">
                        <li>popcat</li>
                        <li>happycat</li>
                    </ul>
                </li>
                <li>
                    <ul type="circle">
                        <li>popcat</li>
                        <li>happycat</li>
                    </ul>
                </li>
                <li>
                    <ul type="circle">
                        <li>popcat</li>
                        <li>happycat</li>
                    </ul>
                </li>
            </ul>
        </body>
    </html>
```::::

::: tabbed-block
请自行查阅[examples/basic_html_stuff/ul.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/ul.html),并确保阅读首页须知
:::
::::::
::::::::
:::::::::

#### 1.2.2.14 \< table\>\< /table\>

- 表格:\< table\>\< /table\>
  - 属性:
    - border:表格边框
    - width:表格宽度
    - height:表格高度
- 表格元素:
  - 行:\< tr\>\< /tr\>
  - 单元格(列):\< td\>\< /td\>
  - 表头单元格: \< th\>\< /th\>
- 表格区域:
  - thead表头
  - tbody表格主体
  - tfoot表格底部

vscode里可以用table\>tr*5\>td*5快捷生成一个5\*5的表格

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="13:2"}
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
            <table border="1">
                <tr>
                    <td>元素11</td>
                    <td>元素12</td>
                </tr>
                <tr>
                    <td>元素21</td>
                    <td>元素22</td>
                </tr>
            </table>
        </body>
    </html>
```::::

::: tabbed-block
请自行查看[example/basic_html_stuff/table.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/table.html),并确保阅读首页须知
:::
::::::
::::::::
:::::::::

##### 1.2.2.14.1 合并单元格

合并方案: - 水平合并:colspan - 垂直合并:rowspan

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="14:2"}
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
            <p>合并21和22:rowspan</p>
            <p>合并35和45:colspan</p>
            <p>合并41,42,51,52:rowspan + colspan</p>
            <br>
            <table border="1" width="600px" height="400px">
                <tr>
                    <td>11</td>
                    <td>12</td>
                    <td>13</td>
                    <td>14</td>
                    <td>15</td>
                </tr>
                <!-- 原先是这样的
                <tr>
                    <td>21</td>
                    <td>22</td>
                    <td>23</td>
                    <td>24</td>
                    <td>25</td>
                </tr>
                -->
                <tr>
                    <td colspan="2">21&22</td>
                    <td>23</td>
                    <td>24</td>
                    <td>25</td>
                </tr>
                <!-- 原先是这样的
                <tr>
                    <td>31</td>
                    <td>32</td>
                    <td>33</td>
                    <td>34</td>
                    <td>35</td>
                </tr>
                -->
                <tr>
                    <td>31</td>
                    <td>32</td>
                    <td>33</td>
                    <td>34</td>
                    <td rowspan="2">35</td>
                </tr>
                <tr>
                    <td rowspan="2" colspan="2">41</td>
                    <td>43</td>
                    <td>44</td>
                </tr>
                <tr>
                    <td>53</td>
                    <td>54</td>
                    <td>55</td>
                </tr>
            </table>
        </body>
    </html>
```::::

::: tabbed-block
请自行查阅[example/basic_html_stuff/table.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/table.html),并确保阅读首页须知
:::
::::::
::::::::
:::::::::

#### 1.2.2.15 \< form\>\< /form\>

(学了vue 和 element-plus 之后感觉不太需要这个)

用于创建可以提交的表单

- action:网址
- name:表单名称, get\|post,因为要提交表单,所以自然不是delete那些

表单内的元素用\< input\>\< /input\>表示

一般来说表单包含以下三个组成部分

- 表单标签
- 表单域
- 表单按钮

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="15:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <form>
        <input type="text">请输入东西
        <input type="submit" value = "提交">
    </form>
```::::

::: tabbed-block
请自行查看[examples/basic_html_stuff/form.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/form.html),并确保阅读首页须知,
:::
::::::
::::::::
:::::::::

#### 1.2.2.16 \< input\>\< /input\>

学了vue之后比较常用,直接v-model和变量绑定

- type: 定义input种类:
- text: 文本框
  - placeholder: 定义提示词
- password: 密码框
  - placeholder: 定义提示词
- radio: 多选框
  - name: 划分组,同一组当中只会有一个被选择
  - checked: 控制选中
- checkbox: 单选框
  - checked: 控制选中
- file: 上传文件

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="16:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <input type="text">
        <input type="checkbox">
        <input type="number">
        <input type="password">
        男<input type="radio" name="gender">
        女<input type="radio" name="gender">
    </body>
    </html>
```::::

::: tabbed-block
请自行查看\[example/basic_html_stuff/input.html\]
:::
::::::
::::::::
:::::::::

#### 1.2.2.17 select:

下拉菜单

内部用option标签设置选项,checked属性表示默认选中的是哪个

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="17:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <select>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
            <option selected="select">6</option>
        </select>
    </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/basic_html_stuff/select.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/select.html),并确保阅读首页须知,
:::
::::::
::::::::
:::::::::

#### 1.2.2.18 \< textarea\>\< /textarea\>:

文本域

可以自行扩大的input,由于用法和input基本相同,不再赘述

#### 1.2.2.19 \< label\>\< /label\>:

用作某个标签的说明文本,也可以写入表单控件,增大点击范围 -
for设置for和对应表单控件的id相同 - 或者直接用label包裹表单控件

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="18:2"}
::: tabbed-labels
代码效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <input type="radio" name="gender" id="man"><label for="man">男</label>
        <label><input type="radio" name="gender">女</label>
    </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/basic_html_stuff/label.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/label.html),并确保阅读首页须知,
:::
::::::
::::::::
:::::::::

#### 1.2.2.20 \< button\>\< /button\>:

- type:
- submit: 提交按钮,可以提交数据到后台
- reset:重置按钮
- button: 普通按钮
- href: 和a标签一样,点击后跳转到链接

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="19:2"}
::: tabbed-labels
代码代码
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <input type="text">
        <input type="checkbox">
        <input type="number">
        <input type="password">
        男<input type="radio" naem="gender">
        女<input type="radio" name="gender">
        <button type="reset">reset</button>
        <button type="submit"></button>
    </body>
    </html>
```::::

::: tabbed-block
请自行查看[examples/basic_html_stuff/button.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/button.html),并确保阅读首页须知,
:::
::::::
::::::::
:::::::::

## 1.3 块元素和行内元素:

简单来说就是排版不一样,类似element-plus的组件中会因此特意提到要针对inline属性做调整

具体可以看下面这个网址,不是很必要就不写了

[点我查看](https://www.runoob.com/html/html-blocks.html)
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
