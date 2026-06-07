# 🚲 Lyon Vélo Data Lake – Hadoop & Kafka Project

A mini Data Engineering project that simulates the ingestion, storage, and processing of bike station data using a modern Big Data architecture.

The project uses:

- Apache Kafka for data ingestion
- Hadoop HDFS for distributed storage
- Hadoop Streaming MapReduce for batch analytics
- Docker for infrastructure deployment
- Python for data processing

---

# 📋 Project Overview

This project demonstrates a complete data pipeline:

```text
Bike Station Data
        │
        ▼
   Kafka Producer
        │
        ▼
    Kafka Topic
        │
        ▼
   Kafka Consumer
        │
        ▼
        HDFS
        │
        ▼
   MapReduce Job #1
        │
        ▼
 Load Factor Metrics
        │
        ▼
   MapReduce Job #2
        │
        ▼
 Hourly Demand Metrics
```

The objective is to simulate how raw operational data can be transformed into analytical datasets using Hadoop.

---

# 🏗️ Architecture

```text
                    +----------------+
                    |  Sample Data   |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    | Kafka Producer |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    | Kafka Topic    |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    | Kafka Consumer |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    | Hadoop HDFS    |
                    +-------+--------+
                            |
             +--------------+--------------+
             |                             |
             v                             v
     MapReduce Job #1              MapReduce Job #2
      Load Metrics                 Hourly Demand
             |                             |
             +-------------+---------------+
                           |
                           v
                  Analytical Datasets
```

---

# 📂 Project Structure

```text
Lyon_velo_hadoop_kafka/
│
├── docker-compose.yml
│
├── producer/
│   └── producer.py
│
├── consumer/
│   └── consumer.py
│
├── mapreduce/
│   ├── mapper_load_factor.py
│   ├── reducer_load_factor.py
│   ├── mapper_hourly_demand.py
│   └── reducer_hourly_demand.py
│
├── data/
│   └── sample.json
│
└── README.md
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Data processing |
| Apache Kafka | Data streaming |
| Hadoop HDFS | Distributed storage |
| Hadoop Streaming | MapReduce execution |
| Docker | Containerization |
| Linux | Execution environment |

---

# 🚀 Environment Setup

## Start Containers

```bash
docker-compose up -d
```

Verify:

```bash
docker ps
```

---


# 📊 MapReduce Job #1 – Load Factor Analytics

## Objective

Calculate station load metrics.

Load Factor:

```text
available_bikes / bike_stands
```

---

## Mapper

Input:

```json
{
  "station_id": 101,
  "available_bikes": 12,
  "bike_stands": 20
}
```

Output:

```text
101    0.60
```

---

## Reducer

Computes:

- Average load factor
- Standard deviation
- Number of valid samples

Output:

```text
101    0.650    0.045    4/4
```

---

## Run MR1

```bash
hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
-input /data-lake/raw/sample.json \
-output /data-lake/processed/load_metrics \
-file mapper_load_factor.py \
-file reducer_load_factor.py \
-mapper "python mapper_load_factor.py" \
-reducer "python reducer_load_factor.py"
```

---

## View Results

```bash
hdfs dfs -cat /data-lake/processed/load_metrics/part-00000
```

---

# 📈 MapReduce Job #2 – Hourly Demand Analysis

## Objective

Measure average station occupancy by hour.

This helps identify usage peaks and demand patterns.

---

## Mapper

Extract:

- Hour from timestamp
- Load factor

Output:

```text
08    0.72
08    0.81
09    0.95
```

---

## Reducer

Computes:

- Average hourly load factor
- Sample count

Output:

```text
08    0.765    2
09    0.950    1
```

---

## Run MR2

```bash
hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
-input /data-lake/raw/sample.json \
-output /data-lake/processed/hourly_demand \
-file mapper_hourly_demand.py \
-file reducer_hourly_demand.py \
-mapper "python mapper_hourly_demand.py" \
-reducer "python reducer_hourly_demand.py"
```

---

## View Results

```bash
hdfs dfs -cat /data-lake/processed/hourly_demand/part-00000
```

---

# 📊 Sample Results

## Load Metrics

```text
101    0.650    0.045    4/4
102    0.720    0.031    4/4
```

Meaning:

| Column | Description |
|----------|-------------|
| station_id | Station identifier |
| avg_load | Average load factor |
| std_load | Standard deviation |
| samples | Valid samples |

---

## Hourly Demand

```text
08    0.742    2
09    0.881    1
10    0.655    1
```

Meaning:

| Column | Description |
|----------|-------------|
| hour | Hour of day |
| avg_load | Average occupancy |
| samples | Number of records |

---

# 🎯 Learning Outcomes

This project demonstrates:

- Kafka Producer/Consumer workflows
- Distributed storage using HDFS
- Hadoop Streaming MapReduce
- Mapper and Reducer design
- Batch analytics pipelines
- Docker-based Big Data environments
- End-to-end Data Engineering concepts

---

# 🔮 Future Improvements

Possible extensions:

- Apache Spark implementation
- Airflow orchestration
- Real-time streaming analytics
- Grafana dashboards
- Data warehouse integration
- Machine learning demand forecasting

---

#  Author

Data Engineering & Big Data Project

Built with:

- Python
- Apache Kafka
- Hadoop HDFS
- Hadoop Streaming
- Docker
