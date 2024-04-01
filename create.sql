CREATE TABLE vehicle (
    vID INT AUTO_INCREMENT PRIMARY KEY,
    lID INT NOT NULL,
    make VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    mileage DECIMAL(10, 2) NOT NULL,
    availability BOOLEAN NOT NULL,
    FOREIGN KEY (lID) REFERENCES location(lID)
);

CREATE TABLE customer (
    cID INT AUTO_INCREMENT PRIMARY KEY,
    fName VARCHAR(255) NOT NULL,
    lName VARCHAR(255) NOT NULL,
    pNumber VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    pref_payment VARCHAR(20) NOT NULL
);

CREATE TABLE rental_history (
    rID INT AUTO_INCREMENT PRIMARY KEY,
    vID INT NOT NULL,
    cID INT NOT NULL,
    rent_Date DATE NOT NULL,
    return_Date DATE NOT NULL,
    rent_loc INT NOT NULL,
    return_loc INT NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    comments TEXT,
    FOREIGN KEY (vID) REFERENCES vehicle(vID),
    FOREIGN KEY (cID) REFERENCES customer(cID),
    FOREIGN KEY (rent_loc) REFERENCES location(lID),
    FOREIGN KEY (return_loc) REFERENCES location(lID)
);

CREATE TABLE employee (
    eID INT AUTO_INCREMENT PRIMARY KEY,
    lID INT NOT NULL,
    fName VARCHAR(255) NOT NULL,
    lName VARCHAR(255) NOT NULL,
    pNumber VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (lID) REFERENCES location(lID)
);

CREATE TABLE location (
    lID INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(255) NOT NULL,
    pNumber VARCHAR(20) NOT NULL,
    open TIME NOT NULL,
    close TIME NOT NULL
);

CREATE TABLE payments (
    paymentID INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    cID INT,
    eID INT,
    rID INT,
    method VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
    comments TEXT,
    FOREIGN KEY (cID) REFERENCES customer(cID),
    FOREIGN KEY (eID) REFERENCES employee(eID),
    FOREIGN KEY (rID) REFERENCES rental_history(rID)
);
