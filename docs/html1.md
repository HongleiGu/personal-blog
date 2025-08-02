
某个网页

# html

## 标签

主要分为单标签和双标签 - 双标签\< html\>\< /html\> - 单标签\< img\>

### html基本骨架:

#### \<!DOCTYPE html\>声明(必须有且只有第一行是这个)

声明这个文档是一个html

#### \< html\>\< /html\>(必须有且仅有一个)

定义html文档

#### \< head\>\< /head\>(必须有且仅有一个)

定义头文件,定义超参数

#### \< body\>\< /body\>(必须有且仅有一个)

定义元素的主体,是直接能在网页里看到的东西

#### \< title\>\< /title\>(必须在\< head\>中出现)

定义这个网页的名称,

#### \< meta\>(可以没有)

描述一个html的属性,关键词等,比如\< meta charset = \"UTF-8\"\>

具体参数看这里:https://www.w3schools.com/tags/tag_meta.asp

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
```
某个网页

### 其他标签:

#### \< h\>\< /h\>

用于定义标题,从h1到h6 - 选择位置: 增加align属性, align =
\"left\"\|\"center\"\|\"right\"

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
```
某个网页

# 标题1

## 标题2

### 标题3

#### 标题4

##### 标题5

###### 标题6

#### \< p\>\< /p\>

定义段落

```    %%html
    <!DOCTYPE html>
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
```
某个网页 something

标题1

标题2

标题3

标题4

标题5

标题6

#### \< br\>

换行,也可以写成\< br/\>

```    %%html
    <!DOCTYPE html>
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
```
某个网页 something

标\
题1

标题2

#### \< hr\>(这里显示不出来颜色,建议直接打开html文件)

水平线 属性(其实都是通用属性) - color:设置水平线的颜色 -
width:设置水平新的长度 - size: 设置水平线的高度 - align: 对齐方式

```    %%html
    <!DOCTYPE html>
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
```
某个网页 something

标题1

------------------------------------------------------------------------

标题2

#### \< img\>

用来显示图片

属性: - src:图片地址,可以是网址 - alt:在图片加载不出来的时候现实的文字 -
title:图片标题,鼠标位于图片上是会显示的文字 - height:图片高度 -
width:图片宽度

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
```
![测试图片](https://prts.wiki/images/ak.png?8efd0){width="100"
height="100" style="color:red;background-color:powderblue"}
![测试图片](https://prts.wi_ki/images/ak.png?8efd0){width="100"
height="100" style="color:red"}

#### \< a\>

用来实现链接

属性 - href: 跳转的网页链接，如果不定义这个和文字没有区别

```    %%html
    <!DOCTYPE html>
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
```
[![测试图片](https://prts.wiki/images/ak.png?8efd0){width="100"
height="100"
style="color:red;background-color:powderblue"}](https://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88){style="color:red;background-color:powderblue"}

#### 文本标签类:

##### \< b\>

加粗

```    %%html
    <!DOCTYPE html>
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
```
**段落1**

段落2

<div>

这是不用p的样式

</div>

##### \< em\>

表强调

```    %%html
    <!DOCTYPE html>
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
```
*段落1*

段落2

<div>

这是不用p的样式

</div>

##### \< del\>

划掉

```    %%html
    <!DOCTYPE html>
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
```
~~段落1~~

段[落]{.mark}2

<div>

这是不用p的样式

</div>

##### \< i\>

斜体

```    %%html
    <!DOCTYPE html>
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
```
*段落1*

段落2

<div>

这是不用p的样式

</div>

##### \< span\>

元素没有特定的含义

```    %%html
    <!DOCTYPE html>
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
```
[段落1]{style="text-align:center" title="example"}

段落2

<div>

这是不用p的样式

</div>

```    %%html
    <!DOCTYPE html>
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
```
p:段落1

\
**b:段落1**\
span:段落1\
*em:段落1*\
*i:段落1*\
~~段落1~~\
**段落1**

#### \< audo\>\< /audio\>

- src: 通过设置src属性设置播放的音频
- controls: 默认是controls,显示控制面板
- loop: 循环播放
- autoplay: 自动播放,但是浏览器会禁用

#### \< video\> \< /video\>

- src: 设置视频路径
- controls: 默认是controls,显示控制面板
- loop: 循环播放
- autoplay: 自动播放,静音状态下才能autoplay
- muted: 静音播放

#### \< ol\>\< /ol\>(jupyter里显示可能有问题)

有序(ordered list),中间的元素用\< li\>\< /li\>标签表示

属性: - type: - 1(数字标号) - a(小写字母标号) - A(大写字母标号) -
i(小写罗马字母标号) - I(大写罗马数字标号)

列表可以嵌套,但是同样需要\< li\>\< /li\>标签

```    %%html
    <!DOCTYPE html>
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
```
1.  1.  popcat
    2.  happycat
2.  a.  popcat
    b.  happycat
3.  A.  popcat
    B.  happycat
4.  i.  popcat
    ii. happycat
5.  I.  popcat
    II. happycat

#### \< li\>\< /li\>

用来表示列表中的元素

#### \< ul\>\< /ul\>

unordered list, 无序列表,不过\< li\>\< /li\>没有改变

ul里面只能有li标签 属性: - type: - disc:实心圆 - circle:空心圆 -
square:小方块 - none:不显示

```    %%html
    <!DOCTYPE html>
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
```
- - popcat
  - happycat
- - popcat
  - happycat
- - popcat
  - happycat
- - popcat
  - happycat
- - popcat
  - happycat

#### \< table\>\< /table\>

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

vscode里可以用table\>tr[\\(\*\\)]{.arithmatex}5\>td[\\(\*\\)]{.arithmatex}5快捷生成一个5[\\(\*\\)]{.arithmatex}5的表格

```    %%html
    <!DOCTYPE html>
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
```
  -------- --------
  元素11   元素12
  元素21   元素22
  -------- --------

##### 合并单元格

合并方案: - 水平合并:colspan - 垂直合并:rowspan

```    %%html
    <!DOCTYPE html>
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
```
合并21和22:rowspan

合并35和45:colspan

合并41,42,51,52:rowspan + colspan

\

+-----+-----+----+----+----+
| 11  | 12  | 13 | 14 | 15 |
+-----+-----+----+----+----+
| 21&22     | 23 | 24 | 25 |
+-----+-----+----+----+----+
| 31  | 32  | 33 | 34 | 35 |
+-----+-----+----+----+    |
| 41        | 43 | 44 |    |
|           +----+----+----+
|           | 53 | 54 | 55 |
+-----------+----+----+----+

#### \< form\>\< /form\>

用于穿件可以提交的表单 - action:网址 - name:表单名称,
get\|post,因为要提交表单,所以自然不是delete那些

表单内的元素用\< input\>\< /input\>表示

一般来说表单包含以下三个组成部分 - 表单标签 - 表单域 - 表单按钮

```    %%html
    <form>
        <input type="text">请输入东西
        <input type="submit" value = "提交">
    </form>
```
请输入东西

#### \< input\>\< /input\>

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

#### select:

下拉菜单

内部用option标签设置选项,checked属性表示默认选中的是哪个

#### \< textarea\>\< /textarea\>:

文本域

#### \< label\>\< /label\>:

用作摸个标签的说明文本,也可以写入表单控件,增大点击范围 -
for设置for和对应表单控件的id相同 - 或者直接用label包裹表单控件

#### \< button\>\< /button\>:

- type:
- submit: 提交按钮,可以提交数据到后台
- reset:重置按钮,这个重置应该是都清空
- button: 普通按钮

## 块元素和行内元素:

https://www.runoob.com/html/html-blocks.html#:\~:text=HTML%20%3Cdiv%3E%20%E5%85%83%E7%B4%A0%E6%98%AF%E5%9D%97%E7%BA%A7%E5%85%83%E7%B4%A0%EF%BC%8C%E5%AE%83%E5%8F%AF%E7%94%A8%E4%BA%8E%E7%BB%84%E5%90%88%E5%85%B6%E4%BB%96%20HTML%20%E5%85%83%E7%B4%A0%E7%9A%84%E5%AE%B9%E5%99%A8%E3%80%82%20%3Cdiv%3E%20%E5%85%83%E7%B4%A0%E6%B2%A1%E6%9C%89%E7%89%B9%E5%AE%9A%E7%9A%84%E5%90%AB%E4%B9%89%E3%80%82%20%E9%99%A4%E6%AD%A4%E4%B9%8B%E5%A4%96%EF%BC%8C%E7%94%B1%E4%BA%8E%E5%AE%83%E5%B1%9E%E4%BA%8E%E5%9D%97%E7%BA%A7%E5%85%83%E7%B4%A0%EF%BC%8C%E6%B5%8F%E8%A7%88%E5%99%A8%E4%BC%9A%E5%9C%A8%E5%85%B6%E5%89%8D%E5%90%8E%E6%98%BE%E7%A4%BA%E6%8A%98%E8%A1%8C%E3%80%82,%3Cdiv%3E%20%E5%85%83%E7%B4%A0%E7%9A%84%E5%8F%A6%E4%B8%80%E4%B8%AA%E5%B8%B8%E8%A7%81%E7%9A%84%E7%94%A8%E9%80%94%E6%98%AF%E6%96%87%E6%A1%A3%E5%B8%83%E5%B1%80%E3%80%82%20%E5%AE%83%E5%8F%96%E4%BB%A3%E4%BA%86%E4%BD%BF%E7%94%A8%E8%A1%A8%E6%A0%BC%E5%AE%9A%E4%B9%89%E5%B8%83%E5%B1%80%E7%9A%84%E8%80%81%E5%BC%8F%E6%96%B9%E6%B3%95%E3%80%82%20%E4%BD%BF%E7%94%A8%20%3Ctable%3E%20%E5%85%83%E7%B4%A0%E8%BF%9B%E8%A1%8C%E6%96%87%E6%A1%A3%E5%B8%83%E5%B1%80%E4%B8%8D%E6%98%AF%E8%A1%A8%E6%A0%BC%E7%9A%84%E6%AD%A3%E7%A1%AE%E7%94%A8%E6%B3%95%E3%80%82%20%3Ctable%3E%20%E5%85%83%E7%B4%A0%E7%9A%84%E4%BD%9C%E7%94%A8%E6%98%AF%E6%98%BE%E7%A4%BA%E8%A1%A8%E6%A0%BC%E5%8C%96%E7%9A%84%E6%95%B0%E6%8D%AE%E3%80%82

# css

## 一般格式:

选择器 {属性1:值;属性2:值}

差不多和json很像

例:(这里直接写入html)

### 注意:由于jupyter notebook直接使用html,更改css可能会导致jupyter notebook整个格式错乱,记得重置

```    #! pip install --upgrade jupyterthemes
    # 也可以用这个设置jupyter风格,不过我习惯默认
    !jt -r
    # refresh the page to reload css
    # remember to save!!!
```
```    Reset css and font defaults in:
    /root/.jupyter/custom &
    /root/.local/share/jupyter/nbextensions
```
```    %%html
    <!DOCTYPE html>
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
```
某个网页

# 标题1

## 标题2

### 标题3

#### 标题4

##### 标题5

###### 标题6

## css的引入方式:

### 行内(不建议)

通过style通用html标签属性直接写在标签里(不建议使用)

```    %%html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <p style="text-indent:30px;color:red">行内css</p>
            <p>不用css</p>
        </body>
    </html>
```
行内css

不用css

### \< style\>\< /style\>

可以直接在\< head\>\< /head\>中添加\< style\>\<
/style\>来定义整个html的css

注意:如果通过\< a\>跳转到其他页面\< style\>\< /style\>里的格式不会生效

```    %%html
    <!DOCTYPE html>
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
```
### \< link\>

通过\< link\>引入外部css文件

同样,跳转到其他页面不会生效

注意,虽然是外部文件,但是这里加载依然会改变整个jupyter
notebook的css,不建议在这里运行

```    %%html
    <!DOCTYPE html>
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
```
某个网页

# 标题1

## 标题2

### 标题3

#### 标题4

##### 标题5

###### 标题6

## css选择器

### 全局选择器:

应用到所有元素上,优先级最低,一般是样式初始化

```    *{
        margin: 0;
        padding: 0;
    }
```
### 元素选择器:

标签名 {属性:值;}

可以是任何html文档中的标签,但是只能同时改变所有这种标签的样式

之前已经有很多这种例子了

```    p{
        font-size:14px;
        color:red;
    }
```
### 类选择器:

需要现在要改样式的标签里定义class属性,然后根据class名写css

- 可以对多种标签使用
- 类名不能以数字开头
- 同一个标签可以用多个类选择器,加上空格隔开的多个class属性就行,如果属性冲突,会优先使用第一个可适用的属性定义

```    # 假设我们有一个class叫example
    .example{
        color:purple;
    }
    # 会应用到如下tag上,注:something这个标签不存在,可以是任意标签
    <something class="example">...</something>
    <something class="example" class="example1">...</something>
```
### id选择器

针对一个特定的标签使用,只能使用一次,css中用#定义 -
id是唯一的(规范上不能重复,语法上可行) - id不能以数字开头

```    #something{
        border:3px dashed green;
    }
```
### 合并选择器

提取相同的样式,减少重复代码

选择器1,选择器2{}

```    .h1.p{
        color:green;
    }
```
### 其他选择器

#### 后代选择器

选择所有被符合选择器1的标签包含的选择器2类标签

```    ul li{
        color:green
    }
```
#### \>选择器：

只选择直接作为选择器1的标签的选择器2类标签应用css,不对更深的标签起作用

可以和上面的选择器一起用

```    ul>li{
        color:green;
    }
```
#### +选择器:

选择跟在符合选择器1条件的标签之后的选择器2类标签应用css

可以和上面的选择器一起用

```    .example+p{
        color:red;
    }
```
#### \~选择器:

选择跟在符合选择器1条件的标签之后的所有选择器2元素,和后代选择器不同的是这个不在选择器1标签里

```    .example~p{
        color:red;
    }
```
### 伪对象选择器:

给元素追加一个虚拟标签,可以节省html的资源开销 -
::after在后面添加一个对象,虚拟对象,装饰作用 -
::before在前面添加一个对象,虚拟对象,装饰作用 -
:nth-chlid(n),选择的n个子元素 - :first-chlid,选择第一个子元素 -
:last-child,选择最后一个子元素 - content(必须有,否则伪对象无效)

其他查表:https://www.w3schools.com/cssref/css_selectors.php

### 优先级

行内样式\>ID选择器\>类选择器\>元素选择器

## css特性

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

## 字体属性:

### color:

- color
  - 各种颜色: 查表https://www.w3schools.com/colors/colors_names.asp
  - 色值:(茴香豆有4种写法,色值有5种写法)
  - RGB值:rgb(255,99,71),三个值分别对应rgb三个值,取值范围0-255
    - \< p style=\"background-color:rgb(255, 99, 71)\"\>html\< /p\>:

      rgb(255,99,71)
  - HEX值:#ff6347,和上面差不多,每两位表示RGB中的一个值,前面加上井号
    - \< p style=\"background-color:#ff6347\"\>html\< /p\>:

      #ff6347
  - RGBA值:rgba(255,99,71,1),rgba加上透明度(这个应该是可以的,但是jupyter不知道为什么会把style吞掉,如果%%html没问题,直接markdown不显示颜色)
    - \< p style=\"background-color:rgba(255, 99, 71, 0.5)\"\>\< /p\>:

      rgba(9, 100%, 64%, 0.5)

```    div{color:red;}
    div{color:#ff0000;}
    div{color:rgb(255,0,0)}
    div{color:rgba(255.0,0,.5)}
```
### font-size

某些浏览器有最小字体大小

```    div{font-size:10px;}
```
### font-weight:

设置文本的粗细 - bold:加粗 - bolder:更粗 - lighter:更细 -
100-900:默认400,bold700

```    #5 {font-weight:normal}
    #6 {font-weight:bold}
    #7 {font-weight:bolder}
    #8 {font-weight:lighter}
    #9 {font-weight:360}
```
### font-style:

设置文本的字体样式 - normal:默认 - italic:斜体字

```    #10 {font-style:normal}
    #11 {font-style:italic}
```
### font-family:

用来指定一个元素的字体,如果字体名称包含空格,则必须用引号包裹

### line-height:

设置文本间距,单倍间距或者双倍间距等 - 数字px - 数据(几倍行距)

### font:

把上面所有font属性写到一起

字号和字体值必须写,不然不生效

### text-indent:

文本缩进 - 数字px - 数字em(1em是当前标签的字号大小)

### text-align:

内容对齐,默认是left,居中的是文字,不是标签

### text-decoration:

加上修饰线 - none; - underline - line-through - overline

```    div {
        # font-style, font-weight font-size line-height font-family
        font: italic 700 30px/2 楷体;
    }
```
```      Cell In[2], line 1
        div {
            ^
    SyntaxError: invalid syntax
```
## 背景

### background-color

和color一样

### background-image

那个url()里面可以填本地地址,直接从本地访问图片

```    .box{
        width: 600px;
        height: 600px;
        background-image: url("some url")
    }
```
### background-repeat:

设置图片如何重复: -
repeat:默认属性,在分配的空间大于图片大小的时候会像两个方向重复图片 -
repeat-x:只在x方向上重复图片 - repeat-y:只在y方向上重复图片 -
no-repeat:不重复图片

```    .box{
        background-image:url("something");
        background-repeat:no-repeat;
    }
```
### background-size:

设置背景图片的大小 -
length:设置背景图片的宽度和高度,可以只设置一个值,另一个会默认成auto -
percentage:设置图片占相对区域面积的百分比,可以只设置一个值,另一个会默认成auto -
cover:将图片设置成能完全覆盖背景区域的最大大小 -
contain:保持图片和总比并且放缩成适合背景定位的最大大小

```    .box{
        background-image: url("something");
        background-size 100% 100%;
    }
```
### background-position:

以下都是第一个位置为水平位置,第二个为垂直位置,英文字面意思,不要多想 -
left top - left center - left bottom - right center - right bottom -
center top - center center - center bottom - x% y% - xpos ypos

```    .box{
        background-image: url("something");
        background-position: left top;
    }
```
### background-attachment

使背景不会跟着元素移动

### background复合:

把上面所有属性写到一起,空格隔开,不区分顺序

## 文本属性

### text-align

文本对齐方式,英文字面意思 - left - right - center

```    h1 {
        text-align:center
    }
```
### text-decoration:

添加到文本的修饰,下划线,上划线,删除线等,英文字面意思? - underline -
overline - line-through

```    h1 {
        text-decoration:underline;
    }
```
### text-transform

还是英文字面意思 - captialize - uppercase - lowercase

```    h1 {
        text-transform:uppercase;
    }
```
### text-indent:

定义缩进,直接是x px

```    h1 {
        text-indent:30px;
    }
```
## 表格属性

### border：

定义表格边框： - 边框距离 - 边框样式 - 边框颜色

```    table,td{
        border: 1px solid black;
    }
```
### border-collapse:

设置边框是折叠成一个单一的边框还是隔开

```    table{
        border-collapse:collapse;
    }
```
### padding:\< td\>\< /td\>和\< th\>\< /th\>的属性

填充四周

```    td{
        padding:15px;
    }
```
## css盒子模型:

封装周围的html元素的整体框架 - margin 外边距,透明的 - border 边框 -
padding 内边距,透明的 - content
实际内容,编辑weight和height的时候实际编辑的是content部分的大小

针对这几个有一堆的css属性,具体自己查https://www.w3schools.com/cssref/index.php

一般border属性都以border开头

常用的对于以上四个都适用的,英文字面意思 - margin-top - margin-bottom -
margin-left - margin-right - border-top - border-bottom - border-left -
border-right - padding-top - padding-bottom - padding-left -
padding-right

盒子大小 - 默认:盒子大小= 内容尺寸 + border尺寸 + 内边距尺寸

margin不算进盒子

![c18e6bf9f1b4991cc11c6af699fe773.png](attachment:c18e6bf9f1b4991cc11c6af699fe773.png) -
border和padding会撑大盒子 - 解决: - 手动做减法 - 内减模式:
box-sizing:border-box

### 外边距问题:

子级添加margin会导致父元素塌陷

解决办法: - 取消自己margin,父级设置padding - 父级设置overflow:hidden -
父级设置border-top

### 行内元素内外边距问题:

行内元素添加margin和padding无法改变垂直位置

解决问题: 加line-height

### 清除默认样式:

比如p标签的空白

```    * {
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
    }
```
### 元素溢出:

用overflow控制,或者overflow-x,overflow-y - scroll :
无论是否溢出都有滚动条 - hidden: 隐藏溢出部分 - auto:
自动识别,溢出就加scroll

### border-radius

创建圆角 - 设置一个值:四个角圆角相同 -
设置两个值:第一个为左上角和右下角,第二个值为右上角和左下角 -
设置三个值:第一个为左上角,第二个为右上角和左下角,第三个是右下角 -
设置四个值:第一个为左上角,第二个为右上角,第三个为左下角,第四个是右下角

```    #border-radius1{
                width:200px;
                height:200px;
                background:violet;
                border-radius:20px;
            }
```
### box-shadow

一共四个值: - h-shadow(必选):水平阴影的位置 -
v-shadow(必选):垂直阴影的位置 - blur(可选):模糊距离 -
color(可选):阴影的颜色

```    #box-shadow1{
                width:200px;
                height:200px;
                background:aqua;
                box-shadow: 10px 20px
            }
```
## css弹性盒子

弹性元素由弹性容器和弹性子元素组成,通过设置display的属性将其定义为弹性容器

弹性盒子默认横向摆放 - display:flex 启用弹性盒子,默认为水平排列

这种子元素可以自动基岩或拉伸

组成部分: - 弹性容器 - 弹性盒子 - 主轴: 默认在水平方向 - 侧轴:
默认在垂直方向

### justify-content:

- flex-start: 默认值,从七点开始依次排列
- flex-end: 弹性盒子从终点开始依次排列
- center: 主轴居中
- space-between: 均匀排列,空白在盒子中间
- space-around: 均匀排列,空白在盒子两侧
- space-evenly: 弹性盒子和容器之间间距相等

### flex-direction:

- row 横向从左到右摆放
- row-reverse 横向从右到左摆放
- column 纵向从上到下排列
- column-reverse 纵向从下到上排列

### align-items:

- flex-start
- flex-end
- center

### align-self:

单独控制某个弹性盒子的侧轴排列方式 - stretch: 沿着测轴拉伸至铺满容器 -
center: 居中 - flex-start: 起点开始排列 - flex-end:
弹性盒子从终点开始依次排列

### flex:

控制弹性盒子在主轴方向的尺寸

属性值: 政治素质,表示占用父级元素剩余尺寸的分数,默认是1

### flex-grow:

设置扩展因子,会根据弹性盒子的扩展因子分配剩余空间

可以设置扩展因子让各个元素大小自动按比例分配

各个元素的比例=扩展因子+1

### flex-wrap:

弹性盒子可以自动挤压或者拉伸,默认情况下,所有天哪星河在一行显示

- wrap: 换行
- no-wrap: 不换行(默认)

### align-content

这个是不会对单行生效的,和align-itmes似乎是一个东西

- flex-start: 默认值,从七点开始依次排列
- flex-end: 弹性盒子从终点开始依次排列
- center: 主轴居中
- space-between: 均匀排列,空白在盒子中间
- space-around: 均匀排列,空白在盒子两侧
- space-evenly: 弹性盒子和容器之间间距相等

## 文档流:

### 问题:

#### 空格折叠

无论放多少个空格都会被折叠成一个空格

#### 元素无间隙:

如果有两个并排的图片一起放置,中间是没有间隙的

### 解决:

脱离文档流: - 浮动 - 绝对定位 - 固定定位

#### 浮动:

float属性:(只有左右浮动,没有上下浮动),可以是元素拖了文档流 -
left(向左浮动) - right(向右浮动)

元素同时向一方向浮动的时候,会变成水平摆放,向左或者向右

当容器大小不足的时候会在下一行摆放

#### 清除浮动:

清除浮动会导致某些元素的位置发生变化,后续元素会收到影响

比如如果父级元素没有高度,子级元素无法撑开父级高度 - 父元素设置相应属性 -
增加clear属性, clear:both - overflow清除浮动 - 伪对象方式,
在父级对象加上一个::after或者::before选择器,设置clear:both

##### clear

- left(清除左浮动)
- right(清除右浮动)
- both(清除左右浮动,如果有的话)

##### overflow:

如果父元素出了问题,同级元素受到影响,可以用overflow清除浮动,这种情况下不能设置父元素的高度 -
visible(全部铺在页面上) - hidden(隐藏) - clip(把多的部分隐藏) -
scroll(增加一个可滚动的轴,大小不调整) - auto(自适应)

## 定位:

position属性 - relative - absolute(脱离文档流) - fixed(脱离文档流)

可以使用left,top,right,bottom四个属性调整位置

对于absolute可以理解成每一个absolute的元素都在一个新的图层上(子绝父相)

fixed一般来说不会有这个问题,因为fixed元素会跟着页面滚动

设置定位后定位随着能定位的父元素决定,直到顶层文档

  定位方式                                 属性值     是否脱离标准流(文档流)   显示模式               参照物
  ---------------------------------------- ---------- ------------------------ ---------------------- ------------------------------------
  相对定位                                 relative   否                       保持标签原有显示模式   自己原来的位置
  绝对定位                                 absolute   是                       行内块特点             已经定位的祖先元素或者浏览器可视区
  固定定位                                 fixed      是                       行内块特点             浏览器窗口
  \### z-index:                                                                                       
  解决图层问题,后来者居上,取值越大越靠上                                                              

## transition:

- 可以在一个元素不同状态之间切换的时候添加过渡效果
- transition: 过渡属性,花费时间
- 注意:
- 过渡属性可以是具体的css属性
- 也可以设置为all,所有不同的属性值都产生过渡效果
- transition设置给元素本身
- 一般和伪对象选择器一起使用,设置不同状态

## opacity:

设置整的元素的透明度,0-1

## SEO:

尽量让网页在搜索引擎里靠前,一般企业里会用

方法: - 氪金 - 网页后缀设置为html -
标签语义化(在合适的地方使用合适的标签) 网页SEO标签 - title: 网页标题标签
\< head\>里的\< title\> - description:网页描述 \< head\>里的\< meta
name=\"description\"\> - keywords: 网页关键词 \< head\>里的\< meta
name=\"keywords\"\>

## Favicon图标:

出现在浏览器标题栏的图标

```    <link rel="shortcut icon" href="文件名" type="image/x-icon">
```
## 各种效果:

### 二维

#### 平移:

transition和translate实现

#### 旋转效果:

```    transform: rotate(角度)
```
https://developer.mozilla.org/zh-CN/docs/Web/CSS/transform-function/rotate

#### 转换原点:

```    transform-origin: 水平位置 垂直位置
```
#### 复合效果:

```    transform: translate() rotate() 
```
transform属性有层叠性,不能一个一个写,必须写进一个transform属性里

#### 缩放:

```    transform: scale(缩放倍数)
```
或者

```    transform: scale(X缩放倍数,Y缩放倍数)
```
#### 倾斜:

transform: skew(角度);

#### 背景渐变:

##### 线性:

```    background-image linear-gradient(
        渐变方向(角度或者to),
        颜色1, 终点位置(可不写)
        颜色2, 终点位置(可不写)
    )
```
https://developer.mozilla.org/zh-CN/docs/Web/CSS/gradient/linear-gradient

##### 径向

```    background-image radial-gradient(
        半径 at 圆形位置(x位置 y位置),
        颜色1, 终点位置(可不写)
        颜色2, 终点位置(可不写)
    )
```
半径可以是两条,这种情况会变成椭圆

### 空间转换:

#### 平移:

```    transform: translate3d(x,y,z); /*这里必须逗号隔开*/
    transform: translateX();
    transform: translateY();
    transform: translateZ();
```
默认z是没有效果的,但是可以给父级元素设置视距

#### 视距

perspective: 视距

添加给直接父级元素

#### 旋转

```    transform: rotateX(值);
    transform: rotateY(值);
    transform: rotateZ(值);
```
或者

```    transform: rotate3d(x,y,z,角度); /*x,y,z是0-1之间的数字*/
```
#### 立体呈现:

```    transform-style: 属性
```
- flat: 子级处于平面中
- preserve-3d: 自己处于3D空间

#### 空间缩放:

```    transform: scale3d(x,y,z);
```
## 动画:

用@keyframes创建动画,这个会一直重复播放

属性太多了,建议自己查表https://www.w3schools.com/css/css3_animations.asp

同时要在对应的元素上加animation属性

```    animation: 动画名称 动画时长 速度曲线 延迟时间 重复次数 动画方向 执行完毕时状态
```
比如

```    #breath:hover{
        animation: breath 2700ms ease-in-out 0s infinite alternate running;
    }
```
或者茶城多个属性值去写 - animation-name - animation-duration -
animation-delay - animation-fill-mode - forwards: 最后一帧状态 -
backwards: 第一帧状态 - animation-timing-function - linear -
ease-in-out - step() - \... - animation-iteration-count - infinite -
数字 - animation-direction - alternate为反向 - animation-play-state -
paused为暂停

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
```
## 兼容不同设备:

- 分辨率:
- 物理分辨率: 出厂设置,电脑显示屏分辨率
- 逻辑分辨率: 调节之后的的分辨率

### 视口:

```    <meta name="viewport" content="width=device-width, initial-scale=1.0">
```
这个大概率不用动,vscode自动生成

表示 - 视口宽度=设备宽度 - 缩放一倍(不缩放)

### 二倍图:

- 移动端参考iPhone6/7/8,设备宽度375px产出设计稿
- 二倍图设计稿尺寸: 宽750px

### 适配方案:

- 宽度适配:宽度自适应,pc端网页
- 百分比布局
- flex布局
- 注意:这两个不能高度自适应
- 等比适配:宽高等比缩放,移动端网页
- rem
- vw

#### rem:

rem是个相对单位,表示1HTML字号大小,是相对HTML标签字号计算出的单位

#### vw vh

也是相对单位,相对试图的尺寸的计算结果,50vw表示50%视图宽

#### 媒体查询:

检测视口的宽度,编写差异化的css, 如果用rem调整大小,只需要固定html字号即可

先设置\< meta\>

用@media创建媒体查询,在不同屏幕大小下设置不同比例

```    @media screen and (max-width:768px) and (min-width:996px){
                    #box{
                        background-color:aqua;
                    }
                    #p{
                        display:none;
                    }
                }
```
#### rem-flexible.js

```    <script src=""></script>
```
##### px转rem

一般设计稿是375px视口,

所以[\\(rem = \\frac{px}{根字号}\\)]{.arithmatex}

### 雪碧图/精灵图

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
### 字体图标:

相当于把图标通过unicode编码变成字体,省内存

## less

css的扩展,使css具备一定的逻辑性计算能力

存放在 .less文件中,网页要引入对应的css,因为浏览器不支持less

VScode的插件Easy less,应该也有别的插件能做到,不过先用这个

### 注释:

单行注释: //

多行注释和css一样

记什么记,ctrl+/

### 支持运算:

加减乘除直接写计算表达式

除法要么用括号括起来,要么用 ./

如果运算中出现多个单位值,最后只会以一个单位为准

### 嵌套

可以生成后代选择器

```    .father{
        color: red;
        .son{
            color: green;
        }
    }
```
用&表示当前元素,相当于this

同时可以写&:hover实现伪对象选择器

### 变量:

- 定义变量: \@变量名:数据;
- 使用变量: CSS属性: 变量名;

### 导入:

```    @import '文件路径';
```
如果是less文件可以省略后缀

### 导出:

文件第一行写

```    // out 路径
```
#### 禁止导出:

对于某些通用属性,我们不希望他们生成css

```    // out:false
```
# js:

有的用es5,有的用es6,看情况

由于notebook里经常会由于手残多次运行一个cell里的代码,用let定义变量不方便,于是以下代码经常有用var的情况,实际开发似乎let居多

## 书写位置

### 直接写在html里面\< script\>\< /script\>

规范问题把js的\< script\>\< /script\>写到\< body\>\< /body\>里面的最下面

### 引入外部js

还是\< script\>\<
/script\>,引用和之前一样,相对引用和绝对应用,通过src属性定义js文件路径,如果有src属性,\<
script\>\< /script\>之间的js语句不会被执行

### 内联js:

可以写入标签内部,vue会用这种模式

## 注释:

### 单行注释

```    // 我是单行注释
```
### 块注释

```    /*
    我是块注释
    */
```
js语句末尾要加分号,不过实际开发中可写可不写,但是尽量要格式统一

## 输入输出

### document.write()

相当于把html当做txt直接写

```    document.write('我是div标签')//这个不会有标签
    document.write('<h1>我是标题</h1>')//这个会直接变成h1标签
```
### alert

直接在浏览器弹出警告

```    alert("alert")
```
### console.log()

在控制台打印,网页上不可见

```    console.log("console")
```
```    console
```
### prompt

让用户输入东西

```    prompt("输入东西:")
```
```    evalmachine.<anonymous>:1

    prompt("输入东西:")

    ^



    ReferenceError: prompt is not defined

        at evalmachine.<anonymous>:1:1

        at Script.runInThisContext (vm.js:120:18)

        at Object.runInThisContext (vm.js:309:38)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
## 各种量

### 变量赋值:

- let
- var

相当于kotlin的var和val,val不允许重新赋值

let可以一行声明多个变量但是不推荐

### 常量:

const

相当于java的final,kotlin的const

```    const a =10
    a =5
```
```    evalmachine.<anonymous>:2

    a =5

      ^



    TypeError: Assignment to constant variable.

        at evalmachine.<anonymous>:2:3

        at Script.runInThisContext (vm.js:120:18)

        at Object.runInThisContext (vm.js:309:38)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
## 数据类型:

- number
- string
- boolean
- undefined
- null

### number:

js的数字部分浮点和整型

常见运算符和python,java等一致

#### NAN:

如果出现数据类型的错误,比如字符串减数组会得到NAN(熟悉的not a number)

任何和NaN的运算都会返回NaN

```    let a = "string"
    console.log(a - 2)
    console.log((a - 2) + 1)
```
```    NaN
    NaN
```
### string:

比python,java等多一个可以用\`\`包裹

同时,js是弱类型语言,可以实现字符串加数字等让某些魔怔人发出尖锐爆鸣声的操作

```    let str = `string`
    console.log(str + 19)
```
```    string19
```
#### 反引号包裹的模版

和.format,printf,以及kotlin的\$差不多,但是模板字符串只能用反引号包裹

```    var a = 19
    console.log(`这里有${a}个人`)
```
```    这里有19个人
```
### boolean

熟悉的boolean,在哪里都差不多

在js里 \'\',0,undefined, null, false,
NaN在逻辑运算上和false等价,其余都是True

### undefined:

Java和kotlin的null,python的None

### null:

这个和上面的区别在于 - undefined表示没有赋值 - null是赋值了,但是内容为空

```    console.log(undefined + 1)
    console.log(null + 1)
```
```    NaN
    1
```
### 监测数据类型:

typeof函数,理论上这个函数可以不写括号,但是可能会被强迫症打死

```    console.log(typeof(undefined))
    console.log(typeof(1))
```
```    undefined
    number
```
### 类型转换:

同样有两种类型转换

#### 隐式类型转换:

某些运算符执行的时候会自动转变类型,比如字符串加数字的时候会自动把数字变成字符串,+可以转换成数字型

#### 显示类型转换:

python的写法,js的类型 - Number() - 如果字符串内容理由非数字,会返回NaN -
NaN的类型是number - parseInt() - 只留整数 - parseFloat() - 可以保留小数

```    var num1 = "2.89"
    var num2 = "2.89px"
    console.log("num1")
    console.log(typeof(num1),num1)
    console.log(typeof(Number(num1)),Number(num1))
    console.log(typeof(parseInt(num1)),parseInt(num1))
    console.log(typeof(parseFloat(num1)),parseFloat(num1))
    console.log("num2")
    console.log(typeof(num2),num2)
    console.log(typeof(Number(num2)),Number(num2))
    console.log(typeof(parseInt(num2)),parseInt(num2))
    console.log(typeof(parseFloat(num2)),parseFloat(num2))
```
```    num1
    string 2.89
    number 2.89
    number 2
    number 2.89
    num2
    string 2.89px
    number NaN
    number 2
    number 2.89
```
## 运算符

### 赋值运算符:

和python,jave那些都差不多 - = - += - -= - /= -
[\\(\\dots\\)]{.arithmatex}

### 自增自减

- i++
- i\--
- \--i
- i\--

java里念了好几遍了,一个先输入后赋值,一个先赋值后输入

### 比较运算符:

- [\\(\>\\)]{.arithmatex}
- [\\(\<\\)]{.arithmatex}
- [\\(\>=\\)]{.arithmatex}
- [\\(\<=\\)]{.arithmatex}
- [\\(==\\)]{.arithmatex} 左右两边值是否相等
- [\\(===\\)]{.arithmatex} 左右两边是否之和类型都相等
- [\\(!==\\)]{.arithmatex} 左右两边是否不全等

会有隐式数据转换

```    console.log(2=="2")
    console.log(2==="2")
    console.log(2!="2")
    console.log(2!=="2")
```
```    true
    false
    false
    true
```
### 逻辑运算符:

- &&
- \|\|
- !

和java一样

js是有和Python一样的or None语法的

```    var x = null
    var a = 5
    console.log(a || 0)
    console.log(x || 0)
```
```    5
    0
```
一般是用来处理null的,并且python,java,js等语言 - a \|\| b,
a为真则不判断b - a && b, a为假则不判断b

## 语句:

### 条件:

#### if:

```    '' == false // ''在逻辑判断里可以当做false
    0 == false
    1 == true // 除了0以外的所有数字都是true
```
```    if (0){
        console.log("我执行了")
    }
    else if(''){
        console.log("如执行")
    }
    else{
        console.log("我没执行")
    }
```
```    我没执行
```
#### 三元运算符:

和java完全一样

```    var a = '' ? 1000 : 2345
    console.log(a)
```
```    2345
```
#### switch:

没记错的话好像也适合java的,但是就算是java里也不常用,kotlin里是when

就是注意switch要求的是值和数据类型全部相等,不是只有值相等就行

一般要搭配break使用,不然会每个条件都判断一次

```    var a = 2
    switch(a){
        case 1:
            console.log("1");
            break
        case "2":
            console.log("'2'")
            break
        case 2:
            console.log("2")
            break
    }
```
```    2
```
### 循环:

#### while:

这东西真的有人不会用吗?

```    var a = 0
    while(++a <= 10){
        console.log(a);
    }
```
```    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
```
#### do while:

有点多此一举的样子,就算是java里也不常用

```    var a = 0
    do{
        console.log(++a)
    }
    while(a < 10)
```
```    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
```
#### for

和java的一致

```    for(var a = 0; a <= 5; a++){
        console.log(a)
    }
```
```    0
    1
    2
    3
    4
    5
```
```    var a = 0
    for(;++a <=5;){
        console.log(a)
    }
```
```    1
    2
    3
    4
    5
```
#### break continue

break是直接跳出整个循环

continue是进入下一次循环

和java类似,可以 锚点1:固定一个点之后直接continue锚点实现类似goto的效果

```    var a = 0
    while(++a < 10){
        if (a == 5){
            break
        }
        console.log(a);
    }
```
```    1
    2
    3
    4
```
```    var a = 0
    while(++a < 10){
        if (a == 5){
            console.log("我跳出去了")
            continue
        }
        console.log(a);
    }
```
```    1
    2
    3
    4
    我跳出去了
    6
    7
    8
    9
```
## 数组:

### 声明:

虽然js应该和java是一家人,但是js是弱类型语言,和python一样不用再new数组的时候声明变量类型,数组内可以存任何东西

```    var a = [1,2,3,4]
    console.log(a)
    var b = new Array(1,2,3,4)
    console.log(b)
```
```    [ 1, 2, 3, 4 ]
    [ 1, 2, 3, 4 ]
```
### 索引:

这个世界上难道存在索引值不从0开始的语言?

```    a[0]
```
```    1
```
### 遍历:

```    for (let i = 0; i < a.length; i++){
        console.log(a[i])
    }
```
```    1
    2
    3
    4
```
### 增:

```    var a = [1,2,3,4,5,6,7,8,9,0]
    a.push(1008,6) // 在末尾加元素
    console.log(a)
    a.unshift(1008,6) // 在头部加元素
    console.log(a)
```
```    [
         1, 2, 3, 4, 5,
         6, 7, 8, 9, 0,
      1008, 6
    ]
    [
      1008, 6,    1, 2, 3,
         4, 5,    6, 7, 8,
         9, 0, 1008, 6
    ]
```
### 删:

```    var a = [1,2,3,4,5,6,7,8,9,0]
    a.pop() // 和python一样,返回并删除最后一个值
    console.log(a)
    a.shift()
    console.log(a) // 返回并删除第一个值
    a.splice(2,2)
    console.log(a) // 返回并删除n到m的元素
```
```    [
      1, 2, 3, 4, 5,
      6, 7, 8, 9
    ]
    [
      2, 3, 4, 5,
      6, 7, 8, 9
    ]
    [ 2, 3, 6, 7, 8, 9 ]
```
## 函数:

用function定义, 参数和python一样不用声明类型

```    function print99(){
        for (let i = 1; i <= 9; i++){
            str = ""
            for (let j = 1; j <= i; j++){
                str += `${i} * ${j} = ${i*j} `
            }
            console.log(str)
        }
    }
    print99()
```
```    1 * 1 = 1 
    2 * 1 = 2 2 * 2 = 4 
    3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 
    4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 
    5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 
    6 * 1 = 6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 
    7 * 1 = 7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 
    8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 
    9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81
```
```    function printnn(n){
        for (let i = 1; i <= n; i++){
            str = ""
            for (let j = 1; j <= i; j++){
                str += `${i} * ${j} = ${i*j} `
            }
            console.log(str)
        }
    }
    printnn(5)
```
```    1 * 1 = 1 
    2 * 1 = 2 2 * 2 = 4 
    3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 
    4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 
    5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25
```
```    function double(a){
        return 2*a
    }
    let n = double(10)
    console.log(n)
```
```    20
```
### 作用域:

好奇究竟是有多闲得没事才会有这种问题

别的和python,java那些一样,如果函数内部有局部变量名字和全局变量一样,用就近原则

```    function f(){
        let num = 5
        return num
    }
    let num = 10
    function g(){
        let num = 20
        function fun(){
            let num = 30
            return num
        }
        return fun()
    }
    console.log(f())
    console.log(g())
```
```    5
    30
```
### 匿名函数

#### 将函数赋值给一个变量:

```    var a = function(n){
        return n+1
    }
    console.log(a)
    console.log(a(9))
```
```    [Function: a]
    10
```
#### 立即执行函数

没有名字,不调用也会立即执行,不过相邻两个立即执行函数需要用分号隔开

```    (function(){console.log(5)})()
    (function(){console.log(6)})()
```
```    5



    evalmachine.<anonymous>:2

    (function(){console.log(6)})()

    ^



    TypeError: (intermediate value)(...) is not a function

        at evalmachine.<anonymous>:2:1

        at Script.runInThisContext (vm.js:120:18)

        at Object.runInThisContext (vm.js:309:38)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
```    (function(n){console.log(n)})(90);
    (function(){console.log(6)})()
```
```    90
    6
```
#### 其他:

不知道放哪里了,先写这里吧

js是有和Python一样的or None语法的

一般是用来处理null的,并且python,java,js等语言 - a \|\| b,
a为真则不判断b - a && b, a为假则不判断b

```    var x = null
    var a = 5
    console.log(a || 0)
    console.log(x || 0)
```
```    5
    0
```
## 对象:

是一种无需的数据类型,类似字典,json

```    var person = {
        name: "someone",
        gender: "armed walmart helicopter",
        age: "unknown"
    }
```
```    console.log(person.name)
    console.log(typeof(person))
```
```    someone
    object
```
### 一些基本操作

```    // 查属性
    console.log(person.gender)
    console.log(person['gender'])
    // 改属性
    person.gender = "armed walmart shopping bag"
    console.log(person)
    // 增加属性:
    person.job = "shopping bag"
    console.log(person)
    // 删属性
    delete person.job
    console.log(person)
```
```    armed walmart shopping bag
    armed walmart shopping bag
    {
      name: 'someone',
      gender: 'armed walmart shopping bag',
      age: 'unknown'
    }
    {
      name: 'someone',
      gender: 'armed walmart shopping bag',
      age: 'unknown',
      job: 'shopping bag'
    }
    {
      name: 'someone',
      gender: 'armed walmart shopping bag',
      age: 'unknown'
    }
```
### 对象内可以使用函数:

```    var person = {
        name: "someone",
        gender: "armed walmart helicopter",
        age: "unknown",
        getage: function(n){
            console.log(n)
        }
    }
```
```    person.getage(20)
```
```    20
```
### 遍历对象:

不过注意,如果是遍历数组返回的是下标,如果是遍历对象返回的是属性名称

这种情况下循环里只能写obj\[k\]的形式

```    for (i in person){
        console.log(i,person[i])
    }
```
```    name someone
    gender armed walmart helicopter
    age unknown
    getage [Function: getage]
```
### 案例: object2table.html

### 内置对象

例如document,console,Math等相当于内置库

#### Math:

- random:0-1的随机数
- ceil
- floor
- max
- min
- pow
- abs
- \...

## 正则表达式

### 语法:

#### 新建正则表达式

```    const 变量名 = /表达式/
```
#### test()

```    正则表达式.test(被检测的字符串)
```
#### exec()

```    正则表达式.exec(字符串)
```
### 字符:

#### 边界符:

- \^ 表示以什么开始
- [\\(\\\$\\)]{.arithmatex}表示以什么结束

#### 量词:

[\\(\\begin{array}{c} \* & 重复零次或者更多次\\\\ + &
重复一次或更多次\\\\ ? & 重复0次或者一次\\\\ \\{n\\} & 重复n次\\\\
\\{n,\\} & 重复n次或者更多次\\\\ \\{n,m\\} & 重复n到m次
\\end{array}\\)]{.arithmatex}

#### 元字符:

- \[abc\]匹配一个字符是否是abc
- \[a-z\]可以用连字符表示一个范围
- \[a-z\]所有小写字母
- \[a-zA-Z\]所有字母
- \^写到中括号里表示取反

预定类: [\\(\\begin{array}{c} \\text{\\d} &
匹配0-9之间的任意数字\[0-9\]\\\\ \\text{\\D} &
匹配所有0-9以外的数字\[\^0-9\]\\\\ \\text{\\w} &
匹配任意的字符,数字和下划线\[A-Za-z0-9\_\]\\\\ \\text{\\W} &
除字符数字,下划线外所有的字符\[\^{} A-Za-z0-9\]\\\\ \\text{\\s} &
匹配空格(包括换行符,制表符,空格符等)\[\\text{\\t\\n\\v\\f}\]\\\\
\\text{\\S} & 匹配非空格的字符\[\^{} \\text{\\t\\r\\n\\v\\f}\]
\\end{array}\\)]{.arithmatex}

```    var str = "abc"
    var pattern = /[A-Z]/
    pattern.test("1000A0000")
```
```    true
```
# API DOM:

实际开发尽可能用const,之后发现要改在改成let,jupyter里为了方便暂时先用var(let不能重新赋值)

每个html标签在js里都是一个对象

## DOM元素:

### 获取DOM元素:

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
```
### 操作元素内容:

.innerText属性可以获取文字内容

.innerHTML属性可以获取HTML文本

### 更改属性:

直接赋值就行,以下是几个常用的

如果属性名称用连字符连接,改写成驼峰命名法的格式, obj.style.fontFamily =
\"SimHei\" - obj.style.(相当于更改这个标签的css,更改样式) - eg.
obj.style.color = \"red\" - obj.src
(更改标签的src属性,可以换图片之类的) - obj.href
(更改标签的href属性,可以换链接之类的)

对于document,由于一个html只会有一个body,可以通过document.body直接获取页面的body标签,然后进行修改

#### className

如果修改的样式很多,直接通过style属性修改会比较麻烦,于是可以通过借助css类名的形式改属性

其实就是修改一个标签的class属性,把他变成某个class从而应用那个类的css

```    元素.className = "active"
```
见案例className.html

可以用css的选择器使得改完类名之后应用css不会覆盖原先的样式而是应用新类的新增样式

#### classList:

```    元素.classList.add('类名') //增加类名

    元素.classList.remove('类名') //删除类名

    元素.classList.toggle('类名') // 切换类名,存在就删,没有就加
```
如果classlist里的css有重复的,则会显示最有一个可用的属性

#### 表单类

其实差不多,见案例form.html

如果获取innerHTML是空,需要通过表单名称.value获取所有的值

### 自定义属性:

自定义属性名称以data-开头

## 间歇函数/计时器:

```    setInterval(函数,间隔时间)
```
- 间隔时间是毫秒,表示美国间隔时间执行一次函数,一旦开启就一直执行,注意函数的位置写的是函数名,也就是不加参数

- setInteval函数会返回一个id

- 用clearInterval(id)暂停执行

```    var a = [0,1]
    console.log(a[])
```
```    undefined
```
## 事件监听

```    元素对象.addEventListener('事件类型',执行函数)
```
\- 事件类型要加引号 - 每次按按钮触发一次函数

```    Math.random()
```
```    0.532913478743734
```
### 事件类型:

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

### 事件对象:

一个存储时间执行是的相关参数的一个对象,是事件监听绑定函数传入的参数,差不多就是一个json -
type: - 获取当前的时间类型 - clientX/clientY -
获取光标相对于浏览器课件窗口左上角的位置 - offsetX/offsetY -
获取光标相对当前DOM元素左上角的位置 - key - 用户按下键的数值 -
(keyCode已经废弃)

### 环境对象：

this, java的this

普通事件里this指的是window

如果是addEventListener返回调用的元素

可以用this.style之类的改参数

### 回调函数:

就是把一个A函数传给另一个B函数,此时A是回调函数

常见的回调函数: - setInterval - addEventListener

## 事件流:

分成两个阶段,捕获和冒泡

捕获阶段冲大往小,冒泡反着来

### 事件捕获:

- 在addEventListener里传入第三个参数,true为使用捕获机制,false为不使用捕获机制
- 如果是用onclick绑定的则没有捕获阶段

### 事件冒泡

- 相当于子类父类继承,如果点击的部分在子类里,他也在父类里,这个时候绑定的同名函数将会按照冒泡阶段从小向大依次执行

### 阻止冒泡:

```    事件对象.stopPropagation()
```
这个是阻断事件流传播, 同时阻止冒泡和捕获

### 解绑事件:

- 如果是onclick,直接把onclick属性赋值成null即可
- addEventListener使用removeEventListener(事件,函数名),(匿名函数无法被解绑)

### 特殊事件:

- mouseover和mouseout有冒泡效果
- mouseenter和眸色leave没有冒泡效果

### 事件委托

同时给多个元素注册事件

就是定义一个父对象,触发子对象的时候会通过冒泡触发父对象的事件

### 阻止事件默认行为:

```    e.preventDefault()
```
### 其他事件:

#### 页面加载事件

##### load

加载外部资源的加载完毕的时候触发的事件 - 等资源加载完处理事情 -
老代码script放在head中,直接找dom找不到

```    window.addEventListener("load", function(){
        // 等页面加载完在处理回调函数
    })
```
window是document的更上一级

也可以对元素加load,等这个文件加载完的时候在处理回调函数

##### DOMContentLoaded:

当初是的html被加载,就触发,不需要等待所有的元素都完全加载

这会是给document加这个事件

#### 元素滚动事件

##### scroll

滚动到某个区域的时候会触发的东西

还是给window加scroll事件

##### scroll获取滚动位置:

- scorllLeft
- scorllTop

##### scrollTo

```    windows.scrollTo(x坐标,y坐标)
```
#### resize事件

当浏览器窗口大小发生变化的时候触发

```    window.addEventListener('resize',function)
```
##### clientWidth clientHeight

获取元素的课件的宽和高(不包含border和margin等,但是包含padding)

##### offsetLeft offsetTop

获取元素距离自己定位父级元素的左,上距离,这个会包含border很margin等

这个父级元素是有position属性的最近的父元素,直到document

## 日期对象:

### 实例化:

java里的new关键字仙剑一个对象(js这么久居然没有新建过对象)

```    const date = new Date()
```
也可以

```    const data = new Date("2022-5-1 8:30:00")
```
### 日期对象方法:

- getFullYear() 获得四位年份
- getMonth() 获得月份 0-11
- getDate() 获得约分钟的某一天
- getDay() 获得星期 0-6
- getHours() 获得小时 0-23
- getMinutes() 获得分钟 0-59
- getSeconds() 获得秒 0-59

### 时间戳:

是指从1970年01月01日00分00秒开始到现在的毫秒数

```    const date = new Date()
    date.getTime()
```
```    +new Date()
```
```    Date.now()
```
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
```
```    '2024-03-19 00:53:28'
```
## 节点操作:

### DOM 节点

- 元素节点
- 所有的标签, body, div
- html是根节点
- 属性节点
- href等
- 文本节点:
- 标签里的字
- 其他类

主要操作元素节点

### 查找节点:

根据关系找

#### 父节点:

```    e.parentNode
```
#### 子节点:

```    e.children
```
#### 兄弟节点:

##### 下一个兄弟节点:

```    e.nextElementSibling
```
##### 上一个兄弟节点:

```    e.previousElementSibling
```
### 添加节点

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
### 克隆节点:

```    元素.cloneNode(Bool)
```
如果参数是True,则会和后代一起克隆

如果是False,则不克隆后代节点

默认是False

注意克隆之后还需要追加节点

### 删除节点

```    父元素.deleteNode(要删除的元素)
```
## M端事件:

移动端特殊事件:

touch事件:

- touchstart
- touchmove
- touchend

## JS插件:

swiper:移动端插件 具体的建议去查api文档

ctrl cv全栈工程师上线

# API BOM

## BOM:

Browser Object Model

[\\(\\text{window}\\begin{cases} \\text{navigator}\\\\
\\text{location}\\\\ \\text{document}\\\\ \\text{history}\\\\
\\text{screen} \\end{cases}\\)]{.arithmatex}

document, alert(),
console.log()等都是window的属性,基本BOM的属性和方法都是window的

在window对象下的属性和方法调用的时候可以省略window

## 定时器-延时函数:

```    setTimeout(回调函数, 等待的毫秒数)
```
是一次性的

清除延时函数:

```    let timer = setTimeout(回调函数, 等待的毫秒数)
    clearTimeout(timer)
```
- 延时器需要等待所以后面的代码先执行
- 每次调用演示器都会产生一个新的延时器

## js执行机制:

事件循环

单线程,于是有了同步和异步 - 异步任务: - 普通事件: click resize -
资源加载: load error - 定时器: setInterval, setTimeout - 同步任务: -
基本上就是其他

先执行同步任务,然后异步任务排队,然后执行完所有同步任务之后执行队列里的异步任务,等时间到了放入执行栈里执行,不断循环

## 各种对象

### location 对象:

location本身是个对象,可以获取一些属性 - href:
当前网页的url,可以用于跳转页面,只需要更改href就可以跳转页面 - search:
post方法穿的参数,但是是字符串格式,获取问号后面的东西 - hash:
同上,但是是井号后面的东西 - reload(): 刷新页面

### navigator 对象:

获取浏览器相关信息: - userAgent: 获取当前浏览器,可以判断是否是手机端页面

### history对象:

一般来说就是

```    forward() // 前进
    back() // 后退
    go(1) // 1为前进,-1为后退
```
## 本地储存:

就是把数据直接存进浏览器,这样更改网页内容的时候,本地数据不会被改动

### localStorage:

永久性的把数据存储进浏览器中

可以多窗口共享:

#### 存储:

```    localStorage.setItem(key,value)
```
只能存字符串,如果存其他复杂数据类型则无法直接使用,
需要把字符串存成对象的字符串

```    JSON.stringify()
```
可以用

```    JSON.parse()
```
从字符串转换成Json,

#### 获取:

```    localStorage.getItem(key)
```
### sessionStorage:

生命周期为关闭浏览器窗口

在同一个页面下数据可以共享

以键值对的形式存储使用

用法和localStorage基本相同

# JS进阶

## 作用域:

### 局部作用域:

#### 函数作用域:

在函数内生命的变量只能在函数内部被访问 - 函数的参数也是函数的局部变量 -
不同函数内声明的变量无法互相访问

```    function foo(){
        const a = 1
    }
    function fooz(){
        const b = a + 1
    }
    foo()
    fooz()
```
```    evalmachine.<anonymous>:5

        const b = a + 1

                  ^



    ReferenceError: a is not defined

        at fooz (evalmachine.<anonymous>:5:15)

        at evalmachine.<anonymous>:8:1

        at Script.runInThisContext (vm.js:120:18)

        at Object.runInThisContext (vm.js:309:38)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
#### 块作用域:

在js中使用{}包裹的代码称为代码块,代码块内部声明的变量外部有可能无法被访问 -
let const 会产生作用域, var不会 - 不同代码块之间的变量无法互相访问

经典实例: for循环

### 全局作用域:

.js文件以及\< script\>标签内部会产生全局作用域

### 作用域链:

变量查找机制 - 优先查找当前作用域的变量 - 入股偶查不到会逐级往上找

## 垃圾回收:

应该和java一样,不用就回收:

内存: - 内存分配: 声明变量函数对象的时候会自动分配内存 - 内存使用:
读写内存 - 内存回收: 使用完被垃圾回收期自动回收

说明: - 全局变量一般不会回收 - 局部变量的值不用了会自动回收

内存泄露: 程序中的内存无法回收等

- 栈: 操作系统自动分配, 基本数据类型
- 堆: 存复杂类型,程序员或垃圾回收机制回收

### 引用计数法:

- 跟踪记录变量使用次数
- 引用一次就++
- 减少引用就\--
- 引用次数为0, 释放内存

### 标记计数法:

- 计算无法到达的对象
- 从根部定期草庙内存中的对象,如果到达不了则回收

## 闭包:

内层函数+外层函数的变量

实现数据私用,回忆一下作用域就懂了

```    function outer(){
        const a = 1
        function fn(){
            console.log(a)
        }
        return fn
    }
    outer()
```
## 变量提升:

仅存在于var变量, let和const没有

把所有var声明的变量提升到当前作用域的最前面,只提升声明,不提升赋值,这样在之前访问变量的时候会是undefined,这样不会出现一下情况:

一般来说python玩家不太会有这个问题

同理函数提升就是把函数声明提升到当前作用域的最前面,如果是直接声明函数不会出错,但是函数表达式必须先声明后赋值否则报错

```    console.log(str + "world")
    var str = "fuck "
```
```    undefinedworld
```
## 函数参数:

### 动态参数

但是javascript直接不写就行

相当于函数默认是这个样子:

```    public static void main(String[] args){
    }
```
```    function getSum(){
        console.log(arguments) // 这个arguments是动态参数,只存在域函数内部
    }
    getSum(1,2,3,4,5,6)
```
```    [Arguments] { '0': 1, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6 }
```
### 剩余参数:

可以将不定数量的参数表示为一个数组

python的\*\*kwargs等

这个是实参上面,那个只是形参

```    function getSum(a,b,...other){
        console.log(other)
    }
    getSum(1,2,3,4,5,6,7,8,9,0,[1,2,3])
```
```    [ 3, 4, 5, 6, 7, 8, 9, 0, [ 1, 2, 3 ] ]
```
## 展开运算符:

\...数组 进行展开

好处在Max等必须要输入元素而不是数组的时候

## 箭头函数:

一般是在函数表达式的时候用

只有一个形参的时候可以省略小括号

如果只有一行代码,可以直接写到一行上,不需要写return,也不需要写大括号

箭头函数可以直接返回一个对象

### 参数:

箭头函数没有arguments动态参数,但是有剩余参数..args

### this:

箭头函数没有自己的this,调用this会返回作用域的上一层

```    const fn = function(){
        console.log(1)
    }
    const f = () => {
        console.log(1)
    }
    const a = (...arr) => {
        console.log(arr)
        console.log(this)
    }

    a(1,2,3,4)
```
```    [ 1, 2, 3, 4 ]
    Object [global] {
      global: [Circular],
      clearInterval: [Function: clearInterval],
      clearTimeout: [Function: clearTimeout],
      setInterval: [Function: setInterval],
      setTimeout: [Function: setTimeout] {
        [Symbol(nodejs.util.promisify.custom)]: [Function]
      },
      queueMicrotask: [Function: queueMicrotask],
      clearImmediate: [Function: clearImmediate],
      setImmediate: [Function: setImmediate] {
        [Symbol(nodejs.util.promisify.custom)]: [Function]
      },
      __filename: '[eval]',
      exports: {},
      module: Module {
        id: '[eval]',
        path: '.',
        exports: {},
        parent: undefined,
        filename: '/mnt/d/Desktop/study/notes/selfstudy/html/[eval]',
        loaded: false,
        children: [],
        paths: [
          '/mnt/d/Desktop/study/notes/selfstudy/html/node_modules',
          '/mnt/d/Desktop/study/notes/selfstudy/node_modules',
          '/mnt/d/Desktop/study/notes/node_modules',
          '/mnt/d/Desktop/study/node_modules',
          '/mnt/d/Desktop/node_modules',
          '/mnt/d/node_modules',
          '/mnt/node_modules',
          '/node_modules'
        ]
      },
      __dirname: '.',
      require: [Function: require] {
        resolve: [Function: resolve] { paths: [Function: paths] },
        main: undefined,
        extensions: [Object: null prototype] {
          '.js': [Function],
          '.json': [Function],
          '.node': [Function]
        },
        cache: [Object: null prototype] {}
      },
      '$$mimer$$': [Function: defaultMimer],
      '$$done$$': [Function: bound bound done],
      console: Console [console] {
        log: [Function: log],
        warn: [Function: warn],
        dir: [Function: dir],
        time: [Function: time],
        timeEnd: [Function: timeEnd],
        timeLog: [Function: timeLog],
        trace: [Function: trace],
        assert: [Function: assert],
        clear: [Function: clear],
        count: [Function: count],
        countReset: [Function: countReset],
        group: [Function: group],
        groupEnd: [Function: groupEnd],
        table: [Function: table],
        debug: [Function: debug],
        info: [Function: info],
        dirxml: [Function: dirxml],
        error: [Function: error],
        groupCollapsed: [Function: groupCollapsed],
        Console: [Function: Console]
      },
      '$$': [Object: null prototype] {
        async: [Function: bound async],
        done: [Function: bound done],
        sendResult: [Function: bound ],
        sendError: [Function: bound ],
        mime: [Function: bound ],
        text: [Function: bound ],
        html: [Function: bound ],
        svg: [Function: bound ],
        png: [Function: bound ],
        jpeg: [Function: bound ],
        json: [Function: bound ],
        input: [Function: bound input],
        display: [Function: bound createDisplay],
        clear: [Function: bound clear]
      }
    }
```
### 对象方法的箭头函数:

```    const obj = {
        name: "ifjeijf",
        sayHi: ()=>{
            console.log(this)
            const i = 10
            const count = () => {
                console.log(this)
            }
            count()
        }
    }
    // obj的sayHi没有this,会返回上一层(obj)的this
    obj.sayHi()
    // window调用obj的sayHi方法,返回window而不是obj
    // jupyter里的window比较奇怪

    //count里没有this,找上一层的sayHi,但是sayHi也没有this.接着找,最后找到window
```
```    evalmachine.<anonymous>:1

    const obj = {

    ^



    SyntaxError: Identifier 'obj' has already been declared

        at evalmachine.<anonymous>:1:1

        at Script.runInThisContext (vm.js:120:18)

        at Object.runInThisContext (vm.js:309:38)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
## 解构赋值:

### 数组:

```    const arr = [1,2,3]
    const [a,b,c] = arr
    console.log(a)
    console.log(b)
    console.log(c)
```
```    1
    2
    3
```
```    let a = 1
    let b = 2; //这里必须有分号, 如果没有编译器会把下一行代码混淆到这一行,
               //就是解构之前哪一行必须要分号
    [b,a] = [a,b]
    console.log(a)
    console.log(b)
```
```    2
    1
```
```    // 同时
    const [a,b,c,d] = [1,2,3]

    console.log(a)
    console.log(b)
    console.log(c)
    console.log(d)
```
```    1
    2
    3
    undefined
```
```    // 为了防止这种情况,可以设置默认值
    const [a = 10, b = 20, c = 30, d = 40] = [1,2,3]

    console.log(a)
    console.log(b)
    console.log(c)
    console.log(d)
```
```    1
    2
    3
    40
```
```    // 支持多维数组
    const [a = 10, b = 20, c = 30, d = 40] = [1,2,[3,4]]

    console.log(a)
    console.log(b)
    console.log(c)
    console.log(d)
```
```    1
    2
    [ 3, 4 ]
    40
```
### 对象:

```    const {name, age} = {
        name : "a",
        age: 12
    }
    console.log(name)
    console.log(age)
```
```    a
    12
```
```    // 属性名必须完全对应,
    // 不要和外面有冲突,不然会报错
    const uname = 10
    const {uname, age} = {
        // 这里相当于两个const赋值语句
        name : "a",
        age: 12
    }
    console.log(name)
    console.log(age)
```
```    evalmachine.<anonymous>:4

    const {uname, age} = {

           ^



    SyntaxError: Identifier 'uname' has already been declared

        at new Script (vm.js:88:7)

        at createScript (vm.js:261:10)

        at Object.runInThisContext (vm.js:309:10)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
```    const {name: uname, age} = {
        name : "a",
        age: 12
    }
    console.log(uname)
    console.log(age)
```
```    a
    12
```
```    // 数组对象解构:
    const pig = [{
        "name":"aaa",
        "age": 16
    }]
    const [{name, age}] = pig
    console.log(name)
    console.log(age)
```
```    aaa
    16
```
```    const pig = {
        name: "aaa",
        family: {
            mother: "mother",
            father: "father",
            sister: "sister"
        },
        age: 6
    }
    const {name, family:{mother, father, sister}} = pig
    console.log(name)
    console.log(mother)
    console.log(father)
    console.log(sister)
```
```    aaa
    mother
    father
    sister
```
```    // 也可以在函数传参的时候解构
    const pig = {
        name: "aaa",
        family: {
            mother: "mother",
            father: "father",
            sister: "sister"
        },
        age: 6
    }
    function f({name, family:{mother, father, sister}}){
        console.log(name)
        console.log(mother)
        console.log(father)
        console.log(sister)
    }
    f(pig)
```
```    aaa
    mother
    father
    sister
```
## 一些函数:

.map() .forEach(), kotlin的老熟人了,用法也差不多

```    const a = [1,2,3].map(b=>b+1)
    console.log(a)
```
```    [ 2, 3, 4 ]
```
```    const pig = {
        name: "aaa",
        family: {
            mother: "mother",
            father: "father",
            sister: "sister"
        },
        age: 6
    }
```
```    evalmachine.<anonymous>:10

    for (i of pig){

              ^



    TypeError: pig is not iterable

        at evalmachine.<anonymous>:10:11

        at Script.runInThisContext (vm.js:120:18)

        at Object.runInThisContext (vm.js:309:38)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
```    for (i of Object.entries(pig)){
        console.log(i)
    }
```
```    [ 'name', 'aaa' ]
    [ 'family', { mother: 'mother', father: 'father', sister: 'sister' } ]
    [ 'age', 6 ]
```
## 对象:

### 创建对象三种方式

#### 直接创建

```    const obj = {
        "name": "aaa"
    }
```
#### new Object(系统默认构造函数)

```    const obj1 = new Object()
    obj1.name = "aaa"
    console.log(obj1)
```
```    { nam2: 'aaa' }
```
#### 自定义构造函数:

约定: - 函数名称首字母大写 - 只能用new操作

说明: - 构造函数内没有参数的时候可以省略括号 -
构造函数内部无需return,return返回值无效 -
系统内置的Object和Date也是构造函数

```    
function Pig(name){
        this.name = name
    }
    obj2 = new Pig("aaa")
    console.log(obj2)
```

```    
Pig { name: 'aaa' }
```
### 成员:

#### 实例成员:

通过构造函数创建的对象是实例对象.实例对象中的属性和方法称为实例成员

- 为构造函数传入参数,结构相同但对象不同,(和java一样,new就是一个全新的地址不同的对象)
- 创建的对象彼此独立,互不影响

#### 静态成员:

构造函数的属性和方法称为静态成员,就想象有个看不到的java static关键字

只能通过构造函数调用

```    Pig.eyes = 2
    Pig.legs = 4
    Pig.sayHi = function(){
        console.log(this)
    }
    console.log(Pig.eyes)
    Pig.sayHi()
    console.log(eyes)
```
```    2
    [Function: Pig] { eyes: 2, legs: 4, sayHi: [Function] }



    evalmachine.<anonymous>:8

    console.log(eyes)

                ^



    ReferenceError: eyes is not defined

        at evalmachine.<anonymous>:8:13

        at Script.runInThisContext (vm.js:120:18)

        at Object.runInThisContext (vm.js:309:38)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
### 包装类型

#### 基本包装类型:

字符串, 数值, boolean, undefined, null

字符串比较特殊:

一般来说只有对象才有属性方法,但是可以调用string.length

在js底层自动包装乘复杂数据类型,
相当于java的int数据类型被自动变成Integer类

```    const str = new String("aaa")
    const string = "aaa"
```
```    evalmachine.<anonymous>:1

    const str = new String("aaa")

    ^



    SyntaxError: Identifier 'str' has already been declared

        at evalmachine.<anonymous>:1:1

        at Script.runInThisContext (vm.js:120:18)

        at Object.runInThisContext (vm.js:309:38)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
#### 内置构造函数:

引用类型: - Object. Array, RegExp, Date\...\...

包装类型: - String, Number, Boolean\...\...

### 内置构造函数:

#### Object:

##### 静态方法 Object.keys()

python的字典.keys()

##### 静态方法 Object.values()

python的字典.values()

##### 静态方法 Object.entries()

python的字典.entries()

```    const o = {name:"aaa",val: 12}
    Object.entries(o)[0][1]
```
```    'aaa'
```
##### 静态方法 Object.assign()

对象拷贝

```    const o = {name:"aaa",val: 12}
    const oo = {age: 111}
    Object.assign(oo,o)
    console.log(oo)
```
```    { age: 111, name: 'aaa', val: 12 }
```
#### Array:

可以new Array,也可以直接写数组

##### forEach:

##### map:

##### filter:

##### reduce:

\`\`\`javascript: arr.reduce(function(上一次的值,当前值){},初始值)

```    ```python
    const arr = [1,2,3,4]
    arr.reduce(function(){},0)
```
想象有个haskell程序

```    -- haskell
    add::Int -> Int -> Int
    add a b = a + b
    foldr add 0 [1,2,3,4,5]
```
```    15
```
等价于:

```    function add(a,b){
        return a + b
    }
    [1,2,3,4,5].reduce(add, 0)
```
```    15
```
##### join

和python的join差不多,但是反过来

```    # python
    (",,,,,").join(["1","2","3","4","5"])
```
```    '1,,,,,2,,,,,3,,,,,4,,,,,5'
```
```    // javascript
    [1,2,3,4,5].join(",,,,,")
```
```    '1,,,,,2,,,,,3,,,,,4,,,,,5'
```
##### find

```    // kotlin
    listOf(1,2,3,4,5).first {it % 6 == 0}
```
```    evalmachine.<anonymous>:2

    listOf(1,2,3,4,5).first {it % 6 == 0}

                            ^



    SyntaxError: Unexpected token '{'

        at new Script (vm.js:88:7)

        at createScript (vm.js:261:10)

        at Object.runInThisContext (vm.js:309:10)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
```    // javascript
    [1,2,3,4,5].find((it) => it % 6 == 0) == undefined
```
```    true
```
##### every

```    // javascript
    [1,2,3,4,5].every((it) => it % 2 == 0)
```
```    false
```
```    // kotlin
    listOf(1,2,3,4,5).all{it % 2 == 0}
```
```    false
```
##### some

```    // javascript
    [1,2,3,4,5].some((it) => it % 2 == 0)
```
```    // kotlin
    listOf(1,2,3,4,5).any{it % 2 == 0}
```
```    true
```
##### concat

```    // javascript
    [1,2,3,4].concat([5,6,7])
```
```    [
      1, 2, 3, 4,
      5, 6, 7
    ]
```
```    # python
    [1,2,3,4] + [1,2,3,4,5]
```
```    [1, 2, 3, 4, 1, 2, 3, 4, 5]
```
##### sort

```    // javascript
    [4,2,3,1].sort()
```
```    [ 1, 2, 3, 4 ]
```
```    # python
    sorted([4,2,3,1])
```
##### reverse

```    // javascript
    [1,2,3,4,5].reverse()
```
```    [ 5, 4, 3, 2, 1 ]
```
```    # python
    list(reversed([1,2,3,4,5]))
```
```    [5, 4, 3, 2, 1]
```
##### findIndex

```    // javascript
    [1,2,3,4,5].findIndex((it) => it== 2)
```
```    1
```
```    # python
    [1,2,3,4,5].index(3)
```
```    2
```
#### String

##### length

```    //javascript
    "hello".length
```
```    5
```
##### split

```    //javascript
    "hello".split("l")
```
```    [ 'he', '', 'o' ]
```
##### substring

```    //javascript
    "hello".substring(3)
```
```    'lo'
```
##### startsWith

```    //javascript
    "hello".startsWith("he")
```
```    true
```
##### includes

```    "hello".includes("ll")
```
```    true
```
##### toUpperCase

```    //javascript
    "hello".toUpperCase()
```
```    'HELLO'
```
##### toLowerCase

```    //javascript
    "HEllO".toLowerCase()
```
```    'hello'
```
##### indexOf

```    //javascript
    "Hello".indexOf("l")
```
```    2
```
```    //javascript
    "He111111o".indexOf("111")
```
```    2
```
##### replace

```    //javascript
    "Hello".replace("l","a")
```
```    'Healo'
```
```    //javascript
    "He199o".replace(/[0-9]+/,"a")
```
```    'Heao'
```
##### match

```    //javascript
    "Hello".match("l")
```
```    [ 'l', index: 2, input: 'Hello', groups: undefined ]
```
```    //javascript
    console.log("He199o222".match(/[0-9]+/g))
    console.log("He199o222".match(/[0-9]+/i))
```
```    [ '199', '222' ]
    [ '199', index: 2, input: 'He199o222', groups: undefined ]
```
### oop:

#### 构造函数:

通过构造函数实现封装

#### 原型:

构造函数通过圆形分配的函数所有该对象公用,可以节省内存

prototype是js对象的一个属性.只想另一个对象

这个对象可以挂载函数

原型对象里的this和构造函数里的this都指向实例化的对象

```    function Star(uname, age){
        this.uname = uname
        this.age = age
    }
    Star.prototype.sing = function(){
        console.log("sing")
    }
    const a = new Star("a",12)
    const b = new Star("b",13)
    console.log(a.sing == b.sing)
    // 方法公用
```
```    true
```
```    Array.prototype.sum = function(){
        return this.reduce((prev, item) => prev + item, 0)
    }
    const a = new Array(1,2,3)
    a.sum()
```
```    6
```
#### constructor:

是个prototype的属性,指向原型对象的构造函数

```    function Star(){
    }
    console.log(Star.prototype.constructor)
```
```    [Function: Star]
```
```    console.log(Star.prototype.constructor)
    console.log("----------------------------")
    Star.prototype = {
        sing: function(){
            console.log("唱歌")
        },
        dance: function(){
            console.log("跳舞")
        }
    }

    console.log(Star.prototype.constructor)
    // 在赋值之后constructor消失
```
```    [Function: Star]
    ----------------------------
    [Function: Object]
```
```    // 所以这样:
    console.log(Star.prototype.constructor)
    console.log("----------------------------")
    Star.prototype = {
        constructor: Star,
        sing: function(){
            console.log("唱歌")
        },
        dance: function(){
            console.log("跳舞")
        }
    }

    console.log(Star.prototype.constructor)
    // 再赋值之后constructor消失
```
```    [Function: Star]
    ----------------------------
    [Function: Star]
```
#### 对象原型\_\_proto\_\_

是js的非标准属性

\[\[Prototype\]\]和\_\_proto\_\_是一个意思

只读不改,

指向构造函数的原型对象,对象原型和原型对象在值上是一个东西

```    function Star(){
    }
    const a = new Star()
    console.log(a.__proto__.constructor)
```
```    [Function: Star]
```
#### 原型继承

```    function Human(){
        this.sense = 5
        this.head = 1
    }
    function Women(){
        this.sense = 6
    }
    function Men(){
    }
    Women.prototype = Human
    Women.prototype.constructor = Women
    Men.prototype = Human
    Men.prototype.constructor = Men
    const w = new Women()
    const m = new Men()
    console.log(w.sense)
    console.log(m.sense)
```
```    6
    undefined
```
```    function Human(){
        this.sense = 5
        this.head = 1
    }
    function Women(){
        this.sense = 6
    }
    function Men(){
    }
    Women.prototype = Human
    Women.prototype.constructor = Women
    Men.prototype = Human
    Men.prototype.constructor = Men
    const w = new Women()
    const m = new Men()
    console.log(w.sense)
    console.log(m.sense)
    // 这里两个构造函数指向同一个地址,改一个就都会改
```
```    evalmachine.<anonymous>:1

    function Human(){

    ^



    SyntaxError: Identifier 'w' has already been declared

        at evalmachine.<anonymous>:1:1

        at Script.runInThisContext (vm.js:120:18)

        at Object.runInThisContext (vm.js:309:38)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
```    function Human(){
        this.sense = 5
        this.head = 1
    }
    function Women(){
        this.sense = 6
    }
    function Men(){
    }
    Women.prototype = new Human()
    Women.prototype.constructor = Women
    Men.prototype = new Human()
    Men.prototype.constructor = Men
    const w = new Women()
    console.log(w.sense)
    console.log(m.sense)
    // 这里两个对象是两个不同的对象
```
#### 原型链:

相当于不断地继承关系

```    function Human(){

    }
    const a = new Human()
    console.log(Human.prototype.constructor)
    console.log(Human.prototype.__proto__.constructor)
```
```    [Function: Human]
    [Function: Object]
```
只要是对象就有\_\_proto\_\_指向原型对象

只要是圆形对象就有consturctor

继承关系为所有-\>Object-\>null

访问一个对象的属性的时候首先查找自身,然后差上一层原型,一直查到Object为止,\_\_proto\_\_为null

可以使用instanceof判断prototype属性是否出现在摸个原形链上

```    var a = [1,2,3,4,5]
    a.splice(1,1)
    a
```
```    [ 1, 3, 4, 5 ]
```
## 深浅拷贝

这样只是设置了一个指针

```    const obj = {
        name: "aaa",
        age: 20
    }
    const o = obj
    o.age = 29
    console.log(obj.age)
```
```    29
```
### 浅拷贝

新建 一个对象,对于引用对象还是存一个指针,但是非引用对象正常

- Object.assign()
- {..obj}
- Array.prototype.concat()
- \[..arr\]

```    const obj = {
        name: "aaa",
        age: 20,
        family: {
        a: "a",
        b:"b"
    }
    }
    const o = {...obj}
    o.age=12
    console.log(obj)
    console.log(o)
```
```    { name: 'aaa', age: 20, family: { a: 'a', b: 'b' } }
    { name: 'aaa', age: 12, family: { a: 'a', b: 'b' } }
```
```    const obj = {
        name: "aaa",
        age: 20,
        family: {
        a: "a",
        b:"b"
    }
    }
    const o = {...obj}
    o.family.a = "aksk"
    console.log(obj)
    console.log(o)
```
```    { name: 'aaa', age: 20, family: { a: 'aksk', b: 'b' } }
    { name: 'aaa', age: 20, family: { a: 'aksk', b: 'b' } }
```
### 深拷贝:

#### 递归

```    function deepcopy(o, obj){

        for (let k in Object.entries(obj)){
            if (obj[k] instanceof Array){
                // 数组instanceof Object == true

                o[k] = []
                deepcopy(o[k], obj[k])
            } else if (obj[k] instanceof Object){
                o[k] = {}
                deepcopy(o[k], obj[k])
            } else {
                o[k] = obj[k]
            }
        }
    }
```
#### lodash/cloneDeep

#### JSON.stringify

```    const obj = {
        name: "aaa",
        age: 20,
        family: {
        a: "a",
        b:"b"
    }
    }
    const o = JSON.parse(JSON.stringify(obj))
    o.family.a = "aksk"
    console.log(obj)
    console.log(o)
```
```    { name: 'aaa', age: 20, family: { a: 'a', b: 'b' } }
    { name: 'aaa', age: 20, family: { a: 'aksk', b: 'b' } }
```
## 异常:

### throw

和java一样, throw new Error()

### try/catch

### debugger:

带要调试的代码框里写debugger,然后在f12里调试

## this:

### 普通函数:

谁调用指向谁

#### 箭头函数:

不存在this,获取最近可用作用域的this

#### 改变this:

##### call()

```    fun.call(thisArg, arg1, arg2.....)
```
thisArg就是fun函数在运行的时候指定的this值

args1,2,3是正常fun的参数

返回值就是fun的返回值

##### apply()

```    fun.apply(thisArgs,[argsArray])
```
相当于

```    fun.call(thisArgs, ...[argsArray])
```
##### bind()

不会调用函数,但是可以改变this指向

```    fun.bind(thisArg, arg1, arg2.....)
```
## 防抖:

单位时间内频繁触发时间只执行最后一次, 回城,被打断重新来

### lodash

```    _.debounce(fun, [wait = 0], [option = ])
```
### 手写:

debounce.html

## 节流:

单位时间内,频繁出发时间,只执行一次,就是设置技能cd

### lodash

```    _.throttle(fun, [wait = 0], [option=])
```
# AJAX:

Asychorous Javascript And Xml

用XMLHttpRequest对象与服务器通信

## intro

### Axios:

一个库: - 引入: https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js -
使用axios函数:

```    axios([
        url:"目标资源地址"
    ]).then((result) => 
        // 对服务器返回的数据做后续处理
           )
```
### params

可以在URL后直接加参数,但params更不容易出错

相当于直接访问https://hmajax.itheima.net/api/city?pname=%E6%B2%B3%E5%8C%97%E7%9C%81###

### 常用方法:

  请求方法   操作
  ---------- ----------------
  GET        获取数据
  POST       提交数据
  PUT        修改数据(全部)
  DELETE     删除数据
  PATCH      修改数据(部分)

```    axios({
        url: "目标资源地址",
        method: "请求方法",
        data:{
            参数名:值
        }
    }).then(result => {
        // 后续处理
    })
```
### 报错

```    axios({
        //请求选项
    }).then(result =>{
        //处理数据
    }).cathc(error=>{
        //处理错误
    })
```
### 请求报文:

规定了服务器返回内容的格式 ![image.png](attachment:image.png)

请求报文的组成部分有: - 请求行:请求方法, URL, 协议 -
请求头:以键值对的格式携带的附加信息,比如Content-type - 空行:空行 -
请求体: 发送的资源

#### 400:

##

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
```
```    {"username":"123567890","password":"124567890"}
```
#### 200:

##

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
```
```    {"username":"123567890","password":"124567890"}
```
### 响应报文:

和上面那个差不多

- 响应行(状态行): 协议, HTTP响应状态码,状态信息
- 响应头: 一键值对的格式携带的附加信息,比如:Content-Type
- 空行:空行
- 响应体:返回的资源

#### 响应状态码:

  状态码   说明
  -------- ------------
  1xx      信息
  2xx      成功
  3xx      重定向
  4xx      客户端错误
  5xx      服务端错误

## bootstrap 弹框:

bootstrap.css和bootstrap.js

## XMLHttpRequest:

AJAX内部用XMLHttpRequest与服务器通信

### 使用:

- 创建XMLHttpRequest对象
- 配置请求方法和url
- 监听lodend时间，接受响应结果
- 发起请求

```      const xhr = new XMLHttpsRequest()
      xhr.open("请求方法"，"url")
      xhr.addEventListener("loadend",()=>{
          console.log(xhr.response)
      })
      xhr,send()
```
### URLSearchParams:

用于把对象转成查询字符串

```    // Pass in a string literal
    var url = new URL("https://example.com?foo=1&bar=2");
    // Retrieve from window.location
    var url2 = new URL(window.location);

    // Retrieve params via url.search, passed into ctor
    var params = new URLSearchParams(url.search);
    var params2 = new URLSearchParams(url2.search);

    // Pass in a sequence
    var params3 = new URLSearchParams([
      ["foo", 1],
      ["bar", 2],
    ]);

    // Pass in a record
    var params4 = new URLSearchParams({ foo: 1, bar: 2 });
    console.log(url)
    console.log(url2)
    console.log(params)
    console.log(params2)
    console.log(params3)
    console.log(params4)
```
```    evalmachine.<anonymous>:4

    var url2 = new URL(window.location);

                       ^



    ReferenceError: window is not defined

        at evalmachine.<anonymous>:4:20

        at Script.runInThisContext (vm.js:120:18)

        at Object.runInThisContext (vm.js:309:38)

        at run ([eval]:1020:15)

        at onRunRequest ([eval]:864:18)

        at onMessage ([eval]:828:13)

        at process.emit (events.js:314:20)

        at emit (internal/child_process.js:877:12)

        at processTicksAndRejections (internal/process/task_queues.js:85:21)
```
### 发送post:

```    document.querySelector(".content button").addEventListener("click",()=>{
                var form = new FormData()
                pname = document.querySelector(".content input").value
                form.append("pname",pname)/
                xhr.open("POST",`https://hmajax.itheima.net/api/data`)
                xhr.send(form)
                console.log(form)
                xhr.onload = ()=>{
                    console.log(xhr.response)
                    const data = JSON.parse(xhr.response)
                    document.querySelector(".content p").innerText = Object.keys(data.data)
                }
            })
```
#### 设置请求头:

```    xhr.setRequestHeader("Content-Type","application/json")
```
这个可以表示你上传的数据是一个json

https://juejin.cn/post/6844904094340120584

## Promise:

Promise对象用于表示一个异步操作的最终完成或失败机器结果值

```    const p = new Promise((resolve, reject)=>{
        // 执行异步任务
    })

    p.then(result => {
        // 成功后的代码
    }).catch(error => {
        // 失败后的代码
    })
```
好处: - 逻辑更清晰 - 解决回调函数地狱问题

resolve表示成功,reject表示throw an error

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
```
### 三种状态:

创建对象的时候会处于pending状态

resolve执行后变成fullfilled状态,直接进入then回调函数

reject执行后状态变成rejected,直接进入catch回调函数

Promise对象一旦被兑现/拒绝就是好已经敲定了,状态无法再被改变

## 同步异步:

同步代码:需要等上一个执行完在执行下一个

异步代码:可以同时执行

异步: - 回调函数 -

### 回调函数地狱:

回调函数来回嵌套,虽然是syntactic sugar

#### Promise链式调用:

new
Promise执行then的时候可以新创建一个Promise对象,然后可以接着调用then的函数

在避免了来回形式调用的同时保证逻辑嵌套

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
### async await

async作为函数的修饰关键字

await在async函数内部取代then函数,等待Promise对象成功状态的结果值

### 事件循环:

之前有,就不写了

### 宏任务和微任务:

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
最后输出1 3 5 4 2

### Promise.all

合并多个Promise对象,这个Promise的then是所有Promise成功,如果一个失败就进catch

```    const p = Promise.all([Promise1, Promise2, Promise3.......])
    p.then(result => {

    }).catch(error => {

    })
```
这样可以让多Promise任务同时执行,而不是一个Promise任务接一个Promise任务

# todo: nodejs

## fs模块:

这个是js自带的

语法: - 加载fs模块对象

```    const fs = require('fs')
```
\- 写入文件内容

```    fs.writeFile("文件路径", "写入内容", err => {
        // 写入后的回调函数
    })
```
\- 读取文件内容

```    fs.readFile("文件路径", (err, data) => {
        // 读取后的回调函数
        // data是文件内容的Buffer数据流
    })
```
## URL端口:

端口号可以是0-65535之间的任意整数

http协议默认访问80端口

但是基本上0-1023都被系统程序占用

## 创建Web服务

- 加载http模块
- 监听request请求事件
- 设置端口,启动web服务
- 访问localhost:3000

## 模块化:

### Commonjs:

在js中,每个文件都被视为一个单独的模块,需要使用标准语法导入导出进行使用

- 导出:设置module.exports属性

```      moduel.exports = {
          属性名:暴露的值或者方法
      }
```- 导入:require模块名或者路径

```      require("js")
      require("./exports.js")
```
### ECMAScript

#### 默认导入导出

- 导出:export default{}

```      export default {}
```- 导入:import

```      import obj from "模块名或者路径"
```
  nodejs默认是支持commonjs的,如果需要ECMA需要再所在文件夹新建package.json文件夹,设置{\"type\":\"module\"}

#### 命名导入导出

- 导出 直接在变量前加export

- 导入:

```      import {something, something} from "模块名或者路径"
```
这两个相当于python

```    from package import *
    # 或者 # import package
```
和

```    from package import somefunc
```
的区别

### 包:

这个和python的概念一样,把init.py换成package.json,一般是如下形式:

```    {
        "name": "包的名字",
        "version": "版本号",
        "description": "描述"
        "main": "软件包入口",
        "author": "作者",
        "license": "许可,没猜错的话就是apache那些github上的license"
    }
```
会默认去找index.js然后找main指定的模块文件

## npm:

专属js的pip,也会自动检测依赖

### 命令

#### 自动生成package.json

```    npm init -y
```
#### 下载软件包:

```    npm i 软件包名称
```
下载的包会在./node_modules文件夹里,自动记录到package.json里

#### 安装所有依赖:

npm下比直接拷贝node_modules快得多

```    npm i
```
### 全局软件包 nodemon

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
```
# webpack:

打包工具, - 把less.sass转成css - ES6降级乘ES5 - 支持多种标准 安装:

```    npm i webpack webpack-cli --save-dev
```
还要在package.json的scripts里加上build:webpack

```    "scripts": {
        "build": "webpack"
    }
```
之后

```    npm run build
```
和gradle一样建立环境,打包输出到dist文件夹

## 修改webpack打包入口和出口

新建webpack.config.js

```    const path = require("path")

    module.exports = {
        entry: path.resolve(__dirname, "./src/login/index"),
        output: {
            path: path.resolve(__dirname, "dist"),
            filename: "./login/index.js",
        }
    }
```
## webpack自动生成html

先装包

```    npm i html-webpack-plugin --save-dev
```
在webpack.config.js里加入plugin属性

## 打包css

加载器css-loader: 解析css代码

加载器style-loader: 插入到DOM中

```    module.exports = {
        module: {
            rules: [
                {
                    test: /\.css$/i,
                    use: ["style-loader", "css-loader"]
                }
            ]
        }
    }
```
### 提取css

css可以被浏览器缓存,减少js文件体积

mini-css-extract-plugin: 提取css代码

这个和style-loader不能一起使用

#### 压缩css

上述方法提取的css没有被压缩,

需要插件:css-minimizer-webpack-plugin插件

需要

```    const CssMinimizerPlugin = require("css-minimizer-webpack-plugin")

    optimization: {
        minimizer: [
            // 在webpack@5中可以使用 ... 语法扩展现有的minimizer(即
            // terser-webpack-plugin插件),讲下一行的取消注释(保证JS代码还能被压缩)
            // `...`,
            new CssMinimizerPlugin(),
        ]
    }
```
## 打包less:

```    {
        test: /\.less$/i,
        use: [
            'style-loader',
            'css-loader',
            'less-loader',
        ],
    }
```
## 打包图片:

webpack5自带内置资源模块(字体,图片等),不需要另加loader

```    {
        test: /\.{png|jpg|jpeg|gif}$/i,
        type: 'asset',
        generator: {
        filename:'assets/[hash][ext][query]'}
    }
```
判断领戒指默认为8kB

大于8kb会发送一个单独的文字并导出URL地址

小于8KB会导出一个data URI

## Webpack搭建开发环境

用webpack-dev-server

启动web服务,自动检测代码变化,热更行到网页,更新是在内存里(速度快)

配置

```    {
        devServer: {
            false; //不允许从目录提供静态文件
        }
    }
```
```    {
        devServer: {
            static:true; //允许从目录提供静态文件,默认是public文件
        }
    }
```
```    {
        devServer{
            static: ["assets"] // 文件夹的名字
        }
    }
```
需要设定模式为开发模式

```    module.exports = {
        mode: "development"
    }
```
配置自定义命令:(可选)

```    "script": {
        "build": "webpack",
        "dev" : "webpack serve --open"
    }
```
这个会根据配置,打包相关的资源在内存里作为服务器的根目录,默认会以public作为根目录

可以写一个html用location.href自动跳转

## 打包优化:

  模式名称   模式名字      特点                  场景
  ---------- ------------- --------------------- ----------
  开发模式   development   调试代码,实时热替换   本地开发
  开发模式   production    压缩代码,资源优化     打包上线

设置方式1: 在webpack.config.js配置文件设置mdoe选项

设置方式2: 在package.json命令行设置mode参数

(注意:命令行的优先级大于配置文件)

## 打包模式的应用:

问题: 早开发模式下用style-loader更快,再生产模式下提取css代码 - 方案1:
webpack.config.js配置导出函数,但是局限性大(只接受两种模式) - 方案2:
家住cross-dev(跨平台通用)报名领,设置参数区分环境

先装包

```    npm i cross-env --save-dev
```
配置自定义参数(参数会绑定到proces.env对象下)

```     "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "build": "cross-env NODE_ENV=production webpack --mode=production",
        "dev": "cross-env NODE_ENV=development webpack serve --open --mode=development"
      },
```
webpack.config.js中区分不同环境使用不同配置

NODE_ENV中的模式和webpack的打包模式没有任何关系

这个值可以在node.js环境中通过process.env访问但是前端代码无法访问process.env.NODE_ENV

## 注入环境变量

新插件DefinePlugin

一个CLI工具,就是把DefinePlugin对象里的所有属性添加到命令后运行

```    //webpack.config.js
    new webpack.DefinePlugin({
        'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV)
    })
```
```    // 其他js
    process.env.NODE_ENV...
```
## 调错source map,

```    module.export = {
        devtool: "inline-source-map"
    }
```
这个应该只在开发模式下生效,因为你肯定补习往其他人看到js代码

## 解析别名alias

解析别名

把相对路径在打包的时候改成绝对路径

```    // webpack.config.js
    const config = {
        resolve:{
            alias:{
                "@": path.resolve(__dirname, "src")
            }
        }
    }
```
## 使用CDN

把静态资源文件/第三方库放在CDN网络各个服务器中,

开发模式使用本地第三方库, 生产模式下使用CDN加载引入

- html下引用第三方库的CDN地址,在html中加入判断

```    <% if(htmlwebpackPlugin.option.useCdn){%>
        <link href="cdn地址">
    <%} %>
```
- 配置webpack.config.js的externals外部扩展选项防止某些import的包背打包

```    {
        externals: {
            "axios": "axios"
            // 这里key是import .. from 语句后面的字符串
            // value
        }
    }
```
例:

```    config.externels = {
        "bootstrap/dist/css/bootstrap.css": "bootstrap",
        // import "bootstrap/dist/css/bootstrap.min.css"
        "axios": "axios",
        // import axios from "axios"
    }
```
```    {
        plugins: [
            new HtmlWebpackPlugin({
                useCdn: process.env.NODE_ENV === "production"
            })
        ]
    }
```
然后可以添加useCdn变量

```    plugins: [
            new HtmlWebpackPlugin({
                template: path.resolve(__dirname, "public/login.html"),
                filename: path.resolve(__dirname, "dist/login/index.html"),
                useCdn: process.env.NODE_ENV === "production"
            }),
        ]
```
## 多页面打包:

- 单页面: 单个html文件, 切换DOM实现效果
- 多页面: 多个html文件, 切换页面实现业务逻辑

步骤: - 准备源码(html,css,js) -
下载form-serialize(应该是可选的)导入到核心代码中 -
配置webpack.config.js多入口(entry),和多页面的设置

例:

```    const config = {
        entry: {
            "模块名1": path.resolve(__dirname, "src/入口1.js"),
            "模块名2": path.resolve(__dirname, "src/入口2.js"),
        },
        output: {
            path: path.resolve(__dirname, "dist")
            filename: "/[name]/index.js"//这里的name会自动替换成模块名
        },
        plugins: [
            new HtmlWebpackPlugin({
                template: "./public/页面2.html",
                filename: "./路径/index.html",
                chunks: ["模块名1"] // 对应上面的模块名
            }),
            new HtmlWebpackPlugin({
                template: "./public/页面2.html",
                filename: "./路径/index.html",
                chunks: ["模块名1"] // 对应上面的模块名
            })
        ],

    }
```
## splitChunks:分割公共代码:

```    const config = {
        optimization: {
            splitChunks: {
                chunks: 'all', // 所有模块动态非动态移入的都分割分析
                cacheGroups: { // 分隔组
                  commons: { // 抽取公共模块
                  minSize: 0, // 抽取的chunk最小大小字节
                  minChunks: 2, // 最小引用数
                  reuseExistingChunk: true, // 当前 chunk 包含已从主 bundle 中拆分出的模块，则它将被重用
                  name(module, chunks, cacheGroupKey) { // 分离出模块文件名
                      const allChunksNames = chunks.map((item) => item.name).join('~') // 模块名1~模块名2
                      return `./js/${allChunksNames}` // 输出到 dist 目录下位置
              }
            }
          }
        }
      }
    }
```
# VUE2:

用于创建UI的框架

这一部分主要是先vue2,然后3

## 简介:

### 创建实例:

[\\(\\begin{cases} 准备容器\\\\ 引包\\\\ \\text{new VUE()}\\\\
指定配置项\\to
渲染数据\\begin{cases}el指定挂载点\\\\data提供数据\\end{cases}
\\end{cases}\\)]{.arithmatex}

### 插值表达式:

- 语法 {{表达式}}
- 使用的数据必须存在,undefined不行
- 支持的是表达式,if for等不行
- 不能在标签属性中使用插值 数据改变,渲染会自动改变

### vue指令:

一堆以v-开头的标签属性,和自定义标签的data-一样

#### v-html:

相当于设置了该标签的innerHTML

#### v-show & v-if:

- v-show
- v-show=\"表达式\": 如果表达式是true显示元素,否则隐藏
- 本质切换的css的display属性
- 一般用于频繁切换显示隐藏的场景
- v-if:
- v-if=\"表达式\": 如果表达式是true显示元素,否则隐藏
- 创建或者移除
- 直接销毁节点,不能来回切换

#### v-on:

事件监听 - v-on:事件名=\"内联语句\"

```    <button v-on:click="count++">按钮</button>
```
\- v-on:事件名=\"methods中的函数名\"

```    <button>v-on:事件名="method"中的函数名</button>
```
这个时候要在新建VUE实例的时候传入methods参数 可以把v-on:事件替换成@事件

也可以写成类似

```    <button @click="fn(fullscore)">切换</button>
```
这样来传参,可以直接传入VUE实例中的数据

#### v-bind:

直接设置一个属性

```    <img v-bind:src="" alt="">
```
可以直接省略v-bind,但是感觉还是写上比较清晰

##### v-bind扩展 class

```    <div class="box" :class="{类名1:bool,类名2:bool}"></div>
    // 对于对象中的每个entry,如果bool是true,classList加入这个类,否则不加入
```
```    <div class="box" :class="[类名1,类名2,类名3]"></div>
    // 对于对象中的每个entry,如果bool是true,classList加入这个类,否则不加入
```
#### v-for

```    <p v-for="(item, index) in 数组"><p>
```
##### key

假设有

```    ul:nth-child(1){
        background-color: red;
    }
```
实际上如果设了key的话,v-for会按照key查找,比如有5个元素,key为1,2,3,4,5,删掉第一个之后

#### v-model:

给表单元素使用,双向数据绑定,可以快速设置和获取元素

##### 常见表单:

- 输入框 input:text
- 文本框 textarea
- 复选框 input:checkbox
- 下拉菜单 input:radio
- [\\(\\dots\\)]{.arithmatex}

#### 指令修饰符:

- 按键修饰符:
- \@keyup.enter: keyup是按键弹起,后面加上enter监听键盘回车
- v-model修饰符:
- v-model.trim: 去除首尾空格
- v-model.number: 转数字
- 事件修饰符:
- \@事件名.stop : 阻止冒泡
- \@事件名.prevent: 阻止默认行为

## 计算属性:

根据现有的数据运算,根据数据变化自动重新计算

在VUE实例中加computed属性

### computed / methods

- computed:
- 写在computed里
- 可以直接使用this.计算属性或者{{计算属性}}
- 会对属性进行缓存,更新的时候再缓存,性能更高
- methods:
- 写在method里,提供一个函数
- 使用的时候需要调用

### 计算属性的完整写法(用于修改):

kotlin写法,就是kotlin但是默认private set

```    computed: {
        属性名: {
            get(){
                //something(计算属性)
                return 结果
            },
            set(){
                //something(修改)
            }
        }
    }
```
## watch监听器:

### 简单写法:

```    data:{
        a: someValue,
    }
    watch:{
        属性名 (newValue, oldValue){
            // something
        },
        '对象.属性名' (newValue, oldValue){
            // something
        }
    }
```
这个时候可以额外做防抖,

### 完整写法:

添加额外配置项 - deep:true 对复杂类型深度监视 - immediate:true
初始化的时候立即执行一次handler方法

```    data:{
        obj:{
            words:"苹果",
            lang:"italy"
        }
    },
    watch:{
        数据属性名{
            deep:true
            handler(newValue){
                //something
            }
        }
    }
```
## VUE生命周期:

- 开始: new Vue()
- 结束: 关闭网页

### 四个阶段

- 创建阶段:把data换成响应式的数据
- 挂载阶段:渲染模板
- 更新阶段:数据修改,更新视图
- 销毁阶段:销毁实例

### 钩子函数:

一共八个 - 创建阶段 - beforeCreate (这个时候没有响应式数据) - created
(这个时候发送初始化渲染请求) - 挂载阶段 - beforeMount - mounted
(这一刻开始才有DOM) - 更新阶段 - beforeUpdate - update - 销毁阶段 -
beforeDestroy (可以释放一些资源,清楚计时器延时器等) - destoryed

## 脚手架VUE CLI

## 重要提示：不要在wsl里用vue，热更新无论怎样都是失效的

- 工程化开发 [\\(\\begin{array}{c} \\begin{array}{\|c\|} \\hline\\\\
  源代码\\\\ \\hline \\end{array}\\\\ \\text{es6语法/typescript}\\\\
  \\text{less/sass}\\\\ \\dots \\end{array}\\to \\begin{array}{c}
  \\begin{array}{\|c\|} \\hline\\\\ 自动化编译压缩组合\\\\ \\hline
  \\end{array}\\\\ \\text{webpack}\\\\ \\\\\\\\ \\end{array}\\to
  \\begin{array}{c} \\begin{array}{\|c\|} \\hline\\\\ 源代码\\\\ \\hline
  \\end{array}\\\\ \\text{js(es3/es5}\\\\ \\text{css}\\\\ \\dots
  \\end{array}\\)]{.arithmatex}
- 全局安装: yarn global add \@vue/cli 或者 npm i \@vue/cli -g
- 查看Vue版本: vue \--version
- 创建项目架子: vue create project-name(项目名称,不能用中文)
- 启动项目: yarn serve 或者 npm run serve, 会自动找package.json

### 脚手架目录:

VUE-DEMO

```    ├─node_modules           第三方文件夹
    │
    ├─public                 放html的地方
    │      favicon.ico        网站图标
    │      index.html         index.html模版文件
    └─src                    源代码目录 -> 以后写代码的文件夹(重要)
    │  │  App.vue            APP根组件 -> 项目看到的内容在这里编写(重要)
    │  │  main.js            入口文件 -> 打包或运行,第一个执行的文件(重要)
    │  │  
    │  ├─assets             静态资源目录 -> 存放图片字体等
    │  │      
    │  └─components         组件目录 -> 存放通用组件
    │  .gitignore             git忽视文件
    │  babel.config.js        babel配置文件
    │  jsconfig.json          js配置文件
    │  package.json           项目配置文件, 和webpack那个一样
    │  README.md              git README
    │  vue.config.js          vue-cli配置文件
    │  yarn.lock              yarn锁文件,由yarn自动生成,锁定安装版本
```
#### index.html

```    <!DOCTYPE html>
    <html lang="">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <link rel="icon" href="<%= BASE_URL %>favicon.ico">
        <title><%= htmlWebpackPlugin.options.title %></title>
      </head>
      <body>
        <noscript> <!--给不支持js的浏览器一个提示-->
          <strong>We're sorry but <%= htmlWebpackPlugin.options.title %> doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
        </noscript>
        <div id="app">
          <!--这里本来应该是VUE容器,但是工程化开发中不在这里写,而是在App.vue里写-->
        </div>
        <!-- built files will be auto injected -->
      </body>
    </html>
```
#### main.js

```    import Vue from 'vue'
    import App from './App.vue'

    console.log(123)
    console.log(456)

    Vue.config.productionTip = true // true为开发模式,false为生产模式

    new Vue({
      el: "#app",
      // render: h => h(App),
      // 完整render写法:
      render: (createElement) => {
       return createElement(App)
      }
    })//.$mount('#app')// 这里$mount和el作用完全一致
```
### 组件化开发

把一个网页拆成多个结构分开维护

其中根组件是整个应用最上层的组件,包裹所有普通小组件

App.vue可以分成三个组成部分

```    //这一部分是结构,定义网页布局(在VUE2中有且只有一个根元素)
    <template>
      <div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
        <img alt="Vue logo" src="./assets/logo.png">
        <HelloWorld msg="Welcome to Your Vue.js App"/>
      </div>
    </template>

    //这一部分定义行为
    <script>
    // 这里可以提供 data(特殊) methods, computed, watch 以及狗子函数
    import HelloWorld from './components/HelloWorld.vue'

    export default {
      name: 'App',
      components: {
        HelloWorld
      }
    }
    </script>

    //这一部分定义样式
    //如果需要让这个支持less,需要设置lang="less"
    //然后装less-loader和less
    <style>
    #app {
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
      margin-top: 60px;
    }
    </style>
```
### 普通组件的注册使用

- 局部注册: 只能在注册的组件中使用
- 创建.vue文件(三个组成部分)(在components文件夹里)
- 在使用的组件内导入注册, 然后就可以知己当做html标签使用

```    // 比如:

    <template>
      <div class="App">
        <!--头部组件-->
        <ExampleHeader></ExampleHeader>
        <!--主体组件-->
        <ExampleBody></ExampleBody>
        <!--底部组件-->
        <ExampleTail></ExampleTail>
      </div>
    </template>

    <script>
    import ExampleHeader from "./components/ExampleHead.vue"
    import ExampleBody from "./components/ExampleBody.vue"
    import ExampleTail from "./components/ExampleTail.vue"
    export default {
      components: {
        //"组件名":"组件对象"
        ExampleHeader: ExampleHeader,
        ExampleBody: ExampleBody,
        ExampleTail: ExampleTail
      }
    }
    </script>

    <style>
    .App{
      width: 600px;
      height: 700px;
      background-color: #87ceeb;
      margin: 0 auto;
      padding: 20px;
    }
    </style>
```
- 全局注册: 所有组件都能使用
- 创建.vue文件(三个组成部分)
- main.js中进行全局注册

和上面那个相比

```    import something from someFile
    Vue.component("something", something)
```
敲\< vue\>可以快捷生成模版

### 三个组成部分

三个组成部分: - \< template\>: 只能有一个根元素 - \< style\>: -
全局样式(默认): 影响所有组件 - 局部样式:
scoped下的样式,之作用于当前组件 - \< script\> - el根示例独有 -
data是一个函数 - 其他配置项一致

#### scoped:

默认: 写在组件里的样式会全局生效,容易造成组件之间的样式问题

```    <style scoped>
        //各种样式
    </style>
```
这样就只会在当前组件生效

scoped的原理是给当前模版内的所有元素,都会被添加上一个 data-v-哈希值
自定义属性

#### data是一个函数:

一个组件的data选项必须是一个函数,保证每个组件实例维护独立的一份数据对象

### 组件通信:

组件和组件之间传递数据 - 组件的数据是独立的,无法直接访问其他组件的数据

组件关系: - 父子关系 - props和\$emit - 非父子关系 - provide & inject -
eventbus

#### 父子关系:

- 父组件通过props将数据传递给子组件
- 子组件通过\$emit使用数据

```    //父组件
    <template>
        <div>
            <Son :title="myTitle" @keyword="fatherFn"></Son>
        </div> 
    </template>

    <script>
    import Son from ...
    export default{
        data(){
            return {
                myTitle: "something"
            }
        },
        methods:{
            fatherFn(){
                //something
            }
        },
        components:{
            Son,
        }
    }
    </script>
```
```    //子组件
    <template>
        <div>
        {{title}}
        </div> 
    </template>

    <script>
    export default{
        props: ["title"],
        methods: {
            sonFn(){
                //something
                this.$emit("keyword",**kwargs)
            }
        }
    }
    </script>
```
##### props：

是组件上注册的一些自定义属性

prop作用:向子组件传递数据

可以传递任意数量,任意类型的props

##### props校验:

给prop验证要求,不符合要求就会有错误提示

- 类型校验:

```    props:{
      校验的属性名: 类型
    }
```
- 非空校验，默认值，自定义校验

```    props: {
        校验的属性名： {
            type: 类型， // Number String Boolean ...
            required: true, // 是否必填
            validator (value) {
                // 自定义校验逻辑
                return 是否通过校验
            }
        }
    }
```
##### prop和data:

- data的数据是自己的: 随便改
- prop的数据是外部的:
  不能随便改,要遵循单向数据流(父组件的数据改动会自动向下流动)

#### 非父子关系: eventbus事件总线:

复杂场景用vuex

- 创建一个都等你访问到的事件总线(空的VUE实例),一般会存到utils文件夹下

```      import Vue from 'vue'
      const Bus = new Vue()
      export default Bus
```
\- 接收方监听Bus实例的事件

```    Bus.$on('sendMsg', (msg) => {
        this.msg = msg
    })
```
- 发送方触发Bus实例的事件

```      Bus.$emit('senfMsg','消息')
```
#### 非父子通信: provide&inject

跨层级共享数据

```    //父组件
    export default{
        provide(){
            return{
                color: this.color,
                userInfo: this.userInfo
            }
        }
    }
```
```    //子组件
    export default{
        inject: ["color","userInfo"],
        created(){
            console.log(this.color, this.userInfo)
        }
    }
```
这个案例里面简单类型(color)是响应式的,如果修改,相应的渲染不会修改

但是复杂类型(userInfo)被修改的时候相应的渲染也会被修改

### v-model:

本质是value属性和input时间的和写

```    <template>
        <div>
            <input v-model="msg" type="text">

            <input :value="msg" @input="msg = $event.target.value" type="text">
        </div>
    </template>
```
#### 表单类组件封装:

数据由父组件提供,子组件修改 - 父传子: props传下去, v-model拆解绑定数据 -
子传父: 监听输入, 传给父组件修改 -
在传给父组件的时候可以用\$event直接获取形参

```    <template>
      <div id="app">
        <BaseSelect
         :cityId="selectId"
         @changeCity="selectId = $event"
        >
        </BaseSelect>
        <p>{{selectId}}</p>
      </div>
    </template>

    <script>
    import BaseSelect from "./components/BaseSelect.vue"
    export default {
      data(){
        return {
          selectId: "102"
        }
      },
      components:{
        BaseSelect
      },
      methods:{
        changeId(value){
          this.selectId = value
        }
      }
    }
    </script>

    <style>

    </style>
```
子组件不能用v-model因为数据室父组件的,但是父组件可以用v-model

父组件v-model简化代码,实现子组件和父组件数据双向绑定

比如在上面的例子中,这个是父组件,所以可以直接用v-model

```    <BaseSelect
     v-model="selectId"
    >
    </BaseSelect>
```
但是子组件的\$emit函数中只能是\'input\', props中只能是value,局限性较大

### sync修饰符:

可以实现子组件和父组件的双向绑定,简化代码

就是:属性名和@update:属性名的合写

- prop属性名可以自定义,不固定为value

```    <!--父组件-->
    <BaseDialog :visible.sync="isShow"/>
    -----------------------------------
    <BaseDialog
      :visible="isShow"
      @update:visible="isShow = $event"
    />
```
```    <!--子组件-->
    props:{
       visible: Boolean
    }

    this.$emit('update:visbale', false)
```
### ref 和 [\\(\\\$\\)]{.arithmatex}refs

queryselector的查找范围是整个文档，但是ref和\$ref的查找范围是当前组件

通过this.\$refs在这个组件里查询这个元素

```    <div ref="something" class="someclass"></div>

    this.$refs.myChart
    // 也可以调用这个组件的方法
    this.$refs.myChart.someMethod()
```
### vue异步更新, [\\(\\\$\\)]{.arithmatex}nextTick

vue的更新机制: 为了提升性能,vue异步更新元素

用[\\(\\\$\\)]{.arithmatex}nextTick等待更新完成

## 组件和自定义指令:

### 自定义指令:

内置指令: v-html, v-model等

举例: autofocus在safari浏览器有兼容性,操作dom的时候需要用focus()

这样每个需要获取焦点的元素都要写一遍

可以写(如果要传值,获取指令的值用参数名.value)

#### 全局注册:

```    Vue.directive("指令名", {
        "inserted" (el) {
            el.focus()
        }
    })
```
#### 局部注册:

```    directives: {
        "指令名": {
            inserted(){
                el.focus()
            }
        }
    }
```
#### 配置项:

inserted: 元素被插入到页面

update: 值被更新

## 插槽:

让组件内的一些结构支持自定义

- 组件内需要定制的结构部分改用\< slot\>\< /slot\>站位
- 使用组件时在标签内部传入结构替换slot

### 后备内容(默认值)

在\< slot\>\< /slot\>标签内防止内容作为显示内容

### 具名插槽(多处slot)

通过name属性区分名字,
在使用组件时,用template标签包裹,用v-slot:名字确定是那个插槽,
其中v-slot:名字可以简写成#名字

### 作用域插槽(不属于插槽结构)

可以绑定数据

给slot标签添加属性

```    <slot :id="item.id" msg="测试文本"></slot>
```
所有的属性都会被收集到一个对象当中

在template中通过`#插槽名="obj"`接收

## 路由

### SPA(Single Page Aplication)单页应用程序

![](image.png)

### 路由:

路径和组件的映射关系, eg localhost:8888/notebook

### VUERouter:

#### 基础步骤

- 下载

  `yarn add vue-router@3.6.5` - 版本: [\\(\\begin{array}{c} \\text{Vue2}
  & \\text{VueRouter3.x} & \\text{Vuex3.x}\\\\ \\hline \\text{Vue3} &
  \\text{VueRouter4.x} & \\text{Vuex4.x} \\end{array}\\)]{.arithmatex}

- 引入

`import VueRouter from 'vue-router'` - 安装注册

`Vue.use(VueRouter)` - 创建路由对象

```    ```const router = new VueRouter()```
```
- 把路由对象注入到VUE实例中

```    new Vue({
        render: h => h(App),
        router
    })
```
#### 核心步骤:

- 创建需要的组件,推荐放到views文件夹下,配置路由规则

```      import Find from './views/Find.vue'
      import My from './views/My.vue'
      import Friend from './views/Friend.vue'

      const router = new VueRouter({
          routes: [
              { path: '/find', component: Find },
              { path: '/my', component: My },
              { path: '/friend', component: Friend}
          ]
      })
```
- 配置导航, 配置路由出口

```      <div class="footer-wrap">
        <a href="#/find">发现音乐</a>
        <a href="#/my">我的音乐</a>
        <a href="#/friend">朋友</a>
      </div>
      <div class="top">
        <router-view></router-view><!--这个是内置的组件-->
      </div>
```
#### 组件存放问题:

##### 页面组件:

用来展示页面,配合路由使用, 放在views文件夹下

##### 复用组件:

用来展示数据,常用于复用, 放在components文件夹下

#### 路由的封装抽离:

在router文件夹下的js文件里设置路由之后在App.vue中import

使用路径时可以用@,@等同于src文件夹的绝对路径

#### 用router-link替换a标签(声明式导航)

`<a href="#/find></a>`

等同于

`<router-link to='/find'></router-link>`

实际也是渲染成a标签,但是可以高亮

激活时会自动加上router-link-active类标签

#### router -link 类名:

- router-link-active 模糊匹配：
  `<a href="#/find" class-"router-link-exact-active">`可以匹配`/my, /my/a, /my/b`

- router-link-axact-active 精准匹配：
  `<a href="#/find" class-"router-link-exact-active">`只能匹配`/my`

#### 自定义匹配的类名(router-link-exact-active):

在index.js里配置类名:

```    const router = new VueRouter({
        routes: [],
        linkActiveClass: "类名1",
        linkExactActiveClass: "类名2"
    })
```
#### 声明式导航：

跳转的时候进行传值

##### 查询参数传参：

- 通过？携带参数,多个参数用&连接

- 对应页面组件接受床底过来的值: `$route.query.参数名`

- 在vue其他地方获取参数要加this`this.$route.query.参数名`

##### 动态路由传参

- 配置动态路由:

```      const router = new VueRouter({
        routes:[
          { path: '/search/:words', component: FirstPage },
        ],
      })
```- 这个时候需要用`$route.params.参数名`

#### 路由重定向

匹配path之后强制重定向到路径

```        const router = new VueRouter({
          routes:[
            { path: '/search/:words', component: FirstPage, redirect: "..." },
          ],
        })
```
可以写

```        const router = new VueRouter({
          routes:[
            { path: '*', component: FirstPage, redirect: "..." },
          ],
        })
```
来避免404

#### 路由模式:

- 默认是hash,就是localhost的那种带井号的
- 可以调整成history去掉井号,以后上线需要服务器支持

```    const router = new VueRouter({
          routes:[
            { path: '/search/:words', component: FirstPage, redirect: "..." },
          ],
          mode: "history"
        })
```
#### 用程序跳转:

- path路径跳转:

```      this.$router.push(`路径`)
```
  `` this.$router.push({ `路径` }) ``

- name路径跳转(适合path比较长的场景)

```      this.$router.push({
          name: "路由名"path: "路径", component: ...
      })
```
##### 传参

- path路径跳转:

  `` this.$router.push({ path: `路径`, query: { 参数1: 参数值1, ... } }) ``

- name路径跳转(适合path比较长的场景)

```      this.$router.push({
          name: "路由名"path: "路径", component: ..., params: {
              参数1: 参数值1,
              ...
          }
      })
```
## 自定义创建项目：

vue create 之后选自定义， 勾选需要的配置项

![](6ba8c5d5fa1eb249504bfb652757995.png)

eslint规范中应用最广的是standard config，无分号规范

### eslint代码规范：

- 字符串使用单引号
- 无分号
- 关键字后加空格
- 函数名后加空格
- 用 === 而不是 ==

#### 手动修改（纯纯折磨）

#### 自动修改：

vscode插件高亮错误, 但感觉还是算了吧

## vuex：

状态管理工具，管理vue通用数据（多组件共享）

应用场景: - 某个状态在很多个组件中使用 - 多个组件共同维护一个数据

可以集中化管理,响应式变化

### 使用:

- 安装vuex,版本看router那里
- 在store(和component同级)的index.js存放vuex
- 创建仓库(Vue.use(Vuex), new Vuex.store())
- main.js导入挂载

### state状态:

提供数据:

```    const store = new Vuex.Store({
        state: {
            count: 101
        }
    })
```
通过`this.$store.state.count`调用

同时可以引入mapState(`import {mapState} from 'vuex'`),
通过`mapState(["count"])`调用

也可以写入computed里

```    computed: {
        ...mapState(['count'])
    },
```
之后就可以直接count调用

不过和data一样,建议写成函数

### 修改数据:

组件中不能直接修改仓库数据, 建议在stor中配置strict:
true开启严格模式,任何视图在组件中直接++等修改数据均会报错

修改仓库中数据智能通过mutations

```    const store = new Vuex.Store({
        state: {
            count: 101
        },
        mutations:{
            add(state){
                state.count += 1
            }
        }
    })
```
调用的时候需要通过commit `this.$store.commit('addCount')`

mutations支持传参,不过第一个参数是state

调用的时候变成`this.$store.commit('addCount', n)`

vuex不支持传多个参数,可以封装一个json过去

### mapMutations

和maoState很像

可以

```    methods: {
        ...mapMutations(['subCount'])
    }
```
之后调用的时候就可以

```    this.subCount(10)
```
等于

``````
### actions:

类似setInterval,异步操作,

mutations里的方法必须是同步的,异步的扔到actions里

actions不能修改state,还是需要commit mutations里的方法

同样有mapActions

### getters

类似计算属性,同样有mapGetters,只不过这个要扔到computed里

### vuex多模块:

同样的方法写多个模块

```    // in store/modules/user.js

    const state = {
        userInfo: {
            name: 'zs',
            age: 18
        }
    }

    const mutations = {}
    const actions = {}
    const getters = {}
    export default {
        state,
        mutations,
        actions,
        getters
    }
```
```    import user from './modules/user'
    const store = new Vuex.Store({
        modules: {
            user
        }
    })
```
不过这样在使用该仓库的时候需要import, 剩下的一样

子模块会被挂在到根处的state

可以通过mapState映射 - 默认根级别的映射: `mapState(['xxx'])` -
自模块的映射:
`mapState('模块名',['xxx'])`,这个时候需要再export里加上namespaced: true

子模块可以在maoState里注册然后直接使用,也可以从根\$store慢慢找数据

- `...mapState(['count', 'user'])`
- `...mapState('user',['userInfo'])`,这个需要namespaced: true

使用子模块中getters的数据 - `$store.getters['模块名/xxx']` -
mapGetters映射 - 根级别映射 `mapGetters(['xxx'])` - 子模块映射
`mapGetters('模块名', ['xxx'])`, 需要namespaced: true

调用子模块中的函数 - `$store.commit('模块名/xxx',参数)` -
mapMutations映射 - `mapMutations(['xxx'])` -
`mapMutations('模块名',['xxx'])`,需要namespaced: true

剩下的actions 一样

## 组件库:

- PC端: element-ui ant-design-vue(vue2,3都支持)
- 移动端 vant-ui Mint-ui Cube UI(后面这俩用的比较少)

### vant组件库:(以下在vue2环境):

- 安装: `npm i vant@latest-v2 -S`

- 使用:

- 自动按需引入:

```        // babel.config.js
        module.exports = {
          plugins: [
            ['import', {
              libraryName: 'vant',
              libraryDirectory: 'es',
              style: true
            }, 'vant']
          ]
        };
```
  之后引入单独的插件:

```      // 接着你可以在代码中直接引入 Vant 组件
      // 插件会自动将代码转化为方式二中的按需引入形式
        import { Button } from 'vant';
```
  \- 手动按需引入:(看官网,不推荐) - 全部引入:

```        // main.js
        import Vant from 'vant'
        import 'vant/lib/index.css'
        Vue.use(Vant)
```
  之后就可以

```        <van-button type="primary"></van-button>
```
  或者为了整洁,把vant配置项放到单独的js文件里,然后import这个js文件

### element-ui

## vw适配:

- 安装: `yarn add postcss-px-to-viewport@1.1.1 -D`
- 使用

```      module.exports = {
          plugins: {
              'postcss-px-to-viewport': {
                  viewportWidth: 375;
              }
          }
      }
```
# vue3:

## 和vue2对比:

```    <!-- vue 2 -->
    <script>
    export default {
        data() {
            return {
                count:0
            }
        },
        methods: {
            addCount(){
                count.value++
            }
        }
    }
    </script>
```
```    <script setup>
    import { ref } from 'vue'
    const count = ref(0)
    const addCount = () => count.value++
    </script>
```
## 创建项目:

create-vue而不是vue-cli

- `node -v` 确认版本\>=16.0
- `npm init vue@lastest`

vscode里记得禁用vetur(vue2),启用Vue-official(vue3)

### 文件夹下文件:

- vite.config.js: 基于vite的配置项 (vue2的webpack.config.js)
- package.json: 项目包 (所有的webpack变成vite)
- main.js: 入口js, 通过createApp创建应用实例,createRouter, createStore
- app.vue: 根组件
- 变化: script和template顺序调整
- 变化: template不要求唯一根元素
- 变换: script添加setup支持组合式api
- index.html: 单页入口

## vue3语法:

### setup:

![5fecefd0a002a082e01d53a2134aeb4.png](attachment:5fecefd0a002a082e01d53a2134aeb4.png)

setup节点在beforeCreate之前

setup里this是undefined

#### 写法1:

setup里的所有数据和函数都以要返回才会有作用

```    <script>
    export default{
      setup(){
        console.log('setup')
        const msg = "vue3"
        const logMessage = () => {
          console.log(msg)
        }
        return {
          msg,
          logMessage
        }
      },
      beforeCreate(){
        console.log('beforeCreate')
      }
    }
    </script>

    <template>
      <div>
        {{msg}}
        <button @click="logMessage"></button>
      </div>
    </template>
```
#### 写法2:

```    <script setup>
    const msg = "vue3"
    const logMessage = () => {
      console.log(msg)
    }
    </script>

    <template>
      <div>
        {{msg}}
        <button @click="logMessage"></button>
      </div>
    </template>
```
### reactive ref:

vue3中数据默认不是响应式的,需要用reactive或者ref

reactive接受的数据必须是对象,但是ref不用

```    <script setup>
    import { reactive } from 'vue'
    const state = reactive({
      count: 100
    })
    const setCount = () => {
      state.count++
    }
    </script>

    <template>
      <div>
        <div>{{state.count}}</div>
        <button @click=setCount>11111</button>
      </div>
    </template>
```
如果用ref: - 在script中调整值需要调.value - 在template中不用.value

### computed:

```    <script setup>
    import { computed, ref } from 'vue'
    const list = ref([1,2,3,4,5,6,7,8])
    console.log(list)
    console.log(list.value)
    const computedList = computed(() => {
      return list.value.filter(it=>it > 2)
    })
    const addFn = () => {
      list.value.push(12345)
    }
    </script>

    <template>
      <div>
        <div>{{list}}</div>
        <div>{{computedList}}</div>
        <button @click="addFn">add</button>
      </div>
    </template>
```
同样可以像kotlin一样写get和set

```    const count = ref(1)
    const plusOne = computed({
      get: () => count.value + 1,
      set: (val) => {
        count.value = val - 1
      }
    })

    plusOne.value = 1
    console.log(count.value) // 0
```
### watch:

```    <script setup>
    import { ref, watch } from 'vue'
    const count = ref(0)
    const nickname = ref("name")

    const changeCount = () => {
      count.value++
    }

    const changeNickname = () => {
      nickname.value = ("some random name")
    }

    // 单个
    watch(count, (newValue, oldValue) => {
      console.log("changed count")
      console.log(newValue, oldValue)
    })

    // 多个
    watch([count, nickname], (newArr, oldArr) => {
      console.log(newArr, oldArr)
    })
    </script>

    <template>
      <div>{{ count }}</div>
      <button @click="changeCount">改数字</button>
      <div>{{ nickname }}</div>
      <button @click="changeNickname">改昵称</button>
    </template>
```
#### immediate:

在一开始立刻触发watch函数, 只不过这个时候oldVal会变成undefined

```    watch(count, (newValue, oldValue) => {
      console.log("changed count")
      console.log(newValue, oldValue)
    }, {
      immediate: true
    })
```
#### deep:

用于对象,如果对象里某个值改了,同样会触发watch

```    watch(count, (newValue, oldValue) => {
      console.log("changed count")
      console.log(newValue, oldValue)
    }, {
      deep: true
    })
```
如果不用deep

```    const info = ref({
        name: "cp",
        age: 18
    })

    watch(
        () => info.value.age,
        () => console.log('age发生变化了')
    )
    // 第一个参数是监视的数据
    // 第二个是调用的函数
```
### 生命周期函数,钩子函数

参见vue2的钩子函数

[\\(\\begin{array}{c} 选项是API & 组合式API\\\\
\\text{beforeCreate/created} & \\text{setup}\\\\ \\text{beforeMount} &
\\text{onDeforeMount}\\\\ \\text{mounted} & \\text{onMounted}\\\\
\\text{beforeUpdate} & \\text{onBeforeUpdate}\\\\ \\text{updated} &
\\text{onUpdate}\\\\ \\text{beforeUnmount} & \\text{onBeforeUnmount}\\\\
\\text{unmounted} & \\text{onUnmounted}\\\\
\\end{array}\\)]{.arithmatex}

如果是created和beforeCreated的代码放到setup里执行

如果是mounted,引入onMounted

如果写成函数的调用方式,可以调用多次

```    <script setup>
    import { onMounted } from 'vue';

    const getList = () => {
      setTimeout(() => {
        console.log('data')
      }, 2000)
    }

    getList()

    onMounted(() => {
      console.log("data1")
    })


    onMounted(() => {
      console.log("data2")
    })
    </script>

    <template>
      <div>something</div>
    </template>
```
### 子组件:

#### 局部注册:

只需要import就行,然后可以直接用

```    <script setup>

    </script>

    <template>
        <div class="son">
          子组件
        </div>
    </template>

    <style scoped>
    .son {
      border: 1px solid #000;
      padding: 30px;
    }
    </style>
```
setup内无法直接写props,要用defineProps

在script中使用要props.属性名,在模板里用直接属性名就行

##### 父传子:

子组件:

```    <script setup>
    const props = defineProps({
      car: String,
      data: Number
    })
    </script>

    <template>
        <div class="son">
          子组件 - {{car}} {{data}}
        </div>
    </template>

    <style scoped>
    .son {
      border: 1px solid #000;
      padding: 30px;
    }
    </style>
```
父组件:

```    <script setup>
    import SonCom from '@/components/son-com.vue'
    import { ref } from 'vue'
    const data = ref(0)
    const car = ref("benz")
    const addData = () => {
      data.value++
    }
    </script>

    <template>
      <div>
        <h3>父组件 - {{data}}</h3>
        <SonCom :data="data" :car="car"></SonCom>
        <button @click="addData">+1</button>
      </div>
    </template>
```
##### 子传父:

不能直接`this.$emit`

先用defineEmits把需要的函数作为emit,之后把emit按照`this.$emit`的方式调用就行

```    <script setup>
    const props = defineProps({
      car: String,
      data: Number
    })
    const emit = defineEmits(['changeMoney'])
    const buy = () => {
      emit('changeMoney', 5)
    }
    </script>

    <template>
        <div class="son">
          子组件 - {{car}} {{data}}
        </div>
        <button @click="buy">花钱</button>
    </template>

    <style scoped>
    .son {
      border: 1px solid #000;
      padding: 30px;
    }
    </style>
```
### 模版引用

通过ref获取对应的组件,然后调用里面的方法

添加ref: - 通过ref生成ref对象 - 通过ref表示绑定

```    <script>
    import { ref } from 'vue'

    const h1Ref = ref(null)
    </script>

    <template>
        <h1 ref="h1Ref">......</>
    </template>
```
不过注意生成ref对象的时候不会立即生效,要等加载完这个对象才不是null

注意,如果ref对象是inp,inp.value拿到DOM,如果是input要获取文本框中的文字,需要在套一层value

### defineExpose:

默认情况下,组件的方法和属性是不开放的,需要用defineExpose去定义暴露的数据和方法

```    <script setup>
    import { defineExpose } from 'vue'
    const count = 999
    const sayHi = () => {
      console.log("Hi")
    }

    defineExpose({
      count,
      say Hi
    })

    </script>

    <template>
      <div class="ref-com"> 
        < p>测试用组件 </p>
      </weig

    ### provide inject
    ```javascript
    import {provide} from 'vue'
    import {inject} from 'vue'
```
如果传的是一个变量,那么直接

```    const count = ...
    provide('count')
```
然后子组件

```    const cnt = inject('count')
```
也可以传函数

```    provide('changeCount', () => {
        ...
    })
    ///////////////////////////////////

    const changeCnt = inject(changeCount)
```
### defineOptions:

props和emits之类的适合setup同级的函数,为了定义其他属性还是要添加一个不同的script,然后正常调整

也可以defineOptions

```    defineOptions({
      name: "LoginIndex,
        ..
    }
```
### defineModel:

可以省去defineprops和defineemits的一套,并且之后可以直接更改对应的值

```    const modelValue = defineModel()
    /////////////之后就可以

    modelValue+=1
    //这个可以直接反映到父组件上
```
由于是实验性,所以需要导入(但好像不用?)

```    // vite.config.js
    import { fileURLToPath, URL } from 'node:url'

    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'

    // https://vitejs.dev/config/
    export default defineConfig({
      plugins: [
        vue({
          script:{
            defineModel: true
          }
        }),
      ],
      resolve: {
        alias: {
          '@': fileURLToPath(new URL('./src', import.meta.url))
        }
      }
    })
```
### pinia

相当于vue3的vuex和router

#### 添加pinia到项目中

```    npm install pinia
```
```    // import './assets/main.css'
    import { createPinia } from 'pinia'

    import { createApp } from 'vue'
    import App from './App.vue'
    const pinia = createPinia()

    const app = createApp(App)
    app.use(pinia)
    app.mount('#app')
    // createApp(App).use(pinia).mount('#app')
```
#### 定义store:

和vue一样有getters,states,\\

如果用组合式api,function()就是actions,ref()就是state,computed()就是getters

只不过这回不需要store.state.参数名,可以直接store.参数名

如果是getters,需要引入computed函数

```    import { defineStore } from 'pinia'
    import { ref, computed } from 'vue'

    const useCounterStore = defineStore('counter', ()=>{
      //state
      const count = ref(0)
      const msg = ref("something")
      //actions
      const addCount = () => count.value++
      const subCount = () => count.value--
      //getters
      const double = computed(() => count.value * 2)
      return {
        count,
        addCount,
        subCount,
        msg,
        double
      }
    })

    export default useCounterStore
```
#### pinia异步:

在pinia中异步函数不需要和同步函数区分开(vuex),可以写到一起,但是该有的await
async不能少

#### pinia解构:

如果对pinia
store进行解构,解构出来的数据会失去响应式,改变后不会反映到这个上面,

如果需要响应式需要storeToRefs函数

原理简单来说就是结构之后,这几个多出来的量是new出来的,所以没有响应式(和原先数据是两份)

#### 持久化:

```    npm i pinia-plugin-persistedstate
```
```    import { createPinia } from 'pinia'
    import piniaPluginPersistedState from 'pinia-plugin-persistedstate'

    const pinia = createPinia()
    pinia.use(piniaPluginPersistedState)
```
如果是组合式api,在defineStore的第三个参数出加上persist:true,第一个参数是名字,第二个是函数主体

默认存到localStore,store.\$id作为id,

也可以个性化:

```    import { defineStore } from 'pinia'
    import { ref, computed } from 'vue'

    const useCounterStore = defineStore('counter', ()=>{
      //state
      const count = ref(0)
      const msg = ref("something")
      //actions
      const addCount = () => count.value++
      const subCount = () => count.value--
      //getters
      const double = computed(() => count.value * 2)
      return {
        count,
        msg,
        addCount,
        subCount,
        double
      }
    },
    {
      persist: {
        key: 'counter',
        path: ['count']
      }
    })

    export default useCounterStore
```
参数: - key: 存在本地的数据的名称 - path: 指定存那些数据

### husky:

提交代码之前做检查

- git init
- 初始化husky: pnpm dlx husky-init && pnpm install
- 修改.husky/pre-commit文件, 把npm

会在提交之前之前package.json下的lint命令,默认是全部检查

#### 暂存区eslint:

只保证自己写的代码是没问题的, - 安装lint-staged: pnpm i lint-staged -
修改package.json

```    {
      ...
      "scripts": {
        ...
        "lint-staged": "lint-staged"
      },
          ...
      "lint-staged": {
        "*.{js,ts,vue}": [
          "eslint --fix"
        ]
      } 
    }
```
### pnpm

和npm一样,只是优化更好

pnpm的语法和yarn一样

### Eslint & prettier:

编辑.eslint.cjs

```    rules: {
        'prettier/prettier': [
          'warn',
          {
            singleQuote: true, // 单引号
            semi: false, // 无分号
            printWidth: 80, // 每行最多80字符
            trailingComma: 'none', // 数组以及对象最后没有逗号
            endOfline: 'auto' // 换行符不限制
          }
        ],
        'vue/multi-word-component-name': [
          'warn',
          {
            ignores: ['index'] // 检查组件名字有多个单词组成的时候忽略index.vue
          }
        ],
        'vue/no-setup-props-destructure': ['off'], // 关闭props解构的检验(解构会丢失响应性)
        'no-undef': 'error'
      }
```
编辑vscode settings.json

```    {
        // Eslint + Vscode 配置自动化格式修复
        "editor.codeActionsOnSave": {
            "source.fixAll.eslint": true
        },
        // 关闭保存自动化
        "editor.formatOnSave": false,
    }
```
### 目录调整:

- 删除初始化的一些默认文件
- 修改剩余daima内容
- 新增调整需要的目录结构
- 拷贝全局样式和图片,安装预处理器支持

### Vuerouter4

![](image.png)

# Maven

## 前排提示:

如果java文件中包含package,先cd到package上一层再运行,或者注释掉package

## vscode maven:

如果要新建maven项目,就新建module

如果要导入Maven项目, vscode会自动检测

删除项目之后需要重启才能移除maven项目

## Maven坐标:

maven中的坐标是资源的唯一标识,通过改坐标可以定位唯一资源位置,在pom.xml中

通过坐标定义项目或者引入项目依赖

Maven 坐标构成: - groupId:
定义当前Maven项目隶属组织名称(一般是域名反写) - artifactId:
定义当前Maven项目名称 - version: 定义当前项目版本号

```        <groupId>com.testmaven</groupId>
        <artifactId>maven-project01</artifactId>
        <version>1.0-SNAPSHOT</version>
```
或者引入依赖:

```        <dependency>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
            <version>1.2.3</version>
        </dependency>
```
## 依赖管理:

### 依赖配置:

```    <dependencies>
        <dependency>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
            <version>1.2.3</version>
        </dependency>
        ......
    </dependencies>
```
然后让vscode刷新maven就行

### 依赖传递

如果项目A依赖于B,B又依赖于其他包

那maven在build的时候会把依赖都处理一遍,和pip类似

假如A依赖B,B依赖junit,但是我不希望在A中引入junit可以用exclusions tag

```    <dependencies>
        <dependency>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
            <version>1.2.3</version>
        </dependency>

        <dependency>
            <groupId>com.example</groupId>
            <artifactId>maven-project2</artifactId>
            <version>1.0-SNAPSHOT</version>
            <exclusions>
                <exclusion>
                    <groupId>junit</groupId>
                    <artifactId>junit</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
    </dependencies>
```
### 依赖范围:

默认情况下可以在任何地方使用,可以通过scope tag指定作用范围

可以用vscode左下角maven-\>lifecycle-\>package打包成jar包

### 生命周期

maven中有三套相互独立的生命周期 - clean: 清理工作 - clean:
移除上一次构建生成的文件 - default: 核心工作,编译,测试,打包,部署等 -
compile: 编译项目源代码 - test: 使用合适的单元测试框架进行测试(junit) -
package: 打包 - install: 安装项目到本地 - site: 生成报告,发布站点等 -
不太关心
按照vscode中lifecycle的排列方式,在同一套生命周期中,后面的执行的时候前面的会一起跟着执行

要运行,第一种是vscode内置的maven组件,第二种是mvn \<周期名称\> 比如mvn
compile等

# springboot:

## 构建springboot项目

vscode里上面敲\>spring,构建Maven项目,加入springweb等

pom.xml里的

```    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.3.2</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
```
是springboot的父工程,所有的springboot功能都需要继承自这个

默认会有这两个

```    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency><!--进行web开发的依赖-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency><!--进行测试的依赖-->
    </dependencies>
```
java目录下会有一个启动类,写法比较固定

```    package com.example.demo;

    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;

    @SpringBootApplication
    public class DemoApplication {

        public static void main(String[] args) {
            SpringApplication.run(DemoApplication.class, args);
        }

    }
```
### 定义一个请求处理类:

```    package com.example.controller;

    import org.springframework.web.bind.annotation.RequestMapping;
    // 请求处理类
    import org.springframework.web.bind.annotation.RestController;

    // 

    @RestController
    public class HelloCtrl {
      @RequestMapping("/hello")
      public String hello(){
        System.out.println("Hello World");
        return "Hello World";
      }
    }
```
于是跟fastapi感觉差不了多少

启动的时候需要大概启动类,跑一下

## http协议:

### 请求头:

- Host: 主机名
- User-Agent: 浏览器版本
- Accept: 表示浏览器能接受的资源类型
- Accept-Language: 表示浏览器偏好的语言
- Accept_encoding: 表示浏览器可以支持的压缩类型, gzip, deflate等
- Content-Type: 请求主体
- Content-Length: 请求主体的大小

get: 请求参数在请求行中,没有请求体,如/brand/findAll?name=OPPO&status=1,
有大小限制

post: 请求函数在请求体中, 没有大小限制

## 请求:

### 简单参数

```    package com.example.controller;

    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RestController;

    import jakarta.servlet.http.HttpServletRequest;
    // javax.servlet 和 jakarta.servlet 是 Java Servlet API 的两个版本。
    // 所以教程里用的是javax那个
    // 大概是因为他用的java11, 我电脑上这个项目用的java17

    @RestController
    public class RequestController {

      @RequestMapping("/simpleParam")
      public String simpleParam(HttpServletRequest request){
        String name = request.getParameter("name");
        String ageStr = request.getParameter("age");
        int age = Integer.parseInt(ageStr);
        System.out.println(name + ":" + age);
        return "OK";
      }
    }
```
http://localhost:8080/simpleParam?name=Tome&age=10

在springboot里,除了一个参数一个参数的读取,这部分被简化成

```    @RequestMapping("/simpleParam1")
    public String simpleParam1(String name, Integer age){
        System.out.println(name + ":" + age);
        return "OK";
    }
```
于是就变成fastapi形式了

但是在fastapi中,如果匹配不到参数会直接报错422,
在springboot里则是自动把未匹配上的参数变成null

可以通过RequestParams规定请求体中的名称

例如

```      @RequestMapping("/simpleParam1")
      public String simpleParam1(@RequestParam(name="name") String username, Integer age){
          System.out.println(name + ":" + age);
          return "OK";
      }
```
可以实现一样的效果

其中@RequestParam(name=\"name\")相当于把name绑定到username上,这样如果我访问

http://localhost:8080/simpleParam1?name=Tome&age=10

username会变成Tome

同理

```      @RequestMapping("/simpleParam1")
      public String simpleParam1(@RequestParam(name="name") String username, Integer age){
          System.out.println(name + ":" + age);
          return "OK";
      }
```
http://localhost:8080/simpleParam1?id=Tome&age=10

username会变成Tome

RequestParam里的required属性默认是True,不传会报错,改成false可以不传

### 实体参数

先定义java类

```    package com.example.pojo;

    public class User {
      private String name;
      private Integer age;


      public String getName() {
        return name;
      }
      public Integer getAge() {
        return age;
      }


      public void setName(String name) {
        this.name = name;
      }
      public void setAge(Integer age) {
        this.age = age;
      }


      @Override
      public String toString() {
        return "User [name=" + name + ", age=" + age + "]";
      }
    }
```
然后定义相应的地址以及函数

```    @RequestMapping("/simplePojo")
    public String simplePojo(User user){
        System.out.println(user);
        return "OK";
    }
```
这样访问http://localhost:8080/simplePojo?name=Tom&age=10

就会返回OK,打印User \[name=Tom, age=10\]

也可以类里再套类

给上面的user增添address属性,

```    package com.example.pojo;

    public class Address {
      private String province;
      private String street;
      public String getProvince() {
        return province;
      }
      public String getStreet() {
        return street;
      }
      public void setProvince(String province) {
        this.province = province;
      }
      public void setStreet(String street) {
        this.street = street;
      }
      @Override
      public String toString() {
        return "Address [province=" + province + ", street=" + street + "]";
      }
    }
```
然后就可以http://localhost:8080/complexPojo?name=Tom&age=10&address.province=北京address.street=天通苑北

### 数组集合类参数:

```    @RequestMapping("simpleArray")
    public String simpleArray(String[] hobby){
        System.out.println(Arrays.toString(hobby));
        return "OK";
    }
```
访问http://localhost:8080/simpleArray?hobby=a&hobby=b&hobby=c则会让hobby变成\[a,b,c\]

不能访问http://localhost:8080/simpleArray?hobby=\[qwertyuiop,a,b\]会出错

也可以

```    @RequestMapping("simpleArray1") 
        public String simpleArray1(@RequestParam List<String> hobby){
        System.out.println(hobby);
        return "OK";
    }
```
### 日期类参数

```    @RequestMapping("/simpleDate")
    public String simpleDate(@DateTimeFormat(pattern="yyyy-MM-dd HH:mm:ss") LocalDateTime updateTime){
        System.out.println(updateTime);
        return "OK";
    }
```
http://localhost:8080/simpleDate?updateTime=2022-12-02%2010:11:12

### Json

```    @RequestMapping("/simpleJson")
    public String simpleJson(@RequestBody User user){
        System.out.print(user);
        return "OK";
    }
```
### 路径参数

```    @RequestMapping("/path/{id}")
    public String simplePath(@PathVariable Integer id){
        System.out.println(id);
        return "OK";
    }
```
和vue配路由一个道理

![4896d63dccacdeadacfa537920ba65e.png](82bf0c2c-45c7-4adb-974b-aac02d9afe7b.png)

### 指定方法

以get为例，可以`@RequestMapping(value="/listDept", method=RequestMethod.GET)`

也可以`@GetMapping("/listDept")`

这样设置了以后用不合适的方法请求会405

如果在@RestController同级使用@RequestMapping,则Controller类内部所有的url前都是带上这段地址

例,如果在Controller上夹@RequestMapping(\"/dept\"),那么之后的@RequestMapping(\"/get\")实际上访问的是\'/dept/get\'

### 设置响应数据

#### \@RequestBody

写在controller上面,将返回值直接响应,如果是实体对象,会转换成json格式

\@RestController = \@Controller + \@ResponseBody

Result类包含code, msg, data和之前vue
axios请求的返回值一样,最好每个哈函数返回值都是一个Result

Result类也有success方法,直接调用就是返回一个200,也可以success(Object
obj)

### 案例:

- dom4j解析xml
- 构建Emp类存储xml数据 把xml变成java类
- 静态页面
- Controller

### 分层解耦:

#### 三层架构:

每一个类只负责一个功能 - Controller: 接受请求,响应数据,
控制层,接受前段发送的请求,对请求进行处理,并响应数据 - Service: 逻辑处理,
业务逻辑层,处理具体的业务逻辑 - Dao: 数据访问,(Data Access
Object)(持久层), 负责数据访问操作,包括数据的增删改查

Controler \<- Service \<- Dao

按照这个链条两两耦合

标准是高内聚低耦合

直接略微改动对象内函数就行了
创建一个容器存储对象然后赋值给对应的接口或者类

#### IOC(控制反转) & DI(依赖注入) & Bean对象

加入@Component
标签,将当前类交给IOC容器管理,成为IOC容器中的bean,然后再需要用对应接口的类的时候加上@Autowired标签表示运行的时候IOC容器会提供该类型的bean对象并赋值给变量

  注解           说明                 位置
  -------------- -------------------- ---------------------------------------------
  \@Component    声明bean的基本注解   不属于以下三类的时候用这个
  \@Controller   \@Component的衍生    控制类, 但是@RestController就相当于用了这个
  \@Service      \@Component的衍生    业务类
  \@Repository   \@Component的衍生    数据访问类(后面和mybatis整合)

前面这四个要想生效还需要@ComponentScan扫描

默认已经包含在@SpringBootApplication, 扫描范围是当前包及子包

但是如果对应的接口下有多个类,那@Autowired会报错,

- \@Primary: 加到类上,代表这个有限选择这个类
- \@Qualifier: \@Qualifier(\"类名\") 指定,这个在@Autowired上写 按类型
- \@Resource: 和Qualifier差不多但是差的是名称,这个不需要@Autowired

# mysql

目前这个电脑装的mysql是基于docker的,文件挂载在d:/docker/mysql

## 数据模型:

![image.png](4f1bc432-06d1-47c6-9c0f-d2ff9dc7daa8.png)

## sql简介:

- sql语句可以单行或者多行书写,以分号结束
- sql语句可以加缩进
- sql里的关键字不区分大小写
- sql的注释,单行注释用\--或者#(mysql),多行注释用(/ *注释* /)
- DDL(Data Definetion Language) DML(Data Manipulation Language) DQL(Data
  Query Language) DCL(Data Control Language)

## DDL:

### 数据库

- 创建数据库: create database 名称;(数据库名字不允许重复),也可以create
  database if not exists 名称
- 查询所有数据库: show databases;
- 使用数据库: use 名称;
- 查询正在使用的数据库: select database();
- 删除数据库: grop database db03;

### 表:

#### 创建表:

```    create table 表名(
      字段1 字段类型 [约束] [comment 字段1注释],
        ...
      字段n 字段类型 [约束] [comment 字段n注释],
    ) [comment 表注释]
```
例:

```    create table table_user(
        id int comment 'ID,唯一标识',
        username varchar(20) comment '用户名',
        name varchar(10) comment '姓名',
        age int comment '年龄',
        gender char(1) comment '性别'
    );
```
对于约束: \|约束\|描述\|关键字\| \|-\|-\|-\|
\|非空约束\|限制该字段不能为null\|not null\|
\|唯一约束\|限制该字段的所有数据都是唯一的\|unique\|
\|主键约束\|主键是一行数据的唯一标识,要求非空且唯一\|primary
key(auto_increment自增)\|
\|默认约束\|保存数据时,如果未指定字段值,则采用默认值\|default\|
\|外键约束\|让两张表的数据建立连接,保证数据的一致性和完整性\|foreign
key\|

对于数据类型

- 数值类型:
  \|类型\|大小(字节数)\|有符号的范围\|无符号(unsigned)的范围\|描述\|备注\|
  \|-\|-\|-\|-\|-\|-\|
  \|tinyint\|1\|\[-128,127\]\|\[0,255\]\|小整数值\|\|
  \|smallint\|2\|\[-2\^15,2\^15-1\]\|\[0,2\^16-1\]\|大整数值\|\|
  \|mediumint\|3\|\[-2\^23,2\^23-1\]\|\[0,2\^24-1\]\|大整数值\|\|
  \|int\|4\|\[-2\^31,2\^31-1\]\|\[0,2\^32-1\]\|大整数值\|\|
  \|bigint\|8\|\[-2\^63,2\^63-1\]\|\[0,2\^64-1\]\|极大整数值\|\|
  \|float\|4\|\[-3.4028235E+38,
  3.4028235E+38\]\|0,\[1.17E-38,3.4E+38\]\|单精度浮点\|float(5,2)5表示数字长度,2表示小数位个数\|
  \|double\|8\|\[-1.79E+308,1.79E+308\]\|\[2.22E-308,1.79E308\]\|双精度浮点\|double(5,2)5表示数字长度,2表示小数位个数\|
  \|decimal\|\|\|\|小数值(精度更高)\|decimal(2,5)5表示数字长度,2表示小数位个数\|

主要是int,double和decimal

- 字符串 \|类型\|大小\|描述\| \|-\|-\|-\|
  \|char\|\[0,255\]字节\|定长字符串\|
  \|varchar\|\[0-65535\]字节\|变长字符串,动态分配内存\|
  \|tinyblob\|\[0-255\]字节\|不超过255个字符的二进制数据\|
  \|tinytext\|\[0-255\]字节\|短文本字符串\|
  \|blob\|\[0-65535\]字节\|二进制形式的长文本数据\|
  \|text\|\[0-65535\]字节\|长文本数据\|
  \|mediumblob\|\[0-2\^24-1\]字节\|二进制形式的中等长度文本数据\|
  \|mediumtext\|\[0-2\^24-1\]字节\|中等长度文本数据\|
  \|longblob\|\[0-2\^31-1\]字节\|二进制形式的极大长度文本数据\|
  \|longtext\|\[0-2\^31-1\]字节\|极大长度文本数据\|

如果是char(10)那无论到没到10个字符内存里都是10个字节

但如果是varchar(10)那最多10个字节,可能会少

- 日期类型 \|类型\|大小\|范围\|格式\|描述\| \|-\|-\|-\|-\|-\|
  \|date\|3\|1001-01-01到9999-12-31\|YYYY-MM-DD\|日期值\|
  \|time\|3\|-838:59:59到838:59:59\|HH:MM:SS\|时间值或持续时间\|
  \|year\|1\|1901到2155\|YYYY\|年份值\| \|datetime\|8\|1000-01-01
  00:00:00 到 9999-12-31 23:59:59\|YYYY-MM-DD
  HH:MM:SS\|混合日期和时间值\| \|timestamp\|4\|1970-01-01 00:00:01 到
  2038-01-19 03:14:07\|YYYY-MM-DD HH:MM:SS\|混合日期和时间值,时间戳\|

#### 表的增删改查:

```    -- Active: 1724136082504@@127.0.0.1@3306@db01
    show TABLES;
    -- 查询当前数据库下的所有表

    desc table_user;
    -- 查询当前字符串下的所有表头

    show create table employers;
    -- 查询建表的时候输入的语句

    ALTER TABLE employers ADD phone_no VARCHAR(11) comment '手机号';
    -- 插入一个叫phone_no的列,类型是动态字符串最长11个字符

    ALTER TABLE employers MODIFY phone_no VARCHAR(13) comment '手机号';
    -- 把phone_no的数据类型变为动态字符串最长13个字符

    ALTER TABLE employers CHANGE phone_no phone_number VARCHAR(11) comment '手机号';
    -- 把phone_no的名称改为phone_number

    ALTER TABLE employers DROP COLUMN phone_number;
    -- 删掉phone_number这一列

    RENAME TABLE employers to emp;
    -- 把employers表重命名为emp

    RENAME TABLE emp to employers;
    -- 还原

    DROP TABLE employers;
    -- 删除employers表
```
- 添加字段: alter table 表名 add字段名 类型(长度) \[comment 注释\]
  \[约束\]
- 修改字段类型: alter table 表名 modify 字段名 新数据类型(长度)
- 修改字段名和字段类型: alter table 表名 旧字段名 新字段名 类型(长度)
  \[comment 注释\] \[约束\]
- 删除字段: alter table 表名 drop column 字段名
- 修改表名: rename table 表名 to 新表名

## DML:

### Insert

- 指定字段添加数据: Insert into 表名 (字段名1,字段名2) values (值1,值2);
- 全部字段添加数据: insert 表名 values (值1,值2,\...);
- 批量添加数据(指定字段): insert into 表名 (字段名1, 字段名2) values
  (值1,值2) (值1,值2);
- 批量添加数据(全部字段): insert into 表名 values (值1,值2) (值1,值2);

### Update

- update 表名 字段名1=值1, 字段名2=值2, \...\[where条件\]

### Delete

- delete from 表名 \[where条件\]

## DQL

SELECT,各种SELECT

基本语法是

```    SELECT
        字段列表
    FROM
        表名列表
    WHERE
        条件列表
    GROUP BY
        分组字段列表
    HAVING
        分组后条件列表
    ORDER BY
        排序字段列表
    LIMIT
        分页参数
```
### 基本查询:

- 查询多个字段 `SELECT 字段1,字段2,字段3 FROM 表名`
- 查询所有字段 `SELECT * FROM 表名`
- 设置别名 `SELECT 字段1 [as 别名1], 字段2 [as 别名2] from 表名`
- 去重: `SELECT DISTINCT 字段列表 FROM 表名`

### 条件查询:

  比较运算符              功能
  ----------------------- ----------------------------------------
  \>                      大于
  \>=                     大于等于
  \<                      小于
  \<=                     小于等于
  =                       等
  \<\>或者!=              不等
  between \... and \...   在某个范围之间(闭区间)
  in(\...)                在列表里的值
  like 占位符             模糊匹配(\_匹配单个字符,%匹配任意字符)
  is null                 是空

  逻辑运算符    功能
  ------------- ------
  and 或者 &&   并且
  or 或者 \$    
  not 或者!!    非

### 分组查询:

`SELECT 字段列表 FROM 表名 [where 条件] GROUP BY [条件] [HAVING条件]`

#### 聚合函数

  函数    功能
  ------- ----------
  count   统计数量
  max     最大值
  min     最小值
  avg     平均值
  sum     求和

基本语法: `select 聚合函数(字段列表) from 表名`

### 排序查询:

`SELECT 字段列表 FROM 表名 [WHERE 条件列表] [GROUP BY 分组字段] ORDER BY 字段1 排序方式1...;` -
升序: ASC - 降序: DESC

### 分页查询

这个在不同数据库中有不同实现方式
`SELECT 字段列表 FROM 表名 LIMIT 开始,结束;`

### 多表:

#### 建表:

##### (多对1)外键:

像primary key那样只不过换成foreign key

建表的时候创建外键

```    CREATE TABLE 表名(
        字段名 数据类型
        ...
        [constraint] [外键名称] foreign key (外键字段名) references 主表(字段名)
    )
```
建完表后添加外键

```    alter table 表名 add constraint 外键名称 foreign key(外键字段名) references 主表 (字段名);
```
##### (1对1)第一范式:

把一个表拆成两张表,其中一个外键对应另一个表的主键

##### (多对多)中间表:

#### 查询:

##### 连接查询:

- 内连接: [\\(A\\cap B\\)]{.arithmatex}
- 隐式内连接: `select 字段列表 from 表1, 表2 where 条件`
- 显式内连接: `select 字段列表 from 表1 [inner] join 表2 on 连接条件`
- 外连接:
- 左外连接: [\\(A + A\\cap B\\)]{.arithmatex}
  - `select 字段列表 from 表1 left [outer] join 表2 on 连接条件`
- 右外连接: [\\(B + A\\cap B\\)]{.arithmatex}
  - `select 字段列表 from 表1 right [outer] join 表2 on 连接条件`

##### 子查询

标量子查询

#### 事务:

注意mysql中默认是把每条语句当做单独的事务处理,要把autocommit关掉,`set autocommit = OFF`

一个事务中的雨具要么都执行要么都不执行,没有commit前可以rollback

- 开启事务: `start transaction`
- 提交事务: `commit`
- 回滚: `rollback`

#### 索引:

提升查找效率,占用储存空间并且降低增删改的效率

默认是B+数

- 创建索引 `create [unique] index 索引名 on 表名(字段名1, ...)`
- 查看索引 `show index from 表名`
- 删除索引 `drop index 索引名 on 表名`

除了当前值以外,主键和唯一限制的列也会被创建索引

import random import datetime import time from pypinyin import
lazy_pinyin def random_name(): str = \"\" for i in
range(random.randint(1,4)): str += chr(random.randint(0x4e00, 0x9fff))
return str def random_time():

```    # 获取当前时间的时间戳（单位：秒）
    now_timestamp = datetime.datetime.now().timestamp()

    # 计算一年前的时间戳
    twenty_year_ago_timestamp = now_timestamp - 365 * 24 * 60 * 60 * 20

    # 生成一个介于一年前和现在之间的随机时间戳
    random_timestamp = random.uniform(twenty_year_ago_timestamp, now_timestamp)

    # 将时间戳转换为日期格式
    random_datetime = datetime.datetime.fromtimestamp(random_timestamp).strftime("%Y-%m-%d %H:%M:%S")
    return random_datetime.split(" ")[0]
```
def random_password(p = 0.8): if random.random() \< p: return \"123456\"
else: password = \"\" for i in range(random.randint(4,10)): password +=
str(random.randint(0,9)) return password

pinyin = set() num = 0 while num \< 2000: name = random_name() time =
random_time() password = random_password() py =
\"\".join(lazy_pinyin(name)) if py in pinyin: continue pinyin.add(py)
num += 1 \# id, username, password, name, gender, image, job, entrydate,
dept_id, created_time, altered_time \#
(1,\'zhenfenleizhan\',\'123456\',\'眹竕攂閚\',1,\'37.jpg\',2,\'2015-06-30\',1,now(),now()),
print(f\"({num},\'{py}\',\'{password}\',\'{name}\',{random.randint(0,1)},\'{random.randint(0,1000)}.jpg\',{random.randint(0,4)},\'{time}\',
{random.randint(1,4)},now(), now()),\")

```    def random_password(p = 0.7):
        if random.random() < p:
            return "123456"
        else:
            password = ""
            for i in range(random.randint(4,10)):
                password += str(random.randint(0,9))
            return password
    random_password()
```
```    '113946955'
```
# mybatis

## 创建:

创建项目的时候在springboot依赖以外还需要mysql-driver和mybatis相关

## 配置:

在application.properties里写如下几个东西:

```    spring.application.name=springboot-mybatis-quick-start
    spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
    # 数据库连接url,最后一个参数是数据库的名称
    spring.datasource.url=jdba:mysql//localhost:3306/db05
    # 数据库登录账号及密码
    spring.datasource.username=root
    spring.datasource.password=123456
```
然后查询的时候:

```    package com.example.mapper;

    import com.example.pojo.User;

    import java.util.List;

    import org.apache.ibatis.annotations.Mapper;
    import org.apache.ibatis.annotations.Select;

    @Mapper//运行的时候框架会自动生成实现类对象,然后交给IOC管理
    public interface UserMapper {

      @Select("select * from users")
      public List<User> list();
    }
```
但实际上是这么写的:

```    package com.example.demo;

    import java.sql.Connection;
    import java.sql.DriverManager;
    import java.sql.ResultSet;
    import java.sql.Statement;
    import java.util.ArrayList;
    import java.util.List;

    import org.junit.jupiter.api.Test;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.boot.test.context.SpringBootTest;

    import com.example.mapper.UserMapper;
    import com.example.pojo.User;

    @SpringBootTest /// 整合测试的注解
    class SpringboootMybatisQuicStartApplicationTests {
        @Autowired
        private UserMapper userMapper;

        @Test
        public void contextLoads() {
            List<User> userList = userMapper.list();
            System.out.print("printing output\n");
            for (User a: userList){
                System.out.println(a);
            }
        }

        @Test
        public void testJdbc() throws Exception {
            // 指定要用的sql driver
            // 1. 注册驱动
            Class.forName("com.mysql.cj.jdbc.Driver");

            // 2. 获取连接对象
            String url = "jdbc:mysql://localhost:3306/db05";
            String username = "root";
            String password = "123456";
            Connection connection = DriverManager.getConnection(url, username, password);

            // 3.获取执行SQL的对象Statement,执行SQL,返回结果
            String sql =  "select * from users";
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(sql);

            // 4.封装结果数据
            List<User> userList = new ArrayList<>();
            while (resultSet.next()){
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                short age = resultSet.getShort("age");
                short gender = resultSet.getShort("gender");
                String phone = resultSet.getString("phone");

                User user = new User(id, name, age, gender, phone);
                userList.add(user);
            }

            // 5. 释放资源
            statement.close();
            connection.close();

            for (User a: userList){
                System.out.println(a);
            }
        }
    }
```
## 数据库连接池:

是一个容器,负责分配管理数据库连接,允许程序使用现有的数据库连接,并且释放空闲时间超过最大空闲时间的连接

springboot默认用的是hakari,也有用的比较多的是Druid,阿里的

如果要切换数据库连接池的话,直接pom.xml引入依赖就行

## Iombook

直接在类上面加注释就可以省掉get/set/constructor

  注释                   说明
  ---------------------- --------------------------------------------------
  \@Getter/@Setter       为所有的属性提供get/set方法
  \@ToString             会给类自动生成toString方法
  \@EqualsAndHashCode    根据类所拥有的非静态字段自动重写equals和hashcode
  \@Data                 上面那些加一起
  \@NoArgsConstructor    无参构造
  \@AllArgsConstructor   全参构造

## 动态设置sql语句:

用mybatis的占位符 -
#{\...}将这个替换为?,生成预编译sql,参数传递的时候用这个 -
\${\...}拼接SQl,直接把参数拼接在sql语句当中,存在sql注入问题,需要动态设置表名和列表的时候使用

# {} 不能出现在引号内,但是\${}可以,因为在预编译的sql中\'?\'会出问题

```    @Delete("delete from employers where id = #{id}")
      public void delete(Integer id);
```
在运行的事务会先预编译一次sql语句,把变量部分用?替代,把预处理的sql缓存到缓存中单做有参函数(预编译) -
性能高 - 更安全(防止sql注入)

sql注入是通过操作数据修改实现定义好的sql语句

返回值是影响的数据条目

也可以把所有的值封装成一个类传递到函数当中

### 删除:

```      @Delete("delete from employers where id = #{id}")
      public void delete(Integer id);
```
### 新增数据

```      @Insert("""
    INSERT INTO employers(username, name, gender, image, job, entrydate, dept_id, created_time, altered_time) VALUES
    (#{username},#{name},#{gender},#{image},#{job},#{entrydate},#{deptId},#{createdTime},#{alteredTime})""")
      public void insert(Employer employer);
```
#### 获取主键:

如果直接插入获取不到主键值(在上面那个案例中,主键id是auto_incremented),需要额外加注解

目前的理解是由于没有提交主键id而是让sql
auto_increment,在sql执行完所有语句更新数据库之前,这个id是不存在的,能拿到的只有我们新增的树脂中给定的量

```    @Options(keyProperty="id", useGeneratedKeys=true)
    @Insert(...
```
### 更新:

```      @Update("update employers set username=#{username}, name=#{name}, image=#{image}, job=#{job}, entrydate=#{entrydate}, dept_id=#{deptId}, altered_time=#{alteredTime} where id=#{id};")
      public void update(Employer employer);
```
### 查询:

```      @Select("SELECT * from employers WHERE id=#{id}")
      public Employer getById(Integer id);
```
myBatis的封装中,如果实体类属性名和数据库返回的字段名一致的话,会自动封装,否则为null -
方法一,sql中起别名 - 方法二,通过Results注解手动映射封装

```    @Results({
      @Result(column="dept_id", property = "deptId"),
      @Result(column="created_time", property = "createdTime"),
      @Result(column="altered_time", property = "alteredTime")
    })
    @Select("SELECT id,username, password, name, gender, image, job, entrydate, dept_id as deptId, altered_time as alteredTime, created_time as createdTime from employers WHERE id = #{id}")
    public Employer getById(Integer id);
```
- 方法三: 开启驼峰自动映射:

```        // 在application.properties中
        mybatis.configuration.map-underscore-to-camel-case=true
```
### XML映射文件:

- XML映射文件的名称和Mapper接口名称一致,并且将XML映射文件和Mapper接口放置在相同包下(通报同名)
- XML映射文件的namspac恶属性为Mapper接口全限定名一致(com.example.mapper.EmployerMapper)
- XML映射文件中的sql语句的id和Mapper中的方法名一致,并保持返回类型一致

```    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
    <!-- 上面这坨不用管,是固定的 -->
    <mapper namespace="com.example.mapper.EmployerMapper">

      <select id="list" resultType="com.example.pojo.Employer">
        select * ...
      </select>

    </mapper>
```
select标签的id属性要和接口当中的方法名一样,

## 设置日志:

`mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl`

## 动态sql:

在xml中加入一堆标签

```    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
    <mapper namespace="com.example.mapper.EmployerMapper">

      <select id="list" resultType="com.example.pojo.Employer"> 
        Select * 
        from employers 
        <where>
          <if test="name != null">
            name LIKE CONCAT('%',#{name},'%') 
          </if>
          <if test="gender != null">
            AND gender = #{gender} 
          </if>
          <if test="begin != null and end != null">
          AND entrydate BETWEEN #{begin} AND #{end} 
          </if>
        </where>
        ORDER BY altered_time; 
      </select>
    </mapper>
```
###

用于逻辑判断

###

假设在上面的代码中gender是1,name是null
那么不用的情况下sql语句是`Select * from employers where and gender = 1`

第一个and需要扔掉,如果用标签的话就没有这个问题

(其实就是一个简单的逻辑判断,不过这样写确实方便很多)

会自动处理所有的and或者or

###

同样的问题,update语句中的逗号

###

参数: - collections: 遍历的集合 - item: 遍历出来的元素 - separator:
分隔符 - open: 遍历开始前拼接的sql语句 - close:
遍历结束的时候拼接的sql语句

###

可以复用一段sql语句

在sql中用id指定sql段的唯一标识,然后用include中用refid指定用哪段sql

```    <sql id="commonSelect">
        Select * 
        from employers 
      </sql>
      <select id="list" resultType="com.example.pojo.Employer"> 
        <!-- Select * 
        from employers  -->
        <include refid="commonSelect">

        </include>
        <where>
          <if test="name != null">
            name LIKE CONCAT('%',#{name},'%') 
          </if>
          <if test="gender != null">
            AND gender = #{gender} 
          </if>
          <if test="begin != null and end != null">
          AND entrydate BETWEEN #{begin} AND #{end} 
          </if>
        </where>
        ORDER BY altered_time; 
      </select>
```
## 文件上传:

把文件传到服务器

前端:

```    <form action="/upload" method="post" enctype="multipart/form-data">
        <!--这里如果enctype是默认的话,只会提交文件名-->
    姓名: <input type="text" name="username"><br>
    年龄: <input type="text" name="age"><br>
    头像: <input type="file" name="image"><br>
    <input type="submit" value="提交">
    </form>
```
element-plus里有el-upload组件

这样发送的请求里Content
Type会有boundary参数表示分隔符,用这个把提交的各项数据隔开

服务端接受请求的时候,java内部有MultiparFile类可以接收这部分数据

如果要进一步存到本地

```    image.transferTo(path);
```
获取原始文件名

```    image.getOringinalFileName
```
```    image.transferTo(new File("D:\\Desktop\\" + image.getOriginalFilename()));
```
为了防止重复,可以用uuid

```    String uuid = UUID.randomUUID().toString();
```
## 配置参数:

在application.properties文件里配置参数,用@Value注解引入
![image.png](c17d65ef-45d3-484f-b49d-7d70fe20d90a.png)

### yaml格式:

除了application.properties以外,也支持application.yml或者yaml

xml比较长,properties比较乱,于是有了yml

yaml字典:

```    user:
        name: Tom
        age: 20
```
yaml数组

```    user:
        - Tome
        - Tom
```
### \@ConfigurationProperties:

```    aliyun:
        oss:
            endpoint: xxx
            accessKeyId: xxx
            accessKeySecret: xxx
            ...
```
```    @Data
    @Component
    @ConfiguraationProperties(prefix="aliyun.oss")
    public class AlyunOSSProperties{
        private String endpoint;
        private String accessKeyId;
        private String accessKeySecret;
    }
```
同时需要引入依赖(自动识别被这个注解识别的量,可选)

```    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-configuration-processor</artifactId>
    </dependency>
```
## 登录:

### 登录功能

实现很简单,条件查询看看有没有数据,有的话就成功,没有就失败,如果有多个那说明表建的有问题