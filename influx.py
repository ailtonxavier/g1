import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "poprn"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="g1"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   

for value in range(3):
  point = (
    Point("measurement1")
    .field("campo_1", value)
  )
  write_api.write(bucket=bucket, org="poprn", record=point)
  time.sleep(1) # separate points by 1 second


query_api = write_client.query_api()

query = """from(bucket: "g1")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="poprn")

for table in tables:
  for record in table.records:
    print(record)
