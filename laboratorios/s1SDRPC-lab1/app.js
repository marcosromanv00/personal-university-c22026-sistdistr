const express = require("express");
const path = require("path");
 
const rpcRoutes = require("./routes/rpcRoutes");
 
const app = express();
 
const PORT = process.env.PORT || 3000;
 
// Middleware para archivos estáticos
app.use(express.static(path.join(__dirname, "public")));
 
// Rutas RPC
app.use("/", rpcRoutes);
 
// Iniciar servidor
app.listen(PORT, () => {
    console.log(`Servidor ejecutándose en http://localhost:${PORT}`);
});