.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM STUDENTS WHERE color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM STUDENTS WHERE color = 'blue' and pet = 'dog';


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM STUDENTS AS a, STUDENTS as b 
  WHERE a.pet = b.pet and a.song = b.song and a.time < b.time;


CREATE TABLE sevens AS
  SELECT seven FROM STUDENTS AS s, numbers AS n
  WHERE s.time = n.time and (s.number = 7 and n.'7' = "True");

CREATE TABLE favpets AS
  SELECT pet, count(pet) AS count FROM STUDENTS GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE dog AS
  SELECT pet, max(count) FROM favpets;


CREATE TABLE bluedog_agg AS
  SELECT song, count(song) AS count FROM bluedog_songs GROUP by song ORDER BY count DESC ;


CREATE TABLE instructor_obedience AS
  SELECT seven, instructor, count(instructor) FROM STUDENTS WHERE seven = '7' GROUP BY instructor;

