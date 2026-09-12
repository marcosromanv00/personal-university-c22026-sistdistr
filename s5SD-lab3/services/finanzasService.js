// ==========================================
// SERVICIO 1: BITCOIN
// ==========================================
 
async function obtenerBitcoin() {
 
    const url =
        "https://api.coingecko.com/api/v3/simple/price" +
        "?ids=bitcoin&vs_currencies=usd";
 
    try {
 
        const respuesta = await fetch(url);
 
        // Si el servidor responde con error HTTP
        if (!respuesta.ok) {
 
            const detalle = await respuesta.text();
 
            console.error(
                "========================================"
            );
 
            console.error(
                "ERROR EN SERVICIO BITCOIN"
            );
 
            console.error(
                "Servicio: CoinGecko"
            );
 
            console.error(
                "URL:",
                url
            );
 
            console.error(
                "Código HTTP:",
                respuesta.status
            );
 
            console.error(
                "Mensaje HTTP:",
                respuesta.statusText
            );
 
            console.error(
                "Respuesta del servidor:",
                detalle
            );
 
            console.error(
                "========================================"
            );
 
            throw new Error(
                `Error consultando Bitcoin. HTTP ${respuesta.status}`
            );
        }
 
        const datos = await respuesta.json();
 
        return {
 
            servicio: "CoinGecko",
 
            moneda: "Bitcoin",
 
            codigo: "BTC",
 
            precioUSD: datos.bitcoin.usd
 
        };
 
    } catch (error) {
 
        console.error(
            "ERROR FINAL EN BITCOIN:",
            error.message
        );
 
        throw error;
    }
}
 
 
// ==========================================
// SERVICIO 2: ETHEREUM
// ==========================================
 
async function obtenerEthereum() {
 
    const url =
        "https://api.coingecko.com/api/v3/simple/price" +
        "?ids=ethereum&vs_currencies=usd";
 
    try {
 
        const respuesta = await fetch(url);
 
        if (!respuesta.ok) {
 
            const detalle = await respuesta.text();
 
            console.error(
                "========================================"
            );
 
            console.error(
                "ERROR EN SERVICIO ETHEREUM"
            );
 
            console.error(
                "Servicio: CoinGecko"
            );
 
            console.error(
                "URL:",
                url
            );
 
            console.error(
                "Código HTTP:",
                respuesta.status
            );
 
            console.error(
                "Mensaje HTTP:",
                respuesta.statusText
            );
 
            console.error(
                "Respuesta del servidor:",
                detalle
            );
 
            console.error(
                "========================================"
            );
 
            throw new Error(
                `Error consultando Ethereum. HTTP ${respuesta.status}`
            );
        }
 
        const datos = await respuesta.json();
 
        return {
 
            servicio: "CoinGecko",
 
            moneda: "Ethereum",
 
            codigo: "ETH",
 
            precioUSD: datos.ethereum.usd
 
        };
 
    } catch (error) {
 
        console.error(
            "ERROR FINAL EN ETHEREUM:",
            error.message
        );
 
        throw error;
    }
}
 
 
// ==========================================
// SERVICIO 3: TIPO DE CAMBIO
// ==========================================
 
async function obtenerTipoCambio() {
 
    const url =
        "https://api.frankfurter.dev/v2/rate/USD/EUR";
 
    try {
 
        const respuesta = await fetch(url);
 
        if (!respuesta.ok) {
 
            const detalle = await respuesta.text();
 
            console.error(
                "========================================"
            );
 
            console.error(
                "ERROR EN SERVICIO TIPO DE CAMBIO"
            );
 
            console.error(
                "Servicio: Frankfurter"
            );
 
            console.error(
                "URL:",
                url
            );
 
            console.error(
                "Código HTTP:",
                respuesta.status
            );
 
            console.error(
                "Mensaje HTTP:",
                respuesta.statusText
            );
 
            console.error(
                "Respuesta del servidor:",
                detalle
            );
 
            console.error(
                "========================================"
            );
 
            throw new Error(
                `Error consultando tipo de cambio. HTTP ${respuesta.status}`
            );
        }
 
        const datos = await respuesta.json();
 
        return {
 
            servicio: "Frankfurter",
 
            origen: "USD",
 
            destino: "EUR",
 
            tipoCambio: datos.rate
 
        };
 
    } catch (error) {
 
        console.error(
            "ERROR FINAL EN TIPO DE CAMBIO:",
            error.message
        );
 
        throw error;
    }
}
 
async function obtenerInformacionFinanciera() {
 
    const resultados =
        await Promise.allSettled([
 
            obtenerBitcoin(),
 
            obtenerEthereum(),
 
            obtenerTipoCambio()
 
        ]);
 
 
    return {
 
        fecha:
            new Date().toLocaleString(),
 
 
        bitcoin:
            resultados[0].status === "fulfilled"
 
                ? resultados[0].value
 
                : {
                    error:
                        resultados[0].reason.message
                },
 
 
        ethereum:
            resultados[1].status === "fulfilled"
 
                ? resultados[1].value
 
                : {
                    error:
                        resultados[1].reason.message
                },
 
 
        tipoCambio:
            resultados[2].status === "fulfilled"
 
                ? resultados[2].value
 
                : {
                    error:
                        resultados[2].reason.message
                }
 
    };
 
}
 
module.exports = {
 
    obtenerInformacionFinanciera
 
};