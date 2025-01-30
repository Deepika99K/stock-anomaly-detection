# Stock Anomaly Detection  
This is the final content after merging conflicts.

# 📈 Stock Anomaly Detection Pipeline 🚀

A real-time stock anomaly detection pipeline using **Kafka, Spark, and Pandas**.

## 📌 Features
- ✅ **Real-time stock data streaming** with Kafka
- 🔥 **Processing and anomaly detection** using Spark
- 📊 **Data visualization** with Pandas
- 🛠 **End-to-end data pipeline setup**

## 🛠 Installation
```sh
git clone https://github.com/Deepika99K/stock-anomaly-detection.git
cd stock-anomaly-detection
pip install -r requirements.txt


This project builds a real-time stock anomaly detection pipeline using:
- **Kafka** for real-time data streaming
- **Spark** for data processing
- **Pandas** for data analysis
- **YFinance** to fetch stock market data

## 🚀 Features:
- Real-time stock price ingestion via Kafka
- Spark-based anomaly detection and moving average calculation
- Data storage for further analysis

## 🛠️ Tech Stack:
- **Kafka** (Producer & Consumer)
- **Apache Spark**
- **Pandas**
- **Python**
- **YFinance**
- **Hadoop (winutils.exe for Windows)**

## 🏃 How to Run:
1. Start Kafka & Zookeeper:
zookeeper-server-start.bat config/zookeeper.properties kafka-server-start.bat config/server.properties
2. Run Kafka Producer:
python kafka/stock_producer.py
3. Run Kafka Consumer:
python kafka/stock_consumer.py
4. Process Data with Spark:
python spark/process_stock_data.py


## 📌 Author
- **Deepika Kolluru**
- [LinkedIn](https://www.linkedin.com/in/deepika-kolluru/)
>>>>>>> 2e0ac69 (🚀 Cleaned nested Git repo and finalized project)
