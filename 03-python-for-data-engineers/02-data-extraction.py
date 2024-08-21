# Question: How do you read data from a sqlite3 database and write to a DuckDB database?
# Hint: Look at importing the database libraries for sqlite3 and duckdb and create connections to talk to the respective databases
import sqlite3

# Connect to the SQLite database
sqlite_conn = sqlite3.connect(
    "database.db"
)

# Fetch data from the SQLite Customer table
customers = sqlite_conn.execute(
    "SELECT * FROM Customer"
).fetchall()

# Insert data into the DuckDB Customer table
import duckdb

duckdb_conn = duckdb.connect("duckdb.db")
insert_query = f"""
INSERT INTO Customer (customer_id, zipcode, city, state_code, datetime_created, datetime_updated)
VALUES (?, ?, ?, ?, ?, ?)
"""

duckdb_conn.executemany(insert_query, customers)

# Hint: Look for Commit and close the connections
# Commit tells the DB connection to send the data to the database and commit it, if you don't commit the data will not be inserted
duckdb_conn.commit()

# We should close the connection, as DB connections are expensive
sqlite_conn.close()
duckdb_conn.close()

# Cloud storage
# Question: How do you read data from the S3 location given below and write the data to a DuckDB database?
# Data source: https://docs.opendata.aws/noaa-ghcn-pds/readme.html station data at path "csv.gz/by_station/ASN00002022.csv.gz"
# Hint: Use boto3 client with UNSIGNED config to access the S3 bucket
import csv
import gzip
from io import StringIO
import boto3
import duckdb
from botocore import UNSIGNED
from botocore.client import Config

# Hint: The data will be zipped you have to unzip it and decode it to utf-8

# AWS S3 bucket and file details
bucket_name = "noaa-ghcn-pds"
file_key = "csv.gz/by_station/ASN00002022.csv.gz"
# Create a boto3 client with anonymous access
s3_client = boto3.client("s3", config=Config(signature_version=UNSIGNED))

# Download the CSV file from S3
response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
compressed_data = response["Body"].read()

# Decompress the gzip data
csv_data = gzip.decompress(compressed_data).decode("utf-8")

# Read the CSV file using csv.reader
csv_reader = csv.reader(StringIO(csv_data))
data = list(csv_reader)

# Connect to the DuckDB database (assume WeatherData table exists)
duckdb_conn = duckdb.connect("duckdb.db")

# Insert data into the DuckDB WeatherData table
insert_query = f"""
INSERT INTO WeatherData (id, date, element, value, m_flag, q_flag, s_flag, obs_time)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

duckdb_conn.executemany(insert_query, data[:100000])

duckdb_conn.commit()
duckdb_conn.close()

# API
# Question: How do you read data from the CoinCap API given below and write the data to a DuckDB database?
# URL: "https://api.coincap.io/v2/exchanges"
# Hint: use requests library
import requests

# Define the API endpoint
url = "https://api.coincap.io/v2/exchanges"

# Fetch data from the CoinCap API
response = requests.get(url=url)
data = response.json()["data"]

# Connect to the DuckDB database
import duckdb

duckdb_conn = duckdb.connect("duck_db.db")

# Insert data into the DuckDB Exchanges table
# Prepare data for insertion
# Hint: Ensure that the data types of the data to be inserted is compatible with DuckDBs data column types in ./setup_db.py
insert_data = [
    (
        exchange["exchangeId"],
        exchange["name"],
        int(exchange["rank"]),
        (
            float(exchange["percentTotalVolume"])
            if exchange["percentTotalVolume"]
            else None
        ),
        float(exchange["volumeUsd"]) if exchange["volumeUsd"] else None,
        exchange["tradingPairs"],
        exchange["socket"],
        exchange["exchangeUrl"],
        int(exchange["updated"]),
    )
    for exchange in data
]

duckdb_conn.executemany(insert_query, insert_data)

duckdb_conn.commit()
duckdb_conn.close()

# Local disk
# Question: How do you read a CSV file from local disk and write it to a database?
# Look up open function with csvreader for python
import csv

file_location = "./file.csv"
with open(file_location, 'r', newline="") as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip header row
    for row in csvreader:
        print(row)


# Web scraping
# Questions: Use beatiful soup to scrape the below website and print all the links in that website
# URL of the website to scrape
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))