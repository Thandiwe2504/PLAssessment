--
-- Question 1
--

DROP TABLE IF EXISTS `calls`;

CREATE TABLE `calls` (
  `call_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `number_dialed` int NOT NULL,
  `date` datetime NOT NULL,
  `call_result` enum('Voicemail','Wrong Number','Answered') NOT NULL,
  PRIMARY KEY (`call_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Question 2
--
SELECT
	user_id,
	COUNT(*)
FROM
	calls
GROUP BY
	user_id, date
ORDER BY 
	user_id DESC, date


--
-- Question 3
--

SELECT
  number_dialed,
  COUNT(*)
FROM
  calls
GROUP BY
  number_dialed
ORDER BY
  number_dialed DESC


--
-- Question 4
--

SELECT
  number_dialed,
  COUNT(*)
FROM  
  calls
GROUP BY 
  number_dialed

--
-- Question 5
--

SELECT
  user_id,
  date,
  ROUND(SUM(CASE WHEN call_result = 'Answered' THEN 1 ELSE 0 END) / COUNT(*) * 100, 1)
FROM
  calls
GROUP BY
  user_id, date
ORDER BY
  user_id DESC, date

--
-- Question 6
--
--Write a query showing the top 10 most dialled numbers ordered in a descending order
SELECT
  number_dialed,
  COUNT(*)
FROM
  calls
GROUP BY
  number_dialed
ORDER BY
  number_dialed DESC
LIMIT 10

--
-- Question 7
--
SELECT
  user_id,
  COUNT(*)
FROM
  calls
GROUP BY
  user_id
HAVING
  COUNT(number_dialed) < 100
ORDER BY
  user_id DESC

--
-- Question 8
--

SELECT
  user_id,
  date,
  SUM(TIMESTAMPDIFF(SECOND, date, date + INTERVAL 1 DAY))
FROM
  calls
GROUP BY
  user_id, date
ORDER BY
  user_id DESC, date
