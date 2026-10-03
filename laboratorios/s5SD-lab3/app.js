const express = require("express");
const path = require("path");
 
const finanzasRoutes = require("./routes/finanzasRoutes");
 
const app = express();
 
const PORT = 3000;
 
 
// ==========================================
// MIDDLEWARE
// ==========================================
 
// Permite recibir JSON
app.use(express.json());
 
 
// Archivos CSS y JavaScript
app.use(
    express.static(
        path.join(__dirname, "public")
    )
);
 
 
// ==========================================
// PUBLICACIÓN DE LA VISTA
// ==========================================
 
app.get("/", (req, res) => {  
 
    res.sendFile(
        path.join(
            __dirname,
            "views",
            "index.html"
        )
    );
 
});
 
 
// ==========================================
// PUBLICACIÓN DE SERVICIOS
// ==========================================
 
app.use(
    "/api/finanzas",
    finanzasRoutes
);
 
 
// ==========================================
// INICIO DEL SERVIDOR
// ==========================================
 
app.listen(PORT, () => {
 
    console.log(
        `Servidor ejecutándose en http://localhost:${PORT}`
    );
 
});