const express = require("express");
 
const {
    obtenerPaises,
    obtenerPersonajes
} = require("../services/graphqlService");
 
const router = express.Router();
 
 
// ============================================
// GET /api/paises
// ============================================
 
router.get("/paises", async (req, res) => {
 
    try {
 
        const datos = await obtenerPaises();
 
        res.json(datos);
 
    } catch (error) {
 
        console.error("Error obteniendo países:", error);
 
        res.status(500).json({
            error: "No fue posible obtener los países"
        });
    }
});
 
 
// ============================================
// GET /api/personajes
// ============================================
 
router.get("/personajes", async (req, res) => {
 
    try {
 
        const datos = await obtenerPersonajes();
 
        res.json(datos);
 
    } catch (error) {
 
        console.error("Error obteniendo personajes:", error);
 
        res.status(500).json({
            error: "No fue posible obtener los personajes"
        });
    }
});
 
 
module.exports = router;