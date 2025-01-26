SELECT 
    id AS pull_id,
    state AS pull_state,
    created_at,
    closed_at,
    user->>'login' AS author
FROM {{ source('raw', 'Pull') }}
