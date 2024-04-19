---
layout: post
title: System design thoughts on building a low-cost scalable backend
date: 2024-02-17 19:35:00-0400
description: 
tags: languages python algorithms backend
categories: backend
giscus_comments: true
featured: true
related_posts: true
---

If you haven't, check out my previous post on [My thought process of building end-to-end low-cost backend](https://christopherle.com/blog/2024/thought-process-project/). Today's post will go more in depth on the system design aspect of building a low-cost scalable backend.

This post comes from real experience as I already built this backend. I also learned what works and what doesn't work for me. FYI, I'm not a system design expert. I am a junior software engineer who is eager to learn and share my thoughts.

But if I have to approach this in a system design interview, here's how I would do it: 
1. Understand the requirements
2. Back of the envelope estimation
3. High-level design
4. Detailed design

## Understand the requirements
### Functional requirements
Functional requirements are what are the functionalities that the system should provide. For my backend for example, I need to be able to:
- Send emails to subscribed users a new challenge every week. 

This is the big question given from the interviewer/manager. How can we break this down into smaller pieces? Go from WHO to HOW
- Who are the users? Users who bought the product and subscribed to the weekly challenge email. 
- How the users will use this system? This comes with smaller questions: 
    - How do users subscribe to the weekly challenge email? -> assumption in this case Shopify already have this a product and we can retrive the list of subscribed users from Shopify API. 
    - How do we send the weekly challenge email? -> In this case, I use AWS SES with Github Actions as cron jobs since they are more cost-effective.
    - How do we know what challenge to send to what users? -> In this case, I will confirm with the interviwer/manager. Assume that we will have a list of various challenges of different levels. We also need to determine user's level.
    - Okay, how do we determine user's level? -> We need to send users an inital questionaire to determine their level. 
    - Ask again, if user did their challenge, how do we know? -> We need to have a server to interact with the backend.
    - If user passed the challenge, how do we update their level? 
    - Can users see their level for progression?
    
That said, here is what I got: 
- We need to have a cron job that run a script to send the weekly challenge email to the subscribed users.
- We need a server for users to interact with the backend. Here are the possible functions and API endpoints users might have: 

    - Update user's level from the questionaire -> POST /questionaire?passed=true&user_id={user_id}
    - User see the challenge -> GET /challenges/{challenge_id}?user_id={user_id}
    - User submit the challenge -> POST /challenges/{challenge_id}?user_id={user_id}&submission=true
    - User see their level -> GET /level?user_id={user_id}

### Non-functional requirements
Non-functional requirements are the constraints that the system should satisfy. There are several non-functional requirements: 
- High availability: The system should be available 24/7.
- Fault tolerence, reliability: The system should be able to handle failure.
- Scalability: The system should be able to handle the increasing number of users. (vertical vs horizontal scaling, scalability (long-term) vs elasticity (short-term)) -> not applicable in this case since the number of users is small.
- Performance: The system should be able to handle the increasing number of requests.
- Durability: The system should be able to store data for a long time.
- Consistency: The system should be able to provide consistent data to the users. (strong consistency requires all duplicates to be updated either now or later) -> not applicable in this case since the data is not critically time-sensitive.
- Maintainability, security, cost, etc.

In this case, confirm what the company wants and what users might need. Here are my current top 3 to focus on:

#### Reliability
- Realibilty (High available + system is correct + system replies within certain expected time): Because you don't want user to click on the challenge and the server is down, or incorrect, or slow. 

Do know that most server providers nowaday have high availability and fault tolerance. The only time I saw it crashed were: 
- When I pushed a new code to the server and it crashed during deployment -> Can we serve the old version of the code while deploying the new version? Once the new version is up, can we switch to the new version without losing data? Use load balancer and server duplication for this. The cons is that it might cost more to have multiple servers.

- When the server was under DDoS attack -> Can we protect the server from DDoS attack? Use rate limiting, shuffle sharding, cell-based architecture, etc.

- Unexpected failures: 
    - Load spike: load spike is when the server is overloaded with requests. Can we protect the server from load spike? Use load shedding, rate limiting, shuffle sharding, cell-based architecture, etc.
    - Dependency failure (HTTP 424): when one action depends on another action and the other action failed. Can we protect the server from failure and performance degradation of its dependencies? Use timeouts, circuit breaker, bulkhead, retries, idempotency, etc. 
    - When something went wrong, can we quickly rollback to the previous version?

I also found more advanced SRE techniques from Google: https://sre.google/sre-book/addressing-cascading-failures/

#### Security
- Security: No matter how big or small the company is, security is always a concern. The CIA triad of security is: Confidentiality, Integrity, Availability. 
    - Confidentiality: Can we protect the user's data from unauthorized access? Use encryption, access control, etc.
    - Integrity: Can we protect the user's data from unauthorized modification? authentication, authorization, etc.
    - Availability: can authorized users access the system when they need it?

#### Cost 
- Cost: The company wants to keep the cost low. 

total cost = engineering cost + maintenance cost + resource cost. 

- Engineering cost: the cost of developing the system, usually the cost of the engineers to design, implement, test, and deploy the system.
- Maintenance cost: Can we automate the process of deployment to reduce the cost?
- Resource cost: Hardware + software cost. 


## Back of the envelope estimation



<!-- #### High availability
High availability is the success ratio of the success or the system uptime for a certain period of time. High available system should be 24/7 available but not neccessarily 100% uptime.

Questions to answer are: 
- Do I have multiple servers in different regions, zones to handle the failure? 
- If yes, do I have a way to switch from one server to anotehr without losing data? (DNS, load balancing, reverse proxy, API gateway, peer discovery, service discovery, …)
- Do I have a way to protect the system from DDoS attack? (load shedding, rate limiting, shuffle sharding, cell-based architecture, etc)
- Do I have a way to protect the system from failure and performance degradation of its dependencies? (timeouts, circuit breaker, bulkhead, retries, idempotency, …)
- Do I monitor the system to detect failure? I use Sentry for error tracking and Cloudwatch, BetterStack for monitoring (data, and server).

However, acknowledge that if you restricts too much perfomance for safety, you might lose some actual requests from users.
 -->
