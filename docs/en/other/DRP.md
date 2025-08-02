[使用 Next JS 构建和部署全栈视频会议应用程序_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1ZD421L78P/?spm_id_from=333.337.search-card.all.click&vd_source=f7139216eae1666b699e977cfab6c368)

先新建项目

```bash
npx create-next-app@latest ./ --typescript --tailwind -- eslint
# if outside the folder
npx create-next-app@latest <path-or-name> --typescript --tailwind -- eslint

```

根据shadcn的文档init shadcn,这样可以用他的组件库

```bash
npx shadcn@latest init
# if pnpm
pnpm dlx shadcn@latest init
```

然后根据shadcn的文档加入组件

```bash
npx shadcn-ui@latest add button
```

他会在components文件夹下穿件对应的tsx文件

在安装Es7+React vscode 插件之后,rafce可以生成一个简单的组件

# socketio:
## 服务器端:

需要两个文件

```typescript
// server.ts
import express from 'express';
import http from 'http';
import { Server } from 'socket.io';
  
const app = express();
const server = http.createServer(app);
const io = new Server(server);

// Handle new connections
io.on('connection', (socket) => {
  console.log(`User connected: ${socket.id}`);  
  // Listen for chat messages
  socket.on('chat-message', (msg) => {
    console.log(`Message from ${socket.id}: ${msg}`);
    // Broadcast to all other clients
    socket.broadcast.emit('message', {
      sender: socket.id,
      text: msg
    });
  });
  
  // Handle disconnections
  socket.on('disconnect', () => {
    console.log(`User disconnected: ${socket.id}`);
  });
});

server.listen(3000, () => {
  console.log('Socket.IO server running on port 3000');
});

```

以及

```typescript
// client.ts
import { createServer } from "node:http";
import next from "next";
import { Server } from "socket.io";
  
const dev = process.env.NODE_ENV !== "production";
const hostname = "localhost";
const port = 3000;
// when using middleware `hostname` and `port` must be provided below
const app = next({ dev, hostname, port });
const handler = app.getRequestHandler();

app.prepare().then(() => {

  const httpServer = createServer(handler);
  const io = new Server(httpServer);
  
  io.on("connection", (socket) => {
    // ...
  });

  httpServer
    .once("error", (err) => {
      console.error(err);
      process.exit(1);
    })
    .listen(port, () => {
      console.log(`> Ready on http://${hostname}:${port}`);
    });
});
```

在package.json里,需要做如下调整

```json
{
  "scripts": {
-   "dev": "next dev",
+   "dev": "node server.js",
    "build": "next build",
-   "start": "next start",
+   "start": "NODE_ENV=production node server.js",
    "lint": "next lint"
  }
}
```

## 客户端:

文件结构:

```
├── src  
│ ├── app  
│ │ └── page.js  
│ └── socket.js  
└── package.json
```

``` javascript
//src/socket.js
"use client";

import { io } from "socket.io-client";

export const socket = io();
```

略微复杂一点:

```typescript
// lib/socket.ts
import { io, Socket } from "socket.io-client";

// 1. Define event types for TypeScript
interface ServerToClientEvents {
  "game-state": (state: GameState) => void;
  "player-moved": (player: PlayerPosition) => void;
  "player-joined": (playerId: string) => void;
}

interface ClientToServerEvents {
  "player-move": (movement: MovementData) => void;
  "chat-message": (message: string) => void;
}

// 2. Create typed socket instance
const socket: Socket<ServerToClientEvents, ClientToServerEvents> = io(
  process.env.NEXT_PUBLIC_SOCKET_URL || "http://localhost:3001",
  {
    // Connection options
    autoConnect: false,
    reconnection: true,
    reconnectionAttempts: 5,
    withCredentials: true,
    auth: {
      token: typeof window !== "undefined" 
        ? localStorage.getItem("authToken")
        : null
    }
  }
);

// 这里就只是链接以及断开的时候控制台输出一个消息
// 3. Connection lifecycle handlers
socket.on("connect", () => {
  console.log("Connected to server:", socket.id);
});

socket.on("disconnect", (reason) => {
  console.log("Disconnected:", reason);
});

// 4. Export reusable socket instance
export default socket;
```

在page.js里可以定义:

```javascript
"use client";

import { useEffect, useState } from "react";
import { socket } from "../socket";

export default function Home() {
  const [isConnected, setIsConnected] = useState(false);
  // 这里也可以
  // const [isConnected, setIsConnected] = useState(socket.connected);
  // 然后忽略掉下面的useEffect
  // 但是会有错误: Uncaught Error: Text content does not match server-rendered HTML.
  const [transport, setTransport] = useState("N/A");
  // transport 可以是:
  // HTTP long-polling (`"polling"`)
  // [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) (`"websocket"`)
  // [WebTransport](https://developer.mozilla.org/en-US/docs/Web/API/WebTransport_API) (`"webtransport"`)

  useEffect(() => {
    if (socket.connected) {
      onConnect();
    }

    function onConnect() {
      setIsConnected(true);
      setTransport(socket.io.engine.transport.name);

      socket.io.engine.on("upgrade", (transport) => {
        setTransport(transport.name);
      });
    }

    function onDisconnect() {
      setIsConnected(false);
      setTransport("N/A");
    }

    socket.on("connect", onConnect);
    socket.on("disconnect", onDisconnect);

    return () => {
      socket.off("connect", onConnect);
      socket.off("disconnect", onDisconnect);
    };
  }, []);

  return (
    <div>
      <p>Status: { isConnected ? "connected" : "disconnected" }</p>
      <p>Transport: { transport }</p>
    </div>
  );
}
```

客户端向服务器端发送消息:

```javascript
socket.emit("hello", "world");
```

客户端接收服务器端的消息

```javascript
socket.on("hello", (value) => {
  // ...
});
```

# clerk认证

## 初始化
创建项目就不说了, 先装包: `pnpm add @clerk/nextjs`

middleware:

在根目录(/src),创建middleware

```typescript
// middleware.ts
import { clerkMiddleware } from '@clerk/nextjs/server'

export default clerkMiddleware()

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}
```

引入ClerkProvider, 例:

```typescript
import type { Metadata } from 'next'
import {
  ClerkProvider,
  SignInButton,
  SignUpButton,
  SignedIn,
  SignedOut,
  UserButton,
} from '@clerk/nextjs'
import { Geist, Geist_Mono } from 'next/font/google'
import './globals.css'

const geistSans = Geist({
  variable: '--font-geist-sans',
  subsets: ['latin'],
})

const geistMono = Geist_Mono({
  variable: '--font-geist-mono',
  subsets: ['latin'],
})

export const metadata: Metadata = {
  title: 'Clerk Next.js Quickstart',
  description: 'Generated by create next app',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
          <header className="flex justify-end items-center p-4 gap-4 h-16">
            <SignedOut>
              <SignInButton />
              <SignUpButton />
            </SignedOut>
            <SignedIn>
              <UserButton />
            </SignedIn>
          </header>
          {children}
        </body>
      </html>
    </ClerkProvider>
  )
}
```
似乎clerk提供一些内置组件

然后pnpm dev就行了

## 个性化的登录和注册页面:

首先先创建一个登录页面:
```typescript
// app/sign-in/[[...sign-in]]/page.tsx
import { SignIn } from '@clerk/nextjs'

export default function Page() {
  return <SignIn />
}
```

如果要保护登录页面,则:

```typescript
// middleware.ts

import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isPublicRoute = createRouteMatcher(['/sign-in(.*)'])

export default clerkMiddleware(async (auth, req) => {
  if (!isPublicRoute(req)) {
    await auth.protect()
  }
})

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}
```

然后更新环境变量

```typescript
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_IN_FALLBACK_REDIRECT_URL=/
NEXT_PUBLIC_CLERK_SIGN_UP_FALLBACK_REDIRECT_URL=/
```

## 获取用户和会议信息

### 服务器端:
用clerk的钩子,auth()和currentUser()

api:

```typescript
// pages/api/auth.ts
import { getAuth, clerkClient } from '@clerk/nextjs/server'
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  // Use `getAuth()` to get the user's ID
  const { userId } = getAuth(req)

  // Protect the route by checking if the user is signed in
  if (!userId) {
    return res.status(401).json({ error: 'Unauthorized' })
  }

  // Initialize the Backend SDK
  const client = await clerkClient()

  // Get the user's full `Backend User` object
  const user = await client.users.getUser(userId)

  return res.status(200).json({ user })
}
```

或者可以用getProps的方式

```typescript
import { getAuth, clerkClient } from '@clerk/nextjs/server'
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  // Use `getAuth()` to get the user's ID
  const { userId } = getAuth(req)

  // Protect the route by checking if the user is signed in
  if (!userId) {
    return res.status(401).json({ error: 'Unauthorized' })
  }

  // Initialize the Backend SDK
  const client = await clerkClient()

  // Get the user's full `Backend User` object
  const user = await client.users.getUser(userId)

  return res.status(200).json({ user })
}
```

### 客户端

可以使用useAuth()和useUser()钩子

```typescript
export default function Example() {
	// 解构出函数
  const { isLoaded, isSignedIn, userId, sessionId, getToken } = useAuth()

  const fetchExternalData = async () => {
    // Use `getToken()` to get the current user's session token
    const token = await getToken()

    // Use `token` to fetch data from an external API
    const response = await fetch('https://api.example.com/data', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })

    return response.json()
  }

  // Use `isLoaded` to check if Clerk is loaded
  if (!isLoaded) {
    return <div>Loading...</div>
  }

  // Use `isSignedIn` to check if the user is signed in
  if (!isSignedIn) {
    // You could also add a redirect to the sign-in page here
    return <div>Sign in to view this page</div>
  }

  return (
    <div>
      Hello, {userId}! Your current active session is {sessionId}.
    </div>
  )
}
```

```typescript
export default function Example() {
  const { isSignedIn, user, isLoaded } = useUser()

  if (!isLoaded) {
    return <div>Loading...</div>
  }

  if (!isSignedIn) {
    return <div>Sign in to view this page</div>
  }

  return <div>Hello {user.firstName}!</div>
}
```

- useUser需要在use client下使用,useAuth则是server
- useUser需要在ClerkProvider内使用,可以在layout中配置
- 需要配置clerk的图片才能正常显示
```javascript
import type { NextConfig } from "next";
  
const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'img.clerk.com',
      },
      // For latest Clerk versions using CDN:
      {
        protocol: 'https',
        hostname: '*.clerkusercontent.com',
      }
    ],
  },
};

export default nextConfig;
```

## 增加验证:
先在clerk网页配置metadata:

```json
{ "metadata": "{{user.public_metadata}}" }
```

然后在types里增加

```typescript
export {}

declare global {
  interface CustomJwtSessionClaims {
    metadata: {
      onboardingComplete?: boolean
    }
  }
}
```

之后可以在middleware里增加验证

```typescript
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'
import { NextRequest, NextResponse } from 'next/server'

const isOnboardingRoute = createRouteMatcher(['/onboarding'])
const isPublicRoute = createRouteMatcher(['/public-route-example'])

export default clerkMiddleware(async (auth, req: NextRequest) => {
  const { userId, sessionClaims, redirectToSignIn } = await auth()

  // For users visiting /onboarding, don't try to redirect
  if (userId && isOnboardingRoute(req)) {
    return NextResponse.next()
  }

  // If the user isn't signed in and the route is private, redirect to sign-in
  if (!userId && !isPublicRoute(req)) return redirectToSignIn({ returnBackUrl: req.url })

  // Catch users who do not have `onboardingComplete: true` in their publicMetadata
  // Redirect them to the /onboarding route to complete onboarding
  if (userId && !sessionClaims?.metadata?.onboardingComplete) {
    const onboardingUrl = new URL('/onboarding', req.url)
    return NextResponse.redirect(onboardingUrl)
  }

  // If the user is logged in and the route is protected, let them view.
  if (userId && !isPublicRoute(req)) return NextResponse.next()
})

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}
```

这个middleware配置的是如果没有登录就引导到onboarding

/onboarding组件

```typescript
'use client'
  
import * as React from 'react'
import { useUser } from '@clerk/nextjs'
import { useRouter } from 'next/navigation'
import { completeOnboarding } from '@/actions/onboarding'
  
export default function OnboardingComponent() {
  const [error, setError] = React.useState('')
  const { user } = useUser()
  const router = useRouter()
  
  const handleSubmit = async (formData: FormData) => {
    const res = await completeOnboarding(formData)
    if (res?.message) {
      // Reloads the user's data from the Clerk API
      await user?.reload()
      router.push('/')
    }
    if (res?.error) {
      setError(res?.error)
    }
  }
  return (
    <div>
      <h1>Welcome</h1>
      <form action={handleSubmit}>
        <div>
          <label>Application Name</label>
          <p>Enter the name of your application.</p>
          <input type="text" name="applicationName" required />
        </div>
  
        <div>
          <label>Application Type</label>
          <p>Describe the type of your application.</p>
          <input type="text" name="applicationType" required />
        </div>
        {error && <p className="text-red-600">Error: {error}</p>}
        <button type="submit">Submit</button>
      </form>
    </div>
  )
}
```

这份代码对应的actions:

```typescript
'use server'
  
import { auth, clerkClient } from '@clerk/nextjs/server'
  
export const completeOnboarding = async (formData: FormData) => {
  const { userId } = await auth()
  
  if (!userId) {
    return { message: 'No Logged In User' }
  }
  
  const client = await clerkClient()
  
  try {
    const res = await client.users.updateUser(userId, {
      publicMetadata: {
        onboardingComplete: true,
        applicationName: formData.get('applicationName'),
        applicationType: formData.get('applicationType'),
      },
    })
    return { message: res.publicMetadata }
  } catch (err) {
    return { error: `There was an error updating the user metadata. ${err}` }
  }
}
```

# Excaliburjs

## 装库:
```
npm install vite typescript --save-exact --save-dev
```

或者pnpm也可

## 初始化引擎:

```ts
import * as ex from 'excalibur'
import { Engine } from 'excalibur'

// configs

// main.ts
import * as ex from 'excalibur';

const game = new ex.Engine({
  width: 400,
  height: 500,
  backgroundColor: ex.Color.fromHex("#54C0CA"),
  pixelArt: true,
  pixelRatio: 2,
  displayMode: ex.DisplayMode.FitScreen
});

game.start();
```

## 加载人物

```typescript
// bird.ts

import * as ex from "excalibur";

export class Bird extends ex.Actor {
    constructor() {
        super({
            pos: ex.vec(200, 300),
            width: 16, // for now we'll use a box so we can see the rotation
            height: 16, // later we'll use a circle collider
            color: ex.Color.Yellow
        })
    }
}
```

添加到默认场景里:

```typescript
// main.ts 
import * as ex from 'excalibur';

import { Bird } from './bird';

const game = new ex.Engine({...});

const bird = new Bird();
game.add(bird); // adds the Bird Actor to the default scene

game.start();
```

Excalibur使用和unity差不多的函数

```typescript
// ground.ts
import * as ex from "excalibur";

export class Ground extends ex.Actor {
    moving = false;
    constructor(pos: ex.Vector) {
        super({
            pos,
            anchor: ex.vec(0, 0),
            height: 64,
            width: 400,
            color: ex.Color.fromHex('#bd9853'),
            z: 1 // position the ground above everything
        })
    }
    
    start() {
	    // init a class
        this.moving = true;
    }

    stop() {
	    // stop
        this.moving = false;
    }
}
```

给人物增加碰撞:

```typescript
// bird.ts
import * as ex from 'excalibur';
import { Ground } from './ground';

export class Bird extends ex.Actor {
    ...

    override onCollisionStart(_self: ex.Collider, other: ex.Collider): void {
        if (other.owner instanceof Ground) {
            this.stop();
        }
    }

    stop() {
        this.vel = ex.vec(0, 0);
        this.acc = ex.vec(0, 0)
    }
}
```

然后添加到默认场景里:

```typescript
// main.ts
import * as ex from 'excalibur';
import { Bird } from './bird';
import { Ground } from './ground';

const game = new ex.Engine({...});

const bird = new Bird();
game.add(bird);

// drawHeight is the height of the visible drawing surface in game pixels
const ground = new Ground(ex.vec(0, game.screen.drawHeight - 64));
game.add(ground);

game.start();
```

人物移动:

```typeScript
// bird.ts
import * as ex from 'excalibur';

export class Bird extends ex.Actor {

    ...

    jumping = false;

    private isInputActive(engine: ex.Engine) {
        // if the space bar or the first pointer was down
        return (engine.input.keyboard.isHeld(ex.Keys.Space) ||
                engine.input.pointers.isDown(0))
    }

    override onPostUpdate(engine: ex.Engine): void {
        if (!this.jumping && this.isInputActive(engine)) {
            this.vel.y += -800; // negative is UP
            this.jumping = true;
        }

        if (!this.isInputActive(engine)) {
            this.jumping = false;
        }

        // keep velocity from getting too big
        this.vel.y = ex.clamp(this.vel.y, -500, 500);

        // The "speed" the bird will move relative to pipes
        this.rotation = ex.vec(200, this.vel.y).toAngle();
    }

    ...

}
```

可以用使用this.kill()相当于Unity的Destroy()

## 场景:
和Unity一样,可以把这些扔到一个场景里

```typescript
// level.ts
import * as ex from 'excalibur';
import { Bird } from './bird';
import { Ground } from './ground';
import { Pipe } from './pipe';

export class Level extends ex.Scene {
    bird: Bird = new Bird();
    ground!: Ground;
    override onInitialize(engine: ex.Engine): void {
        this.add(this.bird);

        this.ground = new Ground(ex.vec(0, engine.screen.drawHeight - 64))
        this.add(this.ground);

        const topPipe = new Pipe(ex.vec(engine.screen.drawWidth, 150), 'top');
        this.add(topPipe);

        const bottomPipe = new Pipe(ex.vec(engine.screen.drawWidth, 300), 'bottom');
        this.add(bottomPipe);
    }
}
```

然后初始化的时候:

```typescript
// main.ts
import * as ex from 'excalibur';
import { Level } from './level';

const game = new ex.Engine({
  ...
  scenes: { Level: Level }
});

game.start().then(() => {
  game.goToScene('Level');
});
```

## 把所有参数整合成一个文件

```typescript
// config.ts
import * as ex from 'excalibur';

export const Config = {
    BirdStartPos: ex.vec(200, 300),
    BirdAcceleration: 1200,
    BirdJumpVelocity: -800,
    BirdMinVelocity: -500,
    BirdMaxVelocity: 500, 
    PipeSpeed: 200,
    PipeInterval: 1500,
    PipeGap: 150
} as const;

```

可以使用timer来定时处理函数

```typescript
// pipe-factory.ts
import * as ex from 'excalibur';
import { Bird } from './bird';
import { Ground } from './ground';
import { Pipe } from './pipe';

export class PipeFactory {

    private timer: ex.Timer;
    constructor(
        private level: Level,
        private random: ex.Random,
        intervalMs: number) {
            this.timer = new ex.Timer({
                interval: intervalMs,
                repeats: true,
                action: () => this.spawnPipes()
            });
            this.level.add(this.timer);
    }

    spawnPipes() {
        const randomPipePosition = this.random.floating(0, this.level.engine.screen.resolution.height - Config.PipeGap);

        const bottomPipe = new Pipe(
            ex.vec(this.level.engine.screen.drawWidth, randomPipePosition + Config.PipeGap),
            'bottom'
        );
        this.level.add(bottomPipe);

        const topPipe = new Pipe(
            ex.vec(this.level.engine.screen.drawWidth, randomPipePosition),
            'top'
        );
        this.level.add(topPipe);
    }

    start() {
        this.timer.start();
    }

    reset() {
        for (const actor of this.level.actors) {
            if (actor instanceof Pipe) {
                actor.kill();
            }
        }
    }

    stop() {
        this.timer.stop();
        for (const actor of this.level.actors) {
            if (actor instanceof Pipe) {
                actor.vel = ex.vec(0, 0);
            }
        }
    }
}
```

但记得启动

```typescript
// level.ts

import { PipeFactory } from './pipe-factory';

export class Level extends ex.Scene {
    random = new ex.Random();
    pipeFactory = new PipeFactory(this, this.random, Config.PipeInterval);
    bird = new Bird();
    ground!: Ground;

    onInitialize(engine: ex.Engine): void {
        ...

        this.pipeFactory.start();
    }
}
```

## 添加文字:

```typescript
// level.ts
export class Level extends ex.Scene {
    ...
    score: number = 0;
    best: number = 0;
    scoreLabel = new ex.Label({
        text: 'Score: 0',
        x: 0,
        y: 0,
        z: 1,
        font: new ex.Font({
            size: 20,
            color: ex.Color.White
        })
    });

    bestLabel = new ex.Label({
        text: 'Best: 0',
        x: 400,
        y: 0,
        z: 1,
        font: new ex.Font({
            size: 20,
            color: ex.Color.White,
            textAlign: ex.TextAlign.End
        })
    });

    onInitialize(engine: ex.Engine): void {
        ...

        this.add(this.scoreLabel);
        this.add(this.bestLabel);

        const bestScore = localStorage.getItem('bestScore');
        if (bestScore) {
            this.best = +bestScore;
            this.setBestScore(this.best);
        } else {
            this.setBestScore(0);
        }
    }

    incrementScore() {
        this.scoreLabel.text = `Score: ${++this.score}`;
        this.setBestScore(this.score);
    }

    setBestScore(score: number) {
        if (score > this.best) {
            localStorage.setItem('bestScore', this.score.toString());
            this.best = score;
        }
        this.bestLabel.text = `Best: ${this.best}`;
    }
}
```

## 导入素材:

```typescript
// resources.ts
import * as ex from 'excalibur'

export const Resources = {
    // Relative to /public in vite
    BirdImage: new ex.ImageSource('./images/bird.png')
} as const;
```

在游戏里导入

```typescript
// main.ts
...
const loader = new ex.Loader(Object.values(Resources));
game.start(loader).then(() => {
  game.goToScene('Level');
});
```

### 动画:
使用精灵图

```typescript
// bird.ts
...
export class Bird extends ex.Actor {
  ...
  upAnimation!: ex.Animation;
  downAnimation!: ex.Animation;

  ...
  override onInitialize(): void {
    // Slice up image into a sprite sheet
    const spriteSheet = ex.SpriteSheet.fromImageSource({
        image: Resources.BirdImage,
        grid: {
            rows: 1,
            columns: 4,
            spriteWidth: 32,
            spriteHeight: 32,
        }
    });

    // Animation to play going up on tap
    this.upAnimation = ex.Animation.fromSpriteSheet(
        spriteSheet,
        [2, 1, 0], // 3rd frame, then 2nd, then first
        150, // 150ms for each frame
        ex.AnimationStrategy.Freeze);

    // Animation to play going down
    this.downAnimation = ex.Animation.fromSpriteSheet(
        spriteSheet,
        [0, 1, 2],
        150,
        ex.AnimationStrategy.Freeze);

    // Register animations by name
    this.graphics.add('down', this.downAnimation);
    this.graphics.add('up', this.upAnimation);
    ...
    
    this.on('exitviewport', () => {
        this.level.triggerGameOver();
    });
  }
  ...
}
```

## 添加到元素

```typescript
// <div class="container snippet-resizer">
//     <canvas id="game"></canvas>
// </div>

const game = new ex.Engine({
    canvasElementId: 'game',
    width: 600,
    height: 400,
    displayMode: ex.DisplayMode.FitContainer
});
```