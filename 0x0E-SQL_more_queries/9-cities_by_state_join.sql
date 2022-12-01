-- script that lists all cities contained in the databASe hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in AScending order by cities.id
-- You can use only one SELECT statement
SELECT cities.id, cities.name, states.name
	FROM cities
	JOIN states
	WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
