SELECT
    login AS contributor_name,
    contributions
FROM {{ source('raw', 'Contributeurs') }}
