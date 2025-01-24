import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

data_activity = {
    'Temps': ['2023-09', '2023-09'],
    'Contributeur': ['Alice', 'Bob'],
    'Origine': ['Interne', 'Externe'],
    'Date de première contribution': ['2023-08-10', '2023-08-15'],
    'Type d\'activité': ['Commit', 'Issue'],
    'Module': ['Core', 'UI']
}

data_commits = {
    'Temps': ['2023-09', '2023-09'],
    'Contributeur': ['Alice', 'Bob'],
    'Origine': ['Interne', 'Externe'],
    'Module': ['Core', 'UI']
}

data_issues = {
    'Temps': ['2023-09-01', '2023-09-02'],
    'Contributeur': ['Alice', 'Bob'],
    'Origine': ['Interne', 'Externe'],
    'Type d\'issue': ['Bug', 'Amélioration'],
    'Module': ['Core', 'UI'],
    'Date d\'ouverture': ['2023-09-01', '2023-09-02'],
    'Date de fermeture': ['2023-09-03', '2023-09-05'],
    'Durée de résolution': [2, 3]
}

data_documentation = {
    'Temps': ['2023-09-01', '2023-09-02'],
    'Documentation Section': ['API', 'Guide'],
    'Date de mise à jour': ['2023-09-01', '2023-09-02'],
    'Feedback': ['Bon', 'Très bon'],
    'Satisfaction': [4, 5]
}

data_automation = {
    'Taux de succès de test': [95, 97],
    'Temps Moyen des Workflows': ['5min', '4min']
}

df_activity = pd.DataFrame(data_activity)
df_commits = pd.DataFrame(data_commits)
df_issues = pd.DataFrame(data_issues)
df_documentation = pd.DataFrame(data_documentation)
df_automation = pd.DataFrame(data_automation)

df_activity.to_parquet('activity.parquet')
df_commits.to_parquet('commits.parquet')
df_issues.to_parquet('issues.parquet')
df_documentation.to_parquet('documentation.parquet')
df_automation.to_parquet('automation.parquet')

df_activity = pd.read_parquet('activity.parquet')
df_commits = pd.read_parquet('commits.parquet')
df_issues = pd.read_parquet('issues.parquet')
df_documentation = pd.read_parquet('documentation.parquet')
df_automation = pd.read_parquet('automation.parquet')

print("Activity DataFrame")
print(df_activity)

print("\nCommits DataFrame")
print(df_commits)

print("\nIssues DataFrame")
print(df_issues)

print("\nDocumentation DataFrame")
print(df_documentation)

print("\nAutomation DataFrame")
print(df_automation)
