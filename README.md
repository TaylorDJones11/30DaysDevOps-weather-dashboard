# ☁️ Weather Data Collection System - DevOps Challenge - Day 1 🌍  

## **Day 1: Building a Weather Data Collection System Using AWS S3 and OpenWeather API**  

This project is a **Weather Data Collection System** that demonstrates **core DevOps principles** while extending functionality with a **frontend dashboard** to visualize stored weather data. It integrates:  

- **External API Integration** (OpenWeather API)  
- **Cloud Storage** (AWS S3)  
- **Version Control** (Git & GitHub Actions)  
- **Serverless Backend** (AWS Lambda)  
- **Dynamic Frontend** (JavaScript-based UI)

## 👩🏽‍💻 Blog

- [Day 1](https://dev.to/onetayjones/day-1-of-my-30-day-devops-challenge-building-a-cloud-powered-weather-dashboard-3h55) 


## 🚀 Features  

### **Backend (Weather Data Collection)**  
✔️ Fetches **real-time weather data** for multiple cities  
✔️ Retrieves **temperature (°F), humidity, and weather conditions**  
✔️ Automatically stores weather data as **JSON files in AWS S3**  
✔️ Supports **multiple cities tracking**  
✔️ **Timestamps** all data for historical tracking  

### **Frontend (Weather Dashboard Extension)**  
✔️ Fetches **stored weather reports from S3**  
✔️ Displays **historical weather data** dynamically  
✔️ Built with **HTML, CSS, and JavaScript**  
✔️ Uses **API Gateway to retrieve S3 data securely** 

## **📡 Technical Architecture**  

| Component         | Technology Used |
|------------------|----------------|
| **Backend Language** | Python 3.x |
| **Frontend Language** | HTML, CSS, JavaScript |
| **Cloud Provider** | AWS (S3, Lambda) |
| **External API** | OpenWeather API |
| **Infrastructure as Code** | AWS Serverless Application Model (SAM) |
| **Version Control** | Git & GitHub Actions |
| **Dependencies** | `boto3`, `python-dotenv`, `requests` |

---

## 🌍 Deployment Workflow

### **1️⃣ Fetching & Storing Weather Data**  
- Uses `requests` to fetch real-time data from **OpenWeather API**.  
- Saves weather data as **JSON files** in an **AWS S3 bucket** for storage.  

### **2️⃣ Retrieving & Listing Weather Data from S3**  
- The **frontend fetches stored weather reports directly from S3** using **public S3 URLs** or **pre-signed URLs** (if the bucket is private).  
- JSON weather data is retrieved and displayed dynamically on the website.  

### **3️⃣ Frontend (Weather Dashboard)**  
- Fetches **stored weather reports from the S3 bucket**.  
- Displays **historical weather data dynamically** using JavaScript.  
- Supports **real-time updates** by fetching the latest stored files.  

### **4️⃣ CI/CD Automation**  
- **Backend:** GitHub Actions automates the deployment of the weather data collection system.  
- **Frontend:** GitHub Actions updates the S3-hosted website and invalidates the CloudFront cache to ensure the latest weather data is visible.   
