const express = require("express");
 
const fs = require("fs");
 
const path = require("path");
 
const {
 
    obtenerInformacionFinanciera
 
} = require("../services/finanzasService");
 
 
const router = express.Router();
 
 
// ==================================================
// SERVICIO 1 DE NUESTRA APLICACIÓN
// GET /api/finanzas
// ==================================================
 
router.get("/", async (req, res) => {
 
    try {
 
        const datos =
            await obtenerInformacionFinanciera();
 
        res.json(datos);
 
    }
    catch (error) {
 
        console.error(error);
 
        res.status(500).json({
 
            error:
                "No fue posible obtener información financiera"
 
        });
    }
});
 
 
// ==================================================
// SERVICIO 2 DE NUESTRA APLICACIÓN
// POST /api/finanzas/guardar
// ==================================================
 
router.post("/guardar", (req, res) => {
 
    try {
 
        const datos = req.body;
 
 
        const carpetaData =
            path.join(
                __dirname,
                "..",
                "data"
            );
 
 
        const archivo =
            path.join(
                carpetaData,
                "historial.txt"
            );
 
 
        // Crear carpeta si no existe
 
        if (!fs.existsSync(carpetaData)) {
 
            fs.mkdirSync(carpetaData);
 
        }
 
 
        // Información que será almacenada
 
        const contenido = `
 
========================================
REGISTRO FINANCIERO
========================================
 
Fecha:
${datos.fecha}
 
 
BITCOIN
----------------------------------------
Servicio: ${datos.bitcoin.servicio}
Código: ${datos.bitcoin.codigo}
Precio USD: ${datos.bitcoin.precioUSD}
 
 
ETHEREUM
----------------------------------------
Servicio: ${datos.ethereum.servicio}
Código: ${datos.ethereum.codigo}
Precio USD: ${datos.ethereum.precioUSD}
 
 
TIPO DE CAMBIO
----------------------------------------
Servicio: ${datos.tipoCambio.servicio}
${datos.tipoCambio.origen} -> ${datos.tipoCambio.destino}
Tipo de cambio: ${datos.tipoCambio.tipoCambio}
 
 
========================================
 
`;
 
 
        fs.appendFileSync(
 
            archivo,
 
            contenido,
 
            "utf8"
 
        );
 
 
        res.json({
 
            mensaje:
                "Información guardada correctamente"
 
        });
 
    }
    catch (error) {
 
        console.error(error);
 
        res.status(500).json({
 
            error:
                "No se pudo guardar la información"
 
        });
 
    }
 
});
 
 
module.exports = router;