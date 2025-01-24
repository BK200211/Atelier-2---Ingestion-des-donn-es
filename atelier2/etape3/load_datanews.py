import duckdb
import pyarrow.parquet as pq
import os

def load_parquet_to_duckdb(file_path, table_name, conn):
    table = pq.read_table(file_path)
    conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM table")

directory = '../etape2'

conn = duckdb.connect('eliza.db')

for filename in os.listdir(directory):
    if filename.endswith('.parquet'):
        file_path = os.path.join(directory, filename)
        table_name = f"raw_{os.path.splitext(filename)[0]}"
        load_parquet_to_duckdb(file_path, table_name, conn)

print("Les fichiers Parquet ont été chargés dans la base DuckDB.")
