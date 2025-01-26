WITH issues AS (
    SELECT * FROM {{ source('raw', 'Temps') }}
    UNION ALL
    SELECT * FROM {{ source('raw', 'Activities') }}
)

SELECT
    id AS issue_id,
    created_at,
    closed_at,
    state,
    title
FROM issues
WHERE id IS NOT NULL
