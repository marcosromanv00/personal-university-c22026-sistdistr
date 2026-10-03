from pathlib import Path
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    """Sets cell padding in dxa (1 pt = 20 dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="000000", sz="8", val="single"):
    """Sets solid black borders to an entire table."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def create_essay_document(output_path):
    doc = Document()

    # Configure Margins (1 inch / 2.54 cm all sides)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Style defaults
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(20, 20, 20)
    normal_style.paragraph_format.line_spacing = 1.2
    normal_style.paragraph_format.space_after = Pt(6)

    # ==========================================
    # PORTADA (COVER PAGE)
    # ==========================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(36)
    p_inst.paragraph_format.space_after = Pt(4)
    r_inst = p_inst.add_run("UNIVERSIDAD NACIONAL DE COSTA RICA")
    r_inst.bold = True
    r_inst.font.size = Pt(13)
    r_inst.font.color.rgb = RGBColor(0, 0, 0)

    p_subinst = doc.add_paragraph()
    p_subinst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_subinst.paragraph_format.space_after = Pt(72)
    r_subinst = p_subinst.add_run("FACULTAD DE CIENCIAS EXACTAS Y NATURALES\nESCUELA DE INFORMÁTICA\nCURSO: SISTEMAS DISTRIBUIDOS")
    r_subinst.font.size = Pt(10.5)
    r_subinst.font.color.rgb = RGBColor(80, 80, 80)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(12)
    r_title = p_title.add_run("Bases Aprendidas del Curso de Sistemas Distribuidos:")
    r_title.bold = True
    r_title.font.size = Pt(20)
    r_title.font.color.rgb = RGBColor(0, 0, 0)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(100)
    r_sub = p_sub.add_run("De la Teoría Arquitectónica y los Protocolos de Comunicación a la Resiliencia, los Microfrontends y el Cómputo Serverless")
    r_sub.italic = True
    r_sub.font.size = Pt(12.5)
    r_sub.font.color.rgb = RGBColor(60, 60, 60)

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_after = Pt(4)
    r_meta1 = p_meta.add_run("Ensayo Académico Reflexivo\n")
    r_meta1.bold = True
    r_meta1.font.size = Pt(11)
    
    p_author = doc.add_paragraph()
    p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_author.paragraph_format.space_after = Pt(4)
    r_author = p_author.add_run("Estudiante: Marco Murillo\nProfesor: M.Sc. Luis Raúl\nI Ciclo Lectivo 2026")
    r_author.font.size = Pt(10.5)
    r_author.font.color.rgb = RGBColor(60, 60, 60)

    doc.add_page_break()

    # ==========================================
    # ÍNDICE DE CONTENIDO
    # ==========================================
    p_idx_title = doc.add_paragraph()
    p_idx_title.paragraph_format.space_before = Pt(12)
    p_idx_title.paragraph_format.space_after = Pt(16)
    r_idx_t = p_idx_title.add_run("ÍNDICE DE CONTENIDO")
    r_idx_t.bold = True
    r_idx_t.font.size = Pt(15)
    r_idx_t.font.color.rgb = RGBColor(0, 0, 0)

    toc_items = [
        ("1. Introducción: El Despertar de la Consciencia Distribuida", "3"),
        ("2. Fundamentos y Fronteras: Arquitectura vs. Sistema Operativo", "4"),
        ("3. El Lenguaje de la Red: Anatomía de Protocolos y el Salto a RPC", "6"),
        ("4. El Dilema de la Ingesta de Datos: De REST y Over-fetching a la Precisión de GraphQL", "8"),
        ("5. La Cruda Realidad del Entorno Distribuido: Resiliencia y la Falacia del 'Simple Try-Catch'", "11"),
        ("6. Modularidad Radical: Contenedores, Principios de Diseño y Microfrontends con Shadow DOM", "14"),
        ("7. La Frontera del Cómputo: Paradigma Serverless, FaaS y Edge Computing", "17"),
        ("8. Síntesis y Conclusiones: Lecciones Aprendidas al Pie de la Máquina", "19"),
        ("9. Referencias Bibliográficas (Normativa APA 7ma Edición)", "21")
    ]

    for title, page in toc_items:
        p_item = doc.add_paragraph()
        p_item.paragraph_format.space_after = Pt(4)
        p_item.paragraph_format.line_spacing = 1.15
        
        r_t = p_item.add_run(title)
        r_t.font.size = Pt(10.5)
        
        # Dots leader simulation
        dots_len = max(5, 75 - len(title))
        r_dots = p_item.add_run(" " + "." * dots_len + " ")
        r_dots.font.color.rgb = RGBColor(160, 160, 160)
        
        r_p = p_item.add_run(page)
        r_p.bold = True
        r_p.font.size = Pt(10.5)

    doc.add_page_break()

    # ==========================================
    # HELPER FUNCTIONS FOR CONTENT
    # ==========================================
    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(14)
        r.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(12)
        r.font.color.rgb = RGBColor(30, 30, 30)
        return p

    def add_p(text, bold_prefix=None, italic=False):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.2
        p.paragraph_format.space_after = Pt(6)
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.color.rgb = RGBColor(0, 0, 0)
        r = p.add_run(text)
        r.italic = italic
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(20, 20, 20)
        return p

    def add_quote(text, author_ref):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Inches(0.5)
        p.paragraph_format.right_indent = Inches(0.4)
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.line_spacing = 1.15
        
        r = p.add_run(f'"{text}" ')
        r.italic = True
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(40, 40, 40)
        
        r_ref = p.add_run(f'— {author_ref}')
        r_ref.bold = True
        r_ref.font.size = Pt(9.5)
        r_ref.font.color.rgb = RGBColor(0, 0, 0)
        return p

    # ==========================================
    # SECCIÓN 1
    # ==========================================
    add_h1("1. Introducción: El Despertar de la Consciencia Distribuida")
    
    add_p(
        "Cuando uno empieza a dar sus primeros pasos en el desarrollo de software, el mundo parece un lugar predecible y seguro. Uno escribe una función en un archivo, la invoca desde otro punto del programa, y si los tipos o la lógica son correctos, el resultado simplemente llega a la memoria de la máquina. La memoria RAM es un espacio compartido, el procesador local ejecuta las instrucciones en riguroso orden secuencial y los errores suelen ser deterministas: un error tipográfico, una referencia nula o una condición de parada mal calculada. Sin embargo, en el momento en que esa misma aplicación necesita interactuar con otro proceso que reside a cientos o miles de kilómetros, en un servidor ajeno y sobre una red física que puede fallar en cualquier milisegundo, todas las certezas del desarrollador monolítico se desmoronan.",
        bold_prefix="El salto del paradigma local al distribuido: "
    )

    add_p(
        "El curso de Sistemas Distribuidos ha sido, ante todo, un viaje de demolición de falsas seguridades y de reconstrucción de criterio técnico. A lo largo de las semanas, las pizarras de clase y los laboratorios prácticos no se quedaron en diapositivas abstractas ni en fórmulas memorísticas; por el contrario, nos obligaron a sentarnos frente a la terminal, inicializar entornos en Node.js, gestionar paquetes, levantar servidores Express, dialogar con blockchains remotas de Ethereum y Solana, consultar grafos con GraphQL, orquestar múltiples microservicios financieros bajo condiciones de fallo, componer microfrontends satelitales con Web Components nativos y desplegar funciones sin servidor en el borde con Cloudflare Workers."
    )

    add_quote(
        "Un sistema distribuido es aquel en el que el fallo de una computadora que ni siquiera sabías que existía puede hacer que tu propia computadora quede inservible.",
        "Leslie Lamport (Premio Turing, citado en Tanenbaum & Van Steen, 2017)"
    )

    add_p(
        "La famosa cita de Leslie Lamport captura con exactitud la esencia de lo aprendido: construir sistemas distribuidos no consiste únicamente en enviar datos por la red, sino en aprender a gobernar la incertidumbre, la asincronía y el fallo inevitable. Este ensayo tiene como propósito tejer un hilo conductor sólido entre los conceptos teóricos plasmados en las pizarras virtuales del curso y las lecciones vivenciales acumuladas en los laboratorios de código, contrastando nuestros hallazgos con la literatura seminal de la ingeniería de software y las ciencias de la computación."
    )

    # ==========================================
    # SECCIÓN 2
    # ==========================================
    add_h1("2. Fundamentos y Fronteras: Arquitectura vs. Sistema Operativo")

    add_p(
        "Una de las primeras discusiones cardinales de la Semana 1 giró en torno a delimitar tres conceptos que en la industria se mezclan con ligereza pero que conceptualmente pertenecen a dimensiones distintas: los Sistemas Distribuidos, los Microservicios y la Programación Web.",
        bold_prefix="Desmitificando las fronteras conceptuales: "
    )

    add_p(
        "En las pizarras de clase se definió con claridad que un Sistema Distribuido describe una arquitectura y un conjunto de computadoras autónomas que cooperan entre sí para presentarse ante los usuarios como un único sistema coherente. Su objetivo fundamental es repartir el procesamiento, el almacenamiento y los recursos de hardware, permitiendo que un servidor de matrícula, uno de biblioteca y uno de autenticación compartan la carga sin que el usuario perciba las costuras del sistema (Tanenbaum & Van Steen, 2017; Coulouris et al., 2012). Por otro lado, los Microservicios representan un estilo arquitectónico de diseño de software en el que una aplicación de gran tamaño se descompone intencionalmente en servicios pequeños, independientes y con bajo acoplamiento que se comunican mediante contratos e interfaces como APIs (Fowler, 2014). Por último, la Programación Web es simplemente el canal tecnológico y de presentación mediante el cual los usuarios finales acceden a esas aplicaciones a través de un navegador y protocolos estándar como HTTP o HTTPS."
    )

    add_p(
        "Una conclusión vital de nuestra primera semana de análisis fue responder a dos preguntas estratégicas: ¿Toda Arquitectura Distribuida es un Sistema Distribuido? La respuesta es rotunda: no. Una arquitectura puede quedarse como un elegante diagrama conceptual en papel o en Figma. En contraste, ¿todo Sistema Distribuido necesita de una arquitectura? Definitivamente sí; todo sistema distribuido en funcionamiento encarna una arquitectura operativa, ya sea deliberada y robusta o accidental y caótica."
    )

    # Tabla 1: Comparativa Conceptual
    p_t1 = doc.add_paragraph()
    p_t1.paragraph_format.space_before = Pt(8)
    p_t1.paragraph_format.space_after = Pt(4)
    r_t1 = p_t1.add_run("Tabla 1. Diferencias esenciales entre Paradigmas de Software según lo analizado en clase")
    r_t1.bold = True
    r_t1.font.size = Pt(10)

    table1 = doc.add_table(rows=4, cols=4)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    table1.autofit = False
    set_table_borders(table1, "000000", "8")

    col_widths = [Inches(1.3), Inches(1.7), Inches(1.8), Inches(1.7)]

    headers1 = ["Paradigma", "¿Qué Describe?", "Objetivo Principal", "Ejemplo Representativo"]
    row_hdr = table1.rows[0]
    for i, h in enumerate(headers1):
        cell = row_hdr.cells[i]
        cell.width = col_widths[i]
        set_cell_background(cell, "1A1A1A")
        set_cell_margins(cell, 140, 140, 160, 160)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    data1 = [
        ("Sistemas Distribuidos", "Arquitectura e infraestructura física/lógica interconectada.", "Distribuir cómputo, almacenamiento y carga entre múltiples máquinas.", "Nodos cooperativos de autenticación, matrícula y finanzas universitarias."),
        ("Microservicios", "Estilo arquitectónico de organización del software.", "Dividir una aplicación monolítica en servicios pequeños y autónomos.", "Servicio independiente de pagos, catálogo, usuarios y logística."),
        ("Programación Web", "Capa de entrega y desarrollo accesible por navegador.", "Proveer interfaces accesibles sobre la red mediante HTTP/HTTPS.", "Frontend en HTML/JS consumiendo endpoints REST mediante fetch/Axios.")
    ]

    for row_idx, row_data in enumerate(data1, start=1):
        row = table1.rows[row_idx]
        for col_idx, val in enumerate(row_data):
            cell = row.cells[col_idx]
            cell.width = col_widths[col_idx]
            set_cell_background(cell, "FFFFFF" if row_idx % 2 != 0 else "F9F9F9")
            set_cell_margins(cell, 100, 100, 120, 120)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx > 0 else WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(9)
            if col_idx == 0:
                r.bold = True

    add_p(
        "Como señalan Coulouris et al. (2012), la esencia de un sistema distribuido radica en atributos no funcionales críticos: transparencia (hacer invisible la distribución al usuario), escalabilidad horizontal (agregar más servidores en lugar de sobredimensionar uno solo), tolerancia a fallos y concurrencia. En nuestros primeros laboratorios, aterrizamos esto en Node.js, comprendiendo el rol del archivo package.json para declarar dependencias, package-lock.json como cerrojo de versiones determinista y node_modules como repositorio local de librerías. Al simular persistencia con archivos de texto (usuarios.txt) y autenticación básica, sentamos las bases para comprender que un servidor web es solo el portal de entrada a un universo distribuido mucho más amplio."
    )

    # ==========================================
    # SECCIÓN 3
    # ==========================================
    add_h1("3. El Lenguaje de la Red: Anatomía de Protocolos y el Salto a RPC")

    add_p(
        "En la Semana 2 y 3 nos adentramos en el núcleo de la comunicación distribuida: los protocolos. Sin un acuerdo estricto y compartido, dos nodos en una red son incapaces de entenderse. En clase desglosamos los elementos irrenunciables de cualquier protocolo: la sintaxis (el formato y estructura de los datos transmitidos), la semántica (el significado asignado a cada campo y código de control), la temporización (el orden, cadencia y sincronización de los mensajes), el control de errores, el control de flujo y la seguridad.",
        bold_prefix="¿Qué es un protocolo y por qué importa? "
    )

    add_p(
        "Durante años, la arquitectura REST (Representational State Transfer), formalizada por Roy Fielding en su tesis doctoral del año 2000, ha sido el estándar de facto para la web. REST propone una visión centrada en recursos sustantivos (`/usuarios/10`), aprovechando los verbos semánticos de HTTP (`GET`, `POST`, `PUT`, `DELETE`), y promoviendo el desacoplamiento mediante respuestas en formato JSON. No obstante, en la Semana 3 nos enfrentamos a un paradigma alternativo de enorme vigencia en entornos de alto rendimiento y redes descentralizadas: el modelo RPC (Remote Procedure Call).",
        bold_prefix="REST vs. RPC: La dicotomía entre Recursos y Acciones: "
    )

    add_quote(
        "El objetivo principal de RPC es hacer que la computación distribuida sea fácil de programar, permitiendo que el llamado a un procedimiento remoto tenga la misma sintaxis y apariencia que un llamado a un procedimiento local en la misma máquina.",
        "Andrew Birrell & Bruce Nelson (1984, pioneros del diseño de RPC)"
    )

    add_p(
        "En el Laboratorio 1 (s1SDRPC-lab1) experimentamos de primera mano esta diferencia al conectarnos con dos de las redes blockchain más grandes del mundo: Ethereum y Solana. A diferencia de una API REST tradicional donde consultaríamos una URL jerárquica, aquí invocamos directamente métodos remotos empaquetados en solicitudes JSON-RPC 2.0 mediante peticiones HTTP POST."
    )

    add_p(
        "El código desarrollado en `services/rpcService.js` requirió construir objetos estructurados con cuatro propiedades fundamentales: `jsonrpc: '2.0'`, `method`, `params` e `id`. Para Ethereum solicitamos el método `eth_blockNumber` para obtener el número de bloque más reciente; para Solana invocamos `getEpochInfo` con el parámetro de compromiso `{ commitment: 'finalized' }`. En ambos casos, el servidor Express actuó como intermediario orquestador entre el navegador y los nodos descentralizados remotos."
    )

    # Tabla 2: REST vs RPC
    p_t2 = doc.add_paragraph()
    p_t2.paragraph_format.space_before = Pt(8)
    p_t2.paragraph_format.space_after = Pt(4)
    r_t2 = p_t2.add_run("Tabla 2. Matriz comparativa entre la Arquitectura REST y el Modelo RPC")
    r_t2.bold = True
    r_t2.font.size = Pt(10)

    table2 = doc.add_table(rows=6, cols=3)
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    table2.autofit = False
    set_table_borders(table2, "000000", "8")

    col_w2 = [Inches(1.8), Inches(2.3), Inches(2.4)]
    headers2 = ["Criterio Técnico", "Arquitectura REST", "Modelo RPC (JSON-RPC / gRPC)"]

    for i, h in enumerate(headers2):
        cell = table2.rows[0].cells[i]
        cell.width = col_w2[i]
        set_cell_background(cell, "1A1A1A")
        set_cell_margins(cell, 140, 140, 160, 160)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    data2 = [
        ("Filosofía Central", "Orientada a Recursos (Entidades, Sustantivos).", "Orientada a Procedimientos / Acciones (Verbos, Métodos)."),
        ("Identificador de Operación", "URI semántica (ej. /usuarios/10).", "Nombre del método en el payload (ej. eth_blockNumber)."),
        ("Uso de Verbos HTTP", "Aprovecha verbos uniformes: GET, POST, PUT, DELETE.", "Casi invariablemente utiliza POST como túnel de transporte."),
        ("Parámetros y Entrada", "Headers, Path variables, Query strings y Request Body.", "Matriz o diccionario unificado dentro del campo 'params'."),
        ("Estructura de Respuesta", "Cuerpo JSON genérico con códigos HTTP semánticos.", "Envoltorio estandarizado: { jsonrpc, result, error, id }.")
    ]

    for row_idx, row_data in enumerate(data2, start=1):
        row = table2.rows[row_idx]
        for col_idx, val in enumerate(row_data):
            cell = row.cells[col_idx]
            cell.width = col_w2[col_idx]
            set_cell_background(cell, "FFFFFF" if row_idx % 2 != 0 else "F9F9F9")
            set_cell_margins(cell, 100, 100, 120, 120)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx > 0 else WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(9)
            if col_idx == 0:
                r.bold = True

    add_p(
        "Uno de los grandes aprendizajes de esta práctica fue el concepto de wrapping de errores. En sistemas distribuidos, una llamada remota puede responder con un código de transporte exitoso (`HTTP 200 OK`), pero contener en su interior un error categórico de procesamiento (`{ error: { code: -32601, message: 'Method not found' } }`). Si el desarrollador únicamente valida `respuesta.ok`, comete el grave error de dar por buena una operación fallida. Esto nos enseñó que la disponibilidad del canal físico y la validez de los datos son dos capas de diagnóstico totalmente disjuntas."
    )

    # ==========================================
    # SECCIÓN 4
    # ==========================================
    add_h1("4. El Dilema de la Ingesta de Datos: De REST y Over-fetching a la Precisión de GraphQL")

    add_p(
        "A medida que un sistema distribuido madura, surge una tensión inevitable entre el oferente (el servidor que expone información) y el consumidor (el cliente o aplicación que ingesta datos). En la Semana 4 nos planteamos dos preguntas estratégicas que marcan el diseño de arquitecturas de datos modernas: desde la perspectiva del consumidor, ¿cómo reduzco la cantidad de llamadas a la red y el volumen de datos descargados sin degradar la experiencia de usuario? Y desde la perspectiva del oferente, ¿cómo mantengo un rendimiento óptimo sin sobrecargar mis procesadores atendiendo peticiones redundantes?",
        bold_prefix="La economía del ancho de banda y las llamadas de red: "
    )

    add_p(
        "Las arquitecturas REST convencionales sufren con frecuencia de dos males endémicos: el over-fetching y el under-fetching (Kleppmann, 2017). El over-fetching ocurre cuando un endpoint devuelve un objeto colosal con decenas de atributos innecesarios para la vista actual (desperdicio de ancho de banda y batería en dispositivos móviles). El under-fetching ocurre cuando un solo endpoint no entrega suficiente información, obligando al cliente a realizar múltiples peticiones secuenciales encadenadas (problema N+1) para poder renderizar una sola pantalla."
    )

    add_p(
        "En el Laboratorio 2 (s4SD-lab2) exploramos cómo GraphQL resuelve de raíz este dilema arquitectónico mediante consultas declarativas donde el cliente especifica con precisión milimétrica los campos requeridos. Consumimos dos servicios públicos de GraphQL: la API de países de Trevor Blades y la API de Rick and Morty. En lugar de recibir cientos de propiedades de cada país o personaje, construimos consultas personalizadas:",
        bold_prefix="Experimentación práctica con GraphQL en Express: "
    )

    add_p(
        "query { countries { code name emoji capital currency } }",
        italic=True
    )

    add_p(
        "Comprobamos que GraphQL, al igual que RPC, viaja sobre peticiones HTTP POST hacia un único endpoint (`/graphql`), empaquetando la consulta dentro del cuerpo de la petición. Esto representó un cambio de mentalidad: en REST pensamos '¿qué recurso quiero consultar?', mientras que en GraphQL la pregunta orientadora es '¿qué datos exactos necesito consumir?'. Además, en la discusión teórica de clase contrastamos el uso de GraphQL Subscriptions (comunicación reactiva bidireccional sobre WebSockets orientada a eventos) con los Cron Jobs tradicionales de servidor (tareas programadas y periódicas orientadas a intervalos de tiempo), comprendiendo que cada mecanismo responde a patrones temporales completamente distintos."
    )

    # ==========================================
    # SECCIÓN 5
    # ==========================================
    add_h1("5. La Cruda Realidad del Entorno Distribuido: Resiliencia y la Falacia del 'Simple Try-Catch'")

    add_p(
        "Si tuviera que señalar el laboratorio que supuso el mayor quiebre entre la programación académica convencional y la ingeniería de sistemas distribuidos real, ese fue sin duda el Laboratorio 3 (s5SD-lab3), enfocado en la orquestación de servicios financieros y consumo de APIs de terceros (CoinGecko y Frankfurter). Fue allí donde nos enfrentamos a la pregunta crucial planteada por el docente: ¿Es el manejo de errores `try-catch` del módulo de servicios igual al de las rutas?",
        bold_prefix="El mito del try-catch universal: "
    )

    add_p(
        "La respuesta descubierta en el código fue un categórico NO. En un entorno monolítico local, un bloque `try-catch` genérico suele ser suficiente para atrapar excepciones. Pero en sistemas distribuidos, las fallas son heterogéneas, parciales y multinivel.",
        bold_prefix="Diferenciación arquitectónica entre Capas de Servicio y Rutas: "
    )

    # Tabla 3: Try-Catch Services vs Routes
    p_t3 = doc.add_paragraph()
    p_t3.paragraph_format.space_before = Pt(8)
    p_t3.paragraph_format.space_after = Pt(4)
    r_t3 = p_t3.add_run("Tabla 3. Responsabilidades y tratamiento de excepciones según la capa arquitectónica")
    r_t3.bold = True
    r_t3.font.size = Pt(10)

    table3 = doc.add_table(rows=5, cols=3)
    table3.alignment = WD_TABLE_ALIGNMENT.CENTER
    table3.autofit = False
    set_table_borders(table3, "000000", "8")

    col_w3 = [Inches(1.8), Inches(2.3), Inches(2.4)]
    headers3 = ["Criterio de Evaluación", "Capa de Servicios (services/)", "Capa de Rutas / Controladores (routes/)"]

    for i, h in enumerate(headers3):
        cell = table3.rows[0].cells[i]
        cell.width = col_w3[i]
        set_cell_background(cell, "1A1A1A")
        set_cell_margins(cell, 140, 140, 160, 160)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    data3 = [
        ("Nivel y Rol Arquitectónico", "Capa de Negocio e Integración Externa con terceros.", "Frontera HTTP, ruteo y presentación hacia el cliente."),
        ("Comportamiento ante fetch()", "Un HTTP 404, 429 o 500 no cae en el catch. Exige validar if (!respuesta.ok) explícito.", "Envuelve la llamada al servicio para evitar que una excepción no controlada tumbe Express."),
        ("Objetivo del Diagnóstico", "Forense y distribuido: registrar URL, latencia, status HTTP y cuerpo crudo del proveedor.", "Estructural: responder al cliente con un status code adecuado (500, 400) y un JSON limpio."),
        ("Manejo de la Excepción", "Registra el detalle y hace re-throw (throw error) para permitir tolerancia orquestada.", "Captura el error final devuelto por el servicio y ejecuta res.status(500).json({ error }).")
    ]

    for row_idx, row_data in enumerate(data3, start=1):
        row = table3.rows[row_idx]
        for col_idx, val in enumerate(row_data):
            cell = row.cells[col_idx]
            cell.width = col_w3[col_idx]
            set_cell_background(cell, "FFFFFF" if row_idx % 2 != 0 else "F9F9F9")
            set_cell_margins(cell, 100, 100, 120, 120)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx > 0 else WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(val)
            r.font.size = Pt(9)
            if col_idx == 0:
                r.bold = True

    add_quote(
        "Todo falla, todo el tiempo. La resiliencia no consiste en pretender que los componentes nunca colapsen, sino en diseñar el sistema para que siga operando con dignidad cuando los componentes fallen.",
        "Werner Vogels (CTO de Amazon, 2006)"
    )

    add_p(
        "El segundo gran pilar aprendido en este laboratorio fue el contraste entre `Promise.all` y `Promise.allSettled`. Si en nuestra aplicación financiera hubiésemos utilizado `Promise.all`, la falla temporal o el bloqueo por límite de peticiones (Rate Limit 429) de CoinGecko al consultar el precio de Bitcoin habría provocado el rechazo inmediato de toda la promesa, cancelando también la consulta de tasas de cambio de Frankfurter. En cambio, mediante el uso de `Promise.allSettled`, logramos que cada servicio resuelva de manera aislada; pudimos evaluar si el estado fue 'fulfilled' o 'rejected', permitiendo que la interfaz mostrara la información disponible y desplegara un mensaje de error específico únicamente en el componente afectado. Esta técnica encarna fielmente el principio de tolerancia a fallos parciales.",
        bold_prefix="Resiliencia mediante Promise.allSettled: "
    )

    # ==========================================
    # SECCIÓN 6
    # ==========================================
    add_h1("6. Modularidad Radical: Contenedores, Principios de Diseño y Microfrontends con Shadow DOM")

    add_p(
        "En la Semana 6, el curso dio un salto conceptual de enorme madurez al integrar dos vertientes: los principios formales de los sistemas distribuidos y la extensión de la arquitectura distribuida hacia el frontend.",
        bold_prefix="Los 10 Principios Inviolables: "
    )

    add_p(
        "Repasamos diez mandamientos que todo arquitecto de software debe grabar en su ADN: diseñar para fallos (no solo probarlos), evitar dependencias síncronas innecesarias, delimitar fronteras claras entre servicios, exigir que cada servicio sea dueño exclusivo de sus datos y almacenamiento, garantizar la idempotencia en operaciones de red, aplicar timeouts explícitos para no retener conexiones infinitamente, incorporar observabilidad desde el día cero, gestionar la consistencia eventual frente a las limitaciones del teorema CAP (Brewer, 2012), asegurar la desplegabilidad independiente y erradicar el estado innecesario privilegiando arquitecturas stateless."
    )

    add_p(
        "Asimismo, desmitificamos la relación entre Microservicios y Contenedores: mientras que los microservicios son un concepto arquitectónico de descomposición lógica, los contenedores (Docker) son unidades físicas de empaquetamiento que encierran el código, sus dependencias y su configuración de ejecución. A su vez, orquestadores como Kubernetes permiten gestionar réplicas, escalabilidad automática y auto-recuperación de dichos contenedores en clústeres elásticos."
    )

    add_p(
        "Pero el hito más innovador fue trasladar esta filosofía al navegador mediante los Microfrontends (Geers, 2020; Jackson, 2019). Durante años, las empresas descompusieron sus backends en cientos de microservicios pero mantuvieron sus frontends como monstruosos monolitos difíciles de desplegar, coordinar y mantener. En el Laboratorio 4 (s6SD-lab4) rompimos con esa inercia utilizando datos satelitales reales de la NASA: la API NASA POWER para radiación solar incidente y NASA GIBS para imágenes satelitales MODIS en color verdadero sobre Costa Rica.",
        bold_prefix="Microfrontends en la práctica con NASA GIBS y NASA POWER: "
    )

    add_p(
        "Implementamos cada tarjeta de visualización (`solar-card.js` y `satellite-card.js`) no como simples plantillas dependientes de un framework pesado, sino como Web Components nativos (`HTMLElement`, `customElements.define`) dotados de Shadow DOM (`attachShadow({ mode: 'open' })`). El Shadow DOM garantizó el encapsulamiento estricto de estilos y estructura interna: ningún estilo de la página principal afecta al componente, y ningún estilo del componente contamina al resto de la interfaz. De este modo, cada microfrontend puede tener su propio ciclo de vida, su propio versionamiento y su propio mecanismo de consulta al backend intermediario en Express.",
        bold_prefix="El rol del Shadow DOM como frontera de aislamiento: "
    )

    # ==========================================
    # SECCIÓN 7
    # ==========================================
    add_h1("7. La Frontera del Cómputo: Paradigma Serverless, FaaS y Edge Computing")

    add_p(
        "La cúspide de nuestro trayecto práctico llegó en el Laboratorio 5 (s7SD-lab5), donde abordamos la evolución más reciente de la computación distribuida en la nube: la computación sin servidor (Serverless) y las Funciones como Servicio (FaaS).",
        bold_prefix="De servidores permanentes a cómputo efímero en el borde: "
    )

    add_p(
        "Durante décadas, el modelo dominante consistió en aprovisionar máquinas virtuales o instancias de servidores que permanecían encendidas las 24 horas del día, devorando energía y costos incluso cuando la demanda era nula. El paradigma Serverless subvierte esta lógica: el desarrollador ya no administra servidores físicos ni contenedores permanentes; simplemente escribe funciones atómicas y autónomas que son instanciadas por la infraestructura en milisegundos únicamente cuando ocurre un evento específico (Castro et al., 2019)."
    )

    add_p(
        "En nuestra práctica trabajamos con Cloudflare Workers, una tecnología pionera que corre sobre V8 Isolates distribuidos en cientos de centros de datos alrededor del planeta (Edge Computing). Al ejecutar el código en el 'borde' de la red, la latencia entre el usuario final y la función de procesamiento se reduce a valores ínfimos.",
        bold_prefix="Arquitectura dirigida por eventos y disparadores programados: "
    )

    add_p(
        "El Laboratorio 5 nos permitió conectar nuestra interfaz local con el worker desplegado (`cloud-worker.fullengineer90253.workers.dev`), explorando tres pilares operativos fundamentales: primero, el enfoque dirigido por eventos (Event-Driven), donde una petición HTTP desencadena la ejecución instantánea del worker; segundo, la propiedad de responsabilidad única de las funciones, donde cada endpoint resuelve una tarea concreta y devuelve su resultado de manera stateless; y tercero, los planificadores temporales (Cron Triggers), en los cuales la plataforma de Cloudflare ejecuta periódicamente la función `scheduled()` sin intervención humana, permitiendo tareas de limpieza, sincronización o consolidación de datos en segundo plano."
    )

    # ==========================================
    # SECCIÓN 8
    # ==========================================
    add_h1("8. Síntesis y Conclusiones: Lecciones Aprendidas al Pie de la Máquina")

    add_p(
        "Al mirar en retrospectiva las pizarras virtuales y los cinco laboratorios desarrollados, queda claro que este curso no ha sido simplemente una materia más sobre desarrollo de software, sino una auténtica transformación en nuestra forma de razonar sobre los sistemas informáticos. Hemos transitado desde las preguntas conceptuales más elementales sobre qué distingue a un sistema distribuido, hasta la implementación de patrones de resiliencia avanzada, modularidad en el frontend y cómputo serverless en el edge.",
        bold_prefix="Un cambio irreversible en el criterio de ingeniería: "
    )

    add_p(
        "Podemos resumir las bases fundamentales asimiladas en cinco lecciones indelebles:",
        bold_prefix="Pilares rectores de nuestra formación distribuida: "
    )

    conclusiones = [
        ("1. La red es inherentemente hostil y no determinista: ", "Las suposiciones de latencia cero, ancho de banda infinito y redes seguras son mitos peligrosos. El código debe asumir que cualquier llamada remota puede retrasarse, fallar o responder con errores envueltos."),
        ("2. El protocolo define el destino del sistema: ", "Elegir entre REST, RPC o GraphQL no es una cuestión de moda, sino una decisión estratégica de arquitectura que impacta el uso de red, el acoplamiento y el rendimiento tanto del oferente como del consumidor."),
        ("3. La tolerancia a fallos debe orquestarse en capas: ", "Un simple try-catch no rescata un sistema distribuido. Se requiere validación explícita de protocolos en los servicios, propagación controlada y patrones de degradación grácil como Promise.allSettled."),
        ("4. La distribución alcanza a todas las capas del stack: ", "La arquitectura distribuida no termina en el servidor de base de datos; se proyecta hacia la interfaz de usuario mediante microfrontends y Web Components aislados con Shadow DOM."),
        ("5. El futuro es efímero, orientado a eventos y cercano al usuario: ", "El auge de FaaS y Edge Computing demuestra que la infraestructura moderna avanza hacia la eliminación del estado innecesario, la facturación por ejecución y la dispersión geográfica del cómputo.")
    ]

    for pref, body in conclusiones:
        add_p(body, bold_prefix=pref)

    add_p(
        "En definitiva, las bases aprendidas en este curso nos dejan una lección primordial: en la era de los sistemas distribuidos, la excelencia de un ingeniero de software no se mide por su capacidad de construir sistemas que nunca fallen en un entorno perfecto, sino por su lucidez para diseñar arquitecturas que continúen operando de manera digna, predecible y elegante en un mundo inevitablemente imperfecto."
    )

    # ==========================================
    # SECCIÓN 9: REFERENCIAS (APA 7ma Edición)
    # ==========================================
    add_h1("9. Referencias Bibliográficas (Normativa APA 7ma Edición)")

    refs = [
        "Birrell, A. D., & Nelson, B. J. (1984). Implementing remote procedure calls. ACM Transactions on Computer Systems (TOCS), 2(1), 39–59. https://doi.org/10.1145/2080.357392",
        "Brewer, E. A. (2012). CAP twelve years later: How the 'rules' have changed. Computer, 45(2), 23–29. https://doi.org/10.1109/MC.2012.37",
        "Castro, P., Ishakian, V., Muthusamy, V., & Slominski, A. (2019). The rise of serverless computing. Communications of the ACM, 62(12), 44–54. https://doi.org/10.1145/3368454",
        "Coulouris, G., Dollimore, J., Kindberg, T., & Blair, G. (2012). Distributed systems: concepts and design (5th ed.). Addison-Wesley.",
        "Fielding, R. T. (2000). Architectural styles and the design of network-based software architectures (Doctoral dissertation, University of California, Irvine). Information and Computer Science.",
        "Fowler, M. (2014). Microservices: a definition of this new architectural term. MartinFowler.com. https://martinfowler.com/articles/microservices.html",
        "Geers, M. (2020). Micro frontends in action. Manning Publications.",
        "Jackson, C. (2019). Micro frontends: Extending the microservice idea to frontend development. MartinFowler.com. https://martinfowler.com/articles/micro-frontends.html",
        "Kleppmann, M. (2017). Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems. O'Reilly Media.",
        "Lamport, L. (1978). Time, clocks, and the ordering of events in a distributed system. Communications of the ACM, 21(7), 558–565. https://doi.org/10.1145/359545.359563",
        "Tanenbaum, A. S., & Van Steen, M. (2017). Distributed systems: principles and paradigms (3rd ed.). CreateSpace Independent Publishing Platform.",
        "Vogels, W. (2009). Eventually consistent. Communications of the ACM, 52(1), 40–44. https://doi.org/10.1145/1435417.1435432"
    ]

    for ref in refs:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Inches(0.5)
        p.paragraph_format.first_line_indent = Inches(-0.5)  # Sangría francesa (Hanging indent)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(ref)
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(30, 30, 30)

    doc.save(output_path)
    print(f"Document successfully created at: {output_path}")

if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    output_docx = current_dir / "ensayo_bases_sistemas_distribuidos.docx"
    create_essay_document(str(output_docx))
