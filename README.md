CREATE DATABASE farmacia;
USE farmacia;

CREATE TABLE medicamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    categoria VARCHAR(50),
    precio DECIMAL(10,2),
    stock INT
);

CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_medicamento INT,
    fecha DATE,
    cantidad INT,
    FOREIGN KEY (id_medicamento) REFERENCES medicamentos(id)
);
