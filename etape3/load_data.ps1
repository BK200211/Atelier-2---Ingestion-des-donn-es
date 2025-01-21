# Définir le chemin de la base de données et du fichier SQL

$databasePath = "mydatabase.db"

$sqlFilePath = "load_data.sql"

# Lire le contenu du fichier SQL

$sqlCommands = Get-Content -Path $sqlFilePath -Raw

# Commande pour exécuter les commandes SQL avec DuckDB

$command = "duckdb.exe $databasePath -c `"$sqlCommands`""

# Exécuter la commande

Invoke-Expression $command