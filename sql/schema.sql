DROP DATABASE IF EXISTS Sales_customers_database_management;
CREATE DATABASE Sales_customers_database_management;
USE Sales_customers_database_management;

CREATE TABLE Salespeople (
    Snum INT PRIMARY KEY,
    sname VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    comm DECIMAL(10,2) NOT NULL
);

CREATE TABLE customer (
    cnum INT PRIMARY KEY,
    cname VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    snum INT NOT NULL,
    CONSTRAINT fk_customer_salesperson
        FOREIGN KEY (snum) REFERENCES Salespeople(Snum)
);

CREATE TABLE `order` (
    onum INT PRIMARY KEY,
    odate DATE NOT NULL,
    oamount DECIMAL(12,2) NOT NULL,
    cnum INT NOT NULL,
    snum INT NOT NULL,
    CONSTRAINT fk_order_customer
        FOREIGN KEY (cnum) REFERENCES customer(cnum),
    CONSTRAINT fk_order_salesperson
        FOREIGN KEY (snum) REFERENCES Salespeople(Snum)
);

CREATE INDEX idx_customer_city ON customer(city);
CREATE INDEX idx_order_customer ON `order`(cnum);
CREATE INDEX idx_order_salesperson ON `order`(snum);
