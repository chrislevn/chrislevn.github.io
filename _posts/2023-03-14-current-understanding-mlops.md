---
layout: post
title: My current understanding of MLOps workflow
date: 2023-07-21 09:56:00-0400
description: 
tags: mlops
categories: AI
giscus_comments: true
featured: false
related_posts: false
related_publications: 
---

## My current understanding of MLOps workflow

This series will be about how to deploy your AI model from A to Z. Everything is based on my current understanding and learning of Machine Learning, Cloud engineering, and Full-stack development.

**Why I created this blog?**

As one of the ML self-taught, I have created many Machine Learning models that don’t have an API out there yet. However, none went to production. In spite of the non-technical challenges, it is hard for a data scientist to scale their Machine Learning model without the help of an ML Engineer/Software Engineer/DevOps Engineer (read more [here](https://towardsdatascience.com/why-90-percent-of-all-machine-learning-models-never-make-it-into-production-ce7e250d5a4a)). This whole workflow of deploying ML models lay in the category of MLOps (Machine Learning Operations). That’s why I was inspired to write this blog series. My main goal is to find a deployment workflow that is scaleable and easy. In the end, I hope data scientists can worry less about scaling and focus on improving the accuracy of their models.

Note that this first blog is an introduction so there will be no coding tutorial.

**Who is this blog for?**

* Machine Learning practitioners/Data scientists who would like to test their ideas in production.

However, this blog is not for a big production or if you prefer on-premise over Cloud workflow. One of the reasons I can think of when using on-premise over Cloud workflow is having sensitive data that some companies are hesitant to store on the Cloud. Another is the lack of full control in response to the convenience of easier deployment.

## **MLOps workflow**

![My current simple understanding of MLOPs workflow](https://cdn-images-1.medium.com/max/2000/1*fyda87Cy6_OZIrgK3jmHEQ.png)

 1. **Get data**

There are many ways to store your data. While on-premise has advantages over control and security, Cloud Data Storage such as GCP, AWS, Azure, and MongoDB offers data storage and infrastructures that you don’t have to worry about maintaining.

Remember that you might need data version control to keep track of changes in the dataset. Read more about data version control with DVC from this [blog](https://medium.com/geekculture/data-version-control-dvc-with-google-cloud-storage-and-python-for-ml-fe99dc7d338).

![*Data management middleware from dvc.org*](https://cdn-images-1.medium.com/max/2000/0*k_33-imUwWHZhv2G.png)

**2. Visualize data**

You can also easily visualize your current data on the Cloud with tools such as BigQuery from GCP, AWS QuickSight, or the Double Cloud (check my previous [post](https://medium.com/@locvicvn1234/visualize-your-data-with-doublecloud-and-clickhouse-db-8713796389ab?postPublishedType=repub)). No need to constantly download and visualize new data.

![Unsplash: data visualization example](https://cdn-images-1.medium.com/max/2000/0*Vo3Rk9uez8kYYAv_)

**3. Pre-processing/Clean data**

Sometimes, data can come in raw like an image, text, sound, video file or as a table (.csv, excel). It’s your job to make these raw data processable for the model that you built.

Sometimes, inputting these data can take a ton of time, considering there are many users for your app or the size of the data. Instead of having your notebook doing everything, one way to optimize this process is to have your cleaning process on Cloud using tools such as Vertex AI from GCP. The Cloud will take in your input file and return your processed input.

![Vertex AI logo](https://cdn-images-1.medium.com/max/2000/0*7WtZCEjTqBAXtN1V.png)

4. Training model

Lastly, training a new model, whether it’s completely new or pre-trained, can take lots of time. Having your model trained on Cloud providers will reduce the training time as well as infrastructure maintenance from your side. There are many tools for this step such as IBM Watson Studio, Databricks Lakehouse, GCP Vertex AI, etc.

5. Deploying your model

Deploying the model is also crucial so that others can make use of and test your model. This post series will focus on making your model an API. If you would like to learn how to have a front end to test your API, consider tools such as [Streamlit](https://streamlit.io/).

![Sample Streamlit app from streamli.io](https://cdn-images-1.medium.com/max/2000/0*dVTeOo1i6Q1zY4NN.png)

From this step, every time you get new data, it can be added for visualization, processed, and tested on the deployed model.

6. Model monitor

Finally, model monitoring with tools such as [Vertex AI](https://cloud.google.com/vertex-ai/docs/model-monitoring) is the essential step to check the accuracy of your model. It also involves of CI/CD to take in new data to be retrained and deployed on a new model.

This is my first post on MLOps. I understand there will be a lot of things I don’t know yet so please give me any feedback. While these steps might sound a lot and vague now, I aim to make the whole process visualized and easier.

Until then, take care! See you in the next blog post on how to deploy your ML model.
