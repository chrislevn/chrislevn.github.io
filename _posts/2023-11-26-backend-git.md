---
layout: post
title: My takeaways of Git
date: 2023-11-10 19:35:00-0400
description: My takeaways of Git
tags: backend git
categories: backend
giscus_comments: true
featured: true
related_posts: false
related_publications: true
---

This is a continuation of my [previous post](https://christopherle.com/blog/2023/inside-browser/) on what happend when you type a URL into a browser. Following [this back-end basic roadmap](https://roadmap.sh/backend), I will be going over the basics of Git in today post. I won't be covering everything, just my takeaways of what I think is valuable. 

# Git 

## 1. What is Git?
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

## 2. How Git works? 
Unlike other VCSs, Git takes a snapshot of your file every time you make a commit. Git stores these snapshots as a reference to the previous commit.

![Figure 5. Storing data as snapshots of the project over time](https://git-scm.com/book/en/v2/images/snapshots.png)

Git also have branches and almost every operation is local. Everything in Git is also checksummed (SHA-1) before it is stored and is then referred to by that checksum. Meaning it is impossible to change the contents of any file or directory without Git knowing about it. This functionality is built into Git at the lowest levels and is integral to its philosophy.


## 3. Why using Git? 
> When you do actions in Git, nearly all of them only add data to the Git database. It is hard to get the system to do anything that is not undoable or to make it erase data in any way

That means you can always undo any action in Git, making it easy to experiment with different ideas, with others, without worrying about losing your original work.

## 4. My takeaways of Git
I won't cover everything about Git, just my takeaways of what I think is valuable.

### 4.1. Don't use git merge
During my time working with backend, I found it is useful to learn how to make a pull request, merge, and rebase. As an engineer, you should also know how to make linear commit history. 

![Image by Bits'n'Bites](https://www.bitsnbites.eu/wp-content/uploads/2015/12/1-nonlinear-vs-linear.png)

It's important not to use `git merge` when you are working on a feature branch. Instead, use `git rebase`. This will make your commit history linear. The reason is that `git merge` will create a new commit that combines the two branches. This will make your commit history look messy.

Here is how I did it. 
```bash
git checkout master
git pull --rebase
git checkout <branch_name>
git rebase origin/master
git push -f origin <branch_name>
```

### 4.2 Make git commits small and atomic

A commit should be a single logical change. Don’t make several logical changes in one commit. For example, if a patch fixes a bug and optimizes the performance of a feature, split it into two separate commits.

Sometimes, we will do a bunch of testing commits since we can't test the system locally. It's important to squash these commits into one commit before making a pull request, making easier for reviewers to review your code.

### 4.3 Identify a branching strategy
While there are several approaches to development, the most common are:

Centralized workflow: Teams use only a single repository and commit directly to the main branch. Centralized workflow is a good approach for small teams and projects.

Feature branching: Teams use a new branch for each feature and don't commit directly to the main branch. It's a good approach for large teams and projects. Feature branching is the most common branching strategy. A branch with feature is usually named `feature/<feature_name>`.

GitFlow: An extreme version of feature branching in which development occurs on the develop branch, moves to a release branch, and merges into the main branch. GitFlow is a good approach for large teams and projects.

Personal branching: Similar to feature branching, but rather than develop on a branch per feature, it's per developer. Every user merges to the main branch when they complete their work. Personal branching is a good approach for small teams and projects.

## 4.4 5 steps to write meaningful commit messages

- Capitalization and Punctuation: Capitalize the first word and do not end in punctuation. If using Conventional Commits, remember to use all lowercase.

- Mood: Use imperative mood in the subject line. Example:
    - Add fix for dark mode toggle state. Imperative mood gives the tone you are giving an order or request.


- Type of Commit: Specify the type of commit. It is recommended and can be even more beneficial to have a consistent set of words to describe your changes. 
Example: 
    - Bugfix, Update, Refactor, Bump, and so on. See the section on Conventional Commits below for additional information.


- Length: The first line should ideally be no longer than 50 characters, and the body should be restricted to 72 characters.

- Content: Be direct, try to eliminate filler words and phrases in these sentences (examples: though, maybe, I think, kind of). Think like a journalist.

## References
- “1.3 Getting Started - What Is Git?” Git, git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F. Accessed 26 Nov. 2023. 
- “What Are Git Version Control Best Practices?” GitLab, GitLab, about.gitlab.com/topics/version-control/version-control-best-practices/. Accessed 26 Nov. 2023. 