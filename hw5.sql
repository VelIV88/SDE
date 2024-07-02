-- По условию задания решение строится на трёх таблицах. 
-- По хорошему, стоило бы создать таблицу с людьми, в которой был бы персональный идентификатор (первичный ключ)
-- и три столбца с внешними ключами, содержащими ссылки справочники фамилий, имён и отчеств
-- такой подход позволил бы снизить объём хранимых данных на больших таблицах

CREATE TABLE IF NOT EXISTS first_name (
   id INT PRIMARY KEY,
   name VARCHAR
);
  
INSERT INTO first_name(id, name) VALUES
(0, 'Иван'),
(1, 'Петр'),
(2, 'Сидор');

CREATE TABLE IF NOT EXISTS middle_name (
   id INT PRIMARY KEY,
   name VARCHAR
);
  
INSERT INTO middle_name(id, name) VALUES
(0, 'Иванович'),
(1, 'Петрович'),
(2, 'Сидорович');

CREATE TABLE IF NOT EXISTS last_name (
   id INT PRIMARY KEY,
   name VARCHAR
);
  
INSERT INTO last_name(id, name) VALUES
(0, 'Иванов'),
(1, 'Петров'),
(2, 'Сидоров');

SELECT ln.name AS last_name, fn.name AS first_name, mn.name AS middle_name
FROM last_name ln
JOIN middle_name mn ON ln.id = mn.id
JOIN first_name fn ON ln.id = fn.id
ORDER BY last_name DESC;
