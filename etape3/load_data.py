import duckdb

con = duckdb.connect('mydatabase.db')

con.execute("CREATE TABLE raw_activity AS SELECT * FROM read_parquet('activity.parquet')")

con.execute("CREATE TABLE raw_commits AS SELECT * FROM read_parquet('commits.parquet')")

con.execute("CREATE TABLE raw_issues AS SELECT * FROM read_parquet('issues.parquet')")

con.execute("CREATE TABLE raw_documentation AS SELECT * FROM read_parquet('documentation.parquet')")

con.execute("CREATE TABLE raw_automation AS SELECT * FROM read_parquet('automation.parquet')")


con.close()
