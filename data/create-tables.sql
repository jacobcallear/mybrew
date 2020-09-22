-- Create 4 tables in `rounds` database

CREATE DATABASE rounds;
USE rounds;

-- Drinks table with id
CREATE TABLE drinks (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    volume_ml INTEGER NOT NULL,
    hot TINYINT NOT NULL,
    fizzy TINYINT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO
    drinks (name, volume_ml, hot, fizzy)
VALUES
    ('tea', 250, 1, 0);

-- People table with id
CREATE TABLE people (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    age INTEGER NOT NULL,
    sex VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO
    people (name, age, sex)
VALUES
    ('Bob', 87, 'm');

-- Preferences table with id
CREATE TABLE preferences (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    person_name VARCHAR(20) NOT NULL,
    person_age INTEGER NOT NULL,
    person_sex VARCHAR(20) NOT NULL,
    drink_name VARCHAR(20) NOT NULL,
    drink_volume_ml INTEGER NOT NULL,
    drink_hot TINYINT NOT NULL,
    drink_fizzy TINYINT NOT NULL,
    PRIMARY KEY (id)
);

-- Rounds table identical to above
CREATE TABLE rounds (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    person_name VARCHAR(20) NOT NULL,
    person_age INTEGER NOT NULL,
    person_sex VARCHAR(20) NOT NULL,
    drink_name VARCHAR(20) NOT NULL,
    drink_volume_ml INTEGER NOT NULL,
    drink_hot TINYINT NOT NULL,
    drink_fizzy TINYINT NOT NULL,
    PRIMARY KEY (id)
);