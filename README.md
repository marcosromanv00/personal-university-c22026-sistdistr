# Sistemas Distribuidos (C2-2026)

Repositorio que recopila el material, laboratorios prácticos, notas de clase y ensayos teóricos de la materia de **Sistemas Distribuidos**.

---

## Estructura del Repositorio

```text
personal-university-c22026-sistdistr/
├── Notas de Clase/                                # Apuntes y pizarras de sesiones teóricas (Semanas 1 a 6)
│   ├── pizarraSemana1-SistemasDistribuidos.txt
│   ├── pizarraSemana2-SistemasDistribuidos.txt
│   ├── pizarra-S3.txt
│   ├── pizarraSemana4.txt
│   ├── pizarraSemana5.txt
│   └── pizarraSemana6.txt
├── s1SDRPC-lab1/                                  # Laboratorio 1: Introducción a Sistemas Distribuidos y RPC
├── s4SD-lab2/                                     # Laboratorio 2: Comunicación entre procesos y sockets
├── s5SD-lab3/                                     # Laboratorio 3: Servicios distribuidos y persistencia
├── s6SD-lab4/                                     # Laboratorio 4: Comunicación en tiempo real y microservicios
├── s7SD-lab5/                                     # Laboratorio 5: Integración distribuida, APIs y balanceo
├── ensayo_bases_sistemas_distribuidos.html        # Ensayo sobre fundamentos de sistemas distribuidos (HTML)
├── ensayo_bases_sistemas_distribuidos.docx        # Ensayo en formato Word (.docx)
├── generate_essay_docx.py                         # Script en Python generador del documento Word
└── .gitignore                                     # Exclusiones de dependencias y temporales
```

---

## Tecnologías y Requisitos

- **Node.js** (v18 o superior) y **npm**
- **Python** (v3.10 o superior) y paquetes `python-docx` para la generación de documentos

---

## Ejecución de Laboratorios

Para ejecutar cualquiera de los laboratorios basados en Node.js / Express:

1. Navegue al directorio del laboratorio deseado:
   ```bash
   cd s1SDRPC-lab1   # o s4SD-lab2, s5SD-lab3, s6SD-lab4, s7SD-lab5
   ```
2. Instale las dependencias locales:
   ```bash
   npm install
   ```
3. Inicie el servidor:
   ```bash
   npm start
   # o bien: node app.js / node server.js según corresponda
   ```
