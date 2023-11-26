---
layout: post
title: Analysis of Current Layoffs in the USA with Tableau
date: 2022-11-21 10:56:00-0400
description: 
tags: tableau analytics
categories: AI
giscus_comments: true
featured: false
related_posts: false
related_publications: 
---

## Analysis of Current Layoffs in the USA with Tableau

When you thought the pandemic was over, the year 2022 hit with a recession with most tech giants doing layoffs. Today’s post will be some of the insights I gained when doing personal exploratory data analysis on the tech layoff dataset. This analysis aims to have some insights into the current layoff situation and market. Therefore, we can somehow learn the cause, and what to prepare for in the future.

Most of the visualizations are done by Tableau with data taken from [Kaggle](https://www.kaggle.com/datasets/swaptr/layoffs-2022), updated on Nov 21, 2022. These visualizations will be backed up with personal assumptions. Note that these personal observations came from my self-learning with Tableau. Please make any necessary suggestions if you think these can be improved.

First, let’s look at the tech industries that were laid off in 2022. We can see the top three were retail, consumer, and transportation. I assumed that with the ongoing recession, people were more aware of controlling their consumption and transportation. Not to mention, the pandemic with remote work has motivated people to stay at home more often.

![](https://cdn-images-1.medium.com/max/4184/1*hCHuS5Wr9QTvpNSTxdzaiQ.png)

Compared to previous years, when you look at the year 2020 when the pandemic first happened, the top laid-off industries were transportation, travel, and finance. In 2021, these industries tended to have fewer layoffs. I assumed that people got used to the pandemic in 2021 and companies started to bounce back.

![](https://cdn-images-1.medium.com/max/4140/1*Dpo_BcpHVLk2kEuq0ffRbA.png)

Let’s have a look at the monthly trend from 2020 to 2022 to see what happened.

![Retail and consumer are the top 2 industries with the most laid-offs in 2022](https://cdn-images-1.medium.com/max/3324/1*wHIbmy1qzQCbf-LnJIou1g.png)

Those companies that laid off the most in 2022 were those at the IPO stage, followed by unknown, series C, and series B.

![](https://cdn-images-1.medium.com/max/4184/1*wUDUxieoXSSYL2JKZ84hYg.png)

Most laid-offs happened in the cities, especially in the West (SF Bay Area, Seattle, Los Angles). This contributes to the fact that most tech companies are located in the West.

![](https://cdn-images-1.medium.com/max/4184/1*cbZwcCDqmktRMvRSwE-fsw.png)

Undoubtedly, the top layoffs came from Meta and Amazon with 11,000 and 10,000 layoffs this year.

![](https://cdn-images-1.medium.com/max/4120/1*6R20lPdW3Fw-0k8AjQ4-Cw.png)

In terms of the funding raised in 2022, the media industry was the highest with a low laid-off value, with the major of funding being for Netflix. My assumption was that with the current pandemic, more and more people stayed at home and spent more time on movies, and streaming services.

![](https://cdn-images-1.medium.com/max/4184/1*KVc145_etG6COGrtbWWndA.png)

Let’s put funds raised and total laid-off in 2022 on a scatterplot to see their relationship. We can generally see that until Meta with a total fund raised of 26,000 million dollars, the higher the fund raised, the more company will lay off. After 26,000 million USD, it was hard to tell the relationship between funds raised and total laid-off.

![](https://cdn-images-1.medium.com/max/2824/1*fexfq15dN5s5MudlDxqkAg.png)

What I did, in addition, was to add clustering and averaging line with 95% CI to see the trend. The resulting trend was below. While it was hard to make sense of these groups (only the future will tell), I will leave this part for the readers to do a self-assessment.

![](https://cdn-images-1.medium.com/max/2360/1*5XTpdnWNiIhcZ_mPXbs8zA.png)

## What I learned from the recession

Remember last year, there were so many LinkedIn posts of people getting six-figure new grad offers from big tech companies. I assume that these companies were aiming for a come-back after the pandemic, therefore hiring as many engineers as possible to prepare for post-pandemic growth. However, that growth did not come with the unexpected recession. One of the best ways companies can right now survive is: to lay off people and focus on areas that show growth.

With the massive layoffs from big tech, smaller companies will have more chances to attract talents with affordable costs, especially those who are under visa restriction. In other words, new grads in 2022 (and maybe 2023) will be likely to face great competition to get a job in tech.

What I observed was that the world somehow always comes back to its balance and nothing is stable forever. The year 2021 came with massive tech hiring with tremendously high salaries and great visa support in STEM majors. This made more people want a career in tech. Therefore, finding and keeping a tech career is no longer easy. With more and more people learning coding interview techniques to get to companies, getting to top companies is no longer something impossible. Certainly, it is not easy to get there.

What one can do is practice coding interviews frequently to prepare for any unexpected. After all, you cannot control external factors; You cannot predict the future nor you cannot change the past. It matters how would you react to the current situation.

**So what can you do now?**

* Control your budget, spending, and saving to prepare for what is coming next.

* Do your best at your current job to prevent being laid off. Also, remember to showcase your work/performance.

* However, practice coding interviews to prepare for a job search in case the uncontrollable happens.

* Review what you actually want (job with high salary, job that you like, or take some gap year for mental break, etc)

* Pick the jobs/industries/companies that are recession-proof. One way, in my opinion, is to see Maslow and the supply chain. What people always need first are physical and safety needs, meaning that you should pick the tech industries that are related to those categories. They may not give you a huge package but should you have some job security in mind first. Again, company research is needed.

![Maslow and the supply chain](https://cdn-images-1.medium.com/max/2000/0*vL9x1MTy0fI7Rd-O)

## Final thoughts

Let’s be honest. Job search is not easy. I remember last year, even before the recession, I found my first internship after +150 rejections. Although the recession may seem pretty bad for the tech job market now, especially for those under visa restrictions, it is also a good time for one to reflect on their values, practice coding interviews, control their budget wisely, or even spend more time with their loved ones. I do believe that at the end of the road, there will be a way. Keep looking! You got this!
