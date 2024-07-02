CREATE TABLE IF NOT EXISTS first_name (
   id INT PRIMARY key,
   name VARCHAR
);
  
INSERT INTO first_name(id, name) VALUES
(0, 'Иван'),
(1, 'Петр'),
(2, 'Сидор');

CREATE TABLE IF NOT EXISTS middle_name (
   id INT PRIMARY key,
   name VARCHAR
);
  
INSERT INTO middle_name(id, name) VALUES
(0, 'Иванович'),
(1, 'Петрович'),
(2, 'Сидорович');

CREATE TABLE IF NOT EXISTS last_name (
   id INT PRIMARY key,
   name VARCHAR
);
  
INSERT INTO last_name(id, name) VALUES
(0, 'Иванов'),
(1, 'Петров'),
(2, 'Сидоров');

SELECT ln.name AS last_name, fn.name AS first_name, mn.name AS middle_name
FROM last_name ln
join middle_name mn on ln.id = mn.id
JOIN first_name fn on ln.id = fn.id
ORDER BY last_name DESC;
