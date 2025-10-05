-- Напишите запрос, который выведет имена пилотов, которые в качестве второго пилота
-- (second_pilot_id) в августе 2023 года летали в New York

SELECT p.name
FROM Pilots p
JOIN Flights f ON f.second_pilot_id = p.pilot_id
WHERE YEAR(f.flight_date) = 2023
AND MONTH(f.flight_date) = 8
AND f.destination = "New York"