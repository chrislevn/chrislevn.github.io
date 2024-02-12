---
layout: post
date: 2024-01-24 07:59:00-0400
inline: true
related_posts: false
---

While Go, Rust, and JS are more popular or performance-wise for web servers, if I have to use Python only (since it is also popular for data science), here are what I am using already for almost any needs: 



General - Build a general website: 

- Web development: Django (+ HTML, CSS).

- Backend: SQL + sqlite3, or NoSQL (ex, DynamoDB with boto3).

- API:  Flask or FastAPI and load testing with Locust.

- Testing & Logging: PyTest and Logging.

From here, you can already deploy on hosting services (Vercel, Render, Heroku). 



Build for scale:

- DevOps:  Docker.

- Security: PyJWT, OAuth.

- CI/CD: Github Actions or Azure DevOps.

- Monitoring: Grafana + Prometheus for Python, add Alerting provisioning HTTP API to handle SRE automation. 

- Packaging: PyPi, pip.

- Cache: functools or redis. 

At this stage (with good finance), considering choosing Kubernetes, or Cloud providers (AWS/GCP/Azure) to meet SLOs. 



Language optimization: 

- Performance: Numba (JIT), Cython, PyPy, multiprocessing, consider list comprehension or numpy. 

- Profiling: CProfile with SnakeViz

- Code analyzer: Pylint



It's worth noting that Python comes with a Global Interpreter Lock and is dynamically typed, which may lead to slower performance compared to Object-Oriented Programming (OOP) languages. Achieving further optimization would require considering the architecture of your software, system, and algorithms. However, if you find Python more convenient for development and are constrained by time to learn another language, achieving your goals is still possible.



Will post more about my learning.

#python #programming #devops