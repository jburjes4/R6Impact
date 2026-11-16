-- Kill counts w/o team kills
SELECT killer, COUNT(*) AS kill_count
FROM kill_events
WHERE NOT (killer_side = victim_side)
GROUP BY killer;

-- Repeat events
SELECT
    match_id,
    map_no,
    round_no,
    elapsed_s,
    killer,
    victim,
    COUNT(*) AS occurrences
FROM kill_events
GROUP BY
    match_id, map_no, round_no,
    elapsed_s, killer, victim
HAVING COUNT(*) > 1;

-- Team kills
	SELECT killer, victim, match_id
    FROM kill_events
    WHERE killer_side = victim_side;