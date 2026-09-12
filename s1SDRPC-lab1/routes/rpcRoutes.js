const express = require("express");
const path = require("path");
 
const {
    obtenerEthereum,
    obtenerSolana
} = require("../services/rpcService");
 
const router = express.Router();
 
 
// ======================================================
// PÁGINA PRINCIPAL
// ======================================================
 
router.get("/", (req, res) => {
 
    res.sendFile(
        path.join(
            __dirname,
            "../views/index.html"
        )
    );
 
});
 
 
// ======================================================
// API INTERNA
// ======================================================
 
router.get("/api/rpc", async (req, res) => {
 
    let ethereum;
    let solana;
 
 
    // ==================================================
    // RPC #1 - ETHEREUM
    // ==================================================
 
    try {
 
        console.log("");
        console.log("========================================");
        console.log("EJECUTANDO RPC #1 - ETHEREUM");
        console.log("========================================");
 
        ethereum =
            await obtenerEthereum();
 
    }
    catch (error) {
 
        console.error(
            "Error Ethereum:",
            error.message
        );
 
        ethereum = {
 
            error: error.message
 
        };
 
    }
 
 
    // ==================================================
    // RPC #2 - SOLANA
    // ==================================================
 
    try {
 
        console.log("");
        console.log("========================================");
        console.log("EJECUTANDO RPC #2 - SOLANA");
        console.log("========================================");
 
        solana =
            await obtenerSolana();
 
    }
    catch (error) {
 
        console.error(
            "Error Solana:",
            error.message
        );
 
        solana = {
 
            error: error.message
 
        };
 
    }
 
 
    // ==================================================
    // RESPUESTA AL NAVEGADOR
    // ==================================================
 
    res.json({
 
        ethereum: ethereum,
 
        solana: solana
 
    });
 
});
 
 
// ======================================================
// EXPORTAR ROUTER
// ======================================================
 
module.exports = router;