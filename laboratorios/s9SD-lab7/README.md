# Laboratorio 7 (Semana 9) - Contenedores Distribuidos y Mensajería con Docker & RabbitMQ

## Descripción
Laboratorio introductorio a la virtualización a nivel de sistema operativo (contenedores) y sistemas de encolamiento de mensajes distribuidos utilizando **Docker Desktop** y **RabbitMQ**.

## Objetivos
1. Configuración de entorno de ejecución de contenedores con motor WSL2 en Windows.
2. Descarga de imagen oficial de RabbitMQ con consola de administración (`rabbitmq:management`).
3. Despliegue de contenedor aislado con mapeo de puertos de red.
4. Próxima integración: Conexión asíncrona de productores y consumidores en Node.js mediante protocolo AMQP.

## Configuración y Despliegue del Contenedor

### 1. Descargar la imagen
```bash
docker pull rabbitmq:management
```

### 2. Ejecutar el contenedor
```bash
docker run -d \
  --hostname rabbitmq-server \
  --name rabbitmq \
  -e RABBITMQ_DEFAULT_USER=admin \
  -e RABBITMQ_DEFAULT_PASS=admin123 \
  -p 5672:5672 \
  -p 15672:15672 \
  rabbitmq:management
```

### 3. Puertos de Servicio
- **AMQP Protocol:** `5672` (Comunicación entre servicios / Node.js)
- **Management Web UI:** `15672` (`http://localhost:15672`)
  - **Usuario:** `admin`
  - **Contraseña:** `admin123`
