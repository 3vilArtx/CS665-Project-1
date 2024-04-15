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

## Conclusion
This README and the accompanying `insert.sql` script are intended to provide a starting point for populating a vehicle rental database with realistic data. It can be used for educational purposes, software development, and database management training related to vehicle rental operations.

# Vehicle Rental Databse Create Script

## Database Overview
This database schema supports a vehicle rental management system. Here's a breakdown of the tables and their purpose:

## Tables

### vehicle:
Stores information about vehicles available for rent.
- **vID**: Unique identifier for each vehicle.
- **lID**: Location ID where the vehicle is primarily located (foreign key to the 'location' table).
- **make**: Vehicle manufacturer.
- **model**: Vehicle model.
- **year**: Vehicle manufacturing year.
- **mileage**: Odometer reading.
- **availability**: Indicates if the vehicle is currently available to rent (Boolean).

### customer:
Stores customer information.
**cID**: Unique identifier for each customer.
**fName**: Customer's first name.
**lName**: Customer's last name.
**pNumber**: Customer's phone number.
**address**: Customer's address.
**pref_payment**: Customer's preferred payment method.

### rental_history:
Stores a record of each rental transaction.
**rID**: Unique identifier for each rental.
**vID**: ID of the rented vehicle (foreign key).
**cID**: ID of the customer who rented the vehicle (foreign key).
**rent_Date**: Date vehicle was rented.
**return_Date**: Date vehicle was returned
**rent_loc**: Location ID where the vehicle was rented from (foreign key).
**return_loc**: Location ID where the vehicle was returned to (foreign key).
**cost**: Total cost of the rental.
**comments**: Any additional notes about the rental.

### employee:
Stores employee information.
**eID**: Unique identifier for each employee.
**lID**: Location ID where the employee works (foreign key).
**fName**: Employee's first name.
**lName**: Employee's last name.
**pNumber**: Employee's phone number.
**address**: Employee's address.
**salary**: Employee's salary.

### location:
Stores information about rental locations.
**lID**: Unique identifier for each location.
**address**: Location's address.
**pNumber**: Location's phone number.
**open**: Location's opening time.
**close**: Location's closing time.

### payments:
Tracks payments related to rentals.
**paymentID**: Unique identifier for each payment.
**amount**: Payment amount.
**cID**: Customer ID associated with the payment (foreign key).
**eID**: Employee ID who processed the payment (foreign key).
**rID**: Rental ID associated with the payment (foreign key).
**method**: Payment method (e.g., cash, credit card).
**date**: Payment date.
**comments**: Any additional notes about the payment.
