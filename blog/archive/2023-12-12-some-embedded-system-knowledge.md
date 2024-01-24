---
layout: post
title: Embedded System Knowledge
date: 2023-12-11 19:35:00-0400
tags: embedded-system 
categories: embedded-system
giscus_comments: true
---
# UART 

# Hardware communication protocols 


| Feature/Protocol   | I2C (Inter-Integrated Circuit) | SPI (Serial Peripheral Interface) | UART (Universal Asynchronous Receiver/Transmitter) | USART (Universal Synchronous/Asynchronous Receiver/Transmitter) | CAN bus (Controller Area Network) |
|--------------------|-------------------------------|-----------------------------------|---------------------------------------------------|----------------------------------------------------------------|-----------------------------------|
| **Basic Function** | A multi-master, multi-slave, packet switched, single-ended, serial computer bus. | A synchronous serial communication interface specification used for short-distance communication. | A serial communication protocol for asynchronous serial data communication. | A communication protocol that can be configured in either asynchronous or synchronous mode. | A robust vehicle bus standard designed to allow microcontrollers and devices to communicate with each other's applications without a host computer. |
| **Data Transfer Speed** | Relatively slow (standard modes up to 400 Kbps, high-speed mode up to 3.4 Mbps). | Faster than I2C (up to tens of Mbps). | Lower speed compared to SPI and I2C (typical baud rates range from 9600 to 115200 bps). | Flexible, supports both UART speeds and higher synchronous speeds. | Moderate (up to 1 Mbps for shorter distances). |
| **Complexity** | Moderate (requires addressing, arbitration, and error checking). | Simple (but requires more I/O lines for multiple devices). | Simple (uses two wires for full-duplex communication). | More complex (combines features of UART with synchronous capabilities). | More complex due to robust error detection and handling features. |
| **Number of Devices Supported** | Supports multiple devices on the same bus (multi-master, multi-slave). | Supports multiple devices but requires additional lines per device (not suitable for very large networks). | Point-to-point communication between two devices. | Similar to UART but with additional synchronous mode capabilities. | Designed for large networks (up to 120 nodes). |
| **Typical Use Cases** | Used in embedded systems for sensor integration, RTC, EEPROM. | Commonly used for short-distance, high-speed communication in embedded systems. | Used in serial communication for PCs, sensors, and low-speed data transfer. | Used in applications that require both types of serial communication. | Primarily used in automotive applications for connecting sensors, actuators, and control units. |


## How these protocols work

| Protocol         | How It Works in Simple Terms                                                                                                                                                   |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **I2C (Inter-Integrated Circuit)** | Uses two wires (SCL for clock, SDA for data). Devices on the bus have addresses. When a device wants to talk, it uses the clock line to signal and sends/receives data on the data line. |
| **SPI (Serial Peripheral Interface)** | Uses at least three wires - one for the clock (SCK), one for master to slave data (MOSI), and one for slave to master data (MISO). A separate select line is used for each slave device. |
| **UART (Universal Asynchronous Receiver/Transmitter)** | Uses two wires for data transmission (TX for transmitting, RX for receiving). Data is sent in a serial form, one bit at a time, without a clock signal to synchronize.                       |
| **USART (Universal Synchronous/Asynchronous Receiver/Transmitter)** | Works like UART but can also operate in a synchronous mode where data and clock signals are synchronized.                                                                                  |
| **CAN bus (Controller Area Network)** | Uses a two-wire bus (CAN_H and CAN_L) for communication. Devices on the network can send messages when the bus is free. Uses a priority system to manage conflicts when two devices transmit at the same time.   |

