# Análisis de Código, Arquitectura y Formato de Desarrollo
**Curso:** Sistemas Distribuidos  
**Laboratorio:** s5SD-lab3 (Finanzas y Consumo de Servicios Distribuidos)

---

## 1. Respuesta Directa: ¿El manejo `try-catch` del módulo de Servicios es igual al de las Rutas?

**No, no es igual.** Tienen propósitos, alcances y responsabilidades completamente distintas dentro de la arquitectura de sistemas distribuidos:

| Criterio | Módulo de Servicios (`services/`) | Módulo de Rutas (`routes/`) |
| :--- | :--- | :--- |
| **Nivel / Capa** | Capa de Negocio e Integración Externa | Capa de Presentación / Controlador HTTP |
| **¿Basta un `try-catch` simple?** | **No.** En llamadas remotas (`fetch`), respuestas `404`, `429` (Rate Limit) o `500` **no caen en el `catch`**, por lo que se requiere validar explícitamente `if (!respuesta.ok)`. | **Sí.** El `try-catch` envuelve la ejecución para evitar que una excepción no controlada detenga el servidor Express. |
| **Objetivo Principal** | Diagnóstico distribuido (origen del fallo, latencia, respuesta cruda del proveedor externo) y transformación/resiliencia de datos. | Responder al cliente de nuestra API con el código HTTP adecuado (ej. `500 Internal Server Error`, `400 Bad Request`) y un mensaje limpio. |
| **Acción en el `catch`** | Imprime logs forenses específicos del servicio y hace **re-throw (`throw error`)** o permite el manejo por `Promise.allSettled`. | Captura el error final, registra en consola y ejecuta **`res.status(500).json(...)`**. |

### Detalle de Diferencias en Código:

#### A. En `services/finanzasService.js` (Consumo Distribuido y Diagnóstico Forense):
1. **Validación explícita de estado HTTP:**
   ```javascript
   const respuesta = await fetch(url);
   if (!respuesta.ok) {
       const detalle = await respuesta.text();
       // Log detallado con delimitadores para monitoreo distribuido
       console.error("========================================");
       console.error("ERROR EN SERVICIO BITCOIN");
       console.error("Servicio: CoinGecko");
       console.error("URL:", url);
       console.error("Código HTTP:", respuesta.status);
       console.error("Mensaje HTTP:", respuesta.statusText);
       console.error("Respuesta del servidor:", detalle);
       console.error("========================================");
       throw new Error(`Error consultando Bitcoin. HTTP ${respuesta.status}`);
   }
   ```
2. **Re-lanzamiento del error:**
   ```javascript
   } catch (error) {
       console.error("ERROR FINAL EN BITCOIN:", error.message);
       throw error; // Permite que el orquestador sepa que falló
   }
   ```
3. **Resiliencia con `Promise.allSettled`:** En lugar de `Promise.all` (donde un fallo aborta toda la petición), se usa `Promise.allSettled` para tolerar fallos parciales de terceros sin tumbar los otros servicios.

#### B. En `routes/finanzasRoutes.js` (Frontera HTTP de la API):
```javascript
router.get("/", async (req, res) => {
    try {
        const datos = await obtenerInformacionFinanciera();
        res.json(datos);
    } catch (error) {
        console.error(error);
        res.status(500).json({
            error: "No fue posible obtener información financiera"
        });
    }
});
```

---

## 2. Arquitectura del Proyecto y Separación de Responsabilidades

El proyecto utiliza una arquitectura modular basada en capas para aplicaciones Node.js / Express:

```
s5SD-lab3/
├── app.js                      # Punto de entrada, configuración de middlewares y montaje de rutas
├── package.json                # Dependencias (express) y scripts
├── routes/
│   └── finanzasRoutes.js       # Endpoints HTTP (GET, POST), validación de peticiones y respuestas
├── services/
│   └── finanzasService.js      # Consumo de APIs externas (CoinGecko, Frankfurter), orquestación y tolerancia a fallos
├── data/
│   └── historial.txt           # Persistencia local (creado dinámicamente)
├── public/                     # Recursos estáticos (CSS, JS cliente)
└── views/
    └── index.html              # Interfaz de usuario servida
```

### Roles de cada capa:
1. **`app.js` (Configurador Global):**
   - Inicializa Express y define el puerto (`PORT = 3000`).
   - Registra middlewares esenciales (`express.json()`, `express.static()`).
   - Sirve la vista principal (`GET /` -> `views/index.html`).
   - Monta los prefijos de rutas (ej. `/api/finanzas` -> `finanzasRoutes`).

2. **`routes/` (Controladores de Entrada/Salida):**
   - Define los verbos HTTP (`router.get`, `router.post`).
   - No contiene lógica pesada de consumo externo; delega al módulo de servicios.
   - Maneja operaciones de I/O directo como lectura/escritura de archivos (`fs`).
   - Emite respuestas JSON estandarizadas con códigos de estado HTTP.

3. **`services/` (Lógica de Negocio y Consumo Distribuido):**
   - Funciones asíncronas dedicadas por cada microservicio/API de terceros (`obtenerBitcoin`, `obtenerEthereum`, `obtenerTipoCambio`).
   - Manejo exhaustivo de protocolos distribuidos (URLs, cabeceras, códigos HTTP externos).
   - Orquestación con `Promise.allSettled` para entregar un consolidado estructurado con indicación de éxito o error individual.

---

## 3. Formato y Guía de Estilo del Profesor

Para programar en sintonía con las expectativas del docente, se deben seguir estas pautas observadas en su código:

### 1. Espaciado Vertical Extensivo ("Respiración" del Código)
El profesor utiliza un estilo muy visual y espacioso:
- Líneas en blanco entre declaraciones, llaves y parámetros.
- Desglose de argumentos y objetos en múltiples líneas.
- Formato de cadenas largas concatenadas en varias líneas:
  ```javascript
  const url =
      "https://api.coingecko.com/api/v3/simple/price" +
      "?ids=bitcoin&vs_currencies=usd";
  ```

### 2. Banners y Separadores de Sección
Uso consistente de delimitadores de 40 a 50 caracteres para organizar el archivo:
```javascript
// ==========================================
// NOMBRE DE LA SECCIÓN O SERVICIO
// ==========================================
```

### 3. Nomenclatura y Lenguaje
- **Idioma:** Todo el código (variables, funciones, mensajes de log y comentarios) está en **español**.
- **Funciones y Variables:** `camelCase` descriptivo (`obtenerInformacionFinanciera`, `carpetaData`, `precioUSD`).
- **Constantes de Configuración:** `UPPERCASE` (`PORT`).
- **Módulos:** Sintaxis **CommonJS** (`require` / `module.exports`).

### 4. Diagnóstico Forense y Trazabilidad en Consola
Al consumir servicios distribuidos, es obligatorio registrar datos clave para depuración:
- Nombre del servicio externo.
- URL invocada.
- Código y mensaje HTTP devuelto (`status`, `statusText`).
- Contenido textual de la respuesta en caso de error (`respuesta.text()`).

### 5. Resiliencia en Servicios Distribuidos
- Usar siempre `Promise.allSettled` cuando se consultan múltiples servicios independientes, mapeando cada resultado a un objeto con su valor resuelto o un objeto `{ error: reason.message }`.

---

## 4. Checklist para Nuevas Funcionalidades

Al desarrollar un nuevo endpoint o servicio en este laboratorio:

- [ ] ¿El consumo de la API externa está en `services/` y no directamente en `routes/`?
- [ ] ¿Se valida `if (!respuesta.ok)` tras el `fetch` antes de hacer `await respuesta.json()`?
- [ ] ¿Se implementó el log delimitado con URL, código HTTP y detalle del error?
- [ ] ¿La ruta en `routes/` está dentro de un bloque `try-catch` que retorne `res.status(500).json(...)` en caso de fallo?
- [ ] ¿El código mantiene la estructura espaciada y los encabezados `// ==========`?
- [ ] ¿Se exporta e importa con `CommonJS` (`module.exports` / `require`)?
