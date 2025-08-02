
:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>webpage</title>
        </head>
        <body>
            some webpack
        </body>
    </html>
```::::

::: tabbed-block
[examples/basic_html_stuff/basic_skeleton.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/basic_skeleton.html)
:::
::::::
::::::::
:::::::::

## 1.2 tag

there are single tags and double tags - double tag\< html\>\< /html\> -
single tag\< img\>

### 1.2.1 html basic skeleton:

#### \<!DOCTYPE html\>declaration (there should only be one of this at the top of the the document)

declare this document is a html

#### 1.2.1.1 \< html\>\< /html\>(there should only be one)

define a html element

#### 1.2.1.2 \< head\>\< /head\>(there should only be one)

define headers and hyperparams

#### 1.2.1.3 \< body\>\< /body\>(there should only be one)

the body part of the html, this is what can be seen in the webpage

#### 1.2.1.4 \< title\>\< /title\>(should be in \< head\>)

define the name of the webpage

#### 1.2.1.5 \< meta\>(optional)

define the attributes of a html, including keywords like \< meta charset
= \"UTF-8\"\>

for specific params :https://www.w3schools.com/tags/tag_meta.asp

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="2:2"}
::: tabbed-labels
codeeffect
:::

:::::: tabbed-content
:::: tabbed-block
```    %%html
    <!DOCTYPE html>
    <html>
        <head>
            <title>webpage</title>
            <meta charset = "UTF-8">
        </head>
        <body>
            some webpage
        </body>
    </html>
```::::

::: tabbed-block
[examples/basic_html_stuff/meta.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/meta.html)
:::
::::::
::::::::
:::::::::

### 1.2.2 other tags:

#### 1.2.2.1 \< h\>\< /h\>

define the titles, from h1 to h6

- to define position: add align attr, align =
  \"left\"\|\"center\"\|\"right\"

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="3:2"}
::: tabbed-labels
codeeffect
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>webppage</title>
        </head>
        <body>
            some webpage
            <h1 align = "center">title1</h1>
            <h2 align = "left">title2</h2>
            <h3 align = "right">title3</h3>
            <h4>title4</h4>
            <h5>title5</h5>
            <h6>title6</h6>
        </body>
    </html>
```::::

::: tabbed-block
[examples/basic_html_stuff/h.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/h.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.2 \< p\>\< /p\>

define paragraph

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="4:2"}
::: tabbed-labels
code效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>webpage</title>
        </head>
        <body>
            some webpage

            <!--even if you put numerous space here, it would not change lines-->
            something
            <p>title1</p>
            <p>title2</p>
            <p>title3</p>
            <p>title4</p>
            <p>title5</p>
            <p>title6</p>
        </body>
    </html>
```::::

::: tabbed-block
[examples/basic_html_stuff/p.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/p.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.3 \< br\>

\\n can also be written as \< br/\>

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
            <title>webpage</title>
        </head>
        <body>
            some webpage
            <!--这里空再多空格也换不了行-->
            <!--no matter how much space you put here, it would not start a new line-->
            something
            <p>标 ti <br>题1 tle 1</p>
            <p>标题2 title2</p>
        </body>
    </html>
```::::

::: tabbed-block
[examples/basic_html_stuff/br.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/br.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.4 \< hr\>

a horizontal line

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="6:2"}
::: tabbed-labels
codeeffect
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>网页 webpage</title>
        </head>
        <body>
            某个网页 some webpage
            <!--no matter how much space you put here, it would not start a new line-->
            <!--这里空再多空格也换不了行-->
            something
            <p>标题1 title1</p>
            <hr color="red">
            <p>标题2 title2</p>
        </body>
    </html>
```::::

::: tabbed-block
[examples/basic_html_stuff/hr.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/hr.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.6 \< img\>

used to display a picture

attributes:

- src: the path to the picture, could be a url
- alt: the text that would display when the pic goes wrong
- title: the title of the img, the text that would display when the
  mouse is over the img
- height: the height of the img
- width: the width of the img

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="7:2"}
::: tabbed-labels
codeeffect
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>webpage</title>
        </head>
        <body>
            <img src="https://prts.wiki/images/ak.png?8efd0" alt="test" width="100" height="100" style="color:red;background-color:powderblue">
            <img src="https://prts.wi_ki/images/ak.png?8efd0" alt="test" width="100" height="100" style="color:red">
        </body>
    </html>
```::::

::: tabbed-block
[examples/basic_html_stuff/img.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/img.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.7 \< a\>

to achieve links

attrs:

- href: the link (url or local path), if no href, then a is just a text

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="8:2"}
::: tabbed-labels
codeeffect
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
                <img src="https://prts.wiki/images/ak.png?8efd0" alt="test" width="100" height="100" style="color:red;background-color:powderblue">
            </a>
        </body>
    </html>
```::::

::: tabbed-block
[examples/basic_html_stuff/a.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/a.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.8 texts:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="9:1"}
::: tabbed-labels
info
:::

:::: tabbed-content
::: tabbed-block
this part is concentrated in
[examples/basic_html_stuff/text.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/text.html)
:::
::::
::::::
:::::::

##### 1.2.2.8.1 \< b\>

bold

:::: {.admonition .example}
code

```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <b style="text-align:center" title="example">paragraph1</b>
            <p style="text-indent:30px;color:red">paragraph2</p>
            <div>the style when we do not use p</div>
        </body>
    </html>
```::::

##### 1.2.2.8.2 \< em\>

emphasis

:::: {.admonition .example}
code

```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <em style="text-align:center" title="example">paragraph1</em>
            <p style="text-indent:30px;color:red">paragraph2</p>
            <div>the style when we do not use p</div>
        </body>
    </html>
```::::

##### 1.2.2.8.3 \< del\>

a line on the words

:::: {.admonition .example}
代码

```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <del style="text-align:center" title="example">paragraph1</del>
            <p style="text-indent:30px;color:red">para<mark>graph</mark>2</p>
            <div>the style when we do not use p</div>
        </body>
    </html>
```::::

##### 1.2.2.8.4 \< i\>

italicize

:::: {.admonition .example}
代码

```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <i style="text-align:center" title="example">paragraph1</i>
            <p style="text-indent:30px;color:red">paragraph2</p>
            <div>the style when we do not use p</div>
        </body>
    </html>
```::::

##### 1.2.2.8.5 \< span\>

no special meanings, add a class for css

:::: {.admonition .example}
code

```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <span style="text-align:center" title="example">paragraph1</span>
            <p style="text-indent:30px;color:red">paragraph2</p>
            <div>the style when we do not use p</div>
        </body>
    </html>
```::::

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="10:1"}
::: tabbed-labels
code intergrated
:::

::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <p>p:paragraph1</p>
            <br>
            <b>b:paragraph1</b>
            <br>
            <span>span:paragraph1</span>
            <br>
            <em>em:paragraph1</em>
            <br>
            <i>i:paragraph1</i>
            <br>
            <del>paragraph1</del>
            <br>
            <strong>paragraph1</strong>
        </body>
    </html>
```::::
:::::
:::::::
::::::::

#### 1.2.2.9 \< audio\>\< /audio\>

- src: src to the the audio
- controls: controls by default, set the control panel
- loop: whether to play the audio in loop
- autoplay: play in auto, but some browsers would not allow this

=== warning \"\" no examples because I simply forgot, would add this
afterwards

#### 1.2.2.10 \< video\> \< /video\>

- controls: controls by default, set the control panel
- loop: whether to play the audio in loop
- autoplay: play in auto, but some browsers would not allow this, could
  only autoplay if muted
- muted: whether the video is muted

=== warning \"\" same as above

#### 1.2.2.11 \< ol\>\< /ol\>(might be error display this in jupyter)

ordered list,list elements are \< li\>\< /li\> tags

attrs:

- type:
  - 1(numbers)
  - a(lower case letter)
  - A(capitalized letters)
  - i(lower case roman numeral)
  - I(upper case roman numeral)

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="11:2"}
::: tabbed-labels
code效果
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
[examples/basic_html_stuff/ol.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/ol.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.12 \< li\>\< /li\>

the list elements in ol or ul

#### 1.2.2.13 \< ul\>\< /ul\>

unordered list, but \< li\>\< /li\> did not change

there can only be li tags in ul, but usually just set the css to flex

属性:

- type:
  - disc:circle
  - circle:hollow circle
  - square:square
  - none:nothing

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="12:2"}
::: tabbed-labels
codeeffect
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
[examples/basic_html_stuff/ul.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/ul.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.14 \< table\>\< /table\>

- tables:\< table\>\< /table\>
  - attrs:
    - border: table border
    - width: table width
    - height: table height
- table elements:
  - rows:\< tr\>\< /tr\>
  - columns/units:\< td\>\< /td\>
  - header units: \< th\>\< /th\>
- table areas:
  - thead header
  - tbody body
  - tfoot footer

in vscode, we can input table\>tr*5\>td*5 to get 5\*5 table

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="13:2"}
::: tabbed-labels
code效果
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
                    <td>elem11</td>
                    <td>elem12</td>
                </tr>
                <tr>
                    <td>elem21</td>
                    <td>elem22</td>
                </tr>
            </table>
        </body>
    </html>
```::::

::: tabbed-block
\[example/basic_html_stuff/table.html\]
:::
::::::
::::::::
:::::::::

##### 1.2.2.14.1 merge unit blocks in table

merge units: - merge columns :colspan - merge rows :rowspan

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="14:2"}
::: tabbed-labels
code效果
:::

:::::: tabbed-content
:::: tabbed-block
```    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <p>merge 21 and 22:rowspan</p>
            <p>merge 35 and 45:colspan</p>
            <p>merge 41,42,51,52:rowspan + colspan</p>
            <br>
            <table border="1" width="600px" height="400px">
                <tr>
                    <td>11</td>
                    <td>12</td>
                    <td>13</td>
                    <td>14</td>
                    <td>15</td>
                </tr>
                <!-- originally
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
                <!-- originally
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
\[examples/basic_html_stuff/table.html\]
:::
::::::
::::::::
:::::::::

#### 1.2.2.15 \< form\>\< /form\>

(after vue and element-plus, i dont think we need this)

to create the form we can submit

- action: webpage
- name: the name of the form, get\|post,

the elements of the form are \< input\>\< /input\>

usually a form consist of the three elements

- title of the form
- the main ares of the form
- the button to submit

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="15:2"}
::: tabbed-labels
codeeffect
:::

:::::: tabbed-content
:::: tabbed-block
```    <form>
        <input type="text">input something
        <input type="submit" value = "submit">
    </form>
```::::

::: tabbed-block
[examples/basic_html_stuff/form.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/form.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.16 \< input\>\< /input\>

usualy used in vue, using v-model to bind with variables

- type: define input type:
- text: textarea
  - placeholder: define prompt
- password: password
  - placeholder: define prompt
- radio: multi selection
  - name: define groups, only one would be selected from each group
  - checked: whether this is checked
- checkbox: single selection
  - checked: whether this is checked
- file: upload files

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="16:2"}
::: tabbed-labels
codeeffect
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
        male<input type="radio" name="gender">
        female<input type="radio" name="gender">
    </body>
    </html>
```::::

::: tabbed-block
\[example/basic_html_stuff/input.html\]
:::
::::::
::::::::
:::::::::

#### 1.2.2.17 select:

drop-down menu

inside select, we can use option tag to set options,checked to set
whether this block is checked

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="17:2"}
::: tabbed-labels
codeeffect
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
[examples/basic_html_stuff/select.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/select.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.18 \< textarea\>\< /textarea\>:

an area of texts

input tag that can be enlarged, usage is the same as input tag

#### 1.2.2.19 \< label\>\< /label\>:

the info for some tag, can also include a form to enlarge the click area

attr: - for to set the corresponding form - or simply use label to
surround the tag

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="18:2"}
::: tabbed-labels
codeeffect
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
        <input type="radio" name="gender" id="man"><label for="man">male</label>
        <label><input type="radio" name="gender">female</label>
    </body>
    </html>
```::::

::: tabbed-block
[examples/basic_html_stuff/label.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/label.html)
:::
::::::
::::::::
:::::::::

#### 1.2.2.20 \< button\>\< /button\>:

- type:
- submit: submit button, to submit data to backend
- reset: reset button
- button: normal button
- href: a link

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="19:2"}
::: tabbed-labels
codeeffect
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
        male<input type="radio" naem="gender">
        female<input type="radio" name="gender">
        <button type="reset">reset</button>
        <button type="submit"></button>
    </body>
    </html>
```::::

::: tabbed-block
[examples/basic_html_stuff/button.html](https://github.com/everythingfades/html/blob/main/examples/basic_html_stuff/button.html)
:::
::::::
::::::::
:::::::::

## 1.3 block elements and inline elements:

the displat type is different, some element-plus componenets need to fix
the inline attr

see:

[this](https://www.runoob.com/html/html-blocks.html)
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
