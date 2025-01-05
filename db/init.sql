CREATE DATABASE sampledb;
use sampledb;

CREATE TABLE employee(
    name VARCHAR(20),
    designation VARCHAR(50)
);

INSERT INTO employee
    (name, designation)
VALUES
    ('Employee1', 'Developer'),
    ('Employee2','Designer')