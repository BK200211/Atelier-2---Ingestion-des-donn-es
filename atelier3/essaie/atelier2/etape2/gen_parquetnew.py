import requests
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def fetch_data(url):
    response = requests.get(url)
    return response.json()

def save_to_parquet(data, filename):
    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, filename)

urls = {
    "public.Temps": "https://api.github.com/repos/elizaOS/eliza/issues?state=all",
    "public.Activities": "https://api.github.com/repos/elizaOS/eliza/issues?state=all",
    "public.Contributeurs": "https://api.github.com/repos/elizaOS/eliza/contributors",
    "Issue.Pull": "https://api.github.com/repos/elizaOS/eliza/pulls?state=all"
}

for table_name, url in urls.items():
    data = fetch_data(url)
    save_to_parquet(data, f"./atelier3/atelier3/raw/{table_name}.parquet")

print("Les données ont été récupérées et converties en format Parquet.")
