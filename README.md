# CS665-Project-1

# Vehicle Rental Database Insert Script

## Overview
This README accompanies the `insert.sql` script designed for a mock vehicle rental database. This database is structured to facilitate the management of vehicles, customers, rental histories, employees, and payments within the context of vehicle rental operations based in Wichita, Kansas. Real car information and local addresses have been utilized to enhance the realism of the mock data.

## Database Schema
The database consists of the following tables:
- **Vehicle**: Holds information about the rental vehicles.
- **Customer**: Stores details of customers.
- **Rental History**: Tracks each rental's details, including dates, locations, and costs.
- **Employee**: Contains employee details who work at different locations.
- **Location**: Lists the locations where vehicles can be rented from or returned to.
- **Payments**: Manages payment transactions associated with rentals.

## Insert Script
The `insert.sql` script populates the database with initial data for all tables mentioned above. Here's a brief overview of the type of data included:
- **Locations**: Addresses and phone numbers for rental locations in Wichita, KS.
- **Vehicles**: Realistic information about vehicles such as make, model, year, and mileage.
- **Customers**: Sample customer information including names, contact details, and preferred payment methods.
- **Employees**: Employee information, including their associated location, name, contact, and salary.
- **Rental Histories**: Sample rental transactions with associated vehicle, customer, rental, and return information.
- **Payments**: Payment records for the rental transactions, including payment method and comments.

## Usage
To use the `insert.sql` script, follow these steps:
1. Ensure you have a MySQL, PostgreSQL, or similar database server running.
2. Create the database schema as defined in a separate script (not included here).
3. Execute the `insert.sql` script to populate the database with the initial data set.

For detailed instructions on how to execute SQL scripts in your database environment, refer to your database management system's documentation.

## Customization
You may customize the `insert.sql` script to fit your specific requirements by editing the SQL INSERT statements. This can include adding new records, modifying existing ones, or removing entries that do not fit your scenario.

# Vehicle Rental Databse Create Script

## Database Overview
This database schema supports a vehicle rental management system. Here's a breakdown of the tables and their purpose:

## Overview
This README accompanies the `insert.sql` script designed for a vehicle rental database. The database schema and sample data emulate a vehicle rental business operating in Wichita, Kansas. The structure is intended to support the management of vehicles, customers, rental histories, employees, locations, and associated payment records.

## Database Schema
The database incorporates the following tables:

- **vehicle**: Stores essential information about each vehicle available for rent.
-- **Fields**: vID (unique ID), lID (location ID), make, model, year, mileage, availability (Boolean)

- **customer**:  Holds customer data.
**Fields**: cID (unique ID), fName, lName, pNumber (phone number), address, pref_payment (preferred payment method)

- **rental_history**:  Tracks rental transactions.
Fields: rID (unique ID), vID, cID, rent_Date, return_Date, rent_loc (rental location ID), return_loc (return location ID), cost, comments

- **employee**: Contains employee information.
Fields: eID (unique ID), lID (location ID), fName, lName, pNumber, address, salary

- **location**: Stores information about rental locations.
Fields: lID (unique ID), address, pNumber, open (opening time), close (closing time)

- **payments**: Manages payment records for rentals.
Fields: paymentID (unique ID), amount, cID, eID, rID, method, date, comments

## Insert Script
The `insert.sql` script provides sample data to populate the database. This data includes:
Locations: Realistic addresses and phone numbers of potential rental locations within Wichita, KS.
Vehicles: Plausible information covering make, model, year, and mileage of rental vehicles.
Customers: Example customer details including names, addresses, phone numbers, and preferred payment options.
Employees: Sample employee data with their assigned location, name, contact information, and salary.
Rental Histories: Representative rental records, including associated vehicle, customer, rental dates, and return details.
Payments: Payment records linked to rental transactions, specifying the payment method and any additional notes.

## Usage
Prerequisites: A running database server (MySQL, PostgreSQL, or similar).
Schema Creation: Create the database schema using a separate script (not included).
Execution: Run the `insert.sql` script to populate the database with the initial data.
Refer to your database system's documentation for specific instructions on script execution.

## Customization
Tailor the `insert.sql` script to your needs by modifying the SQL INSERT statements. Add new data, change existing values, or delete entries as required.
