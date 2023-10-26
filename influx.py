import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

  
token = os.environ.get("INFLUXDB_TOKEN")
org = "poprn"
url = "http://localhost:8086"
bucket = "g1"

def save(titulos):
  try:  
    point = (
      Point("lista_de_titulos")
      .field("titulos", titulos)
    )
    
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket=bucket, org="poprn", record=point)
    client.close()
  except influxdb_client.Error() as error:
    print(error)



def read():
  try:
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    query_api = client.query_api()
    query = """from(bucket: "g1")
    |> range(start: -10m)
    |> filter(fn: (r) => r._measurement == "lista_de_titulos")"""
    tables = query_api.query(query, org="poprn")

    for table in tables:
      for record in table.records:
        print(record)
  except influxdb_client.Error() as error:
    print(error)
