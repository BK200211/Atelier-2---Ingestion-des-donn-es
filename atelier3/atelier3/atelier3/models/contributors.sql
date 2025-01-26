SELECT 
    id AS contributor_id,
    name AS contributor_name,
    email AS contributor_email
FROM {{ source('raw', 'Contributeurs') }}
