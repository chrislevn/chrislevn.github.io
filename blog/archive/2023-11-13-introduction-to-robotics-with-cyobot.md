---
layout: post
title: Deep dive into robotics with Cyobot
date: 2023-11-28 19:35:00-0400
description: 
tags: database
categories: backend
giscus_comments: true
featured: false
related_posts: true
---

Hey guys, it 

## Microcontrollers
Microcontrollers are small computers that are used to control other devices. They are used in a wide range of applications, including robotics, home automation, and industrial automation. They are also used in a wide range of industries, including automotive, aerospace, and medical. They are great for specific tasks that require a lot of processing power, but they are not good for general purpose computing.

Usually in a microcontroller, there are 3 main components: CPU, memory and I/O peripherals. 

- CPU is the brain of the microcontroller. It is responsible for executing instructions and performing calculations.
- Memory is used to store data and instructions. There are 2 main types of memory: RAM and ROM. RAM is used to store data and instructions temporarily. ROM is used to store data and instructions permanently.
- I/O peripherals -- The input and output devices are the interface for the processor to the outside world. The input ports receive information and send it to the processor in the form of binary data. The processor receives that data and sends the necessary instructions to output devices that execute tasks external to the microcontroller.


## What is Cyobot?
![Mircocontroller](https://images.ctfassets.net/2lpsze4g694w/4jQGyUQTjMglSA7GjGvGPa/10949b5cd522330327e7d9917589c1f9/PICO_BOARD_TOP_WHITE.jpg?w=800)

CYOBot is the companion that guides students through different skill levels and interests within the STEAM fields through personalized and interactive learning activities. Their latest product is CYOCrawler, a 4-legged robot that can be programmed to walk, dance, or anything you can program it to do.

## CYOCrawler
![Cyobot](../assets/img/cyobot/cyocrawler.png)

Let's talk about how to create CYOCrawler from scratch: 

Imagine you are





CYO

- ESP32 Wi-Fi & Bluetooth MCU: 
    - a popular WiFi and Bluetooth module based on the ESP32 chip.
- PCA9685 providing 12-channel servo controller
    - 
- LSM6D IMU
- Onboard speaker with MAX98357
- Onboard microphone with MAX9814
- 33-NeoPixel-LED matrix and 12-NeoPixel-LED ring
- Micro SD card reader
- USC C battery charger and smart charging/discharging system
- Extension block with power, I2C, SPI, UART, GPIO