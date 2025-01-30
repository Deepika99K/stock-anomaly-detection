from confluent_kafka import Producer
import json
import yfinance as yf
import time

# Kafka configuration
conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

def delivery_report(err, msg):
    """Callback for message delivery reports"""
    if err is not None:
        print(f"❌ Message delivery failed: {err}")
    else:
        print(f"✅ Message delivered to {msg.topic()} [{msg.partition()}]")

def stream_stock_data(ticker="AAPL"):
    while True:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d", interval="1m").tail(1).to_dict(orient='records')[0]

        # Convert to JSON and send to Kafka
        message = json.dumps(data)
        producer.produce('stock_prices', message.encode('utf-8'), callback=delivery_report)
        producer.flush()

        print(f"Sent: {message}")
        time.sleep(60)  # Stream every 60 seconds

if __name__ == "__main__":
    stream_stock_data()
