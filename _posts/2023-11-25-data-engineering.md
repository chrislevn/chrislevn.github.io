---
layout: post
title: Data Engineering
date: 2023-11-25 18:35:00-0400
description: Data Engineering
tags: dataengineering security
categories: tech notes
giscus_comments: true
featured: false
related_posts: false
related_publications:
---

<details close>
<summary>Motivation</summary>
A collections of notes on papers, tech talks and articles that I’ve found interesting.

My goal is to extract the ideas I found particularly interesting so I can connect them all together into a bigger picture. 
</details>

# Content

1. What I learned after one year of building a Data Platform from scratch - Jeremy [Medium](https://medium.com/@jeremysrgt/what-i-learned-after-one-year-of-building-a-data-platform-from-scratch-d7075629cab1)

Jeremy shared his view on building data platform. Some of the key takeaways are: 
- KISS (Keep It Simple and Stupid at first, then improve if needed) as the things you provision for scaling might never need to scale.
- Don’t forget the security of your infrastructure. These basics can be: 
    - Never expose a database or your warehouse to the internet
    - Use encryption at rest and in transit whenever possible
    - Use a secret manager such as AWS Secret Manager to securely deal with token, and database password
    - Do not expose the ssh port of your instance to the internet

- Logging: Don’t forget basic logging. It will prevent you from scratching your head over the table because you can’t have a proper stack trace of errors
- Slack is a perfect place to start for alerting (I did this during my DevOps internship)
- Data culture is important
- Data quality is important. 
