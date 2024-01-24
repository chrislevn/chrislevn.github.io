---
layout: post
title: Is serverless for you?
date: 2023-11-29 19:35:00-0400
description: 
tags: serverless
categories: devops
giscus_comments: true
featured: true
related_posts: true
---
[[paper](https://faculty.washington.edu/wlloyd/courses/tcss562/talks/ServerlessComputing-DesignImplementationandPerformance.pdf)][[video](https://www.youtube.com/watch?v=W_VV2Fx32_Y&ab_channel=Fireship)]

Let's talk about serverless today. We all know that the big names in cloud (GCP, AWS, Azure) all have their own serverless offerings (Cloud Functions, Lambda, Functions). While it sounds great with "pay as you go" and autoscale, is it really for you? Let's find out.

As always, we will consider these 3 factors: cost, performance, and availability. 

## What is serverless?
[[Website](https://www.datadoghq.com/knowledge-center/serverless-architecture/#:~:text=Serverless%20architecture%20is%20an%20approach,storage%20systems%20at%20any%20scale.)]

Let's say there is this guy Steve. Steve wants to build a website. He has a few options:
1. Buy a server and host it himself
2. Buy a server and host it on the cloud
3. Use serverless

With option 1, Steve has to buy a server and host it himself. This is the most expensive option. This includes: server, electricity, cooling, data warehouse, etc. This is the past as now companies are moving to the cloud.

With option 2, Steve has to buy a server and host it on the cloud. Cloud handles hosting. Although he has to manage scaling, logging, monitoring, etc. This is a cheaper option. This is what most companies are doing now.

With option 3, Steve doesn't have to buy a server: serverless. He just has to pay for the service. This is the cheapest option. All he has to do is be a good code monkey and make money as it will cost more to autoscale when there are more users for his service.

However, serverless does not mean there is no server. There is still a server. It's just that the server is managed by the cloud provider. Let's talk about how it works:

### Serverless architecture



###








## 