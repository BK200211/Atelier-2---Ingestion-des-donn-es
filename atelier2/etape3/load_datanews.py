import requests
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import duckdb

# Fonction pour récupérer les données de l'API GitHub
def fetch_data(url):
    response = requests.get(url)
    return response.json()

# Fonction pour convertir les données en DataFrame
def json_to_dataframe(data):
    return pd.DataFrame(data)

# URL de l'API pour chaque table
urls = {
    "raw_Temps": "https://api.github.com/repos/elizaOS/eliza/issues?state=all",
    "raw_Activities": "https://api.github.com/repos/elizaOS/eliza/issues?state=all",
    "raw_Contributeurs": "https://api.github.com/repos/elizaOS/eliza/contributors",
    "raw_Issue_Pull": "https://api.github.com/repos/elizaOS/eliza/pulls?state=all"
}

# Créer une connexion à la base DuckDB
conn = duckdb.connect('eliza.db')

# Récupérer et charger les données pour chaque table
for table_name, url in urls.items():
    data = fetch_data(url)
    df = json_to_dataframe(data)
    conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")

print("Les données ont été récupérées et chargées dans la base DuckDB.")
