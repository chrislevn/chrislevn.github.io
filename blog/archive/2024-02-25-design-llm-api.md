---
layout: post
title: Design LLM API
date: 2024-02-25 19:35:00-0400
description: 
tags: languages python algorithms backend
categories: backend
giscus_comments: true
featured: true
related_posts: true
---

LLM and AI are very hot topics right now. As someone who is interested in backend, data engineering, and AI, I want to combine them all into one project. The other day I saw a cool product called ChatPDF, a platform where you can chat with your documents. As I reseach about this product, I learned that they used a technique called Retriver-Augumented Generation (RAG) to generate the response. 

Like how humans find answers in document by scanning and skimming, RAG does the same thing. It splits the document into chunks and store them as embeddings in a vector database. When user asks a question, the question will be converted into an embedding and compare with the embeddings in the vector database. The most similar embeddings will be retrieved and used to generate the response along with the LLM model. 


Today I want to make a project that tick 2 checkboxes: RAG and data engineering. I want to create something similar to ChatPDF but more like a note. User can take notes of what they have learned. They can ask questions from their notes and see the history of their AI responses. 

## Understand the requirements
### Functional requirements

There are a few main functionalities that the system should provide.
- Client side: 
    - User can take notes and save them. 
    - User can ask questions from their notes. 
    - User can see the history of their AI responses.
- Server side:
    - The server should be able to store user's notes.
    - The server should be able to retrieve user's notes.
    - The server should be able to retrieve the most similar notes to the user's question.
    - The server should be able to generate the response from the most similar notes and the LLM model.

- GET: 

### Non-functional requirements
