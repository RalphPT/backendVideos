CREATE DATABASE IF NOT EXISTS introduccion;
 
 USE introduccion;
 
 CREATE TABLE productos(
 id INT AUTO_INCREMENT PRIMARY KEY,
 nombre VARCHAR(50) NOT NULL,
 precio FLOAT DEFAULT 10.00
 );
 
 CREATE TABLE pedidos(
 id INT AUTO_INCREMENT PRIMARY KEY,
 fecha DATE,
 producto_id INT,
 FOREIGN KEY (producto_id) REFERENCES productos(id)
 );
 
 ALTER TABLE pedidos ADD total FLOAT AFTER fecha;
 
 ALTER TABLE pedidos MODIFY total INT;
 
 ALTER TABLE pedidos CHANGE COLUMN total total_entero INT;
 
 ALTER TABLE pedidos DROP COLUMN total_entero;
 
 -- Elimina los datos
 TRUNCATE TABLE pedidos;
 
 -- Elimina la tabla
 DROP TABLE pedidos;
 
 DROP DATABASE introduccion;
 
 -- INSERT
 INSERT INTO productos (id, nombre, precio) VALUES (DEFAULT, 'Papaya', 5.80);
 
 INSERT INTO productos (id, nombre, precio ) VALUES (DEFAULT, 'Manzana', 4.30),
													(DEFAULT, 'Pera', 2.80),
                                                    (DEFAULT, 'Platano', 1.50),
                                                    (DEFAULT, 'Coliflor', 1.20),
                                                    (DEFAULT, 'Lechuga', 1.00);
                                                    
INSERT INTO productos VALUES (DEFAULT, 'Mandarina', 1.00);

SELECT * FROM productos WHERE precio >= 3.0 OR id = 7;

SELECT * FROM productos WHERE nombre LIKE '%a%a%';

SELECT * FROM productos WHERE nombre LIKE '_a__y%';

SELECT * FROM productos WHERE nombre LIKE BINARY 'p%';

SELECT * FROM productos LIMIT 3 OFFSET 0;

SELECT * FROM productos WHERE nombre LIKE '_a__y%' LIMIT 3 OFFSET 0;

SELECT * FROM productos;

UPDATE productos SET nombre = 'Piña' WHERE precio = 1;

SET SQL_SAFE_UPDATES = true;
 
 DELETE FROM productos WHERE id = 6;
 
 
 
 
 -- DDL > Data Definition Language
 -- ALTER > modificar TABLAS, VISTAS, DB, PROCEDIMIENTOS ALMACENADOS
 -- TRUNCATE > resetear la información y todos los valores predeterminados
 -- DROP > eliminar TABLAS, VISTAS DB, PROCEDIMIENTOS ALMACENADOS entre otros 