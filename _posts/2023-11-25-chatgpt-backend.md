---
layout: post
title: I studied backend engineering for 3 months. Here is what I learned.
date: 2023-11-25 19:35:00-0400
description: I asked ChatGPT to create backend projects for me. Here is what it generated.
tags: backend tech
categories: system
giscus_comments: true
featured: true
related_posts: false
related_publications:
---

# Basics

## Git

comments on merge, linear history, rebase, squash, cherry-pick, git flow, git bisect, git blame, git stash, git revert, git reset, git
Common git 


## Terminal 

## POSIX Baics
POSIX (Portable Operating System Interface) is a family of standards for maintaining compatibility between operating systems. It describes utilities, APIs, and services that a compliant OS should provide to software, thus making it easier to port programs from one system to another.

A practical example: in a Unix-like operating system, there are three standard streams, stdin, stdout and stderr - they are I/O connections that you will probably come across when using a terminal, as they manage the flow from the standard input (stdin), standard output (stdout) and standard error (stderr).

So, in this case, when we want to interact with any of these streams (through a process, for example), the POSIX operating system API makes it easier - for example, in the <unistd.h> C header where the stdin, stderr, and stdout are defined as STDIN_FILENO, STDERR_FILENO and STDOUT_FILENO.

POSIX also adds a standard for exit codes, filesystem semantics, and several other command line utility API conventions.

examples of stdin, stdout, stderr: 
- stdin
```
$ echo "Hello World" | cat
Hello World
```

With stdin, we can pipe the output of one command to the input of another command. In this case, we are piping the output of echo "Hello World" to the input of cat, which will print the output of echo "Hello World" to the terminal.

- stdout
```
$ echo "Hello World" > hello.txt
$ cat hello.txt
Hello World
```

With stdout, we can redirect the output of a command to a file. In this case, we are redirecting the output of echo "Hello World" to the file hello.txt.

- stderr
```
$ cat hello.txt > hello2.txt
cat: hello.txt: No such file or directory
$ cat hello2.txt
```
With stderr, we can redirect the error output of a command to a file. In this case, we are redirecting the error output of cat hello.txt to the file hello2.txt.

pipes: 
```
$ echo "Hello World" | cat
Hello World
```

## OS and General Knowledge


## Databases


### Relational Databases

### NoSQL Databases

### Scaling Databases

## API


## Cache

## Security

## Testing

## CI/CD

##

# Software Design and Architecture

## Design and development principles

## Architectural patterns

## Message brokers

## Containerization vs virtualization

## GraphQL

## WebSockets

## Server Sent Events

## Web servers

# Building for scale
