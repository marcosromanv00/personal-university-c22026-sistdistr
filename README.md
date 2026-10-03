# Sistemas Distribuidos (C2-2026)

Repositorio centralizado que recopila el material formativo, laboratorios prácticos, notas de clase teóricas, proyecto de curso y ensayos de investigación de la materia de **Sistemas Distribuidos**.

---

## Estructura del Repositorio

El repositorio se encuentra organizado de forma modular por categorías funcionales:

```text
personal-university-c22026-sistdistr/
├── laboratorios/                                  # Prácticas y desarrollos semanales en Node.js, Express y Edge
│   ├── s1SDRPC-lab1/                             # Lab 1: Introducción a SD y JSON-RPC (Ethereum & Solana)
│   ├── s4SD-lab2/                                # Lab 2: Consultas declarativas con GraphQL (Countries & Rick and Morty)
│   ├── s5SD-lab3/                                # Lab 3: Orquestación financiera y resiliencia (Promise.allSettled)
│   ├── s6-7SD-lab4/                              # Lab 4: Microfrontends satelitales NASA (Web Components & Shadow DOM)
│   ├── s7-8SD-lab5/                              # Lab 5: Edge Computing y Serverless con Cloudflare Workers
│   ├── s8SD-lab6/                                # Lab 6: Consolidación Serverless y preparación de entorno
│   └── s9SD-lab7/                                # Lab 7: Contenedores y mensajería distribuida (Docker & RabbitMQ)
├── notas-de-clase/                               # Pizarras virtuales y notas teóricas de cada sesión
│   ├── semana-01-pizarra.txt
│   ├── semana-02-pizarra.txt
│   ├── semana-03-pizarra.txt
│   ├── semana-04-pizarra.txt
│   ├── semana-05-pizarra.txt
│   ├── semana-06-pizarra.txt
│   ├── semana-08-pizarra.txt
│   └── semana-09-pizarra.txt
├── ensayos/                                      # Producción académica formal y generador automatizado
│   ├── ensayo_bases_sistemas_distribuidos.html   # Ensayo en formato web enriquecido
│   ├── ensayo_bases_sistemas_distribuidos.docx   # Ensayo formal en formato Word (.docx)
│   └── generate_essay_docx.py                    # Script de compilación programática del documento Word
├── proyecto/                                     # Especificaciones y entregables del proyecto de curso
│   ├── Proyecto.pdf                              # Especificación y rúbrica oficial del proyecto
│   └── README.md                                 # Guía y lineamientos del proyecto
├── .gitignore                                    # Exclusiones de dependencias, temporales y builds
└── README.md                                     # Documentación principal del repositorio
```

---

## Laboratorios Prácticos

| Laboratorio | Semanas | Directorio | Tecnologías | Conceptos Clave |
| :--- | :--- | :--- | :--- | :--- |
| **Lab 1** | S1 | [s1SDRPC-lab1](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/laboratorios/s1SDRPC-lab1) | Node.js, Express, Axios | JSON-RPC 2.0, blockchain pública (Ethereum, Solana), llamadas a procedimientos remotos. |
| **Lab 2** | S4 | [s4SD-lab2](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/laboratorios/s4SD-lab2) | Node.js, Express, GraphQL | Over-fetching / under-fetching, consultas declarativas, APIs de países y Rick & Morty. |
| **Lab 3** | S5 | [s5SD-lab3](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/laboratorios/s5SD-lab3) | Node.js, Express, APIs Financieras | Tolerancia a fallos, resiliencia con `Promise.allSettled`, orquestación de servicios (CoinGecko, Frankfurter). |
| **Lab 4** | S6-7 | [s6-7SD-lab4](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/laboratorios/s6-7SD-lab4) | Web Components, Shadow DOM, NASA APIs | Microfrontends nativos, aislamiento de estilos, NASA POWER & GIBS satelital. |
| **Lab 5** | S7-8 | [s7-8SD-lab5](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/laboratorios/s7-8SD-lab5) | Cloudflare Workers, Wrangler, Express | Edge Computing, arquitectura Serverless/FaaS, Cron Triggers planificados. |
| **Lab 6** | S8 | [s8SD-lab6](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/laboratorios/s8SD-lab6) | Cloudflare Workers, Node.js | Consolidación y despliegue del worker serverless en producción. |
| **Lab 7** | S9 | [s9SD-lab7](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/laboratorios/s9SD-lab7) | Docker Desktop, WSL2, RabbitMQ | Contenedores distribuidos, puertos AMQP 5672 y Management 15672. |

---

## Ensayos y Producción Teórica

Ubicados en el directorio [ensayos](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/ensayos):

- **Ensayo Web:** [ensayo_bases_sistemas_distribuidos.html](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/ensayos/ensayo_bases_sistemas_distribuidos.html) — Lectura interactiva con diagramas, tablas comparativas y citas bibliográficas en estándar APA.
- **Ensayo en Documento Formal:** [ensayo_bases_sistemas_distribuidos.docx](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/ensayos/ensayo_bases_sistemas_distribuidos.docx) — Formateado con estándares editoriales, tablas estilizadas, sangría francesa y tipografía formal.
- **Compilador Python:** [generate_essay_docx.py](file:///c:/Users/marco/OneDrive/Desktop/Proyectos/2-%20Activos/3-%20Otros/personal-university-c22026-sistdistr/ensayos/generate_essay_docx.py) — Script automatizado que genera el archivo Word a partir de la especificación técnica.

Para recompilar el documento Word:
```bash
python ensayos/generate_essay_docx.py
```

---

## Guía de Ejecución

### Requisitos Previos
- **Node.js:** v18.0 o superior
- **Docker Desktop:** con backend WSL2 activo (para laboratorios de contenedores)
- **Python:** v3.10 o superior (con paquete `python-docx` para generación de documentos)

### Ejecutar un Laboratorio de Node.js
```bash
# 1. Ingresar al directorio del laboratorio
cd laboratorios/s1SDRPC-lab1    # o s4SD-lab2, s5SD-lab3, s6-7SD-lab4, s7-8SD-lab5

# 2. Instalar dependencias
npm install

# 3. Iniciar el servidor
npm start
# O bien: node app.js / node server.js según corresponda
```

### Ejecutar el Contenedor de RabbitMQ (Lab 7)
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
Acceso a la consola web: `http://localhost:15672` (Credenciales: `admin` / `admin123`).
