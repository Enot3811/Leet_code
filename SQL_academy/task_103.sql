-- Вывести список имён сотрудников, получающих большую заработную плату,
-- чем у непосредственного руководителя.

SELECT e.name
FROM Employee e
JOIN Employee m ON e.chief_id = m.id
WHERE e.salary > m.salary