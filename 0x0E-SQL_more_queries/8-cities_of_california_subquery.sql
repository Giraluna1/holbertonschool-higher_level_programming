-- this scrip lists all the cities of California
-- that can be found in the database hbtn_0d_usa
SELECT states.name FROM states
WHERE name = California
INNER JOIN cities
ON cities.state_id = state.id
