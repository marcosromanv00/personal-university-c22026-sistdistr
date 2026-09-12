const express = require("express");
const path = require("path");
 
const graphqlRoutes = require("./routes/graphqlRoutes");
 
const app = express();
 
const PORT = 3000;
 
// Permite recibir información JSON
app.use(express.json());
 
// Servir archivos estáticos
app.use(express.static(path.join(__dirname, "public")));
 
// Servir la vista HTML
app.use(express.static(path.join(__dirname, "views")));
 
// Rutas relacionadas con GraphQL
app.use("/api", graphqlRoutes);
 
// Página principal
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "views", "index.html"));
});
 
// Iniciar servidor
app.listen(PORT, () => {
    console.log(`Servidor ejecutándose en http://localhost:${PORT}`);
});