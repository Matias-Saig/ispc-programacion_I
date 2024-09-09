CREATE DATABASE db_evidencia_4;

USE db_evidencia_4;

CREATE TABLE IF NOT EXISTS Product (
    product_id VARCHAR(255),
    PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS Product_details (
    model_id VARCHAR(255),
    product_id VARCHAR(255),
    brand VARCHAR(255),
    origin VARCHAR(255),
    height FLOAT,
    width FLOAT,
    weight FLOAT,
    flywheel VARCHAR(255),
    resistance_type VARCHAR(255),
    resistance_levels INT,
    max_weight_capacity FLOAT,
    product_description TEXT,
    PRIMARY KEY (model_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);


-- Máximo de 10  usuarios
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT,
    user_name VARCHAR(255),
    PRIMARY KEY (user_id)
) MAX_ROWS = 10;


-- Máximo de 10 registros por usuario
CREATE TABLE IF NOT EXISTS user_log (
    log_id INT AUTO_INCREMENT,
    user_id INT,
    log_date DATE,
    exercise_time VARCHAR(20),
    heart_rate_monitor INT,
    resistance_level INT,
    distance FLOAT,
    calories FLOAT,
    speed FLOAT,
    PRIMARY KEY (log_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
) MAX_ROWS = 10;


-- SENTENCIAS INSERT

-- Eliptica-001
INSERT INTO Product (product_id) VALUES ('eliptica_001');
INSERT INTO Users (user_name) VALUES ('Juan'), ('Ana'), ('Esteban');
INSERT INTO Product_details (
    model_id, brand, origin, height, width, weight, flywheel, resistance_type, resistance_levels, max_weight_capacity, product_description
) VALUES (
    'E1-power-basic', 'power', 'China', 1.5, 0.5, 20.0, '5kg', 'Fricción', 5, 100.0, 'Modelo básico de elíptica'
);
INSERT INTO user_log (
    user_id, log_date, exercise_time, heart_rate_monitor, resistance_level, distance, calories, speed) VALUES
    (1, '2023-05-10', '30 mins', 120, 4, 10.0, 300.0, 40.0),
    (2, '2024-03-30', '20 mins', 90, 2, 8.0, 200.0, 10.0),
    (3, '2024-06-25', '60 mins', 130, 5, 12.5, 600.0, 30.0);

-- Eliptica-002
INSERT INTO Product (product_id) VALUES ('eliptica_002');
INSERT INTO Users (user_name) VALUES ('Carlos'), ('Laura'), ('Diego'), ('Sofia');
INSERT INTO Product_details (
    model_id, brand, origin, height, width, weight, flywheel, resistance_type, resistance_levels, max_weight_capacity, product_description
) VALUES (
    'E2-power-advance', 'power', 'China', 1.5, 0.5, 21.0, '10kg', 'Magnetico', 10, 150.0, 'Modelo avanzado de elíptica'
);
INSERT INTO user_log (
    user_id, log_date, exercise_time, heart_rate_monitor, resistance_level, distance, calories, speed) VALUES
    (1, '2024-07-10', '70 mins', 110, 7, 10.0, 300.0, 40.0),
    (2, '2022-03-30', '50 mins', 100, 5, 8.0, 200.0, 10.0),
    (3, '2023-09-25', '60 mins', 120, 10, 12.5, 600.0, 30.0),
    (4, '2024-06-15', '60 mins', 130, 10, 15.5, 800.0, 30.0);

-- Eliptica-003
INSERT INTO Product (product_id) VALUES ('eliptica_003');
INSERT INTO Users (user_name) VALUES ('Nicolas');
INSERT INTO Product_details (
    model_id, brand, origin, height, width, weight, flywheel, resistance_type, resistance_levels, max_weight_capacity, product_description
) VALUES (
    'E2-power-pro', 'power', 'China', 1.5, 0.5, 25.0, '20kg', 'Magnetico', 20, 150.0, 'Modelo Pro de elíptica'
);
INSERT INTO user_log (
    user_id, log_date, exercise_time, heart_rate_monitor, resistance_level, distance, calories, speed) VALUES
    (1, '2024-09-12', '120 mins', 120, 18, 10.0, 900.0, 40.0);


-- SENTENCIAS SELECT
SELECT * FROM db_evidencia_4.Product;

SELECT * FROM db_evidencia_4.Product_details WHERE resistance_levels >= 10;

SELECT * FROM db_evidencia_4.user_log WHERE calories = 600;

SELECT model_id FROM db_evidencia_4.Product_details;

SELECT user_name FROM db_evidencia_4.Users WHERE user_id >= 1 AND user_id <= 5;