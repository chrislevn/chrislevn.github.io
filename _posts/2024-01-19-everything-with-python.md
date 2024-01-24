---
layout: post
title: Clean code with Python 
date: 2024-01-19 19:35:00-0400
description: 
tags: languages python 
categories: backend
giscus_comments: true
featured: true
related_posts: true
---

If you learn programming, you will eventually learn Python as it is not only easy to learn but also very popular in data science and machine learning. However, Python is not well used in other productions such as web server, mobile, and desktop applications due to its slow speed. I covered this in my [previous post](https://christopherle.com/blog/2023/backend-languages/). As a result, if you major in Computer Science and want to work as a software engineer, you will likely have to learn Java (for enterprise applications), C#/C++, .NET, Go, JavaScript (web server). This post, however, is not about telling you to be the jack of all trades but to find a way to use and master Python efficiently. 

# Part 1: Clean and maintainable code

Let's start with a simple code: 
    
```python
def find_user(user_id: str, users: List[User]) -> Optional[User]:
    """Find a user by ID.

    Args:
        user_id (str): The ID of the user to find.
        users (List[User]): The list of users to search.

    Returns:
        Optional[User]: The user if found, otherwise None.
    """
    for user in users:
        if user.id == user_id:
            return user
    return None
```

This code is simple. It searches for a user by ID with user id is uuid. This would take O(n) time. However, if we use a dictionary, we can reduce the time complexity to O(1). The function return Optional[User] meaning that it can return either a User or None. This is a good practice as it is better than returning None or raising an exception.

```python
def find_user(user_id: str, users: Dict[str, User]) -> Optional[User]:
    """Find a user by ID.

    Args:
        user_id (str): The ID of the user to find.
        users (Dict[str, User]): The dictionary of users to search.

    Returns:
        Optional[User]: The user if found, otherwise None.
    """
    return users.get(user_id)
```

## Class and Special methods

Now, let's construct a class: 
    
```python
class User:
    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, email={self.email})"

class Users:
    def __init__(self, users: dict[User]):
        self.users = users

    def __getitem__(self, user_id: str) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def __repr__(self) -> str:
        return f"Users(users={self.users})"
```

The code above contains two classes: User and Users. The User class represents a single user, while the Users class represents a collection of users. The Users class is a wrapper around a list of users. It provides a way to access users by ID. 

The special method __getitem__ is used to implement the [] operator. This allows us to access users by ID using the following syntax: users[user_id]. The difference between __getitem__ and def get(self, user_id: str) is that __getitem__ is called when we use the [] operator, while get is called when we use the get() method. 

The special method __repr__ is used to implement the repr() function. This allows us to print the object using the following syntax: print(user). The difference between __repr__ and def __str__(self) is that __repr__ is used for debugging, while __str__ is used for displaying the object to the user.



