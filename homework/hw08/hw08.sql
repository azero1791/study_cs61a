CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE height <= max and height > min;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT dc.name FROM dogs AS dc, parents AS p, dogs AS dp 
  WHERE dc.name = p.child and dp.name = p.parent
  ORDER BY dp.height DESC;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT p1.child AS name1, p2.child AS name2 FROM parents AS p1, parents AS p2
  WHERE p1.parent = p2.parent and name1 < name2
  ;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT s.name1 || ' and ' || s.name2 || ' are ' || s_d1.size || ' siblings'
  FROM siblings AS s, size_of_dogs AS s_d1, size_of_dogs AS s_d2
  WHERE s.name1 = s_d1.name and s.name2 = s_d2.name and s_d1.size = s_d2.size;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper1(dog, stack_height, last_height, n);
CREATE TABLE stacks_helper2(d1, d2, s_h, l_h, n);
CREATE TABLE stacks_helper3(d1, d2, d3, s_h, l_h, n);
CREATE TABLE stacks_helper4(d1, d2, d3, d4, s_h, l_h, n);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper1 SELECT name, height, height, 1 FROM dogs;

INSERT INTO stacks_helper2 SELECT s1.dog, s2.dog, s1.stack_height + s2.stack_height, s2.last_height, 2 
FROM stacks_helper1 AS s1, stacks_helper1 AS s2 WHERE s1.dog != s2.dog and s1.last_height < s2.last_height;

INSERT INTO stacks_helper3 SELECT s1.d1, s1.d2, s2.dog, s1.s_h + s2.stack_height, s2.last_height, 3 
FROM stacks_helper2 AS s1, stacks_helper1 AS s2 WHERE s1.d2 != s2.dog and s1.l_h < s2.last_height;

INSERT INTO stacks_helper4 SELECT s1.d1, s1.d2, s1.d3, s2.dog, s1.s_h + s2.stack_height, s2.last_height, 4 
FROM stacks_helper3 AS s1, stacks_helper1 AS s2 WHERE s1.d3 != s2.dog and s1.l_h < s2.last_height;

CREATE TABLE stacks AS
  SELECT d1 || ', ' || d2 || ', ' || d3 || ', ' || d4, s_h FROM stacks_helper4 WHERE s_h >= 170 ORDER BY s_h ASC;

