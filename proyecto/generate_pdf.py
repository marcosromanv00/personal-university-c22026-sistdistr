import base64
import os
import subprocess

def get_b64(path):
    with open(path, 'rb') as f:
        return f'data:image/png;base64,{base64.b64encode(f.read()).decode()}'

img1 = get_b64('docs/screenshots/interfaz-1-dashboard.png')
img2 = get_b64('docs/screenshots/interfaz-2-consulta.png')
img3 = get_b64('docs/screenshots/interfaz-3-gestion.png')
img4 = get_b64('docs/screenshots/interfaz-4-reportes-rpc-ws.png')

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Grupo-6-SD-Explicacion - Universidad Nacional</title>
    <style>
        @page {{
            size: A4;
            margin: 1.4cm 1.4cm 1.4cm 1.4cm;
        }}
        * {{
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
            color: #1e293b;
            line-height: 1.45;
            font-size: 9.1pt;
            background: #ffffff;
            margin: 0;
            padding: 0;
        }}
        .page {{
            page-break-after: always;
            box-sizing: border-box;
            max-height: 26.5cm;
            overflow: hidden;
        }}
        .page-last {{
            page-break-after: avoid;
        }}
        
        /* PORTADA */
        .cover {{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 25.5cm;
            padding: 1.5cm 0.8cm 1cm 0.8cm;
            border-top: 8px solid #c92a2a;
        }}
        .cover-header {{
            text-align: center;
        }}
        .cover-inst {{
            font-size: 15pt;
            font-weight: 700;
            color: #0f172a;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }}
        .cover-school {{
            font-size: 12pt;
            color: #475569;
            font-weight: 600;
            margin-top: 4px;
        }}
        .cover-course {{
            font-size: 11pt;
            color: #c92a2a;
            font-weight: 700;
            margin-top: 8px;
            letter-spacing: 0.3px;
        }}
        .cover-main {{
            text-align: center;
            margin: auto 0;
        }}
        .cover-tag {{
            display: inline-block;
            background: #fee2e2;
            color: #991b1b;
            padding: 5px 18px;
            border-radius: 999px;
            font-size: 9pt;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin-bottom: 16px;
            border: 1px solid #fecaca;
        }}
        .cover-title {{
            font-size: 20pt;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.25;
            margin: 0 0 10px 0;
        }}
        .cover-subtitle {{
            font-size: 11.5pt;
            color: #64748b;
            max-width: 620px;
            margin: 0 auto;
        }}
        .cover-meta {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 16px 20px;
            margin-top: 24px;
        }}
        .cover-meta table {{
            width: 100%;
            border-collapse: collapse;
        }}
        .cover-meta td {{
            padding: 5px 8px;
            font-size: 9.3pt;
        }}
        .cover-meta .label {{
            font-weight: 700;
            color: #475569;
            width: 28%;
        }}
        .cover-meta .val {{
            color: #0f172a;
        }}

        /* ENCABEZADOS Y TEXTO */
        h1 {{
            font-size: 13pt;
            color: #0f172a;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 3px;
            margin-top: 0;
            margin-bottom: 8px;
        }}
        h2 {{
            font-size: 10.5pt;
            color: #1e293b;
            margin-top: 10px;
            margin-bottom: 5px;
        }}
        h3 {{
            font-size: 9.5pt;
            color: #334155;
            margin-top: 8px;
            margin-bottom: 3px;
        }}
        p, li {{
            color: #334155;
            margin-bottom: 5px;
            text-align: justify;
        }}
        ul, ol {{
            margin-top: 2px;
            margin-bottom: 6px;
            padding-left: 18px;
        }}
        .code-box {{
            background: #0f172a;
            color: #f1f5f9;
            padding: 6px 9px;
            border-radius: 4px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 7.1pt;
            white-space: pre-wrap;
            word-break: break-all;
            margin: 4px 0 8px 0;
            border-left: 3px solid #c92a2a;
            line-height: 1.35;
        }}
        .cols-2 {{
            display: flex;
            gap: 10px;
            margin: 4px 0 8px 0;
        }}
        .cols-2 > div {{
            flex: 1;
        }}
        table.data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 6px 0 8px 0;
            font-size: 7.8pt;
        }}
        table.data-table th {{
            background: #0f172a;
            color: #ffffff;
            font-weight: 600;
            text-align: left;
            padding: 4px 6px;
            border: 1px solid #334155;
        }}
        table.data-table td {{
            padding: 3.5px 6px;
            border: 1px solid #e2e8f0;
            color: #334155;
        }}
        table.data-table tr:nth-child(even) {{
            background: #f8fafc;
        }}
        .badge {{
            display: inline-block;
            padding: 1px 4px;
            border-radius: 3px;
            font-size: 6.8pt;
            font-weight: 700;
            font-family: monospace;
        }}
        .badge-get {{ background: #e0f2fe; color: #0369a1; }}
        .badge-post {{ background: #dcfce7; color: #15803d; }}
        .badge-put {{ background: #fef3c7; color: #b45309; }}
        .badge-delete {{ background: #fee2e2; color: #b91c1c; }}
        .badge-status {{ background: #f1f5f9; color: #475569; }}
        
        .screenshot-card {{
            border: 1px solid #cbd5e1;
            border-radius: 5px;
            padding: 5px;
            background: #f8fafc;
            margin: 5px 0 8px 0;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
            text-align: center;
        }}
        .screenshot-card img {{
            max-width: 100%;
            max-height: 6.8cm;
            width: auto;
            border-radius: 3px;
            display: inline-block;
            border: 1px solid #e2e8f0;
        }}
        .screenshot-cap {{
            font-size: 7.4pt;
            color: #64748b;
            text-align: center;
            margin-top: 4px;
            font-weight: 600;
        }}
        .quote-box {{
            background: #f8fafc;
            border-left: 3.5px solid #c92a2a;
            padding: 8px 12px;
            margin: 5px 0 8px 0;
            font-style: italic;
            color: #334155;
            border-radius: 0 5px 5px 0;
            font-size: 8.6pt;
        }}
    </style>
</head>
<body>

<!-- PÁGINA 1: PORTADA (RÚBRICA SECCIÓN 9) -->
<div class="page cover">
    <div class="cover-header">
        <div class="cover-inst">Universidad Nacional (UNA)</div>
        <div class="cover-school">Facultad de Ciencias Exactas y Naturales • Escuela de Informática</div>
        <div class="cover-course">EIF-401 Sistemas Distribuidos • II Ciclo 2026</div>
    </div>
    
    <div class="cover-main">
        <div class="cover-tag">DOCUMENTACIÓN OFICIAL DEL PROYECTO</div>
        <div class="cover-title">Proyecto Grupal: Desarrollo de Aplicación Web con REST, RPC y Servicios Web</div>
        <div class="cover-subtitle">Sistema de Gestión Académica Distribuido (SGA) con Arquitectura de Tres Capas e Integración de Protocolos</div>
    </div>
    
    <div class="cover-meta">
        <table>
            <tr>
                <td class="label">Institución:</td>
                <td class="val">Universidad Nacional (UNA) - Escuela de Informática</td>
            </tr>
            <tr>
                <td class="label">Curso:</td>
                <td class="val">Sistemas Distribuidos (EIF-401)</td>
            </tr>
            <tr>
                <td class="label">Proyecto:</td>
                <td class="val">Proyecto Grupal: Desarrollo de Aplicación Web con REST, RPC y Servicios Web</td>
            </tr>
            <tr>
                <td class="label">Tema Seleccionado:</td>
                <td class="val"><strong>Tema 3: Sistema de gestión académica</strong></td>
            </tr>
            <tr>
                <td class="label">Grupo:</td>
                <td class="val"><strong>Grupo #6</strong></td>
            </tr>
            <tr>
                <td class="label">Integrantes:</td>
                <td class="val">
                    • <strong>Marcos Román Valverde</strong> (Cédula: 3-0529-0253)<br>
                    • <strong>Emanuel Soto Cordero</strong> (Cédula: 1-1823-0492)<br>
                    • <strong>Anthony Cerdas Morales</strong> (Cédula: 4-0231-0814)
                </td>
            </tr>
            <tr>
                <td class="label">Fecha:</td>
                <td class="val">02 de Octubre del 2026</td>
            </tr>
        </table>
    </div>
</div>

<!-- PÁGINA 2: INTRODUCCIÓN Y DESCRIPCIÓN DEL SISTEMA (RÚBRICA SECCIÓN 9) -->
<div class="page">
    <h1>1. Introducción</h1>
    <p>La administración y seguimiento académico en una institución de educación superior contemporánea involucra la gestión coordinada de múltiples procesos transaccionales: control de expedientes de matrícula, asignación y verificación de cupos en asignaturas curriculares, cálculo algorítmico de ponderaciones de calificaciones por créditos, y la vinculación con entidades externas para la homologación de convenios internacionales de movilidad estudiantil.</p>
    <p>El problema central que pretende resolver esta aplicación es la integración unificada, eficiente y desacoplada de estos procesos en una única solución de software distribuida. Frecuentemente, en las organizaciones educativas estas operaciones se efectúan de manera aislada o mediante herramientas dispersas, lo cual suscita inconsistencias de información, cuellos de botella en el procesamiento centralizado de notas y retrasos al validar procedencias y aranceles de estudiantes foráneos.</p>
    <p>La solución desarrollada articula en una sola plataforma web los tres mecanismos fundamentales de comunicación entre aplicaciones y servicios estudiados en el curso: <strong>solicitudes REST</strong> para la manipulación orientada a recursos y persistencia, <strong>solicitudes RPC</strong> para la ejecución remota de cómputos algorítmicos en el servidor, y <strong>Servicios Web</strong> para la interoperabilidad con servicios externos.</p>

    <h1>2. Descripción del Sistema</h1>

    <h2>2.1 Objetivo</h2>
    <p>Desarrollar e implementar una aplicación web distribuida, funcional e integrada para la administración integral de estudiantes, cursos, matrículas y calificaciones de la Escuela de Informática de la Universidad Nacional, demostrando de manera práctica la integración de solicitudes REST, procedimientos remotos RPC y consumo de un Servicio Web externo.</p>

    <h2>2.2 Usuarios del Sistema</h2>
    <ul>
        <li><strong>Administrador Académico / Cátedra:</strong> Supervisa el dashboard general, analiza las métricas de cohorte en tiempo real, monitorea la ocupación de cursos y administra los expedientes del estudiantado.</li>
        <li><strong>Docentes y Evaluadores:</strong> Consultan listas de clase, asientan y modifican evaluaciones parciales (Parcial 1, Parcial 2, Proyecto, Laboratorios) y verifican el estado de aprobación de los alumnos.</li>
        <li><strong>Coordinador de Movilidad e Intercambio Internacional:</strong> Valida información geográfica de estudiantes foráneos mediante el servicio web externo y liquida aranceles semestrales diferenciados.</li>
    </ul>

    <h2>2.3 Funcionalidades Principales</h2>
    <ul>
        <li><strong>Dashboard de Monitoreo Académico:</strong> Indicadores en tiempo real (KPIs): población estudiantil activa, catálogo de cursos, matrículas formalizadas y porcentaje global de aprobación.</li>
        <li><strong>Consulta Reactiva de Expedientes:</strong> Visualización tabular de estudiantes y asignaturas con filtros instantáneos por cédula, nombre o código de materia.</li>
        <li><strong>Gestión Integral de Expedientes (CRUD):</strong> Alta de estudiantes, formalización de matrículas con control de cupos, asentamiento ponderado de notas y eliminación en cascada.</li>
        <li><strong>Cálculo Remoto de Promedio Ponderado por Créditos (RPC):</strong> Invocación en servidor que pondera las notas según el peso curricular de cada materia y determina la condición de honor.</li>
        <li><strong>Análisis Estadístico de Rendimiento de Grupo (RPC):</strong> Cálculo algorítmico centralizado de media aritmética, varianza, desviación estándar poblacional y tasa de aprobación.</li>
        <li><strong>Homologación de Estudiantes Extranjeros y Aranceles (Servicio Web):</strong> Consulta de países, capitales y divisas mediante GraphQL con mecanismo de contingencia y tolerancia a fallos.</li>
    </ul>

    <h2>2.4 Tema Seleccionado</h2>
    <p>Se seleccionó el <strong>Tema 3: Sistema de gestión académica</strong>, correspondiente al catálogo de temas propuestos en la rúbrica oficial (Sección 3 del documento de especificación).</p>
</div>

<!-- PÁGINA 3: INTERFACES (1 y 2) (RÚBRICA SECCIÓN 9) -->
<div class="page">
    <h1>3. Interfaces (Parte 1: Dashboard y Consulta)</h1>
    <p>Conforme al punto 4 de la especificación técnica, la aplicación cuenta con 4 interfaces web funcionales, integradas, navegables entre sí mediante una barra de navegación superior estandarizada y con diseño institucional uniforme:</p>

    <h2>3.1 Interfaz 1: Inicio / Dashboard (Ruta: <code>/</code>)</h2>
    <p><strong>Función de la Interfaz:</strong> Funciona como la página principal de la aplicación. Ofrece al usuario un centro de monitoreo ejecutivo con el nombre del sistema, el menú de navegación completo, el resumen de información mediante cuatro tarjetas métricas (KPIs), la tabla de arquitectura con el mapeo de tecnologías, el estado de los micro-servicios y el registro de estudiantes recientes.</p>
    <div class="screenshot-card">
        <img src="{img1}" alt="Interfaz 1 - Inicio / Dashboard">
        <div class="screenshot-cap">Figura 1: Interfaz 1 - Inicio / Dashboard (Centro de Mando y KPIs Académicos en Tiempo Real)</div>
    </div>

    <h2>3.2 Interfaz 2: Consulta de Información (Ruta: <code>/consulta</code>)</h2>
    <p><strong>Función de la Interfaz:</strong> Permite consultar la información almacenada en el sistema mediante solicitudes REST (HTTP GET). Provee alternancia entre la vista de Estudiantes y la vista de Cursos, un buscador reactivo instantáneo por cédula o nombre, un modal interactivo con el desglose de notas parciales y un inspector técnico que expone los datos de la petición REST efectuada.</p>
    <div class="screenshot-card">
        <img src="{img2}" alt="Interfaz 2 - Consulta de Información">
        <div class="screenshot-cap">Figura 2: Interfaz 2 - Consulta de Información (Catálogo Reactivo y Búsqueda vía HTTP GET)</div>
    </div>
</div>

<!-- PÁGINA 4: INTERFACES (3 y 4) (RÚBRICA SECCIÓN 9) -->
<div class="page">
    <h1>3. Interfaces (Parte 2: Gestión y Operaciones Especiales)</h1>

    <h2>3.3 Interfaz 3: Registro / Gestión de Información (Ruta: <code>/gestion</code>)</h2>
    <p><strong>Función de la Interfaz:</strong> Permite crear, modificar y gestionar la información académica del sistema a través de las operaciones mutativas del protocolo REST. Contiene cuatro formularios específicos para registrar estudiantes (POST), formalizar matrículas (POST), asentar y actualizar calificaciones (PUT) y tramitar la baja de estudiantes (DELETE), con retroalimentación visual inmediata mediante mensajes de éxito y error.</p>
    <div class="screenshot-card">
        <img src="{img3}" alt="Interfaz 3 - Registro / Gestión de Información">
        <div class="screenshot-cap">Figura 3: Interfaz 3 - Registro / Gestión de Información (Operaciones CRUD REST: POST, PUT y DELETE)</div>
    </div>

    <h2>3.4 Interfaz 4: Operaciones Especiales / Reportes (Ruta: <code>/reportes</code>)</h2>
    <p><strong>Función de la Interfaz:</strong> Implementa las operaciones avanzadas del sistema mediante RPC y Servicios Web. Permite ejecutar remotamente el cálculo de promedio ponderado y la estadística de rendimiento de grupo (RPC), así como homologar estudiantes extranjeros consultando datos geográficos y calculando aranceles en tiempo real (Servicio Web GraphQL), mostrando en vivo las tramas técnicas enviadas y recibidas.</p>
    <div class="screenshot-card">
        <img src="{img4}" alt="Interfaz 4 - Operaciones Especiales / Reportes">
        <div class="screenshot-cap">Figura 4: Interfaz 4 - Operaciones Especiales / Reportes (Procedimientos RPC y Servicio Web GraphQL)</div>
    </div>
</div>

<!-- PÁGINA 5: REST (RÚBRICA SECCIÓN 9) -->
<div class="page">
    <h1>4. REST</h1>

    <h2>4.1 Endpoints Utilizados y Métodos HTTP Implementados</h2>
    <table class="data-table">
        <thead>
            <tr>
                <th>Método</th>
                <th>Endpoint</th>
                <th>Propósito / Descripción</th>
                <th>Código HTTP</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><span class="badge badge-get">GET</span></td>
                <td><code>/api/academico/dashboard</code></td>
                <td>Retorna los 4 KPIs globales y estado del sistema</td>
                <td><span class="badge badge-status">200 OK</span></td>
            </tr>
            <tr>
                <td><span class="badge badge-get">GET</span></td>
                <td><code>/api/academico/estudiantes</code></td>
                <td>Retorna lista de estudiantes con notas y cursos</td>
                <td><span class="badge badge-status">200 OK</span></td>
            </tr>
            <tr>
                <td><span class="badge badge-get">GET</span></td>
                <td><code>/api/academico/estudiantes/:id</code></td>
                <td>Consulta expediente individual por cédula</td>
                <td><span class="badge badge-status">200 / 404</span></td>
            </tr>
            <tr>
                <td><span class="badge badge-get">GET</span></td>
                <td><code>/api/academico/cursos</code></td>
                <td>Retorna catálogo de asignaturas y cupos</td>
                <td><span class="badge badge-status">200 OK</span></td>
            </tr>
            <tr>
                <td><span class="badge badge-post">POST</span></td>
                <td><code>/api/academico/estudiantes</code></td>
                <td>Crea un nuevo estudiante en archivo plano</td>
                <td><span class="badge badge-status">201 / 400</span></td>
            </tr>
            <tr>
                <td><span class="badge badge-post">POST</span></td>
                <td><code>/api/academico/matriculas</code></td>
                <td>Formaliza matrícula verificando cupo activo</td>
                <td><span class="badge badge-status">201 / 400</span></td>
            </tr>
            <tr>
                <td><span class="badge badge-put">PUT</span></td>
                <td><code>/api/academico/calificaciones</code></td>
                <td>Actualiza notas y calcula promedio ponderado</td>
                <td><span class="badge badge-status">200 / 400</span></td>
            </tr>
            <tr>
                <td><span class="badge badge-delete">DELETE</span></td>
                <td><code>/api/academico/estudiantes/:id</code></td>
                <td>Elimina estudiante y matrículas en cascada</td>
                <td><span class="badge badge-status">200 / 404</span></td>
            </tr>
        </tbody>
    </table>

    <h2>4.2 Información Enviada e Información Recibida</h2>
    <ul>
        <li><strong>Consultas GET:</strong> Parámetros en URL (ej. <code>:id</code> con la cédula). Servidor devuelve 200 OK y el arreglo/objeto JSON respectivo.</li>
        <li><strong>Alta de Estudiantes (POST):</strong> Cliente envía JSON con <code>id</code>, <code>nombre</code>, <code>carrera</code>, <code>pais</code>, <code>codigoPais</code>. Servidor valida, persiste y retorna 201 Created con el expediente generado.</li>
        <li><strong>Matrícula (POST):</strong> Cliente envía <code>estudianteId</code> y <code>cursoId</code>. Servidor valida cupo disponible, persiste y retorna 201 Created.</li>
        <li><strong>Calificaciones (PUT):</strong> Cliente envía notas parciales (Parcial 1: 25%, Parcial 2: 25%, Proyecto: 30%, Labs: 20%). Servidor actualiza y responde 200 OK.</li>
        <li><strong>Eliminación (DELETE):</strong> Parámetro en URL. Servidor remueve expediente y sus vínculos en cascada, retornando confirmación 200 OK.</li>
    </ul>

    <h2>4.3 Ejemplos de Solicitudes y Respuestas</h2>
    <div class="cols-2">
        <div>
            <p><strong>Solicitud de Alta (POST /api/academico/estudiantes):</strong></p>
            <div class="code-box">POST /api/academico/estudiantes HTTP/1.1
Host: localhost:3000
Content-Type: application/json

{{
  "id": "1-0999-0888",
  "nombre": "Carlos Mora Alvarado",
  "carrera": "Informática",
  "pais": "Costa Rica",
  "codigoPais": "CR"
}}</div>
        </div>
        <div>
            <p><strong>Respuesta del Servidor (HTTP 201 Created):</strong></p>
            <div class="code-box">HTTP/1.1 201 Created
Content-Type: application/json

{{
  "metodo": "POST",
  "status": 201,
  "mensaje": "Estudiante registrado con éxito.",
  "datos": {{
    "id": "1-0999-0888",
    "nombre": "Carlos Mora Alvarado",
    "email": "109990888@est.una.ac.cr",
    "estado": "Activo"
  }}
}}</div>
        </div>
    </div>
</div>

<!-- PÁGINA 6: RPC (RÚBRICA SECCIÓN 9) -->
<div class="page">
    <h1>5. RPC</h1>

    <h2>5.1 Funcionalidad Implementada</h2>
    <p>Se implementó un despachador formal bajo el estándar <strong>JSON-RPC 2.0</strong> en la ruta <code>/api/rpc</code>, el cual atiende dos procedimientos algorítmicos integrados en la lógica académica del sistema:</p>
    <ul>
        <li><strong><code>calcularPromedioPonderado</code>:</strong> Realiza el cómputo formal del promedio ponderado multiplicando la calificación final por los créditos curriculares de cada materia matriculada, dividiendo entre los créditos totales y clasificando la condición de honor.</li>
        <li><strong><code>analizarRendimientoGrupo</code>:</strong> Procesa el análisis estadístico de la cohorte matriculada (global o por asignatura), calculando media aritmética, varianza, desviación estándar poblacional y tasa de aprobación.</li>
    </ul>

    <h2>5.2 Cómo se Realiza la Llamada RPC</h2>
    <p>El cliente despacha una solicitud HTTP <code>POST</code> hacia el endpoint único <code>/api/rpc</code> con un sobre JSON conteniendo los cuatro campos requeridos por el estándar: <code>jsonrpc: "2.0"</code>, <code>method</code> con el nombre de la función, <code>params</code> con los argumentos requeridos, y un <code>id</code> numérico correlativo.</p>

    <h2>5.3 Parámetros Enviados y 5.4 Resultado Obtenido</h2>
    <div class="cols-2">
        <div>
            <p><strong>Trama Enviada (JSON-RPC Request):</strong></p>
            <div class="code-box">POST /api/rpc HTTP/1.1
Host: localhost:3000
Content-Type: application/json

{{
  "jsonrpc": "2.0",
  "method": "calcularPromedioPonderado",
  "params": {{
    "estudianteId": "3-0529-0253"
  }},
  "id": 101
}}</div>
        </div>
        <div>
            <p><strong>Resultado Obtenido (JSON-RPC Response):</strong></p>
            <div class="code-box">HTTP/1.1 200 OK
Content-Type: application/json

{{
  "jsonrpc": "2.0",
  "result": {{
    "estudianteId": "3-0529-0253",
    "nombre": "Marcos Román Valverde",
    "creditosTotales": 8,
    "creditosAprobados": 8,
    "promedioPonderado": 94.0,
    "condicionAcademica": "Excelencia (Honor)",
    "desgloseCursos": [
      {{ "cursoId": "EIF-401", "cred": 4, "nota": 96.2 }},
      {{ "cursoId": "EIF-402", "cred": 4, "nota": 91.8 }}
    ]
  }},
  "id": 101
}}</div>
        </div>
    </div>
</div>

<!-- PÁGINA 7: SERVICIOS WEB (RÚBRICA SECCIÓN 9) -->
<div class="page">
    <h1>6. Servicios Web</h1>

    <h2>6.1 Servicio Implementado / Utilizado</h2>
    <p>Se integró el <strong>Servicio Web público de Países y Divisas basado en GraphQL</strong> (<code>https://countries.trevorblades.com/</code>), aplicando rigurosamente los conceptos y el código estudiados durante la Semana 4 y el Laboratorio 2 del curso.</p>

    <h2>6.2 Función del Servicio</h2>
    <p>El servicio web resuelve una necesidad operativa concreta del Sistema de Gestión Académica: la homologación de estudiantes foráneos de intercambio internacional (por ejemplo, el caso de prueba de la estudiante <em>Elena Becker</em> procedente de Alemania). A partir del código de país, el servicio obtiene en tiempo real los datos geográficos oficiales (nombre internacional, bandera emoji, ciudad capital y moneda oficial), permitiendo liquidar automáticamente los aranceles de matrícula diferenciados en dólares ($USD) conforme a la reglamentación institucional.</p>

    <h2>6.3 Datos Enviados y Recibidos</h2>
    <div class="cols-2">
        <div>
            <p><strong>Datos Enviados (Consulta GraphQL):</strong></p>
            <div class="code-box">query ObtenerPaisesConvenio {{
  countries {{
    code
    name
    emoji
    capital
    currency
  }}
}}</div>
        </div>
        <div>
            <p><strong>Datos Recibidos (Estructura JSON):</strong></p>
            <div class="code-box">{{
  "data": {{
    "countries": [
      {{ "code": "DE", "name": "Germany",
         "emoji": "🇩🇪", "capital": "Berlin",
         "currency": "EUR" }},
      {{ "code": "CR", "name": "Costa Rica",
         "emoji": "🇨🇷", "capital": "San José",
         "currency": "CRC" }}
    ]
  }}
}}</div>
        </div>
    </div>

    <h2>6.4 Forma en que se Integra con la Aplicación</h2>
    <p>La integración se ejecuta mediante el módulo backend <code>services/webService.js</code> en Node.js. Cuando el usuario interactúa con la Interfaz 4 o cuando se consulta la ficha de un estudiante internacional, la aplicación consulta el endpoint GraphQL y expone los datos procesados en la vista.</p>
    <p>Para asegurar el funcionamiento continuo en el aula y proteger la aplicación ante contingencias de conectividad (cumpliendo con la regla 5a de la rúbrica), el servicio incorpora <strong>tolerancia a fallos</strong> mediante un timeout de 5000 ms y <strong>caché estructurada en disco</strong>. Si la red externa no responde, conmuta en 0 ms al respaldo local sin generar errores ni interrumpir la navegación del usuario.</p>
</div>

<!-- PÁGINA 8: CONCLUSIONES (RÚBRICA SECCIÓN 9) -->
<div class="page page-last">
    <h1>7. Conclusiones</h1>
    <p>Conforme a la rúbrica oficial, a continuación se presentan las conclusiones individuales de cada uno de los integrantes del equipo sobre los aprendizajes adquiridos durante el desarrollo del proyecto:</p>

    <h2>7.1 Conclusión: Marcos Román Valverde (Cédula: 3-0529-0253)</h2>
    <div class="quote-box">
    "El desarrollo del proyecto permitió comprender de manera tangible la distinción operativa entre arquitecturas orientadas a recursos (REST) y modelos orientados a ejecución de funciones remotas (RPC). La implementación de JSON-RPC 2.0 sobre Node.js demostró que desacoplar la lógica de cómputo algorítmico pesado del navegador alivia el procesamiento del cliente y unifica reglas de negocio críticas, como la ponderación de notas por créditos. Asimismo, la estructuración de persistencia en archivos planos mediante Node.js nativo reforzó la importancia del control de concurrencia y la tolerancia a fallos en sistemas distribuidos reales."
    </div>

    <h2>7.2 Conclusión: Emanuel Soto Cordero (Cédula: 1-1823-0492)</h2>
    <div class="quote-box">
    "La integración del servicio web GraphQL evidenció las ventajas del paradigma de consulta declarativa frente al over-fetching común de ciertas APIs REST tradicionales. Poder solicitar únicamente los campos code, name, capital y currency reduce drásticamente el consumo de ancho de banda y la sobrecarga de serialización entre servidores distribuidos. El proyecto nos capacitó para coordinar servicios heterogéneos y diseñar arquitecturas web resistentes a fallos de conectividad mediante patrones de respaldo local."
    </div>

    <h2>7.3 Conclusión: Anthony Cerdas Morales (Cédula: 4-0231-0814)</h2>
    <div class="quote-box">
    "El valor fundamental de este proyecto radicó en consolidar en una única aplicación los conceptos vistos en las Semanas 2, 3 y 4, logrando que el frontend no actúe de manera aislada sino como un consumidor transparente de múltiples protocolos. Entender cómo Express puede servir simultáneamente como API Gateway para llamadas REST, despachador de procedimientos RPC y cliente consumidor de servicios web externos nos brindó una perspectiva práctica de cómo se estructuran las plataformas empresariales en la industria tecnológica."
    </div>
</div>

</body>
</html>
'''

with open('docs/documento_impresion.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('HTML written successfully, now generating PDF via Edge headless...')

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = os.path.abspath('docs/documento_impresion.html')
pdf_path = os.path.abspath('Grupo-6-SD-Explicacion.pdf')

cmd = [
    edge,
    '--headless',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_path}',
    f'file:///{html_path.replace(os.sep, "/")}'
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_path):
    print(f'PDF Generated: {pdf_path} ({os.path.getsize(pdf_path)} bytes)')
else:
    print('Failed to generate PDF, stderr:', res.stderr)
