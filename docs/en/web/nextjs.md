
next-js的文件结构:

- /app: routes,components,logic
- /app/lib: functions used in your application
- /app/ui: all the UI components for the application, cards, tables, and
  forms, nextjs provide some styling
- /public: all the static assets

# chapter 2:

tailwind, leave this for later

# chapter 3:

## font:

when using the next/font module, the fonts are automatically optimised

```    import {Inter} from 'next/font/google';

    export const inter = Inter({subsets: ['latin']});

    // in other file

    import '@/app/ui/global.css';
    import { inter } from '@/app/ui/fonts';
    so 
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode; // this part is for identifing the type
    }) {
      return (
        <html lang="en">
          <body className={`${inter.className} antialiased`}>{children}</body>
        </html>
      );
    }
```
so actually, the Inter({subsets: \[\'latin\'\]}) just return a DOM with
the desired className

## pic:

to add a image, use the image tag

The Component is an extension of the HTML

tag, and comes with automatic image optimization, such as:

- Preventing layout shift automatically when images are loading.
- Resizing images to avoid shipping large images to devices with a
  smaller viewport.
- Lazy loading images by default (images load as they enter the
  viewport).
- Serving images in modern formats, like WebP and AVIF, when the browser
  supports it.

### clsx to toggle classnames

for example

```    import clsx from 'clsx';

    export default function InvoiceStatus({ status }: { status: string }) {
      return (
        <span
          className={clsx(
            'inline-flex items-center rounded-full px-2 py-1 text-sm',
            {
              'bg-gray-100 text-gray-500': status === 'pending',
              'bg-green-500 text-white': status === 'paid',
            },
          )}
        >
        // ...
    )}
```
# chapter 4:

next js does the routing for you, you just have to create corresponding
folders in app/

for each folder in the app/ folder that is not named as lib, query,
seed, ui

the page stuff goes into the page.tsx in the corresponding directory

## layout:

something like this:

```    import SideNav from '@/app/ui/dashboard/sidenav';

    export default function Layout({ children }: { children: React.ReactNode }) {
      return (
        <div className="flex h-screen flex-col md:flex-row md:overflow-hidden">
          <div className="w-full flex-none md:w-64">
            <SideNav />
          </div>
          <div className="flex-grow p-6 md:overflow-y-auto md:p-12">{children}</div>
        </div>
      );
    }
```
this takes in a children ReactNode, acts like Outlet in native react

a root layout is required

# chapter 5:

navigation

so we import Link from \'next/link\'

and then use the Link instead of a tags, it prefetches the code for the
routes

```    import {
      UserGroupIcon,
      HomeIcon,
      DocumentDuplicateIcon,
    } from '@heroicons/react/24/outline';
    import Link from 'next/link';

    // Map of links to display in the side navigation.
    // Depending on the size of the application, this would be stored in a database.
    const links = [
      { name: 'Home', href: '/dashboard', icon: HomeIcon },
      {
        name: 'Invoices',
        href: '/dashboard/invoices',
        icon: DocumentDuplicateIcon,
      },
      { name: 'Customers', href: '/dashboard/customers', icon: UserGroupIcon },
    ];

    export default function NavLinks() {
      return (
        <>
          {links.map((link) => {
            const LinkIcon = link.icon;
            return (
              <Link
                key={link.name}
                href={link.href}
                className="flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none md:justify-start md:p-2 md:px-3"
              >
                <LinkIcon className="w-6" />
                <p className="hidden md:block">{link.name}</p>
              </Link>
            );
          })}
        </>
      );
    }
```
so then we could use the pathnames to match the corresponding link and
assign it a different css with clsx

```    "use client";

    import {
      UserGroupIcon,
      HomeIcon,
      DocumentDuplicateIcon,
    } from '@heroicons/react/24/outline';
    import Link from 'next/link';
    import { usePathname } from 'next/navigation';
    import clsx from 'clsx';

    // Map of links to display in the side navigation.
    // Depending on the size of the application, this would be stored in a database.
    const links = [
      { name: 'Home', href: '/dashboard', icon: HomeIcon },
      {
        name: 'Invoices',
        href: '/dashboard/invoices',
        icon: DocumentDuplicateIcon,
      },
      { name: 'Customers', href: '/dashboard/customers', icon: UserGroupIcon },
    ];

    export default function NavLinks() {
      const pathname = usePathname()
      return (
        <>
          {links.map((link) => {
            const LinkIcon = link.icon;
            return (
              <Link
                key={link.name}
                href={link.href}
                className={clsx(
                  'flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none md:justify-start md:p-2 md:px-3',
                  {
                    'bg-sky-100 text-blue-600': pathname === link.href,
                  },
                )}
              >
                <LinkIcon className="w-6" />
                <p className="hidden md:block">{link.name}</p>
              </Link>
            );
          })}
        </>
      );
    }
```
but notice to use usePathname hook in next, we need to mark this code as
\"use client\" at the top of the code

# chapter 6:

database

in the vercel -\> storage, we can create a database

we need to get the .env.local inside

and we need to also set .env to the gitignore

## seed the database:

seed it with initial data

we can use /app/route.ts to seed the database

basically its just like springboot router

```    // import bcrypt from 'bcrypt';
    // import { db } from '@vercel/postgres';
    // import { invoices, customers, revenue, users } from '../lib/placeholder-data';

    // const client = await db.connect();

    // async function seedUsers() {
    //   await client.sql`CREATE EXTENSION IF NOT EXISTS "uuid-ossp"`;
    //   await client.sql`
    //     CREATE TABLE IF NOT EXISTS users (
    //       id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    //       name VARCHAR(255) NOT NULL,
    //       email TEXT NOT NULL UNIQUE,
    //       password TEXT NOT NULL
    //     );
    //   `;

    //   const insertedUsers = await Promise.all(
    //     users.map(async (user) => {
    //       const hashedPassword = await bcrypt.hash(user.password, 10);
    //       return client.sql`
    //         INSERT INTO users (id, name, email, password)
    //         VALUES (${user.id}, ${user.name}, ${user.email}, ${hashedPassword})
    //         ON CONFLICT (id) DO NOTHING;
    //       `;
    //     }),
    //   );

    //   return insertedUsers;
    // }

    // async function seedInvoices() {
    //   await client.sql`CREATE EXTENSION IF NOT EXISTS "uuid-ossp"`;

    //   await client.sql`
    //     CREATE TABLE IF NOT EXISTS invoices (
    //       id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    //       customer_id UUID NOT NULL,
    //       amount INT NOT NULL,
    //       status VARCHAR(255) NOT NULL,
    //       date DATE NOT NULL
    //     );
    //   `;

    //   const insertedInvoices = await Promise.all(
    //     invoices.map(
    //       (invoice) => client.sql`
    //         INSERT INTO invoices (customer_id, amount, status, date)
    //         VALUES (${invoice.customer_id}, ${invoice.amount}, ${invoice.status}, ${invoice.date})
    //         ON CONFLICT (id) DO NOTHING;
    //       `,
    //     ),
    //   );

    //   return insertedInvoices;
    // }

    // async function seedCustomers() {
    //   await client.sql`CREATE EXTENSION IF NOT EXISTS "uuid-ossp"`;

    //   await client.sql`
    //     CREATE TABLE IF NOT EXISTS customers (
    //       id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    //       name VARCHAR(255) NOT NULL,
    //       email VARCHAR(255) NOT NULL,
    //       image_url VARCHAR(255) NOT NULL
    //     );
    //   `;

    //   const insertedCustomers = await Promise.all(
    //     customers.map(
    //       (customer) => client.sql`
    //         INSERT INTO customers (id, name, email, image_url)
    //         VALUES (${customer.id}, ${customer.name}, ${customer.email}, ${customer.image_url})
    //         ON CONFLICT (id) DO NOTHING;
    //       `,
    //     ),
    //   );

    //   return insertedCustomers;
    // }

    // async function seedRevenue() {
    //   await client.sql`
    //     CREATE TABLE IF NOT EXISTS revenue (
    //       month VARCHAR(4) NOT NULL UNIQUE,
    //       revenue INT NOT NULL
    //     );
    //   `;

    //   const insertedRevenue = await Promise.all(
    //     revenue.map(
    //       (rev) => client.sql`
    //         INSERT INTO revenue (month, revenue)
    //         VALUES (${rev.month}, ${rev.revenue})
    //         ON CONFLICT (month) DO NOTHING;
    //       `,
    //     ),
    //   );

    //   return insertedRevenue;
    // }

    export async function GET() {
      return Response.json({
        message:
          'Uncomment this file and remove this line. You can delete this file when you are finished.',
      });
      // try {
      //   await client.sql`BEGIN`;
      //   await seedUsers();
      //   await seedCustomers();
      //   await seedInvoices();
      //   await seedRevenue();
      //   await client.sql`COMMIT`;

      //   return Response.json({ message: 'Database seeded successfully' });
      // } catch (error) {
      //   await client.sql`ROLLBACK`;
      //   return Response.json({ error }, { status: 500 });
      // }
    }
```
because nextjs integrated the database items in javascript, when we need
to retrieve data in the components, we can make a component async

# chapter 7

about retrieving, if you know sql, then this is just misc

# chapter 8

static rendering and dynamic rendering

with dynamic rendering, the application is only as fast ad the slowest
data fetch

# chapter 9:

add loading page

so now a sepcial file called loading.tsx

then whatever in loading.tsx will show up until the page is rendered

we can also add some loading skeletons

a trick is that whatever in parenthsis is not going to be included in
the URL, so we could create some folder with (something) so that the
loading page only applies to the root compoenent of dashboard

we cna also do the similar stuff with the Suspense of react

so something like

```    <Suspense fallback={<RevenueChartSkeleton />}>
      <RevenueChart />
    </Suspense>
```
# chapter 10:

Partial Prerendering

in the next.config.mjs file add

```    /** @type {import('next').NextConfig} */

    const nextConfig = {
      experimental: {
        ppr: 'incremental',
      },
    };

    export default nextConfig;
```
or in next.config.js

```    import type { NextConfig } from 'next';

    const nextConfig: NextConfig = {
      /* config options here */
      experimental: {
        ppr: "incremental"
      }
    };

    export default nextConfig;
```
according to stackoverflow
https://stackoverflow.com/questions/79222268/canaryonlyerror-the-experimental-feature-experimental-ppr-can-only-be-enabled

need to pnpm i next@canary

and in the component to enable ppr, we do

export const experimental_ppr = true;

# chapter 11:

nextjs has its own useParams, useSearchParams, useRouter

to do the same as this.\$router.push in Vue

we could do

```    const {replace} = useRouter()

    replace(path) // but when we use this, the entry in history will also be removed, so the user cannot go back

    // or

    const router = useRouter()

    router.push(path)
```
for router see
https://nextjs.org/docs/app/api-reference/functions/use-router

nextjs provides debounce

so inside the search component, we can useDebouncedCallback like we
would do with lodash

# chapter 12:

mutating data

so when mutating data, we need to signal the code as \"use server\"

we can also use zod to validate the data before passing them to the sql
query

basically a sql query can be done as this

```    'use server';

    import { z } from 'zod';
    import { sql } from '@vercel/postgres';


    const FormSchema = z.object({
      id: z.string(),
      customerId: z.string(),
      amount: z.coerce.number(),
      status: z.enum(['pending', 'paid']),
      date: z.string(),
    });

    const CreateInvoice = FormSchema.omit({ id: true, date: true });

    // ...
    export async function createInvoice(formData: FormData) {
      const { customerId, amount, status } = CreateInvoice.parse({
        customerId: formData.get('customerId'),
        amount: formData.get('amount'),
        status: formData.get('status'),
      });
      const amountInCents = amount * 100;
      const date = new Date().toISOString().split('T')[0];
      await sql`
        INSERT INTO invoices (customer_id, amount, status, date)
        VALUES (${customerId}, ${amountInCents}, ${status}, ${date})
      `;
    }
```
after updating the data, we can use

```    import { revalidatePath } from 'next/cache';
    revalidatePath('/dashboard/invoices');
```
to refresh the page

and

```    import { redirect } from 'next/navigation';
    redirect('/dashboard/invoices');
```
to redirect the user back to the page

we can also use dynamic router segment with a folder in square brackets

for example invoices/\[id\]/edit

then to read the id param

we can do

```    export default async function Page(props: { params: Promise<{ id: string }> }) {
      const params = await props.params;
      const id = params.id;
      //...
    }
```
# chapter 13

instead of try-catching all the blocks

we could do

again error.tsx is another special file

```    'use client';

    import { useEffect } from 'react';

    export default function Error({
      error,
      reset,
    }: {
      error: Error & { digest?: string };
      reset: () => void;
    }) {
      useEffect(() => {
        // Optionally log the error to an error reporting service
        console.error(error);
      }, [error]);

      return (
        <main className="flex h-full flex-col items-center justify-center">
          <h2 className="text-center">Something went wrong!</h2>
          <button
            className="mt-4 rounded-md bg-blue-500 px-4 py-2 text-sm text-white transition-colors hover:bg-blue-400"
            onClick={
              // Attempt to recover by trying to re-render the invoices route
              () => reset()
            }
          >
            Try again
          </button>
        </main>
      );
    }
```
so then we can add a conditional to redirect to 404 page if not exist

and then a special file name non-found.tsx

# chapter 15:

for adding auth, we can use the nextjs auth module

add an auth.config.ts file

```    import type { NextAuthConfig } from 'next-auth';

    export const authConfig = {
      pages: {
        signIn: '/login',
      },
      callbacks: {
        authorized({ auth, request: { nextUrl } }) {
          const isLoggedIn = !!auth?.user;
          const isOnDashboard = nextUrl.pathname.startsWith('/dashboard');
          if (isOnDashboard) {
            if (isLoggedIn) return true;
            return false; // Redirect unauthenticated users to login page
          } else if (isLoggedIn) {
            return Response.redirect(new URL('/dashboard', nextUrl));
          }
          return true;
        },
      },
      providers: [], // Add providers with an empty array for now
    } satisfies NextAuthConfig;
```
we also need a middleware.ts file

```    import NextAuth from 'next-auth';
    import { authConfig } from './auth.config';

    export default NextAuth(authConfig).auth;

    export const config = {
      // https://nextjs.org/docs/app/building-your-application/routing/middleware#matcher
      matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)'],
    };
```
in the seed.js we used bcrypt to hash the user\'s password before
storing it in the database, we can also do this for safety issues

```    import NextAuth from 'next-auth';
    import { authConfig } from './auth.config';

    export const { auth, signIn, signOut } = NextAuth({
      ...authConfig,
    });
```
we can also use some 3rd party signup with

```    import NextAuth from 'next-auth';
    import { authConfig } from './auth.config';
    import Credentials from 'next-auth/providers/credentials';

    export const { auth, signIn, signOut } = NextAuth({
      ...authConfig,
      providers: [Credentials({})],
    });
```
we can add the sign in functionality and use zod to validate before
sending it to the sql
:::::::::::::::::::::::
:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::
