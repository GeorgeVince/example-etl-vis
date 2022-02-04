### Example Streaming / Viz ETL


##### Pipeline
![pipeline](pipeline.png)

##### Overview

This application will generate some example sales data, push to Kafka via FastAPI, use PySpark to monitor the topic and push to a mongoDB database.  Finally Streamlit is used to show a real time view of the data being generated.


Fancied learning some new tech, so this gave me an exposure to the following
- `FastAPI`: https://fastapi.tiangolo.com/
- `Apache Kafka`: https://kafka.apache.org/
- `Pyspark Streaming`: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
- `MongoDB`: https://www.mongodb.com/
- `Streamlit`: https://streamlit.io/

##### Deployment

```
docker compose up -d
```

##### Start a producer
```
pip install requests
python -m producer.py
```

##### TODO
- [x] Inital local working version 
- [x] Dockerise Kafka
- [x] Dockerise PySpark
- [x] Dockerise Streamlit
- [x] Dockerise FastAPI
- [ ] Docker Compose
- [ ] End to End Test

##### Wip:
DC -> Need to start kafka containers once kafka up and running, possibly using kafkacat?
docker run -it --network=host edenhill/kcat:1.7.1 -b localhost:9092 -L