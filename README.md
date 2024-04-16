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

## Overview
This README accompanies the `create.sql` script, which constructs the database schema for a vehicle rental management system. The database is designed with a focus on storing information about vehicles, customers, rental transactions, employees, locations, and payments likely to be relevant to a Wichita, Kansas-based vehicle rental operation.

## Database Schema
The `create.sql` incorporates the following tables:

- **vehicle**: Stores essential information about each vehicle available for rent.
  - **Fields**: vID (unique ID), lID (location ID), make, model, year, mileage, availability (Boolean)

- **customer**:  Holds customer data.
  - **Fields**: cID (unique ID), fName, lName, pNumber (phone number), address, pref_payment (preferred payment method)

- **rental_history**:  Tracks rental transactions.
  - **Fields**: rID (unique ID), vID, cID, rent_Date, return_Date, rent_loc (rental location ID), return_loc (return location ID), cost, comments

- **employee**: Contains employee information.
  - **Fields**: eID (unique ID), lID (location ID), fName, lName, pNumber, address, salary

- **location**: Stores information about rental locations.
  - **Fields**: lID (unique ID), address, pNumber, open (opening time), close (closing time)

- **payments**: Manages payment records for rentals.
  - **Fields**: paymentID (unique ID), amount, cID, eID, rID, method, date, comments

## Create Script
The `create.sql` script provides sample data to populate the database. This data includes:
- **Locations**: Realistic addresses and phone numbers of potential rental locations within Wichita, KS.
- **Vehicles**: Plausible information covering make, model, year, and mileage of rental vehicles.
- **Customers**: Example customer details including names, addresses, phone numbers, and preferred payment options.
- **Employees**: Sample employee data with their assigned location, name, contact information, and salary.
- **Rental** Histories: Representative rental records, including associated vehicle, customer, rental dates, and return details.
- **Payments**: Payment records linked to rental transactions, specifying the payment method and any additional notes.

## Usage
1. **Prerequisites**: A database server (MySQL, PostgreSQL, or similar) capable of executing SQL scripts.
2. **Execution**: Run the `create.sql` script to build the database schema.
3. **Population**: Utilize a separate script (e.g., `insert.sql`) to insert data into the newly created tables.

## Customization
The schema defined in create.sql provides a foundation. You can customize it further by:
- **Adding Tables**: Create additional tables to support new features or data types.
- **Modifying Columns**: Alter existing columns, add new columns, or remove columns based on your requirements.
- **Adjusting Constraints**: Change foreign key relationships, add or remove constraints for data integrity.

# Vehicle Rental Databse CRUD

## Overview
This README accompanies the `crud.sql` script, which demonstrates core CRUD (Create, Read, Update, Delete) operations for the vehicle rental database schema. The included SQL statements serve as examples for how to manipulate data within the database.

## CRUD Operations
The script covers the following actions:

- **Create** :The insertion of new records into the rental_history and payments tables is illustrated within the context of adding a rental transaction. Note that full table creation would likely be defined within a separate create.sql script.
- **Read**:Various SELECT queries provide examples for retrieving information. Report types include vehicle lists, rental histories, available vehicles, financial overviews, and data integrity checks.
- **Update**:Statements demonstrate adjustments to records within the 'location', 'vehicle', 'employee', 'customer', and 'rental_history' tables.
- **Delete**: Examples showcase the removal of records based on scenarios such as a location closure, vehicle damage, customer data removal, employee termination, and erroneous rental entries.

## Usage
- **Prerequisites**:
  - An existing database with the defined schema (presumably created via a create.sql script).
  - A database server (like MySQL or PostgreSQL) capable of executing SQL scripts.
- **Execution**: Sections of crud.sql can be executed individually to perform specific actions.  **Use caution, especially with DELETE statements, as they permanently remove data.**

## Important Notes
- **Data Sensitivity**: Consider the sensitivity of any real data before running DELETE operations. Backups are always recommended.
- **Customization**: Adapt the provided examples to fit your specific data and scenarios.
- **Complementary Scripts**:
  - A `create.sql` script would likely define the initial database structure.
  - An `insert.sql` script could handle the population of those database tables with initial data.
