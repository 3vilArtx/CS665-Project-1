--crud operations, Update, Read, Delete, Create(Covered in the insert.sql)

--Update
UPDATE location
SET open = '8:00'
WHERE address = '1845 Fairmount St, Wichita, KS 67260';

UPDATE vehicle
SET lID = 2
WHERE vID = 1;

UPDATE employee
SET pNumber = '316-555-4433'
WHERE eID = 3;

UPDATE customer
SET pref_payment = 'PayPal'
WHERE cID = 3;

UPDATE rental_history
SET  comments = CONCAT(comments, 'Addendum: Customer left their phone in the car')
WHERE rID = 3;

--Delete statements
--The idea behind the following is that a location has closed, and all cars in it's lot are being redirected
UPDATE vehicle
SET lID = 1
WHERE vID = (SELECT vID FROM vehicle WHERE lID = 4)

DELETE FROM location
WHERE lID = 4

--vehicle was damaged, and being removed from listings until repaired.
DELETE FROM vehicle
WHERE vID = 3;

--Customer requested their data be removed from the data base
DELETE FROM customer
WHERE cID = 2;

--employee is no longer working with us
DELETE FROM employee
where eID = 1;

--A record in the rental_history was proven to be false, and as such it and the associated payment is removed from history.
DELETE FROM rental_history rh
INNER JOIN payments p on p.rID = rh.ID
WHERE rID = 2;

--Read statements
--Report of all vechicles
SELECT make, model FROM vehicle;

--rental_history reports from a given customer
select * from rental_history
where cID = 3;

--Report of all available vechicles and where they are located
select address, make, model FROM vehicle
INNER JOIN location on location.lID = vehicle.lID
WHERE availability = 1
ORDER BY address DESC;

--Total amount earned
SELECT SUM(amount) FROM payments
WHERE cID IS NOT NULL AND rID IS NOT NULL;

--Total payroll
SELECT SUM(amount) FROM payments
WHERE EID IS NOT NULL;

--List of all open rentals
select make, model FROM vehicle
where availability = 0;

--Check for errors on rental_history, the idea being to check for incomplete rental histories, where the associated vehicle is listed as available
SELECT make, model, availability, rh.* FROM vechicle v
INNER JOIN rental_history rh on rh.vID = v.vID
WHERE (return_date IS NULL OR return_loc IS NULL) AND availability = 1

--Example of a car being rented
UPDATE vechicles
SET availability = 0
WHERE vID = 3;

--
INSERT INTO rental_history (vID, cID,rent_Date, rent_loc, cost) 
VALUES (3, 2, '4/2/2024',3, 250.00)
RETURNING rID INTO @new_rID;

insert INTO payments (amount, cID, rID, method, date)
VALUES (250.00, 2, @new_rID, 'Debit Card', '4/2/2024', 'Payment for Toyota Camry rental completed.')

--Upon return of the vehicle
UPDATE vechicles
SET availability = 1
WHERE vID = 3;

--
INSERT INTO rental_history (return_Date, return_loc, comments) 
VALUES ('4/2/2024',4, 'Seems the car was damaged on return.')
RETURNING rID INTO @new_rID;