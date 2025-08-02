
(不清楚为什么这个会出错,加上\--legacy-peer-deps或者改用yarn, yarn create
react-app react-basic)

创建之后会有App.js和index.js,就相当于vue的App.Vue和main.js

## JSX

javascript和XML

JSX用babel编译成JS

### 简单的JSX

```    function App() {
      return (
        <div className="App">
          this is app
          {/* 使用引号传递字符串 */}
          {'This is message'}
          {/* 识别js变量 */}
          {count}
          {/* 函数调用 */}
          {getName()}
          {/* 方法调用 */}
          {new Date().getDate()}
          {/* 使用js对象 */}
          <div style={{color:'red'}}>this is something</div>
        </div>
      );
    }
```
其实和VUE差不多

### 列表等循环:

```      <ul>
        {list.map(it=><li key={item.id}>{it.name}</li>)}
      </ul>
```
差不多和v-for一个道理,需要key以提升性能

### 条件渲染

类似v-if

可以写

```    {flag && <span>aaa</span>}
```
或者

```    {loading ? <span>loading...</span> : <span>this is span</span>}
```
也可以写进函数里,然后返回一个组件

## 事件绑定

直接加入 on + 事件名称的tag就行

```    {<button onClick={() => {count = 12;console.log(count)}}></button>}
```
## react组件

组件其实就是一个首字母大写的函数,然后只需要返回一个html组件就行

比如:

```    const Button = () => {
      return <div><button onClick={console.log("clicked")}>button component</button></div>
    }
```
然后就和Vue一样

## useState

相当于一个vue3的ref

```    const [count,setCount] = useState(0)
```
- 这里count是变量名称
- setCount是count的setter
- useState里的参数表示count的初始值

但是useState必须在组件内部定义

在react中,状态被认为是只读的,所以如果之间改,就算前面变成let改值之后也不会更新

可以借助js的解构技巧

```    const [form, setForm] = useState({
      name: 'aaa'
    })

    const handleChangeName = () => {
      setForm({
        ...form,
        name: "bbb" // 这里会自动替换重复的属性值
      })
    }
```
## css类

没什么好说的,就是因为js占用了关键字class,所以在react组件里要用className去替换class

```    <div className="foo"></div>
```
## 双向绑定:

v-model = v-bind:value + v-on:change

在react里是value和onChange

## 获取DOM

需要用useRef钩子函数

和vue3的ref很像

```    // 先定义一个ref对象

    const inputRef = useRef(null)
    // 在对应的DOM里加上ref属性
    <input type="text" ref={inputRef}/>

    // DOM可用的时候可以用inputRef.current获取DOM对象

    inputRef.current
```
## 组件通信,props和emit

和Vue也差不多,

```    <Son name={name}/>

    // 把父组件的name传递给子组件作为子组件的name

    // 同时在定义子组件的时候

    function Son(props) {
      // props 是一个对象
    }
```
父组件可以传递任意类型的数据,和Vue一样,子组件无法直接修改父组件的数据

### props children

子组件中嵌套的标签会自动包含在父组件props的children属性里

```    <Son><p>grandson</p></Son>
```
那么Son接收到的props里会自动出现一个children属性,值为子组件包含的children
DOM,不会直接渲染

### 子传父

没有emit函数,但是可以直接把一个函数传进去,子组件直接调用

可以使用状态提升,就是让兄弟组件有共同的父组件,这样可以让相同辈分的子组件使用同一套API

## Context

类似Vue的store,但是是局部的store,不想pinia定义的是全局的store

- 使用createContext方法创建一个上下文
- 在顶层组件(App)中通过Ctx.Provider提供数据
- 在底层组件使用useContext钩子函数获取数据

context只有一个域可以传递数据,要传递多个数据的时候可以打包成一个对象

# useEffect

用于创建由渲染引起的操作,比如发送AJAX,更改DOM等

```    useEffect(()=>{ }, [])
```
第一个参数表示副作用函数,是需要执行的操作,第二个参数是依赖项,不同依赖项会影响第一个参数执行的时机,如果是空数组则只会执行一次

不过要注意useEffect不允许传入异步函数,如果需要异步需要在内部定义一个异步函数,然后立即执行

  依赖项       执行时机
  ------------ ---------------------------------
  没有依赖项   组件初始化+组件更新
  空数组依赖   只在初始化的时候渲染一次
  特定依赖项   组件初始化+Vue的watch所有依赖项

## 清除副作用

比如在UseEffect里面开了一个倒计时,如果不管他会一直计时下去

就是在useEffect里再定义一个return()

比如

```    useEffect(() => {
      return () =>{
        //在组建卸载的时候清除副作用
      }
    }, [])
```
## 自定义hook

以use开头的函数,和普通函数没有区别,以use开头只是规范

```    function useToggle () {
      const [value, setValue] = useState(true)
      const toggle = () => setValue(!value)

      // 把所有需要的函数和值都返回
      return {
        value
        toggle
      }
    }

    // 在组件里就可以解构出来使用
```
## 钩子函数使用规则:

- 只能在组建或者其他自定义库里调用
- 只能在组件的顶层调用,不能嵌套在if,for,其他函数中

# redux:

类似于vuex或者pinia,但是可以独立于框架运行

- 定义一个reducer函数(根据当前想要的修改返回一个新的状态)

- 使用createStore方法传入reducer函数生成一个store实例对象

- 使用store实例的subscribe方法订阅数据的变化

- 使用store实例的dispatch方法提交action对象触发数据变化

- 使用store实例的getState方法获取最新的状态数据更新到视图中

- state: 一个对象,存放管理的数据

- action: 一个对象,描述操作

- reducer: 一个函数,根据action的描述生成一个新的state

\[examples/react/react-redux/redux.html\]

## 在react里使用

需要安装Redux toolkit以及react-redux

第一个用于简化redux逻辑,第二个用于在react里支持redux

例:

```    import {createSlice} from "@reduxjs/toolkit"

    const counterStore = createSlice({
      name: 'counter',

      // 初始状态
      initialState: {
        count: 0
      },
      reducers: {
        increment (state) {
          state.count++
        },
        decrement (state) {
          state.count--
        }
      }
    })

    // 解构出来actionCreater函数
    const {increment, decrement} = counterStore.actions

    // 获取reducer
    const counterReducer = counterStore.reducer

    // 以按需导出的方式导出actionCreator
    export {increment, decrement}

    // 以默认导出的方式导出reducer
    export default counterReducer
```
```    import { configureStore } from "@reduxjs/toolkit";

    import counterReducer from "./modules/counterStore";

    export default configureStore({
      reducer: {
        counter: counterReducer
      }
    })
```
然后和pinia一样需要在改在的时候配置store

```    import React from 'react';
    import ReactDOM from 'react-dom/client';
    // import './index.css';
    import App from './App';
    // import reportWebVitals from './reportWebVitals';

    import store from './store';
    import {Provider} from 'react-redux'

    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(
      <React.StrictMode>
        <Provider store="store">
          <App />
        </Provider>
      </React.StrictMode>
    );

    // If you want to start measuring performance in your app, pass a function
    // to log results (for example: reportWebVitals(console.log))
    // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
    // reportWebVitals();
```
需要使用useSelector把在store中的数据映射到组件中

和VUE的useState(\[\...\]) 差不多

```    const {count} = useSelector(state => state.counter)
```
在组件中使用的话

```    // import logo from './logo.svg';
    // import './App.css';

    import { useSelector } from "react-redux";

    function App() {
      const {count} = useSelector(state => state.counter)
      return (
        <div className="App">
          {count}
        </div>
      );
    }

    export default App;
```
在react组件里修改store中的数据有且仅有一种方法: useDispatch,
作用是生成提交action对象的dispatch函数

```    // import logo from './logo.svg';
    // import './App.css';

    import { useSelector, useDispatch } from "react-redux";
    import { increment, decrement } from "./store/modules/counterStore";

    function App() {
      const {count} = useSelector(state => state.counter)
      const dispatch = useDispatch()
      return (
        <div className="App">
          <button id="inc" onClick={()=>dispatch(increment())}>+</button>
          <span>{count}</span>
          <button id="dec" onClick={()=>dispatch(decrement())}>-</button>
        </div>
      );
    }

    export default App;
```
### 提交action(传参)

```    const counterStore = createSlice({
      name: 'counter',

      // 初始状态
      initialState: {
        count: 0
      },
      reducers: {
        increment (state) {
          state.count++
        },
        decrement (state) {
          state.count--
        },
        addToNum(state, action) {
          state.count = action.payload
        }
      }
    })
```
```    // import logo from './logo.svg';
    // import './App.css';

    import { useSelector, useDispatch } from "react-redux";
    import { increment, decrement, addToNum} from "./store/modules/counterStore";

    function App() {
      const {count} = useSelector(state => state.counter)
      const dispatch = useDispatch()
      return (
        <div className="App">
          <button id="inc" onClick={()=>dispatch(increment())}>+</button>
          <span>{count}</span>
          <button id="dec" onClick={()=>dispatch(decrement())}>-</button>
          <button id="inc10" onClick={()=>dispatch(addToNum(10))}>+10</button>
          <button id="inc20" onClick={()=>dispatch(addToNum(20))}>+10</button>
        </div>
      );
    }

    export default App;
```
### 异步:

- 创建store的写法不变,配置好同步修改状态的方法
- 单独封装一个函数,在函数内部return一个新函数,在新函数中
- - 封装异步请求获取数据
- - 调用同步actionCreater传入一步数据生成一个action对象,用dispatch提交
- 组件中dispatch的写法保持不变

### devtools

和vue那个一样,略过

# router

引入包: `npm i react-router-dom`

然后就差不多和VUE一样了

```    import React from 'react';
    import ReactDOM from 'react-dom/client';
    import './index.css';
    import App from './App';
    import reportWebVitals from './reportWebVitals';

    import {
      createBrowserRouter,
      RouterProvider,
    } from "react-router-dom";

    // 创建router实例并配置路由对应关系

    const router = createBrowserRouter([
      {
        path: '/login',
        element: <div>我是登录页</div>
      },
      {
        path: '/article',
        element: <div>我是文章页</div>
      }
    ])

    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(
      <React.StrictMode>
        <RouterProvider router={router}>

        </RouterProvider>
      </React.StrictMode>
    );

    // If you want to start measuring performance in your app, pass a function
    // to log results (for example: reportWebVitals(console.log))
    // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
    // reportWebVitals();
```
react和vue一样,路由方面的规范一般是新建一个文件夹专门放router,然后新建一个文件夹专门放所有页面

## 跳转:

### Link标签

```    import { Link } from 'react-router-dom'

    const Login = () => {
      return (
        <div>我是登录页
          <Link to="/article">链接</Link>
        </div>
      )
    }

    export default Login
```
### useNavigate

在组件内部用useNaivgate获取一个navigate对象,然后之间navigate(路径)

但感觉,不如this.\$router.push,可惜react没有this

### useSearchParams

比如说你传传入几个参数,那么你的url会和get请求url差不多,?后面跟着一堆参数

可以用useSearchParams()把所有参数转成一个Json对象,比较没意思,毕竟可想而知底层就是处理一下字符串

但是要用get获取特定参数

比如url是

```    const params = useSearchParams()
    params.get("id")
```
### useParams

用来获取路径参数

比如在router里有

\"/article/:id\"

就可以用

```    const [params] = useParams()
    const id = params.id
```
### 嵌套路由

可以用children配置路由嵌套关系

比如

```    {
      path: "/",
      element: <Layout />,
      children: [
        {
          path: "board",
          element: <Board />
        },
        {
          path: "about",
          element: <About />
        }
      ]
    }
```
然后二级路由需要用\< OutLet/\>在父组件渲染

```    import { Link, Outlet } from "react-router-dom"

    export const Layout = () => {
      return (
        <div>
          一级路由
          <Link to="/board">面板</Link>
          <Link to="/about">关于</Link>
          <Outlet></Outlet>
        </div>
      )
    }
```
#### 默认路由

例,原本是localhost:3000,这里有一个二级路由,希望在访问localhost:3000的时候直接显示

在路由配置项中对应的位置去掉path变成index

```    ...
    children: [
      {
        index: true,
        element: <Board/>
      },
      ...
    ]
    ...
```
### 404:

和vue一样,用通配符\*放到最后匹配所有找不到的路径

### history和hash:

和vue3一样,如果不想要那个#就history,但是history需要有后端(真的会有纯前端的网页吗)

# useReducer:

用来管理相对复杂的值

const \[state, dispatch\] = useReducer(reducer,0)

然后 dispatch({type:\"DEC\"})和之前redux的reducer一个意思

# useMemo

和useEffect+useState一样,不同的是useMemo会缓存数据所以重新渲染的次数比useEffect少

就是空间换时间,一般推荐在复杂运算的时候使用

# React.Memo:

React组件默认如果父组件重新渲染,子组件也会重新渲染

如果用memo,那么只有在props发生变化的时候才会重新渲染

```    const MemoComponent = memo(function SomeComponent(props) {
      //...
    })
```
就使用memo把子组件包住, 只考虑props,context变的话这个不管

## memo和props

对于简单类型,会直接比较值,不然会比较内存地址,除非引用改变否则不重新渲染

# useCallback

和useMemo差不多,但是作用于函数

比如p标签的空白

```    function component() {
      const someFunc = useCallback((value) => console.log(value),[])
      ...
      //然后可以直接把someFunc传入子组件
    }
```
# forwardRef:

如果不用这个的话父组件中获取不到ref的相关信息,暴露子组件的DOM

```    function App () {
      const sonRef = useRef(null) // 定义ref引用
      return (
        <div>
          <Son ref={sonRef}>
        </div>
      )
    }

    const Son = forwardRef((props, ref) => {
      return <div>Son</div>
    })
```
# useImperativeHandle

暴露子组件的方法

```    const Input = forwardRef((props, ref) => {
      const inputRef = useRef(null)
      const focusHandler = () => {
        inputRef.current.focus()
      }
      useImperativeHandle(ref, () => {
        return {
          focusHandler
        }
      })
      return <input type="text" ref={inputRef}>
    })

    // 然后就可以在父组件里直接sonRef.current.focusHandler()
```
# 类组件:

用类来组织组件,但现在的react不推荐这么做,主要是人家给了一堆API

就和vue很像了,vue里每个组件本质上是一个Json对象,这个里每个组件是一个类

vue的data -\> react的state

方法调用就直接写到类里面

例如

```    class A extends Component {
      state = {
        count: 0,
        ...
      }

      setCount = () => {
        ...
      }

      render () {
        return ...
      }
    }
```
UI模版在render()里

## 生命周期

只有类组件有生命周期,其他组件可以用useEffect

- componentDidMount -\> vue的onMounted
- componentWillUnmount 卸载组件时触发,清除副作用

## 通信

思想上完全一致

子组件在this.props中获取,父组件通过this.state传入

# zustand

是redux的平替

用法和pinia差不多

```    import { Button, Avatar, Badge, Space, Image } from 'antd'
    import { create } from 'zustand'

    type Store = {
      count: number
      inc: () => void
    }

    const useStore = create<Store>()((set) => ({
      // 这里所有修改数据的操作都必须调用set,就和之前的useState一个道理,不能直接修改,只能替换
      count: 1,
      inc: () => set((state) => ({ count: state.count + 1 })),
    }))

    function Counter() {
      const { count, inc } = useStore()

      return (
        <Space size="large">
          <Badge count={count}>
            <Image src="https://docs.pmnd.rs/zustand.ico" style={{ width: '60px', height: '60px' }} preview={false} />
          </Badge>
          <Button type="primary" onClick={inc}>one up</Button>
        </Space>
      )
    }

    export default Counter
```
## 异步:

就直接写异步就行

```    const useStore = create((set) => {
      return {
        channelList: [],
        fetchChannelList: async () => {
          const res = await fetch (URL)
          const jsonData = await res.json()
          set({
            ...
          })
        }
      }
    })
```
## 切片:

```    import { create } from 'zustand'

    const createCounterStore = (set) => {
      return {
        return {
          count : 0,
          setCount: () => {
            set(state => ({count: state.count + 1}))
          }
        }
      }
    }

    const createChannelStore = (set) => {
      return {
        channelList: [],
        fetchChannelList: async () => {
          const res = await fetch(URL)
          const jsonData = await res.json()
          set({ channelList: jsonData.data.channels })
        }
      }
    }

    //组合

    const useStore = create((...a) => {
      ...createCounterStore(...a),
      ...createChannelStore(...a)
    })
```
使用的时候直接

```    const {count, inc, channelList, fetchChannelList } = useStore()
```
就行,会直接解构出来

# React + TypeScript

用vite创建ts+react

```    npm create vite my-vue-app --template react-ts
```
## useState:

react会通过自动推导机制判断变量类型

## 传递泛型参数:

例:

```    type User = {
      name: string
      age: number
    }

    const [user, setUser] = useState<User>({
      // ...
    })

    // 或者

    const [user, setUser] = useState<User>(
      () => { return {
        name: ...,
        age: ...
      }
    })
```
这样就可以限制参数类型

### 初始值为NULL

由于在ts中,null不属于任何类而是一个源石数据类型

所以

```    type User = {
      name: string,
      age: number
    }

    const [user, setUser] = useState<User | null> (null)
```
## props

为了给type加上类型,使用type对象或者interface接口做注解

```    type A = {
      //...
    }

    function Button(props: A) {
      ...
    }
```
## children

内置了一个ReactNode类型做注解

比如

```    type Props = {
      className: string
      children: React.ReactNode
    }

    function Button(props: Props) {
      const {className, children } = props
      return <button className={classname}{children}></button>
    }
```
## props包含函数

比如

```    type Props = {
      someFunc: (someParam: string) => void
    }
```
如果绑定的是内联函数则可以直接推断出类型,

```    <A onClick={() => console.log("Ah")}></A>
```
但如果不是内联函数,例如用const生命一个箭头函数,那么需要额外声明变量类型

## ref

可以把需要的元素类型传递给useRef,会自动推断出current的属性

## 封装axios

```    import axios from 'axios'

    const httpInstance = axios.create({
      baseURL: 'randomURL',
      timeout: 500
    })

    httpInstance.interceptors.request.use (
      (config) => {
        return config
      },
      (error) => {
        return Promise.reject(error)
      }
    )

    httpInstance.interceptors.response.use (
      (response) => {
        return config
      },
      (error) => {
        return Promise.reject(error)
      }
    )

    export { httpInstance }


    // 其他需要用axios的地方

    import {httpInstance as http}
```
### axios + ts

```    import {httpInstance as http}

    type ResType<T> = {
      message: string
      data: T
    }

    export function somfunc() {
      return http.request<ResType<someType>>({
        url: "randomURL"
      })
    }
```::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
