from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('Movimientos',b'aaaaaaaaaaaa')

producer.flush()
producer.close()