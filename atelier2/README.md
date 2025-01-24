Atelier 2 - Ingestion des données
ElizaOS
Outils et sources de données
Outil utilisé :
Git

   ### Sources de données identifiées :
   
#Repositories
#Commits
#Issues
#Users
#Pull Requests
#Branches
#Releases
#Tags
#Organizations
#Projects


## Outils Utilisés
- **API REST**
## Sources de Données
1. **public.Temps** : Informations sur les dates et les temps.
2. **public.Activities** : Détails des activités.
3. **public.Contributeurs** : Informations sur les contributeurs.
4. **Issue.Pull** : Détails des issues et des pull requests.



   ## Indicateurs d'investissement

   
Activité des contributeurs :
Nombre de contributeurs actifs.
Diversité des contributeurs.

   
Fréquence et consistance des commits :
Nombre de commits par période.
Consistance des périodes d'activité.

   
Gestion des issues et des pull requests :
Nombre d'issues ouvertes, fermées et délai de résolution.
Qualité des pull requests.
Engagement externe.

   
Documentation et support communautaire :
Mises à jour de la documentation.
Feedback communautaire sur la documentation.

   
Automatisation et intégration continue :
Taux de succès des tests automatisés.
 
Temps moyen des workflows.

 ![image](https://github.com/user-attachments/assets/dcb7d395-7208-4072-bf56-79df0c73e49b)

# Installation et utilisation de DuckDB depuis PowerShell

Ce guide explique comment installer et utiliser DuckDB sur Windows via PowerShell.

## Prérequis

- **PowerShell** (installé par défaut sur Windows)
- **Python 3.x** (si vous souhaitez utiliser DuckDB avec Python)
- **pip** (gestionnaire de paquets Python)

## Étape 1 : Installation de DuckDB via `winget`

DuckDB peut être installé directement via le gestionnaire de paquets `winget`:

### 1. Ouvrir PowerShell en tant qu'administrateur

### 2. Installer DuckDB CLI

Exécutez la commande suivante dans PowerShell pour installer DuckDB CLI :

```powershell
winget install DuckDB.cli
```
### 3. Lancer Duckdb

Pour cela : .open 'C:/chemin/vers/votre/fichier/my_database.db'

Pour effectuer une requête SQL sur les données, comme une sélection de toutes les lignes d'une table, utilisez :

SELECT * FROM ma_table;


## Exemple d'usage de DuckDB pour ingérer des fichiers Parquet

Avant de le lancer, placé vous dans le bon dossier puis :

```
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
 
```

##Résultat sur Duckdb:

![image](https://github.com/user-attachments/assets/1110d819-cc93-4977-b5d5-3571bf7333c1)
