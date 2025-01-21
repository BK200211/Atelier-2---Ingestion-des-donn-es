CREATE TABLE raw_activity AS SELECT * FROM read_parquet('activity.parquet');

CREATE TABLE raw_commits AS SELECT * FROM read_parquet('commits.parquet');

CREATE TABLE raw_issues AS SELECT * FROM read_parquet('issues.parquet');

CREATE TABLE raw_documentation AS SELECT * FROM read_parquet('documentation.parquet');

CREATE TABLE raw_automation AS SELECT * FROM read_parquet('automation.parquet');