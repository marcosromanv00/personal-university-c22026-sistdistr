// =====================================================
// SERVIDOR EXPRESS
// =====================================================
 
// Importamos Express.
const express = require("express");
 
// Importamos path para manejar rutas.
const path = require("path");
 
// Creamos la aplicación Express.
const app = express();
 
// Puerto local.
const PORT = 3000;
 
 
// =====================================================
// ARCHIVOS ESTÁTICOS
// =====================================================
 
// La carpeta public contiene:
//
// - CSS
// - JavaScript del navegador
//
// Express permitirá acceder a estos archivos.
app.use(
    express.static(
        path.join(__dirname, "public")
    )
);
 
 
// =====================================================
// RUTA PRINCIPAL
// =====================================================
 
// Cuando el usuario entra a:
//
// http://localhost:3000
//
// Express devuelve la interfaz gráfica.
app.get("/", (req, res) => {
 
    res.sendFile(
        path.join(
            __dirname,
            "views",
            "index.html"
        )
    );
 
});
 
 
// =====================================================
// INICIO DEL SERVIDOR
// =====================================================
 
app.listen(PORT, () => {
 
    console.log("==============================");
 
    console.log("Frontend ejecutándose en:");
 
    console.log(
        `http://localhost:${PORT}`
    );
 
    console.log("==============================");
 
});