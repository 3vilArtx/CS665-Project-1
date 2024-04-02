-- insert.sql with real car information based in Wichita, Kansas

-- Inserting into location
INSERT INTO location (address, pNumber, open, close) VALUES
('1845 Fairmount St, Wichita, KS 67260', '316-978-3456', '08:00', '18:00'),
('701 Amidon St, Wichita, KS 67203', '316-838-8841', '09:00', '17:00'),
('455 N Main St, Wichita, KS 67202', '316-268-4361', '10:00', '20:00'),
('2021 N Amidon Ave, Wichita, KS 67203', '316-832-9871', '07:00', '19:00');

-- Inserting into vehicle
INSERT INTO vehicle (lID, make, model, year, mileage, availability) VALUES
(1, 'Ford', 'F-150', 2019, 10500, TRUE),
(2, 'Chevrolet', 'Silverado', 2018, 15700, TRUE),
(1, 'Toyota', 'Camry', 2020, 6000, TRUE),
(2, 'Honda', 'Civic', 2021, 3200, TRUE);

-- Inserting into customer
INSERT INTO customer (fName, lName, pNumber, address, pref_payment) VALUES
('James', 'Johnson', '316-555-0198', '1234 N Broadway St, Wichita, KS 67214', 'Credit Card'),
('Maria', 'Martinez', '316-555-0287', '5678 W Maple St, Wichita, KS 67213', 'Debit Card'),
('Robert', 'Smith', '316-555-0376', '91011 E Douglas Ave, Wichita, KS 67211', 'Cash'),
('Patricia', 'Brown', '316-555-0465', '1213 S Seneca St, Wichita, KS 67213', 'PayPal');

-- Inserting into employee
INSERT INTO employee (lID, fName, lName, pNumber, address, salary) VALUES
(1, 'Ethan', 'Adams', '316-555-1122', '1314 W 21st St N, Wichita, KS 67203', 52000.00),
(2, 'Sophia', 'Clark', '316-555-2233', '1516 S Tyler Rd, Wichita, KS 67209', 47000.00),
(3, 'Noah', 'Garcia', '316-555-3344', '1718 N Rock Rd, Wichita, KS 67206', 43000.00),
(4, 'Emma', 'Davis', '316-555-4455', '1920 E 1st St N, Wichita, KS 67214', 56000.00);

-- Inserting into rental_history
INSERT INTO rental_history (vID, cID, rent_Date, return_Date, rent_loc, return_loc, cost, comments) VALUES
(1, 1, '2024-04-01', '2024-04-03', 1, 2, 250.00, 'Smooth ride, great experience.'),
(2, 2, '2024-04-05', '2024-04-07', 2, 1, 300.00, 'Truck was in excellent condition.'),
(3, 3, '2024-04-09', '2024-04-11', 1, 1, 200.00, 'Car was clean and well-maintained.'),
(4, 4, '2024-04-13', '2024-04-15', 2, 2, 180.00, 'Rental process was quick and easy.');

-- Inserting into payments
INSERT INTO payments (amount, cID, eID, rID, method, date, comments) VALUES
(250.00, 1, 1, 1, 'Credit Card', '2024-04-03', 'Payment for Ford F-150 rental completed.'),
(300.00, 2, 2, 2, 'Debit Card', '2024-04-07', 'Payment for Chevrolet Silverado rental completed.'),
(200.00, 3, 3, 3, 'Cash', '2024-04-11', 'Payment for Toyota Camry rental completed.'),
(180.00, 4, 4, 4, 'PayPal', '2024-04-15', 'Payment for Honda Civic rental completed.');
