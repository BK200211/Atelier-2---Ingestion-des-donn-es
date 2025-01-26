SELECT *
FROM {{ source('raw', 'Temps') }}
WHERE id IS NOT NULL
