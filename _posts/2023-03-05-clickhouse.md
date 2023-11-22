---
layout: post
title: Visualize your data from cloud with DoubleCloud and ClickHouse DB
date: 2023-03-05 09:56:00-0400
description: Visualize your data from cloud with DoubleCloud and ClickHouse DB
tags: cloud demo
categories: demo
giscus_comments: true
featured: false
related_posts: false
related_publications: 
---


## Visualize your data from cloud with DoubleCloud and ClickHouse DB

Today, I will introduce to you a new platform I found for integrating your Cloud provider (AWS, GCP, Azure) and visualizing the data: DoubleCloud.

![Visualization of DoubleCloud workflow](https://cdn-images-1.medium.com/max/2000/1*F7S-_NfF_4LWk14v-PbM-Q.png)

For those who don’t know, DoubleCloud is a new platform that helps you build sub-second data analytical solutions and pipelines on proven open-source technologies like ClickHouse® and Apache Kafka®.

The reason why I wrote about this tool was the same reason I found visualizing data from cloud providers automatically can be a bit hassle. Of course, there are other players in this function too like AWS QuickSight, Tableau, etc. However, I believe that this particular new tool offers unique features, and DB options, that make it worth considering for anyone who regularly works with data from cloud providers.

![DoubleCloud Logo](https://cdn-images-1.medium.com/max/3600/0*YUHFTfwuWOdphc_B.jpg)

For your inquiries:

![ClickHouse](https://cdn-images-1.medium.com/max/2800/0*n39rgloE4aHnh3B3)
>  ClickHouse is a powerful and high-performance database management system designed for real-time data processing and analysis. It was originally created by Yandex, a Russian search engine, to support their web analytics platform called Metrica.
>  Compared to other database providers, ClickHouse is an open-source software that uses a columnar data model to store and retrieve data. This means that data is stored in columns rather than rows, which allows for faster query processing and data compression.
>  ClickHouse is particularly well-suited for OLAP workloads, where complex queries are executed on large datasets. It supports SQL-like query language and allows for real-time data processing and analysis, making it ideal for applications that require fast and accurate insights from large volumes of data.

![Apache Kafka](https://cdn-images-1.medium.com/max/2000/0*FgyBIh3kI-pue7Go.png)
>  Apache Kafka is a software platform that facilitates the distributed processing of large volumes of data streams in real-time. It is an open-source system that allows companies to build high-performance data pipelines, real-time data processing systems, and streaming analytics applications at scale.
>  Apache Kafka allows users to publish, subscribe to, store, and process streams of records in real-time. It is designed to handle large volumes of data efficiently, allowing users to process data as it arrives, without the need to wait for it to be fully collected or batched.
>  One of the key benefits of Apache Kafka is its ability to handle large-scale data processing tasks across multiple nodes in a distributed environment. It provides high availability and fault tolerance, ensuring that data streams are processed consistently and reliably.

In this blog, we will use ClickHouse as our main DB connection.

## Table of content

 1. Preparing our dataset

 2. Create Cluster — Setting up DoubleCloud

 3. Transfer — Create a connection between your AWS S3 Database and ClickHouse

 4. Visualize your dataset

## Preparing our dataset

### Getting the data.

In this blog, we will use the layoff dataset from my previous [blog](https://medium.com/@locvicvn1234/analysis-of-current-layoffs-in-the-usa-with-tableau-a8b1077a16b4). You can get it [here](https://www.kaggle.com/datasets/swaptr/layoffs-2022) from Kaggle (FYI, you might need to log in to download the dataset). The dataset will be named “layoffs.csv”

![What the layoffs dataset will look like](https://cdn-images-1.medium.com/max/2000/1*3C_uxIJCNDb_SvMm6alQ8A.png)

### Uploading the dataset to AWS S3 Bucket

As of now, DoubleCloud offers connections with AWS so we will use AWS as our endpoint.

To upload your dataset to AWS S3 Bucket, you need to:

 1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

 2. In the left navigation pane, choose **Buckets**.

 3. Choose **Create bucket**.

 4. The **Create bucket** page opens.

 5. For **Bucket name**, enter a name for your bucket. For now, let’s name it **doublecloudtest**

![Create AWS S3 bucket](https://cdn-images-1.medium.com/max/2180/1*KTezo2EaR5yRwiD6t0Nz-g.png)

6. Once your bucket is created, upload your dataset “layoffs.csv” from your local computer.

![](https://cdn-images-1.medium.com/max/2000/1*jmT4AVYMjNLSSPzk-zZbXw.png)

7. The result should be like this.

![](https://cdn-images-1.medium.com/max/2594/1*1zRq14f-1ObbeA_ytZnK7Q.png)

More on creating AWS S3 Bucket from [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).

Note that, this tutorial only focuses on csv file. In real life, you might configure for the real-time database.

## Setting up DoubleCloud

 1. First, you need a Managed ClickHouse® cluster.

* To do this, create or log in to your account. Go to [console](https://auth.double.cloud/login?client_id=yc.oauth.doubleconsole&redirectUrl=https%3A%2F%2Fauth.double.cloud%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3Dyc.oauth.doubleconsole%26scope%3Dopenid%26redirect_uri%3Dhttps%253A%252F%252Fapp.double.cloud%252Fauth%252Fcallback%26state%3DzoCg90o7ZO5lqMfsOrJyGXwT7ASzFcMEr9s31ms).

* Create a Cluster with ClickHouse service. Let’s name it “doublecloud1” for now

* At this moment, DoubleCloud is supporting AWS. We will choose AWS as our data source now.

![Creating cluster with DoubleCloud](https://cdn-images-1.medium.com/max/2000/1*ZyEYkoVG4TgE4400DbgmYA.png)

* For now, we will use default settings for our tutorial. Click submit to create a cluster. Once your cluster is done, the status will be Alive.

![](https://cdn-images-1.medium.com/max/2246/1*79YwG1q5XvSFVRZymZfGtA.png)

## Create a database on the newly created cluster

 1. Install ClickHouse.

    # For MacOS
    curl https://clickhouse.com/ | sh 
    
    # For Linux
    curl https://clickhouse.com/ | sh
    sudo ./clickhouse install
    

2. Go to your Cluster detail on DoubleCloud, copy the native interface code, and run in the terminal. It should look like this:
>  clickhouse-client — host ***********************.at.double.cloud — port **** — secure — user admin — password ***************************************************************

Notice that you might change the code due to recent ClickHouse’s update.
>  ./clickhouse client — host ***********************.at.double.cloud — port **** — secure — user admin — password ***************************************************************

![Cluster detail interface](https://cdn-images-1.medium.com/max/2146/1*J_NAMvneP15HP7IfHaoUzQ.png)
>  Note that you will need to save the **user, **and **password** information elsewhere for later usage in the transfer.

3. Create a database from your terminal
>  create database [YOUR_DATABASE_NAME] on CLUSTER [DOUBLECLOUD_CLUSTER_NAME]

where:

* YOUR_DATABASE_NAME: the name you want for your database. Let’s do it Sample-ClickHouse-DB for now

* DOUBLECLOUD_CLUSTER_NAME: The name of your DoubleCloud cluster, which is “TestCluster” for now.

## Create a connection between your AWS S3 Database and ClickHouse

 1. Go to **Transfer**.

 2. Go to **Endpoints.**

### For source:

 1. Click **Create endpoint**, choose **Source**

 2. Choose **AWS S3** as your source

 3. Choose a name of your choice. For now, let’s name it **s3-source-quickstart**

 4. Configure your endpoint parameters:

* Dataset is **layoffs**

* path pattern is ***csv**

![](https://cdn-images-1.medium.com/max/2000/1*5yl2zfenjgInxjmN_sXNzA.png)

5. In the **S3: Amazon Web Services**, enter your bucket name, AWS Access Key ID, and AWS Secret Access Key.

6. Submit.

![](https://cdn-images-1.medium.com/max/2000/1*ofJWRQXWHQ68U2XhL8EQcg.png)

### To get your AWS access key ID and secret access key

 1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

 2. On the navigation menu, choose **Users**.

 3. Choose your IAM user name (not the check box).

 4. Open the **Security credentials** tab, and then choose **Create access key**.

 5. To see the new access key, choose **Show**. Your credentials resemble the following:

* Access key ID: AKIAIOSFODNN7EXAMPLE

* Secret access key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

6. To download the key pair, choose **Download .csv file**. Store the .csv file with keys in a secure location.

### For target

 1. Click **Create endpoint**, choose **Target**

 2. Choose **ClickHouse** as your target

 3. Choose a name of your choice. For now, let’s name it **clickhouse-target-quickstart**

 4. Configure your endpoint parameters:

* Database is **Sample-ClickHouse-DB**

* Pass your user and password from your Cluster information.

![](https://cdn-images-1.medium.com/max/2000/1*sdhUtfZWExJVMO_yjGiVaA.png)

6. Leave the rest for the default settings.

7. Submit.

### Test the connection

Once source and target endpoints are created, go back to the transfers tab and choose **Activate.**

![](https://cdn-images-1.medium.com/max/2170/1*QnTNVVjiAUGqDc9mmcX6xQ.png)

If the status is **Done**, the connection is successful.

If the status is **Error** with the red color, click on the Error, then **Logs**, to see the error message. Usually, double-check if you already entered all the correct credentials from ClickHouse and AWS.

## Visualize your dataset

 1. Go to **Visualization**.

 2. Create a new **workbook**. Let’s name it Demo Workbook.

 3. Create a new **connection**. Choose **ClickHouse.** The interface will ask for Hostname, Username and Password.

4. Go to your cluster from Clusters, and go to **Hosts** to obtain host information

![](https://cdn-images-1.medium.com/max/2116/1*uUUdIhTNY7buxLO6JRdu_Q.png)

5. Copy host, username, and password in the Connection.

![](https://cdn-images-1.medium.com/max/2000/1*c9i16hS1Xjg1ZmuEsqCF3Q.png)

5. **Check connection**. If there is a green tick then **Create connection.**

6. Create dataset. Select the layoffs dataset.

You might see the column is combined as a string instead of separate columns.

![](https://cdn-images-1.medium.com/max/2000/1*2FUvjYr0AvgMPAjgp3DTcA.png)

While this is a small issue, to handle this, we create a new **field**. Let's name it the **company** for example. There, we split the combined string with “,” and select the first index returned from the split array, which is the company name. Choose **formula**, then enter this below

    SPLIT([company,location,industry,total_laid_off,percentage_laid_off,date,stage,country,funds_raised], ",", 1)

![After spliting company name, the result will be like this](https://cdn-images-1.medium.com/max/2000/1*QgXt-H-y_EJ9fuRrpNMQ4A.png)

Click **save**. Do the same for other columns you want to add. Remember to change to the corresponding type (string, integer, fractional number, etc).

For now, let’s create 2 new fields with **industry (index 3)**, and **total_laid_off (index 4)** for simple visualization.

    // industry
    SPLIT([company,location,industry,total_laid_off,percentage_laid_off,date,stage,country,funds_raised], ",", 3)
    
    // total_laid_off
    SPLIT([company,location,industry,total_laid_off,percentage_laid_off,date,stage,country,funds_raised], ",", 4)

7. Once the database preparation is done, click **create chart**

8. Drop **total_laid_off in Y**, and **industry in X.** The result will be as below.

![](https://cdn-images-1.medium.com/max/3548/1*E9b949iDj6MaD5gaL1v9ww.png)

## Conclusion

If you reach this far, congratulations! You just learned to visualize your data from the cloud provider (AWS S3) with DoubleCloud and ClickHouse.

My thought on this new platform is that it is very simple to use: the visualization tool with drag and drop reminds me of Tableau. Meanwhile, the simple experience to connect with data from a cloud provider with no code is impressive. Really looking forward to seeing how DoubleCloud goes in the future with more Cloud options from GCP and Azure.

## References

 <iframe src="https://medium.com/media/e72cf162a23a457b10900eea98aa9093" frameborder=0></iframe>

* AWS S3 Documentation

* AWS IAM Documentation

* DoubleCloud Documentation

* ClickHouse Documentation
