
:::: tabbed-content
::: tabbed-block
这部分内容请自行查看example/js_involved/html/script_tag_js.html
```::::
::::::
:::::::

规范问题把js的\< script\>\< /script\>写到\< body\>\< /body\>里面的最下面

### 3.1.2 引入外部js

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="2:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
这部分内容请自行查看example/js_involved/html/outer_js.html
:::
::::
::::::
:::::::

还是\< script\>\<
/script\>,引用和之前一样,相对引用和绝对应用,通过src属性定义js文件路径,如果有src属性,\<
script\>\< /script\>之间的js语句不会被执行

### 3.1.3 内联js:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="3:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
这部分内容请自行查看example/js_involved/html/inline_js.html
:::
::::
::::::
:::::::

可以写入标签内部,vue会用这种模式

## 3.2 注释:

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="4:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
这部分内容请自行查看example/js_involved/html/comments.html
:::
::::
::::::
:::::::

### 3.2.1 单行注释

:::: {.admonition .example}
代码

```    // 我是单行注释
```::::

### 3.2.2 块注释

:::: {.admonition .example}
代码

```    /*
    我是块注释
    */
```::::

js语句末尾要加分号,不过实际开发中可写可不写,但是尽量要格式统一

## 3.3 输入输出

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="5:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
这部分内容请自行查看example/js_involved/html/input_output.html
:::
::::
::::::
:::::::

### 3.3.1 document.write()

相当于把html当做txt直接写

:::: {.admonition .example}
代码

```    document.write('我是div标签')//这个不会有标签
    document.write('<h1>我是标题</h1>')//这个会直接变成h1标签
```::::

### 3.3.2 alert

直接在浏览器弹出警告

:::: {.admonition .example}
代码

```    alert("alert")
```::::

### 3.3.3 console.log()

在控制台打印,网页上不可见

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="6:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    console.log("console")
```::::

::: tabbed-block
console
:::
::::::
::::::::
:::::::::

### 3.3.4 prompt

让用户输入东西

:::: {.admonition .example}
代码

```    prompt("输入东西:")
```::::

## 3.4 各种量

::::::: {.admonition .info}
Info

:::::: {.tabbed-set .tabbed-alternate tabs="7:1"}
::: tabbed-labels
说明
:::

:::: tabbed-content
::: tabbed-block
这部分内容请自行查看example/js_involved/html/var.html
:::
::::
::::::
:::::::

### 3.4.1 变量赋值:

- let
- var

相当于kotlin的var和val,val不允许重新赋值

let可以一行声明多个变量但是不推荐

### 3.4.2 常量:

const

相当于java的final,kotlin的const

:::: {.admonition .example}
代码

```    const a =10
    a =5 // Explo--osion!!!
```::::

## 3.5 数据类型:

- number
- string
- boolean
- undefined
- null

### 3.5.1 number:

js的数字部分浮点和整型

常见运算符和python,java等一致

#### 3.5.1.1 NAN:

如果出现数据类型的错误,比如字符串减数组会得到NAN(熟悉的not a number)

任何和NaN的运算都会返回NaN

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="8:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const a = "string"
    console.log(a - 2)
    console.log((a - 2) + 1)
```::::

::: tabbed-block
NaN NaN
:::
::::::
::::::::
:::::::::

### 3.5.2 string:

比python,java等多一个可以用\`\`包裹,相当于python的f\'\',可以往字符串中加变量值

同时,js是弱类型语言,可以实现字符串加数字等让某些魔怔人发出尖锐爆鸣声的操作

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="9:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const str = `string`
    console.log(str + 19)
```::::

::: tabbed-block
string19
:::
::::::
::::::::
:::::::::

#### 3.5.2.1 反引号包裹的模版

和.format,printf,以及kotlin的\$差不多,但是模板字符串只能用反引号包裹

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="10:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const a = 19
    console.log(`这里有${a}个人`)
```::::

::: tabbed-block
这里有19个人
:::
::::::
::::::::
:::::::::

### 3.5.3 boolean

熟悉的boolean,在哪里都差不多

在js里 \'\',0,undefined, null, false,
NaN在逻辑运算上和false等价,其余都是True

### 3.5.4 undefined:

Java和kotlin的null,python的None

### 3.5.5 null:

这个和上面的区别在于

- undefined表示没有赋值
- null是赋值了,但是内容为空

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="11:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    console.log(undefined + 1)
    console.log(null + 1)
```::::

::: tabbed-block
NaN 1
:::
::::::
::::::::
:::::::::

### 3.5.6 监测数据类型:

typeof函数,理论上这个函数可以不写括号,但是可能会被强迫症打死

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="12:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    console.log(typeof(undefined))
    console.log(typeof(1))
```::::

::: tabbed-block
undefined number
:::
::::::
::::::::
:::::::::

### 3.5.7 类型转换:

同样有两种类型转换

#### 3.5.7.1 隐式类型转换:

某些运算符执行的时候会自动转变类型,比如字符串加数字的时候会自动把数字变成字符串,+可以转换成数字型

#### 3.5.7.2 显示类型转换:

python的写法,js的类型 - Number() - 如果字符串内容理由非数字,会返回NaN -
NaN的类型是number - parseInt() - 只留整数 - parseFloat() - 可以保留小数

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="13:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
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
```::::

::: tabbed-block
num1 string 2.89 number 2.89 number 2 number 2.89 num2 string 2.89px
number NaN number 2 number 2.89
:::
::::::
::::::::
:::::::::

## 3.6 运算符

### 3.6.1 赋值运算符:

和python,java那些都差不多

- =
- +=
- -=
- /=
- [\\(\\dots\\)]{.arithmatex}

### 3.6.2 自增自减

- i++
- i\--
- \--i
- i\--

java里念了好几遍了,一个先输入后赋值,一个先赋值后输入

### 3.6.3 比较运算符:

- [\\(\>\\)]{.arithmatex}
- [\\(\<\\)]{.arithmatex}
- [\\(\>=\\)]{.arithmatex}
- [\\(\<=\\)]{.arithmatex}
- [\\(==\\)]{.arithmatex} 左右两边值是否相等
- [\\(===\\)]{.arithmatex} 左右两边是否和与类型都相等
- [\\(!==\\)]{.arithmatex} 左右两边是否不全等

会有隐式数据转换

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="14:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    console.log(2=="2")
    console.log(2==="2")
    console.log(2!="2")
    console.log(2!=="2")
```::::

::: tabbed-block
true false false true
:::
::::::
::::::::
:::::::::

### 3.6.4 逻辑运算符:

- &&
- \|\|
- !

和java一样

js是有和Python一样的or None语法的

:::::::::::: {.admonition .example}
Example

:::::: {.tabbed-set .tabbed-alternate tabs="15:1"}
::: tabbed-labels
代码
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

```    var x = null
    var a = 5
    console.log(a || 0)
    console.log(x || 0)
```
:::::: {.tabbed-set .tabbed-alternate tabs="16:1"}
::: tabbed-labels
输出
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

5 0
::::::::::::

一般是用来处理null的,并且python,java,js等语言

- a \|\| b, a为真则不判断b
- a && b, a为假则不判断b

## 3.7 语句:

### 3.7.1 条件:

#### 3.7.1.1 if:

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="17:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    '' == false // ''在逻辑判断里可以当做false
    0 == false
    1 == true // 除了0以外的所有数字都是true
```::::
:::::
:::::::
::::::::

因此:

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="18:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    if (0){
        console.log("我执行了")
    }
    else if(''){
        console.log("如执行")
    }
    else{
        console.log("我没执行")
    }
```::::

::: tabbed-block
我没执行
:::
::::::
::::::::
:::::::::

#### 3.7.1.2 三元运算符:

和java完全一样

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="19:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    var a = '' ? 1000 : 2345
    console.log(a)
```::::

::: tabbed-block
2345
:::
::::::
::::::::
:::::::::

#### 3.7.1.3 switch:

没记错的话好像也是java的,但是就算是java里也不常用,kotlin里是when

就是注意switch要求的是值和数据类型全部相等,不是只有值相等就行(===而不是==)

一般要搭配break使用,不然会每个条件都判断一次

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="20:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
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
```::::

::: tabbed-block
2
:::
::::::
::::::::
:::::::::

### 3.7.2 循环:

#### 3.7.2.1 while:

哪里的while都差不多

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="21:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    var a = 0
    while(++a <= 10){
        console.log(a);
    }
```::::

::: tabbed-block
1 2 3 4 5 6 7 8 9 10
:::
::::::
::::::::
:::::::::

#### 3.7.2.2 do while:

有点多此一举的样子,就算是java里也不常用

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="22:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    var a = 0
    do{
        console.log(++a)
    }
    while(a < 10)
```::::

::: tabbed-block
1 2 3 4 5 6 7 8 9 10
:::
::::::
::::::::
:::::::::

#### 3.7.2.3 for

和java的一致,然而最基本的这种几乎没用过

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="23:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    for(let a = 0; a <= 5; a++){
        console.log(a)
    }
```::::

::: tabbed-block
0 1 2 3 4 5
:::
::::::
::::::::
:::::::::

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="24:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    let a = 0
    for(;++a <=5;){
        console.log(a)
    }
```::::

::: tabbed-block
1 2 3 4 5
:::
::::::
::::::::
:::::::::

##### 3.7.2.3.1 for\...of:

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="25:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const a = ["yi","er","san"]
    for (let i of a){
      console.log(i)
    }
```::::

::: tabbed-block
yi er san
:::
::::::
::::::::
:::::::::

##### 3.7.2.3.2 for\...in:

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="26:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const a = ["yi","er","san"]
    for (let i in a){
      console.log(i)
    }
```::::

::: tabbed-block
1 2 3
:::
::::::
::::::::
:::::::::

#### 3.7.2.4 break continue

break是直接跳出整个循环

continue是进入下一次循环

和java类似,可以 锚点1:固定一个点之后直接continue锚点实现类似goto的效果

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="27:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    let a = 0
    while(++a < 10){
        if (a == 5){
            break
        }
        console.log(a);
    }
```::::

::: tabbed-block
1 2 3 4
:::
::::::
::::::::
:::::::::

:::::::::::: {.admonition .example}
Example

:::::: {.tabbed-set .tabbed-alternate tabs="28:1"}
::: tabbed-labels
代码
:::

:::: tabbed-content
::: tabbed-block
:::
::::
::::::

```    let a = 0
    while(++a < 10){
        if (a == 5){
            console.log("我跳出去了")
            continue
        }
        console.log(a);
    }
```
:::::: {.tabbed-set .tabbed-alternate tabs="29:1"}
::: tabbed-labels
输出
:::

:::: tabbed-content
::: tabbed-block
1 2 3 4 我跳出去了 6 7 8 9
:::
::::
::::::
::::::::::::

## 3.8 数组:

### 3.8.1 声明:

虽然js应该和java是一家人,但是js是弱类型语言,和python一样不用再new数组的时候声明变量类型,数组内可以存任何东西

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="30:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const a = [1,2,3,4]
    console.log(a)
    const b = new Array(1,2,3,4)
    console.log(b)
```::::

::: tabbed-block
\[ 1, 2, 3, 4 \] \[ 1, 2, 3, 4 \]
:::
::::::
::::::::
:::::::::

### 3.8.2 索引:

这个世界上难道存在索引值不从0开始的语言?

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="31:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    const a = [1,2,3,4]
    a[0]
```::::
:::::
:::::::

== \"输出\" 1
::::::::

### 3.8.3 遍历:

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="32:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    for (let i = 0; i < a.length; i++){
        console.log(a[i])
    }
```::::

::: tabbed-block
1 2 3 4
:::
::::::
::::::::
:::::::::

### 3.8.4 增:

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="33:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const a = [1,2,3,4,5,6,7,8,9,0]
    a.push(1008,6) // 在末尾加元素
    console.log(a)
    a.unshift(1008,6) // 在头部加元素
    console.log(a)
```::::

::: tabbed-block
\[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1008, 6 \] \[ 1008, 6, 1, 2, 3, 4, 5,
6, 7, 8, 9, 0, 1008, 6 \]
:::
::::::
::::::::
:::::::::

### 3.8.5 删:

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="34:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const a = [1,2,3,4,5,6,7,8,9,0]
    a.pop() // 和python一样,返回并删除最后一个值
    console.log(a)
    a.shift()
    console.log(a) // 返回并删除第一个值
    a.splice(2,2)
    console.log(a) // 返回并删除n到m的元素
```::::

::: tabbed-block
\[ 1, 2, 3, 4, 5, 6, 7, 8, 9 \] \[ 2, 3, 4, 5, 6, 7, 8, 9 \] \[ 2, 3, 6,
7, 8, 9 \]
:::
::::::
::::::::
:::::::::

## 3.9 函数:

用function定义, 参数和python一样不用声明类型

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="35:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
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
```::::

::: tabbed-block
1 \* 1 = 1 2 \* 1 = 2 2 \* 2 = 4 3 \* 1 = 3 3 \* 2 = 6 3 \* 3 = 9 4 \* 1
= 4 4 \* 2 = 8 4 \* 3 = 12 4 \* 4 = 16 5 \* 1 = 5 5 \* 2 = 10 5 \* 3 =
15 5 \* 4 = 20 5 \* 5 = 25 6 \* 1 = 6 6 \* 2 = 12 6 \* 3 = 18 6 \* 4 =
24 6 \* 5 = 30 6 \* 6 = 36 7 \* 1 = 7 7 \* 2 = 14 7 \* 3 = 21 7 \* 4 =
28 7 \* 5 = 35 7 \* 6 = 42 7 \* 7 = 49 8 \* 1 = 8 8 \* 2 = 16 8 \* 3 =
24 8 \* 4 = 32 8 \* 5 = 40 8 \* 6 = 48 8 \* 7 = 56 8 \* 8 = 64 9 \* 1 =
9 9 \* 2 = 18 9 \* 3 = 27 9 \* 4 = 36 9 \* 5 = 45 9 \* 6 = 54 9 \* 7 =
63 9 \* 8 = 72 9 \* 9 = 81
:::
::::::
::::::::
:::::::::

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="36:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
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
```::::

::: tabbed-block
1 \* 1 = 1 2 \* 1 = 2 2 \* 2 = 4 3 \* 1 = 3 3 \* 2 = 6 3 \* 3 = 9 4 \* 1
= 4 4 \* 2 = 8 4 \* 3 = 12 4 \* 4 = 16 5 \* 1 = 5 5 \* 2 = 10 5 \* 3 =
15 5 \* 4 = 20 5 \* 5 = 25
:::
::::::
::::::::
:::::::::

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="37:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    function double(a){
        return 2*a
    }
    let n = double(10)
    console.log(n)
```::::

::: tabbed-block
20
:::
::::::
::::::::
:::::::::

### 3.9.1 作用域:

别的和python,java那些一样,如果函数内部有局部变量名字和全局变量一样,用就近原则,作用域就是当前变量在的这个大括号

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="38:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
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
```::::

::: tabbed-block
5 30
:::
::::::
::::::::
:::::::::

### 3.9.2 匿名函数

(最前排提醒,这东西很重要)

#### 3.9.2.1 将函数赋值给一个变量:

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="39:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    var a = function(n){
        return n+1
    }
    console.log(a)
    console.log(a(9))
```::::

::: tabbed-block
\[Function: a\] 10
:::
::::::
::::::::
:::::::::

#### 3.9.2.2 立即执行函数

没有名字,不调用也会立即执行,不过相邻两个立即执行函数需要用分号隔开

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="40:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    (function(){console.log(5)})();
    (function(){console.log(6)})()
```::::

::: tabbed-block
5 6
:::
::::::
::::::::
:::::::::

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="41:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    (function(n){console.log(n)})(90);
    (function(){console.log(6)})()
```::::

::: tabbed-block
90 6
:::
::::::
::::::::
:::::::::

#### 3.9.2.3 其他:

(写过了,但懒得删了) 不知道放哪里了,先写这里吧

js是有和Python一样的or None语法的

一般是用来处理null的,并且python,java,js等语言

- a \|\| b, a为真则不判断b
- a && b, a为假则不判断b

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="42:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    var x = null
    var a = 5
    console.log(a || 0)
    console.log(x || 0)
```::::

::: tabbed-block
5 0
:::
::::::
::::::::
:::::::::

## 3.10 对象:

是一种无需的数据类型,类似字典,json

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="43:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const person = {
        name: "someone",
        gender: "armed walmart helicopter",
        age: "unknown"
    }
    console.log(person.name)
    console.log(typeof(person))
```::::

::: tabbed-block
someone object
:::
::::::
::::::::
:::::::::

### 3.10.1 一些基本操作

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="44:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const person = {
        name: "someone",
        gender: "armed walmart helicopter",
        age: "unknown"
    }
    // 查属性
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
```::::

::: tabbed-block
armed walmart shopping bag armed walmart shopping bag { name:
\'someone\', gender: \'armed walmart shopping bag\', age: \'unknown\' }
{ name: \'someone\', gender: \'armed walmart shopping bag\', age:
\'unknown\', job: \'shopping bag\' } { name: \'someone\', gender:
\'armed walmart shopping bag\', age: \'unknown\' }
:::
::::::
::::::::
:::::::::

### 3.10.2 对象内可以使用函数:

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="45:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    const person = {
        name: "someone",
        gender: "armed walmart helicopter",
        age: "unknown",
        getage: function(n){
            console.log(n)
        }
    }
    person.getage(20)
```::::

::: tabbed-block
20
:::
::::::
::::::::
:::::::::

### 3.10.3 遍历对象:

不过注意,如果是遍历数组返回的是下标,如果是遍历对象返回的是属性名称,
之后会有解构,会跟方便且复杂一些

这种情况下循环里只能写obj\[k\]的形式

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="46:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    for (i in person){
        console.log(i,person[i])
    }
```::::

::: tabbed-block
name someone gender armed walmart helicopter age unknown getage
\[Function: getage\]
:::
::::::
::::::::
:::::::::

::: {.admonition .example}
案例

查看[examples/js_involved/html/object2table.html](https://github.com/everythingfades/html/blob/main/examples/js_involved/html/object2table.html)
:::

### 3.10.4 内置对象

例如document,console,Math等相当于内置库

#### 3.10.4.1 Math:

- random:0-1的随机数
- ceil
- floor
- max
- min
- pow
- abs
- \...

## 3.11 正则表达式

### 3.11.1 语法:

#### 3.11.1.1 新建正则表达式

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="47:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    const 变量名 = /表达式/
```::::
:::::
:::::::
::::::::

#### 3.11.1.2 test()

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="48:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    正则表达式.test(被检测的字符串)
```::::
:::::
:::::::
::::::::

#### 3.11.1.3 exec()

:::::::: {.admonition .example}
Example

::::::: {.tabbed-set .tabbed-alternate tabs="49:1"}
::: tabbed-labels
代码
:::

::::: tabbed-content
:::: tabbed-block
```    正则表达式.exec(字符串)
```::::
:::::
:::::::
::::::::

### 3.11.2 字符:

#### 3.11.2.1 边界符:

- \^ 表示以什么开始
- [\\(\\\$\\)]{.arithmatex}表示以什么结束

#### 3.11.2.2 量词:

::: arithmatex
\\\[\\begin{array}{c} \* & \\text{重复零次或者更多次}\\\\ + &
\\text{重复一次或更多次}\\\\ ? & \\text{重复0次或者一次}\\\\ \\{n\\} &
\\text{重复n次}\\\\ \\{n,\\} & \\text{重复n次或者更多次}\\\\ \\{n,m\\} &
\\text{重复n到m次} \\end{array}\\\]
:::

#### 3.11.2.3 元字符:

- \[abc\]匹配一个字符是否是abc
- \[a-z\]可以用连字符表示一个范围
- \[a-z\]所有小写字母
- \[a-zA-Z\]所有字母
- \^写到中括号里表示取反

预定类:

::: arithmatex
\\\[\\begin{array}{c} \\text{\\d} &
\\text{匹配0-9之间的任意数字}\[0-9\]\\\\ \\text{\\D} &
\\text{匹配所有0-9以外的数字}\[\^0-9\]\\\\ \\text{\\w} &
\\text{匹配任意的字符,数字和下划线}\[A-Za-z0-9\_\]\\\\ \\text{\\W} &
\\text{除字符数字,下划线外所有的字符}\[\^{} A-Za-z0-9\]\\\\ \\text{\\s}
&
\\text{匹配空格(包括换行符,制表符,空格符等)}\[\\text{\\t\\n\\v\\f}\]\\\\
\\text{\\S} & \\text{匹配非空格的字符}\[\^{} \\text{\\t\\r\\n\\v\\f}\]
\\end{array}\\\]
:::

::::::::: {.admonition .example}
Example

:::::::: {.tabbed-set .tabbed-alternate tabs="50:2"}
::: tabbed-labels
代码输出
:::

:::::: tabbed-content
:::: tabbed-block
```    var str = "abc"
    var pattern = /[A-Z]/
    pattern.test("1000A0000")
```::::

::: tabbed-block
true
:::
::::::
::::::::
:::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
