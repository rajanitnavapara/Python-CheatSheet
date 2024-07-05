/*
Basic Queries
Display snum,sname,city and comm of all salespeople.
Display all snum without duplicates from all orders.
Display names and commissions of all salespeople in london.
All customers with rating of 100.
Produce orderno, amount and date form all rows in the order table.
All customers in San Jose, who have rating more than 200
All customers who were either located in San Jose or had a rating above 200.
All orders for more than $1000.
Names and citires of all salespeople in london with commission above 0.10.
All customers excluding those with rating < = 100 unless they are located in Rome.
All salespeople either in Barcelona or in london.
All salespeople with commission between 0.10 and 0.12. (Boundary values should be excluded)
All customers with NULL values in city column.
All orders taken on Oct 3Rd and Oct 4th 1994.
All customers serviced by peel or Motika
All customers whose names begin with a letter from A to B.
All orders except those with 0 or NULL value in amt field.
Count the number of salespeople currently listing orders in the order table
Largest order taken by each salesperson, datewise.
Largest order taken by each salesperson with order value more than $3000.
Which day had the hightest total amount ordered.
count all orders for Oct 3rd.
Count the number of different non NULL city values in customers table.
Select each customer’s smallest order.
First customer in alphabetical order whose name begins with G.
Get the output like "For dd/mm/yy there are_orders.
Assume that each salesperson has a 12% commission. Produce order no., salesperson no., and amount of salesperson’s commission for that order.
Find highest rating in each city. Put the output in this form. For the city (city), the highest rating is : (rating).
Display the totals of orders for each day and place the results in descending order.
All combinations of salespeople and customers who shared a city. (ie same city )
Name of all customers matched with the salespeople serving them.
List each order number followed by the name of the customer who made the order.
Names of salesperson and customer for each order after the order number.
Produce all customer serviced by salespeople with a commission above 12%.
Calculate the amount of the salesperson’s commission on each order with a rating above 100.
Find all pairs of customers having the same rating.
Policy is to assign three salesperson to each customers. Display all such combinations.
Display all customers located in cities where salesman serres has customer.
Find all pairs of customers served by single salesperson.
Produce all pairs of salespeople which are living in the same city. Exclude combinations of salespeople with themselves as well as duplicates with the order reversed.
Produce names and cities of all customers with the same rating as Hoffman.
Extract all the orders of Motika.
All orders credited to the same salesperson who services Hoffman.
All orders that are greater than the average for Oct 4.
Find average commission of salespeople in london.
Find all orders attributed to salespeople servicing customers in london.
Extract commissions of all salespeople servicing customers in London.
Find all customers whose cnum is 1000 above the snum of serres.
Count the customers with rating above San Jose’s average.
*/


-- 1. Display snum,sname,city and comm of all salespeople.
SELECT snum, sname, city, comm FROM salespeople;

-- 2. Display all snum without duplicates from all orders.
SELECT DISTINCT snum FROM orders;

-- 3. Display names and commissions of all salespeople in london.
SELECT sname, comm FROM salespeople WHERE city = 'London';

-- 4. All customers with rating of 100.
SELECT * FROM customers WHERE rating = 100;

-- 5. Produce orderno, amount and date form all rows in the order table.
SELECT orderno, amount, date FROM orders;

-- 6. All customers in San Jose, who have rating more than 200
SELECT * FROM customers WHERE city = 'San Jose' AND rating > 200;

-- 7. All customers who were either located in San Jose or had a rating above 200.
SELECT * FROM customers WHERE city = 'San Jose' OR rating > 200;

-- 8. All orders for more than $1000.
SELECT * FROM orders WHERE amount > 1000;

-- 9. Names and citires of all salespeople in london with commission above 0.10.
SELECT sname, city FROM salespeople WHERE city = 'London' AND comm > 0.10;

-- 10. All customers excluding those with rating < = 100 unless they are located in Rome.
SELECT * FROM customers WHERE rating > 100 OR city = 'Rome';

-- 11. All salespeople either in Barcelona or in london.
SELECT * FROM salespeople WHERE city = 'Barcelona' OR city = 'London';

-- 12. All salespeople with commission between 0.10 and 0.12. (Boundary values should be excluded)
SELECT * FROM salespeople WHERE comm > 0.10 AND comm < 0.12;

-- 13. All customers with NULL values in city column.
SELECT * FROM customers WHERE city IS NULL;

-- 14. All orders taken on Oct 3Rd and Oct 4th 1994.
SELECT * FROM orders WHERE date = '1994-10-03' OR date = '1994-10-04';

-- 15. All customers serviced by peel or Motika
SELECT * FROM customers WHERE sname = 'peel' OR sname = 'Motika';

-- 16. All customers whose names begin with a letter from A to B.
SELECT * FROM customers WHERE cname LIKE 'A%' OR cname LIKE 'B%';

-- 17. All orders except those with 0 or NULL value in amt field.
SELECT * FROM orders WHERE amount IS NOT NULL AND amount != 0;

-- 18. Count the number of salespeople currently listing orders in the order table
SELECT COUNT(DISTINCT snum) FROM orders;

-- 19. Largest order taken by each salesperson, datewise.
SELECT snum, MAX(amount) FROM orders GROUP BY snum;

-- 20. Largest order taken by each salesperson with order value more than $3000.
SELECT snum, MAX(amount) FROM orders WHERE amount > 3000 GROUP BY snum;

-- 21. Which day had the hightest total amount ordered.
SELECT date, SUM(amount) FROM orders GROUP BY date ORDER BY SUM(amount) DESC LIMIT 1;

-- 22. count all orders for Oct 3rd.
SELECT COUNT(*) FROM orders WHERE date = '1994-10-03';

-- 23. Count the number of different non NULL city values in customers table.
SELECT COUNT(DISTINCT city) FROM customers WHERE city IS NOT NULL;

-- 24. Select each customer’s smallest order.
SELECT cnum, MIN(amount) FROM orders GROUP BY cnum;

-- 25. First customer in alphabetical order whose name begins with G.
SELECT * FROM customers WHERE cname LIKE 'G%' ORDER BY cname LIMIT 1;

-- 26. Get the output like "For dd/mm/yy there are_orders.
SELECT date, COUNT(*) FROM orders GROUP BY date;

-- 27. Assume that each salesperson has a 12% commission. Produce order no., salesperson no., and amount of salesperson’s commission for that order.
SELECT orderno, snum, amount, amount * 0.12 FROM orders;

-- 28. Find highest rating in each city. Put the output in this form. For the city (city), the highest rating is : (rating).
SELECT CONCAT('For the city ', city, ', the highest rating is: ', MAX(rating)) AS output
 FROM customers GROUP BY city;

-- 29. Display the totals of orders for each day and place the results in descending order.
SELECT date, SUM(amount) FROM orders GROUP BY date ORDER BY SUM(amount) DESC;

-- 30. All combinations of salespeople and customers who shared a city. (ie same city )
SELECT s.sname, c.cname FROM salespeople s, customers c WHERE s.city = c.city;

-- 31. Name of all customers matched with the salespeople serving them.
SELECT c.cname, s.sname FROM salespeople s, customers c WHERE s.snum = c.snum;

-- 32. List each order number followed by the name of the customer who made the order.
SELECT o.orderno, c.cname FROM orders o, customers c WHERE o.cnum = c.cnum;

-- 33. Names of salesperson and customer for each order after the order number.
SELECT o.orderno, s.sname, c.cname FROM orders o, salespeople s, customers c WHERE o.snum = s.snum AND o.cnum = c.cnum;

-- 34. Produce all customer serviced by salespeople with a commission above 12%.
SELECT c.cname FROM customers c, salespeople s WHERE c.snum = s.snum AND s.comm > 0.12;

-- 35. Calculate the amount of the salesperson’s commission on each order with a rating above 100. 
SELECT o.orderno, o.amount, o.amount * s.comm FROM orders o, salespeople s WHERE o.rating > 100 AND o.snum = s.snum;

-- 36. Find all pairs of customers having the same rating.
SELECT c1.cname, c2.cname FROM customers c1, customers c2 WHERE c1.rating = c2.rating AND c1.cnum != c2.cnum;

-- 37. Policy is to assign three salesperson to each customers. Display all such combinations.
SELECT c.cname, s1.sname, s2.sname, s3.sname FROM customers c, salespeople s1, salespeople s2, salespeople s3 WHERE c.snum = s1.snum AND c.snum = s2.snum AND c.snum = s3.snum;

-- 38. Display all customers located in cities where salesman serres has customer.
SELECT c.cname FROM customers c, salespeople s WHERE c.city = s.city AND c.snum = s.snum;

-- 39. Find all pairs of customers served by single salesperson.
SELECT s.sname, c1.cname, c2.cname FROM salespeople s, customers c1, customers c2 WHERE c1.snum = s.snum AND c2.snum = s.snum AND c1.cnum != c2.cnum;

-- 40. Produce all pairs of salespeople which are living in the same city. Exclude combinations of salespeople with themselves as well as duplicates with the order reversed.
SELECT s1.sname, s2.sname FROM salespeople s1, salespeople s2 WHERE s1.city = s2.city AND s1.snum < s2.snum;

-- 41. Produce names and cities of all customers with the same rating as Hoffman.
SELECT c.cname, c.city FROM customers c, customers h WHERE c.rating = h.rating AND h.cname = 'Hoffman';

-- 42. Extract all the orders of Motika.
SELECT * FROM orders WHERE snum = (SELECT snum FROM salespeople WHERE sname = 'Motika');

-- 43. All orders credited to the same salesperson who services Hoffman.
SELECT * FROM orders WHERE snum = (SELECT snum FROM customers WHERE cname = 'Hoffman');

-- 44. All orders that are greater than the average for Oct 4.
SELECT * FROM orders WHERE amount > (SELECT AVG(amount) FROM orders WHERE date = '1994-10-04');

-- 45. Find average commission of salespeople in london.
SELECT AVG(comm) FROM salespeople WHERE city = 'London';

-- 46. Find all orders attributed to salespeople servicing customers in london.
SELECT * FROM orders WHERE snum IN (SELECT snum FROM customers WHERE city = 'London');

-- 47. Extract commissions of all salespeople servicing customers in London.
SELECT comm FROM salespeople WHERE snum IN (SELECT snum FROM customers WHERE city = 'London');

-- 48. Find all customers whose cnum is 1000 above the snum of serres.
SELECT * FROM customers WHERE cnum = (SELECT snum + 1000 FROM salespeople WHERE sname = 'serres');

-- 49. Count the customers with rating above San Jose’s average.
SELECT COUNT(*) FROM customers WHERE rating > (SELECT AVG(rating) FROM customers WHERE city = 'San Jose');
