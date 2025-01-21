import duckdb

# Connect to a DuckDB database (or create it if it doesn't exist)

con = duckdb.connect('mydatabase.db')

# Load Parquet files into tables with 'raw' prefix

con.execute("CREATE TABLE raw_activity AS SELECT * FROM read_parquet('activity.parquet')")

con.execute("CREATE TABLE raw_commits AS SELECT * FROM read_parquet('commits.parquet')")

con.execute("CREATE TABLE raw_issues AS SELECT * FROM read_parquet('issues.parquet')")

con.execute("CREATE TABLE raw_documentation AS SELECT * FROM read_parquet('documentation.parquet')")

con.execute("CREATE TABLE raw_automation AS SELECT * FROM read_parquet('automation.parquet')")

# Close the connection

con.close()