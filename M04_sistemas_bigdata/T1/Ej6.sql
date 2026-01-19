
-- 1️⃣ CREAR LA BASE DE DATOS
CREATE DATABASE books_db;

-- ==============================================
-- 2️⃣ CREAR TABLA 'books' SI NO EXISTE
-- ==============================================

CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- ==============================================
-- 3️⃣ INSERTAR DATOS (10 libros)
-- ==============================================

INSERT INTO books (title, price) VALUES
('A Light in the Attic', 51.77),
('Tipping the Velvet', 53.74),
('Soumission', 50.10),
('Sharp Objects', 47.82),
('Sapiens: A Brief History of Humankind', 54.23),
('The Requiem Red', 22.65),
('The Dirty Little Secrets of Getting Your Dream Job', 33.34),
('The Coming Woman', 17.93),
('The Boys in the Boat', 22.60),
('Set Me Free', 17.46);

-- ==============================================
-- 4️⃣ CONSULTAS SQL
-- ==============================================

-- a) Todos los libros ordenados por precio descendente
SELECT * FROM books
ORDER BY price DESC;

-- b) Precio promedio de todos los libros
SELECT ROUND(AVG(price), 2) AS promedio_precio
FROM books;

-- c) Libro más caro y más barato
SELECT * FROM books
WHERE price = (SELECT MAX(price) FROM books)
   OR price = (SELECT MIN(price) FROM books);

-- d) Cuántos libros tienen un precio superior a 50
SELECT COUNT(*) AS libros_mayor_50
FROM books
WHERE price > 50;

-- e) Títulos de los 5 libros más baratos
SELECT title, price
FROM books
ORDER BY price ASC
LIMIT 5;

-- f) Precio total de todos los libros
SELECT ROUND(SUM(price), 2) AS total_precio_libros
FROM books;

-- ==============================================
-- 5️⃣ CONSULTA AVANZADA
-- Clasifica los libros en "Barato" o "Caro" según el promedio
-- ==============================================

SELECT
    title,
    price,
    CASE
        WHEN price < (SELECT AVG(price) FROM books) THEN 'Barato'
        ELSE 'Caro'
    END AS categoria
FROM books
ORDER BY price DESC;

