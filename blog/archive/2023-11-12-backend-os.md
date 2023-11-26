---
layout: post
title: Computer's terms you should know for backend development
date: 2023-11-12 21:35:00-0400
tags: os
categories: backend
giscus_comments: true
featured: false
related_posts: true
---

> This is a small continuation of my [previous post]() on my takeaways of Git. Following [this back-end basic roadmap](https://roadmap.sh/backend), I will be going over some of the terms mentioned in the previous post: threads, concurrency, I/O, memory management, ownership system, thread-safe code, core, multi-core, parallelism, etc.

# Threads and Concurrency

## Threads
A thread is a sequence of instructions given to the CPU by a program or application. The more threads a CPU can execute at once, the more tasks it can complete. 

![Thread image by GeeksForGeeks](https://media.geeksforgeeks.org/wp-content/uploads/20200305160539/Thread-example-2.jpg)

### Multithreading
Multithreading refers to the ability of a program to execute multiple threads simultaneously within a single process. Each thread runs independently of the other threads and can perform its own set of tasks. Multithreading can help improve the responsiveness of a program by allowing it to continue running while performing other tasks in the background.

## Concurrency
Concurrency, on the other hand, refers to the ability of multiple threads to access shared resources simultaneously. In a concurrent program, multiple threads can access the same piece of data or code at the same time, which can result in conflicts and synchronization issues if not handled properly. Concurrency means happening at (about) the same time. As opposed to happening in parallel, truly.

![Cocurrency vs Multi-threading](https://anarsolutions.com/wp-content/uploads/2017/09/Multithreading-and-Concurrency.jpg)

> What multi-threading allows for is concurrency within each application/process.

> An example would be within a word processing program, while one thread is displaying the entered text, another thread could be continually checking for spellings and another for grammar, etc.
From https://www.quora.com/What-is-the-difference-between-multi-threading-and-concurrency

### Parallelism
Parallelism means that an application splits its tasks up into smaller subtasks which can be processed in parallel, for instance on multiple CPUs at the exact same time.

Parallelism does not require two tasks to exist. It literally physically run parts of tasks OR multiple tasks, at the same time using the multi-core infrastructure of CPU, by assigning one core to each task or sub-task.

![Cocurrency vs Parallelism](https://www.baeldung.com/wp-content/uploads/sites/4/2022/01/vs-1024x462-1.png)


- To be continued...s

# References
- https://www.quora.com/What-is-the-difference-between-multi-threading-and-concurrency