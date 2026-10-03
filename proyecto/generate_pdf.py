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
            margin: 1.8cm 1.5cm 2cm 1.5cm;
        }}
        body {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
            color: #1e293b;
            line-height: 1.55;
            font-size: 10pt;
            background: #ffffff;
            margin: 0;
            padding: 0;
        }}
        .cover {{
            page-break-after: always;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 25cm;
            padding: 2cm 1cm 1.5cm 1cm;
            box-sizing: border-box;
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
            margin-top: 6px;
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
            padding: 5px 16px;
            border-radius: 999px;
            font-size: 9.5pt;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin-bottom: 18px;
            border: 1px solid #fecaca;
        }}
        .cover-title {{
            font-size: 22pt;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.25;
            margin: 0 0 12px 0;
        }}
        .cover-subtitle {{
            font-size: 12pt;
            color: #64748b;
            max-width: 650px;
            margin: 0 auto;
        }}
        .cover-meta {{
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 18px 24px;
            margin-top: 30px;
        }}
        .cover-meta table {{
            width: 100%;
            border-collapse: collapse;
        }}
        .cover-meta td {{
            padding: 6px 8px;
            font-size: 9.5pt;
        }}
        .cover-meta .label {{
            font-weight: 700;
            color: #475569;
            width: 30%;
        }}
        .cover-meta .val {{
            color: #0f172a;
        }}
        h1 {{
            font-size: 15pt;
            color: #0f172a;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 6px;
            margin-top: 26px;
            margin-bottom: 12px;
            page-break-after: avoid;
        }}
        h2 {{
            font-size: 12pt;
            color: #1e293b;
            margin-top: 18px;
            margin-bottom: 8px;
            page-break-after: avoid;
        }}
        h3 {{
            font-size: 10.5pt;
            color: #334155;
            margin-top: 14px;
            margin-bottom: 6px;
            page-break-after: avoid;
        }}
        p, li {{
            color: #334155;
            margin-bottom: 8px;
            text-align: justify;
        }}
        ul, ol {{
            margin-top: 4px;
            margin-bottom: 12px;
            padding-left: 24px;
        }}
        .code-box {{
            background: #0f172a;
            color: #f1f5f9;
            padding: 10px 14px;
            border-radius: 6px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 8pt;
            white-space: pre-wrap;
            word-break: break-all;
            margin: 8px 0 14px 0;
            border-left: 4px solid #c92a2a;
            page-break-inside: avoid;
        }}
        table.data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0 16px 0;
            font-size: 8.5pt;
            page-break-inside: avoid;
        }}
        table.data-table th {{
            background: #0f172a;
            color: #ffffff;
            font-weight: 600;
            text-align: left;
            padding: 7px 9px;
            border: 1px solid #334155;
        }}
        table.data-table td {{
            padding: 6px 9px;
            border: 1px solid #e2e8f0;
            color: #334155;
        }}
        table.data-table tr:nth-child(even) {{
            background: #f8fafc;
        }}
        .badge {{
            display: inline-block;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 7.5pt;
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
            border-radius: 6px;
            padding: 8px;
            background: #f8fafc;
            margin: 12px 0 18px 0;
            page-break-inside: avoid;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        .screenshot-card img {{
            width: 100%;
            border-radius: 4px;
            display: block;
            border: 1px solid #e2e8f0;
        }}
        .screenshot-cap {{
            font-size: 8pt;
            color: #64748b;
            text-align: center;
            margin-top: 6px;
            font-weight: 600;
        }}
        .quote-box {{
            background: #f8fafc;
            border-left: 4px solid #c92a2a;
            padding: 10px 14px;
            margin: 8px 0 12px 0;
            font-style: italic;
            color: #334155;
            border-radius: 0 6px 6px 0;
            page-break-inside: avoid;
        }}
        .page-break {{
            page-break-before: always;
        }}
    </style>
</head>
<body>

<!-- PORTADA -->
<div class="cover">
    <div class="cover-header">
        <div class="cover-inst">Universidad Nacional de Costa Rica (UNA)</div>
        <div class="cover-school">Facultad de Ciencias Exactas y Naturales • Escuela de Informática</div>
        <div class="cover-course">EIF-401 Sistemas Distribuidos • II Ciclo 2026</div>
    </div>
    
    <div class="cover-main">
        <div class="cover-tag">DOCUMENTACIÓN TÉCNICA OFICIAL</div>
        <div class="cover-title">Sistema de Gestión Académica Distribuido</div>
        <div class="cover-subtitle">Integración de Arquitecturas REST, Invocación de Procedimientos Remotos (JSON-RPC 2.0) y Consumo de Servicios Web GraphQL con Tolerancia a Fallos</div>
    </div>
    
    <div class="cover-meta">
        <table>
            <tr>
                <td class="label">Número de Grupo:</td>
                <td class="val"><strong>Grupo #6</strong> (Tema 3: Sistema de Gestión Académica)</td>
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
                <td class="label">Profesor Catedrático:</td>
                <td class="val">M.Sc. Luis Raúl</td>
            </tr>
            <tr>
                <td class="label">Fecha de Entrega:</td>
                <td class="val">02 de Octubre del 2026</td>
            </tr>
        </table>
    </div>
</div>

<!-- SECCION 1: ARCHIVO TXT DEL EQUIPO -->
<h1>1. Información Formal del Equipo (Grupo-6.txt)</h1>
<p>En estricto cumplimiento con la directriz obligatoria del proyecto (Rúbrica punto 2a y 5i), a continuación se reproduce el contenido fidedigno del archivo formal <code>Grupo-6.txt</code> incluido en la raíz de la entrega:</p>

<div class="code-box">================================================================================
UNIVERSIDAD NACIONAL (UNA) - ESCUELA DE INFORMÁTICA
CURSO: SISTEMAS DISTRIBUIDOS (C2-2026)
GRUPO NÚMERO: 6
TEMA ASIGNADO: Tema 3 - Sistema de gestión académica
================================================================================

INTEGRANTES DEL EQUIPO:

1. Nombre Completo: Marcos Román Valverde
   Cédula: 3-0529-0253
   Correo Institucional: marcos.roman.valverde@est.una.ac.cr

2. Nombre Completo: Emanuel Soto Cordero
   Cédula: 1-1823-0492
   Correo Institucional: emanuel.soto.cordero@est.una.ac.cr

3. Nombre Completo: Anthony Cerdas Morales
   Cédula: 4-0231-0814
   Correo Institucional: anthony.cerdas.morales@est.una.ac.cr

================================================================================
FECHA DE ENTREGA: 02 de Octubre del 2026
PROFESOR: M.Sc. Luis Raúl
================================================================================</div>

<!-- SECCION 2: INTRODUCCION Y DESCRIPCION -->
<h1>2. Introducción y Arquitectura del Sistema</h1>
<p>La administración académica en el entorno universitario actual exige el manejo eficiente y desacoplado de información transaccional distribuida: el control de expedientes de matrícula, la oferta y cupos de asignaturas curriculares, el cómputo algorítmico centralizado de ponderaciones de calificaciones por créditos, y la interoperabilidad con servicios externos para convalidar convenios internacionales de intercambio.</p>
<p>El presente proyecto implementa una solución de software de arquitectura distribuida de tres capas (Three-Tier Architecture) sobre la plataforma Node.js y Express, unificando tres paradigmas fundamentales estudiados durante el curso:</p>
<ul>
    <li><strong>Semana 2 - Solicitudes REST:</strong> Operaciones CRUD sobre recursos canónicos (<code>/api/academico/estudiantes</code>, <code>/matriculas</code>, <code>/calificaciones</code>, <code>/cursos</code>) utilizando los verbos HTTP <code>GET</code>, <code>POST</code>, <code>PUT</code> y <code>DELETE</code>.</li>
    <li><strong>Semana 3 - Solicitudes RPC:</strong> Implementación del estándar formal <strong>JSON-RPC 2.0</strong> sobre HTTP POST para la invocación remota de procedimientos algorítmicos complejos en el servidor (cálculo de promedio ponderado y análisis estadístico de cohorte).</li>
    <li><strong>Semana 4 - Servicios Web:</strong> Consumo de una API externa basada en <strong>GraphQL</strong> (Países y Monedas) para homologar automáticamente estudiantes foráneos y liquidar aranceles internacionales con mecanismo de tolerancia a fallos (resiliencia y caché local).</li>
</ul>

<div class="page-break"></div>

<!-- SECCION 3: INTERFACES WEB CON EVIDENCIAS -->
<h1>3. Evidencia y Detalle de las 4 Interfaces Web</h1>
<p>Conforme al punto 4 de la especificación técnica, la aplicación cuenta con 4 interfaces web funcionales, integradas, navegables y con coherencia visual bajo la regla de diseño institucional 90-10 de la Universidad Nacional:</p>

<h2>3.1 Interfaz 1: Dashboard y Analítica Ejecutiva (Ruta: <code>/</code>)</h2>
<p><strong>Propósito:</strong> Centro de comando y monitoreo en tiempo real de la cohorte académica. Despliega tarjetas de métricas clave (KPIs de población activa, asignaturas, matrículas formalizadas y porcentaje de aprobación), gráfico SVG de distribución de rendimiento, estado de los micro-servicios y el registro reciente de expedientes.</p>
<div class="screenshot-card">
    <img src="{img1}" alt="Interfaz 1 - Dashboard Ejecutivo">
    <div class="screenshot-cap">Figura 1: Interfaz 1 (Dashboard de Monitoreo Académico y Arquitectura Distribuida en Tiempo Real)</div>
</div>

<h2>3.2 Interfaz 2: Consulta de Información REST (Ruta: <code>/consulta</code>)</h2>
<p><strong>Propósito:</strong> Demuestra el consumo de operaciones REST mediante el verbo HTTP <code>GET</code>. Incluye buscador reactivo instantáneo por cédula, nombre o código, catálogo alternable de Estudiantes y Cursos, modal de desglose de notas (Parcial 1, Parcial 2, Proyecto, Labs) y una consola inspectora en vivo de la solicitud HTTP.</p>
<div class="screenshot-card">
    <img src="{img2}" alt="Interfaz 2 - Consulta REST">
    <div class="screenshot-cap">Figura 2: Interfaz 2 (Búsqueda Reactiva y Consulta de Expedientes vía HTTP GET)</div>
</div>

<div class="page-break"></div>

<h2>3.3 Interfaz 3: Gestión Académica CRUD (Ruta: <code>/gestion</code>)</h2>
<p><strong>Propósito:</strong> Demuestra las operaciones mutativas del protocolo REST. Provee 4 formularios específicos para: registro de nuevos estudiantes (<code>POST</code>), formalización de matrículas (<code>POST</code>), asentamiento y ponderación de calificaciones (<code>PUT</code>) y desafiliación de expedientes (<code>DELETE</code>), con retroalimentación inmediata en UI mediante toasts.</p>
<div class="screenshot-card">
    <img src="{img3}" alt="Interfaz 3 - Gestión REST CRUD">
    <div class="screenshot-cap">Figura 3: Interfaz 3 (Módulo de Operaciones Mutativas REST: POST, PUT y DELETE)</div>
</div>

<h2>3.4 Interfaz 4: RPC y Servicios Web (Ruta: <code>/reportes</code>)</h2>
<p><strong>Propósito:</strong> Espacio especializado donde convergen la ejecución remota de funciones algorítmicas (JSON-RPC 2.0) y la integración del servicio web externo (GraphQL). Incluye consolas técnicas que despliegan en crudo las tramas de petición y respuesta intercambiadas por la red.</p>
<div class="screenshot-card">
    <img src="{img4}" alt="Interfaz 4 - RPC y Servicios Web">
    <div class="screenshot-cap">Figura 4: Interfaz 4 (Invocación JSON-RPC 2.0 y Consumo de Servicio Web GraphQL)</div>
</div>

<div class="page-break"></div>

<!-- SECCION 4: EVIDENCIAS REST -->
<h1>4. Evidencias de Solicitudes REST (Semana 2)</h1>
<p>El servicio REST está estructurado en <code>rest/academicoRoutes.js</code> y orquestado por la capa de lógica <code>services/academicoService.js</code>, garantizando persistencia transaccional en archivos planos dentro de <code>data/</code>.</p>

<h2>4.1 Matriz de Endpoints Implementados</h2>
<table class="data-table">
    <thead>
        <tr>
            <th>Método</th>
            <th>Endpoint</th>
            <th>Propósito del Servicio</th>
            <th>Respuesta Exitosa</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><span class="badge badge-get">GET</span></td>
            <td><code>/api/academico/dashboard</code></td>
            <td>Retorna los 4 KPIs agregados y estado general del sistema</td>
            <td><span class="badge badge-status">200 OK</span></td>
        </tr>
        <tr>
            <td><span class="badge badge-get">GET</span></td>
            <td><code>/api/academico/estudiantes</code></td>
            <td>Lista expedientes con cálculo consolidado de promedios</td>
            <td><span class="badge badge-status">200 OK</span></td>
        </tr>
        <tr>
            <td><span class="badge badge-get">GET</span></td>
            <td><code>/api/academico/estudiantes/:id</code></td>
            <td>Consulta de expediente individual por número de cédula</td>
            <td><span class="badge badge-status">200 OK</span></td>
        </tr>
        <tr>
            <td><span class="badge badge-post">POST</span></td>
            <td><code>/api/academico/estudiantes</code></td>
            <td>Crea un nuevo estudiante en el registro permanente</td>
            <td><span class="badge badge-status">201 Created</span></td>
        </tr>
        <tr>
            <td><span class="badge badge-post">POST</span></td>
            <td><code>/api/academico/matriculas</code></td>
            <td>Asigna un estudiante a un curso activo verificando cupo</td>
            <td><span class="badge badge-status">201 Created</span></td>
        </tr>
        <tr>
            <td><span class="badge badge-put">PUT</span></td>
            <td><code>/api/academico/calificaciones</code></td>
            <td>Actualiza evaluaciones parciales y recalcula promedio</td>
            <td><span class="badge badge-status">200 OK</span></td>
        </tr>
        <tr>
            <td><span class="badge badge-delete">DELETE</span></td>
            <td><code>/api/academico/estudiantes/:id</code></td>
            <td>Elimina expediente y matrículas asociadas en cascada</td>
            <td><span class="badge badge-status">200 OK</span></td>
        </tr>
    </tbody>
</table>

<h2>4.2 Ejemplo de Petición y Respuesta HTTP REST</h2>
<p><strong>Solicitud de Alta (POST /api/academico/estudiantes):</strong></p>
<div class="code-box">POST /api/academico/estudiantes HTTP/1.1
Host: localhost:3000
Content-Type: application/json

{{
  "id": "1-0999-0888",
  "nombre": "Carlos Mora Alvarado",
  "carrera": "Ingeniería en Sistemas de Información",
  "pais": "Costa Rica",
  "codigoPais": "CR"
}}</div>

<p><strong>Respuesta Recibida (HTTP 201 Created):</strong></p>
<div class="code-box">HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8

{{
  "metodo": "POST",
  "recurso": "/api/academico/estudiantes",
  "status": 201,
  "mensaje": "Estudiante registrado satisfactoriamente en el SGA.",
  "datos": {{
    "id": "1-0999-0888",
    "nombre": "Carlos Mora Alvarado",
    "carrera": "Ingeniería en Sistemas de Información",
    "nivel": "I Nivel",
    "email": "109990888@est.una.ac.cr",
    "pais": "Costa Rica",
    "codigoPais": "CR",
    "estado": "Activo"
  }}
}}</div>

<!-- SECCION 5: EVIDENCIAS RPC -->
<h1>5. Evidencias de la Implementación RPC (Semana 3)</h1>
<p>Conforme al código y conceptos analizados en la Semana 3, la invocación de procedimientos remotos (RPC) no opera sobre URLs de recursos estáticos, sino mediante el envío de un sobre estructurado hacia un punto de entrada único (<code>POST /api/rpc</code>), transportando el método a ejecutar y sus parámetros correspondientes.</p>

<h2>5.1 Especificación JSON-RPC 2.0 Implementada</h2>
<ul>
    <li><strong>Método 1: <code>calcularPromedioPonderado</code></strong>: Recibe la identificación de un estudiante, consulta en el servidor todos sus cursos matriculados, pondera la nota final por los créditos curriculares respectivos, suma el total de créditos y clasifica la condición académica del estudiante (Excelencia con Honor, Sobresaliente, Regular o Alerta).</li>
    <li><strong>Método 2: <code>analizarRendimientoGrupo</code></strong>: Recibe el código de una materia (o vacío para global), iterando la cohorte para calcular la media aritmética, varianza, desviación estándar poblacional y tasa de aprobación porcentual.</li>
</ul>

<p><strong>Trama Enviada (JSON-RPC Request):</strong></p>
<div class="code-box">POST /api/rpc HTTP/1.1
Host: localhost:3000
Content-Type: application/json

{{
  "jsonrpc": "2.0",
  "method": "calcularPromedioPonderado",
  "params": {{ "estudianteId": "3-0529-0253" }},
  "id": 101
}}</div>

<p><strong>Resultado Obtenido (JSON-RPC Response):</strong></p>
<div class="code-box">HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{{
  "jsonrpc": "2.0",
  "result": {{
    "estudianteId": "3-0529-0253",
    "nombre": "Marcos Román Valverde",
    "carrera": "Ingeniería en Sistemas de Información",
    "totalCursos": 2,
    "creditosTotales": 8,
    "creditosAprobados": 8,
    "promedioPonderado": 94.0,
    "condicionAcademica": "Excelencia Académica (Honor)",
    "desgloseCursos": [
      {{ "cursoId": "EIF-401", "creditos": 4, "notaFinal": 96.2, "ponderacion": 384.8, "estado": "Aprobado" }},
      {{ "cursoId": "EIF-402", "creditos": 4, "notaFinal": 91.8, "ponderacion": 367.2, "estado": "Aprobado" }}
    ]
  }},
  "id": 101
}}</div>

<div class="page-break"></div>

<!-- SECCION 6: EVIDENCIAS SERVICIO WEB -->
<h1>6. Evidencias del Servicio Web (Semana 4)</h1>

<h2>6.1 Servicio Web GraphQL de Países y Divisas</h2>
<p>Se integró el servicio web público basado en el protocolo <strong>GraphQL</strong> (<code>https://countries.trevorblades.com/</code>), cumpliendo rigurosamente el contenido de la Semana 4 y el Laboratorio 2. Este servicio web permite resolver una necesidad real del SGA: la convalidación de procedencia de estudiantes internacionales de intercambio y la liquidación arancelaria semestral diferenciada.</p>

<h2>6.2 Consulta Declarativa GraphQL Utilizada</h2>
<div class="code-box">query ObtenerPaisesConvenio {{
  countries {{
    code
    name
    emoji
    capital
    currency
  }}
}}</div>

<h2>6.3 Resiliencia y Tolerancia a Fallos (Offline Continuity)</h2>
<p>Para asegurar que durante la evaluación en clase la aplicación no experimente caídas por fallos de conectividad en el aula (Rúbrica punto 2b: <em>"Aplicación web funcional sin errores..."</em>), el módulo <code>services/webService.js</code> implementa un temporizador de 5000 ms y <strong>caché local enriquecida en disco</strong>. Si el servicio remoto no responde, conmuta en 0 ms al respaldo local de forma transparente para el usuario.</p>

<!-- SECCION 7: GUIA DE PRESENTACION DE 15 MINUTOS -->
<h1>7. Guía y Cronograma de Demostración Presencial (15 Minutos)</h1>
<p>Plan de distribución cronometrado para la defensa presencial ante el profesor M.Sc. Luis Raúl:</p>

<table class="data-table">
    <thead>
        <tr>
            <th>Bloque / Tiempo</th>
            <th>Responsable</th>
            <th>Puntos Rúbrica</th>
            <th>Acción Concreta en Demostración</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>B1: 00:00 - 02:30</strong></td>
            <td>Equipo Completo</td>
            <td>15 pts (4 Interfaces)</td>
            <td>Presentación del equipo, navegación por las 4 interfaces desde el encabezado común.</td>
        </tr>
        <tr>
            <td><strong>B2: 02:30 - 06:30</strong></td>
            <td>Emanuel Soto</td>
            <td>25 pts (REST Operativo)</td>
            <td>En <code>/gestion</code> crear estudiante (POST 201), matricularlo, calificarlo (PUT 200) y verificar en <code>/consulta</code> (GET).</td>
        </tr>
        <tr>
            <td><strong>B3: 06:30 - 10:00</strong></td>
            <td>Anthony Cerdas</td>
            <td>25 pts (RPC Operativo)</td>
            <td>En <code>/reportes</code> ejecutar promedio ponderado JSON-RPC 2.0 y analítica de cohorte en vivo.</td>
        </tr>
        <tr>
            <td><strong>B4: 10:00 - 13:00</strong></td>
            <td>Marcos Román</td>
            <td>20 pts (Servicio Web)</td>
            <td>En <code>/reportes</code> homologar estudiante extranjera (Alemania) con GraphQL, aranceles y respaldo offline.</td>
        </tr>
        <tr>
            <td><strong>B5: 13:00 - 15:00</strong></td>
            <td>Equipo Completo</td>
            <td>15 pts (Integración)</td>
            <td>Resumen de integración frontend-servicios y sesión de preguntas del profesor.</td>
        </tr>
    </tbody>
</table>

<!-- SECCION 8: BANCO DE RESPUESTAS RAPIDAS -->
<h1>8. Banco de Preguntas y Respuestas para la Defensa</h1>
<ul>
    <li><strong>¿Por qué RPC utiliza HTTP POST en vez de GET?</strong><br>
    <em>Respuesta:</em> RPC modela la invocación de una acción o cálculo algorítmico remoto con parámetros complejos (<code>params</code>), no el acceso a un identificador uniforme de recurso (URI). Además, el estándar oficial JSON-RPC 2.0 define su transporte sobre POST.</li>
    <li><strong>¿Dónde y cómo se realiza la persistencia de datos?</strong><br>
    <em>Respuesta:</em> En archivos planos JSON dentro de la carpeta <code>data/</code> del servidor mediante el módulo nativo <code>fs</code> de Node.js, garantizando atomicidad y serialización de lecturas y escrituras tal como se orientó en clase.</li>
    <li><strong>¿Qué ventaja ofreció GraphQL frente a REST en el Servicio Web?</strong><br>
    <em>Respuesta:</em> Elimina el <em>over-fetching</em>. Permite solicitar con exactitud los 5 campos requeridos (código, nombre, bandera, capital, divisa), optimizando el ancho de banda y la velocidad de red.</li>
</ul>

<div class="page-break"></div>

<!-- SECCION 9: CONCLUSIONES INDIVIDUALES -->
<h1>9. Conclusiones Individuales de los Integrantes</h1>

<h3>9.1 Conclusión de Marcos Román Valverde (Cédula: 3-0529-0253)</h3>
<div class="quote-box">
"El desarrollo del proyecto permitió comprender de manera tangible la distinción operativa entre arquitecturas orientadas a recursos (REST) y modelos orientados a ejecución de funciones remotas (RPC). La implementación de JSON-RPC 2.0 sobre Node.js demostró que desacoplar la lógica de cómputo algorítmico pesado del navegador alivia el procesamiento del cliente y unifica reglas de negocio críticas, como la ponderación de notas por créditos. Asimismo, la estructuración de persistencia en archivos planos mediante Node.js nativo reforzó la importancia del control de concurrencia y la tolerancia a fallos en sistemas distribuidos reales."
</div>

<h3>9.2 Conclusión de Emanuel Soto Cordero (Cédula: 1-1823-0492)</h3>
<div class="quote-box">
"La integración del servicio web GraphQL evidenció las ventajas del paradigma de consulta declarativa frente al over-fetching común de ciertas APIs REST tradicionales. Poder solicitar únicamente los campos code, name, capital y currency reduce drásticamente el consumo de ancho de banda y la sobrecarga de serialización entre servidores distribuidos. El proyecto nos capacitó para coordinar servicios heterogéneos y diseñar arquitecturas web resistentes a fallos de conectividad mediante patrones de respaldo local."
</div>

<h3>9.3 Conclusión de Anthony Cerdas Morales (Cédula: 4-0231-0814)</h3>
<div class="quote-box">
"El valor fundamental de este proyecto radicó en consolidar en una única aplicación los conceptos vistos en las Semanas 2, 3 y 4, logrando que el frontend no actúe de manera aislada sino como un consumidor transparente de múltiples protocolos. Entender cómo Express puede servir simultáneamente como API Gateway para llamadas REST, despachador de procedimientos RPC y cliente consumidor de servicios web externos nos brindó una perspectiva práctica de cómo se estructuran las plataformas empresariales en la industria tecnológica."
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
