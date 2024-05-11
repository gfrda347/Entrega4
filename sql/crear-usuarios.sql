-- Crea la tabla de usuarios
create table usuarios (
nombre text not null,
motivo_salida text not null,
fecha_inicio_labores varchar(20),
fecha_ultimas_vacaciones varchar(20),
dias_vacaciones_acumulados varchar(20),
); 

create table familiares (
cedula_usuario varchar(20),
parentezco varchar(40), 
nombre text, 
apellido text, 
fecha_nacimiento date
);