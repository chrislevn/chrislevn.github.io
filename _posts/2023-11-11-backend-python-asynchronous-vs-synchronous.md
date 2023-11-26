---
layout: post
title: Asynchronous vs Synchronous frameworks in Python
date: 2023-11-11 20:35:00-0400
description: 
tags: languages python frameworks
categories: backend
giscus_comments: true
featured: false
related_posts: true
---

> This is a small continuation of my [previous post](https://christopherle.com/blog/2023/backend-git/) on top backend languages. Following [this back-end basic roadmap](https://roadmap.sh/backend), I will be going over the basics of backend languages in today post. I won't be covering everything, just my takeaways of what I think is valuable.

When it comes to backend development, there are two types of frameworks: Asynchronous and Synchronous.

## 1. Synchronous Frameworks
Synchronous frameworks are the most common type of frameworks. They are easy to use and understand. They are also easy to debug. However, they are not as fast as asynchronous frameworks.

### How it works
Synchronous frameworks work by blocking the execution of the code until the response is received. This means that the code will wait for the response before it can continue executing. This is why they are called synchronous frameworks.

### When to use
Synchronous frameworks are best used when you need to process a lot of data. They are also best used when you need to process data in real-time.

### Examples
- Flask
- Django

## 2. Asynchronous Frameworks
Asynchronous frameworks are the fastest type of frameworks. They are also the most difficult to use and understand. They are also the most difficult to debug.

### How it works
Asynchronous frameworks work by executing the code in parallel. This means that the code will execute in parallel with the response. This is why they are called asynchronous frameworks.

### When to use
Asynchronous frameworks are best used when you need to process a lot of data in real-time. They are also best used when you need to process data in real-time.

### Examples
- gevent
- Tornado
- Sanic
- aiohttp