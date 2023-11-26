---
layout: post
title: Top backend languages and when to use them
date: 2023-11-11 19:35:00-0400
description: 
tags: languages python rust go 
categories: backend
giscus_comments: true
featured: true
related_posts: true
---

> This is a continuation of my [previous post](https://christopherle.com/blog/2023/backend-git/) on my takeaways of Git. Following [this back-end basic roadmap](https://roadmap.sh/backend), I will be going over the basics of backend languages in today post. I won't be covering everything, just my takeaways of what I think is valuable.



When it comes to Backend Web Development – we primarily require a backend (or you can say server-side) programming language to make the website function along with various other tools & technologies such as databases, frameworks, web servers, etc.

Pick a language from the given list and make sure to learn its quirks, core details about its runtime e.g. concurrency, memory model, etc.

## Comparison of backend languages
| Language   | Concurrency                                  | Runtime                          | Memory Model             | Use Cases                                            |
|------------|----------------------------------------------|----------------------------------|--------------------------|------------------------------------------------------|
| Python     | Multi-threading, asyncio                     | Interpreted, CPython, PyPy       | Dynamic, managed         | Web applications, Data analysis, AI/ML, Scripting    |
| Rust       | Async, multi-threading, Actor model          | Compiled                         | Ownership, Borrowing     | System programming, WebAssembly, Embedded systems    |
| Go         | Goroutines, channels                         | Compiled, Go runtime             | Garbage collected        | Network services, Concurrent processing             |
| PHP        | Multi-threading (limited), async (libraries) | Interpreted, Zend Engine         | Dynamic, managed         | Web development, CMS, E-commerce platforms          |
| JavaScript | Event loop, async/await                      | Interpreted, Node.js runtime     | Dynamic, managed         | Web development, Server-side applications           |
| Java       | Threads, Future, CompletableFuture           | Compiled to bytecode, JVM        | Garbage collected        | Enterprise applications, Android apps, Web services |
| C#         | Async/await, Task Parallel Library           | Compiled to bytecode, CLR        | Garbage collected        | Web applications, Desktop applications, Games       |
| Ruby       | Threads, Fibers                              | Interpreted, YARV                | Dynamic, managed         | Web applications (Rails), Scripting, Prototyping    |

Let's look at some of the criteria to considered:

### Concurrency:
- Python and Ruby have limitations in concurrency due to GIL (Global Interpreter Lock), though they support multi-threading and have asynchronous libraries.
- Rust and Go are known for their efficient concurrency models. Rust uses advanced concepts like ownership and borrowing, while Go uses goroutines and channels.
- Java, C#, and JavaScript (Node.js) support asynchronous programming and are quite capable in handling concurrent processes.

### Runtime:
![Image by ByteByteGo](https://i.ytimg.com/vi/hnlz0YYCpBU/maxresdefault.jpg)

- Python, PHP, JavaScript, and Ruby are interpreted languages with dynamic memory management, often leading to slower runtime performance compared to compiled languages.
- Rust, Go, Java, and C# have compiled runtimes, offering generally better performance. Java and C# run on virtual machines (JVM and CLR), which offer cross-platform support.
- Memory Model:
Rust has a unique memory model focusing on safety without a garbage collector.
- Go, Java, and C# use garbage collection to manage memory, balancing performance and ease of use.
- Python, PHP, JavaScript, and Ruby have dynamic memory models with managed garbage collection, which simplifies development at the cost of some control and efficiency.

### Use Cases:
- Python and Ruby are often chosen for their ease of use and rapid development capabilities, especially in web applications and scripting.
- ust is gaining popularity for system-level programming and scenarios where safety and performance are critical.
- Go is preferred for networked applications and services requiring high concurrency.
- PHP remains a staple for traditional web development.
- JavaScript (Node.js) is ubiquitous in modern web development.
- Java and C# are used extensively in enterprise environments for their robustness and scalability.

## Other criteria to consider include:

| Language   | Targeted Platform                            | Elasticity of Language           | Time to Production       | Performance                          | Support and Community                          |
|------------|----------------------------------------------|----------------------------------|--------------------------|--------------------------------------|------------------------------------------------|
| Python     | Cross-platform, web, data science            | High (Dynamic typing)            | Fast                     | Lower (interpreted)                  | Very large, widespread use                     |
| Rust       | Cross-platform, system, embedded, WebAssembly| Low (Strict type system)         | Slower                   | Very high (compiled)                 | Growing, strong backing by Mozilla             |
| Go         | Cross-platform, server-side, cloud           | Moderate (Balanced simplicity)   | Quick                    | High (compiled, efficient for concurrency)| Growing, strong backing by Google           |
| PHP        | Web development                              | High (Dynamic, flexible)         | Fast                     | Moderate (interpreted)               | Large, especially in web development          |
| JavaScript | Web, server-side (Node.js), mobile (React Native)| High (Dynamic, flexible)     | Fast                     | Good (V8 engine optimizations)       | Very large, diverse applications              |
| Java       | Cross-platform, enterprise, Android          | Moderate (Strong typing, flexible frameworks) | Moderate | Good (JVM optimizations)            | Very large, enterprise focus                  |
| C#         | Cross-platform (.NET Core), desktop, web, mobile, games | Moderate (Strong typing, flexible frameworks) | Moderate | Good (CLR optimizations)            | Large, strong backing by Microsoft            |
| Ruby       | Cross-platform, web (Ruby on Rails)          | High (Dynamic typing)            | Fast                     | Lower (interpreted)                  | Dedicated, particularly around Rails          |



#### Notes: 
I didn't make comparison in terms of speed due to the fact that it's hard to compare languages. It's better to compare the speed of a specific task. Also, although it can be faster to run a specific task, would it be faster to develop considering the learning curve and current codebase?

It's also worth noting that: 
- the performance of a language is not the only factor that affects the performance of a web application. The performance of a web application is also affected by the performance of the web server, the database, the network, and the client-side code.
- programming languages are always updated and improved. For example, Python 3.10 is faster than Python 3.9 due to faster method calls and more efficient memory management. There are always pros and cons. Don't learn everything, just learn what you need for your use cases and master it. 

---
> One note about Python and Mojo:

### Overcome the limitations of Python
Python is known for its slow speed. However, I just got to know about Mojo 
> Mojo combines the usability of Python with the performance of C, unlocking unparalleled programmability of AI hardware and extensibility of AI models.

![Sample code with Mojo](https://miro.medium.com/v2/resize:fit:942/1*GamnxUBaLlHbSKoOdbEK7g.png)

The reason why Mojo is fast is Mojo is compiled to machine code, while Python is interpreted. This means that Mojo code can be executed directly by the CPU, while Python code must first be translated into an intermediate form called bytecode. This translation process adds to the overhead of executing Python code. I will cover another in-depth post about Mojo in the future.

Read more about Mojo [here](https://www.modular.com/mojo).

How Mojo is 35,000x faster than Python? Read more [here](https://www.modular.com/blog/how-mojo-gets-a-35-000x-speedup-over-python-part-1).

---

In the next post, I will talk about the basics of CPU (cocurrency, I/O, memory management, etc)

# References
- https://www.makeuseof.com/build-http-web-server-in-rust/
- https://discourse.julialang.org/t/why-mojo-can-be-so-fast/98458
- https://www.fast.ai/posts/2023-05-03-mojo-launch.html
- https://blog.logrocket.com/when-to-use-rust-when-to-use-golang/
- https://www.freecodecamp.org/news/what- is-java-used-for/
- https://data-flair.training/blogs/pros-and-cons-of-java/