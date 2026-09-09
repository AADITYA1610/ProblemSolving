WITH marked AS (
    SELECT
        user_id,
        action_date,
        action,
        COUNT(*) OVER (
            PARTITION BY user_id, action_date
        ) AS actions_per_day,
        LAG(action_date) OVER (
            PARTITION BY user_id
            ORDER BY action_date
        ) AS prev_date,
        LAG(action) OVER (
            PARTITION BY user_id
            ORDER BY action_date
        ) AS prev_action
    FROM activity
),
grouped AS (
    SELECT
        user_id,
        action_date,
        action,
        SUM(
            CASE
                WHEN actions_per_day = 1
                     AND prev_date = action_date - INTERVAL 1 DAY
                     AND prev_action = action
                THEN 0
                ELSE 1
            END
        ) OVER (
            PARTITION BY user_id
            ORDER BY action_date
        ) AS grp
    FROM marked
),
streaks AS (
    SELECT
        user_id,
        action,
        COUNT(*) AS streak_length,
        MIN(action_date) AS start_date,
        MAX(action_date) AS end_date
    FROM grouped
    GROUP BY user_id, action, grp
)
SELECT
    user_id,
    action,
    streak_length,
    start_date,
    end_date
FROM streaks
WHERE streak_length >= 5
ORDER BY streak_length DESC, user_id ASC;