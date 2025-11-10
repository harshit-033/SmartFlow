<div align="center">

# 🚦 **SmartFlow**

### _AI-Powered Intelligent Traffic Management System_

![SmartFlow Logo](https://dummyimage.com/600x160/0b0c10/66fcf1&text=SmartFlow+%7C+AI+Traffic+Management)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Framework-YOLOv8L-red.svg?logo=yolo&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-4.x-green.svg?logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/github/license/YourUser/SmartFlow?color=lightgrey" />
  <img src="https://img.shields.io/github/stars/YourUser/SmartFlow?style=social" />
</p>

> 🚗 **SmartFlow** is a computer vision-based intelligent traffic management system that detects, classifies, and analyzes vehicle flow in real time to optimize traffic efficiency and reduce congestion.

</div>

---

## 🔍 Project Overview

SmartFlow leverages **Deep Learning (YOLOv8)** and **Computer Vision (OpenCV)** to detect vehicles from real-time traffic footage.  
The system computes **lane-wise density**, transmits live data via APIs, and is designed to power **adaptive traffic signals** in the future.

---

## 🧠 Dataset & Model Training

📸 **Dataset Summary:**
- **Total images:** 8105  
  - 📂 6484 for training  
  - 📁 1621 for validation/testing  

🎯 **Classes Detected:**  
🚗 Cars 🚌 Buses 🏍️ Motorbikes 🚛 Trucks 🚐 Vans 🚲 Bicycles 🛺 Rickshaws  

💻 **Technical Details**

| Parameter | Value |
|------------|--------|
| **Framework** | Ultralytics YOLOv8L |
| **GPU Used** | NVIDIA GeForce RTX 3050 (6 GB) |
| **Training Duration** | ~2 Days |
| **mAP50 (Cars)** | 0.753 |
| **Overall mAP50–95** | 0.576 |
| **Inference Speed** | ⚡ 0.3 ms preprocess \| 40.4 ms per image |

---

## ⚙️ Real-Time Inference System

Developed a **real-time detection and analytics system** using:
- 🧩 **OpenCV + Python Multithreading** for parallel frame processing  
- 🌐 **Backend API Integration** for seamless data flow  
- 📊 **Optimized visualization** for lane density & traffic metrics  

The result is **low-latency**, **high-speed** detection ideal for smart city applications.

---

## 🔄 Workflow

```mermaid
flowchart LR
A[📷 Traffic Camera Feed] --> B[🧠 YOLOv8 Detection]
B --> C[📈 Lane-wise Vehicle Count]
C --> D[🌐 API Data Transmission]
D --> E[📊 Dashboard Visualization]
E --> F[🚦 Adaptive Signal Optimization]
