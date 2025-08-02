---
comments: true
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
hide:
- navigation
- toc
- footer
- feedback
level: Imperial
---

# IO and Error Handling

## Console:

even though Java hava a System, but scala has it own Console, so we should avoid using System.in at all

the Console object exposes def in, def out, def err, and also println, printf

### IO Redirection with Console

Console exposes the standard streams via def. so it can be temporarily redirected somewhere

```scala
def withOut[A](out: OutoutStream)(body: => A): A
def withIn[A](int: InputStream)(body: => A): A
def withErr[A](err: OutputStream)(body: => A): A
```

so we can do something like this

```scala
val fileOut: OutputStream = ...
Console.withOut(fileOut) {
  println("""something""".stripMargin)
}
```

## File-IO: OS-Lib

need to refer to the library ReadMe.md

```scala
// os.pwd = ., os.root = /, os.home = ~, and os.up = ..
val fileContent: String = os.read(os.pwd / "hello.txt")
val fileLines: InexedSeq[String] = os.read.lines(os.home / ".bashrc")
val fileStream: java.io.InputStream = os.read.inputStream(os.pwd / "hello.txt")

os.write.over(os.pwd / "hello.text", "Hello World")

val out: java.io.OutputStream = 
  os.write.outputStram(os.pwd / os.up / "hello2.txt")

os.call("pwd") // call the pwd command
os.proc("echo","hello world").call()
```

## Error Handling

the tradition try-catch-finally is available in Scala, pattern match in the catch block with case

### Try class

```scala
sealed abstract class Try[+A] {
  ...
}

case class Success[A](x:A) extends Try[A]
case class Failure(err: Throwable) extends Try[Nothing]
```

Failure is not an object, rather it just store the exception that resulted in the failure

in Try must run a computation, and catch any possible non-fatal exceptions, so the argument has to be passed lazily

```scala
object Try {
  def apply[A](r: => A): Try[A] = 
    try Success(r) catch {
      case NonFatal(e) => Failure(e)
    }
}
```

so we would do

```scala
val src: Try[String] = Try {
  os.read(os.pwd / "foo.txt")
}
```

we can also use the Try's combinators

```scala
sealed abstract class Try[+A]:
  def orElse[B >: A](default: => Try[B]): Try[B]
  def getOrElse[B >: A](default: => B): B
  def map[B](f: A => B): Try[B]
  def flatMap[B](f: A => Try[B]): Try[B]
  def recover[B >: A](pf: PartialFunction[Throwable, B]): Try[B]
  def recoverWith[B :> A](pf: PartialFunction[Throwable, Try[B]]): Try[B]
```

#### pipeline example
for example

```scala
for src1 <- Try(os.read.lines(os.pwd / "foo.txt")).recoverWith {
    case e: IOException => Try {
      os.read.lines(os.pwd / "backup.txt")
    }
  }
  src2 <- Try(os.read.lines("f2.txt"))
yield (src1, src2).zipped((s1,s2) => s"$s1:$s2").mkString("\n")
```

### Aside: PartialFunction and Error Recovery:

PartialFunction is used for recover and recover With. 

but PartialFunction[Throwable, A] is only defined for certain exceptions, if exception in a Failure is not one of them, no recovery occurs: the Failure continues as normal