from confluent_kafka import Consumer, KafkaException
import json
import pandas as pd

# Kafka Consumer Configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'stock-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['stock_prices'])

print("✅ Kafka Consumer is listening for stock data...")

try:
    while True:
        msg = consumer.poll(1.0)  # Wait for message
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        # Deserialize message
        data = json.loads(msg.value().decode('utf-8'))
        print(f"Received: {data}")

        # Append data to CSV file
        df = pd.DataFrame([data])
        df.to_csv("data/processed_stock_data.csv", mode='a', header=False, index=False)

except KeyboardInterrupt:
    print("\n❌ Stopping Kafka Consumer...")
finally:
    consumer.close()
 
