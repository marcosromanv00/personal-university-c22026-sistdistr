let informacion = null;
 
 
// =================================================
// CONSULTAR LOS SERVICIOS FINANCIEROS
// =================================================
 
document
    .getElementById("btnConsultar")
    .addEventListener(
        "click",
        async () => {
 
            const mensaje =
                document.getElementById(
                    "mensaje"
                );
 
 
            mensaje.textContent =
                "Consultando servicios...";
 
 
            try {
 
                // =================================
                // LLAMADA A NUESTRO SERVICIO
                // =================================
 
                const respuesta =
                    await fetch(
                        "/api/finanzas"
                    );
 
 
                if (!respuesta.ok) {
 
                    throw new Error(
                        "Error en el servidor"
                    );
 
                }
 
 
                informacion =
                    await respuesta.json();
 
 
                // =================================
                // BITCOIN
                // =================================
 
                document
                    .getElementById("btcServicio")
                    .textContent =
                    informacion
                        .bitcoin
                        .servicio;
 
 
                document
                    .getElementById("btcCodigo")
                    .textContent =
                    informacion
                        .bitcoin
                        .codigo;
 
 
                document
                    .getElementById("btcPrecio")
                    .textContent =
                    "$ " +
                    Number(
                        informacion
                            .bitcoin
                            .precioUSD
                    ).toLocaleString(
                        "en-US",
                        {
                            minimumFractionDigits:
                                2
                        }
                    );
 
 
                // =================================
                // ETHEREUM
                // =================================
 
                document
                    .getElementById("ethServicio")
                    .textContent =
                    informacion
                        .ethereum
                        .servicio;
 
 
                document
                    .getElementById("ethCodigo")
                    .textContent =
                    informacion
                        .ethereum
                        .codigo;
 
 
                document
                    .getElementById("ethPrecio")
                    .textContent =
                    "$ " +
                    Number(
                        informacion
                            .ethereum
                            .precioUSD
                    ).toLocaleString(
                        "en-US",
                        {
                            minimumFractionDigits:
                                2
                        }
                    );
 
 
                // =================================
                // TIPO DE CAMBIO
                // =================================
 
                document
                    .getElementById("tcServicio")
                    .textContent =
                    informacion
                        .tipoCambio
                        .servicio;
 
 
                document
                    .getElementById("tcValor")
                    .textContent =
                    Number(
                        informacion
                            .tipoCambio
                            .tipoCambio
                    ).toFixed(4);
 
 
                // =================================
                // FECHA
                // =================================
 
                document
                    .getElementById("fecha")
                    .textContent =
                    "Fecha de consulta: " +
                    informacion.fecha;
 
 
                mensaje.textContent =
                    "Información actualizada correctamente.";
 
            }
            catch (error) {
 
                console.error(error);
 
                mensaje.textContent =
                    "Error al consultar los servicios.";
 
            }
 
        }
    );
 
 
// =================================================
// GUARDAR EN TXT
// =================================================
 
document
    .getElementById("btnGuardar")
    .addEventListener(
        "click",
        async () => {
 
 
            if (!informacion) {
 
                alert(
                    "Primero debe consultar la información."
                );
 
                return;
 
            }
 
 
            try {
 
                const respuesta =
                    await fetch(
                        "/api/finanzas/guardar",
                        {
 
                            method:
                                "POST",
 
                            headers: {
 
                                "Content-Type":
                                    "application/json"
 
                            },
 
                            body:
                                JSON.stringify(
                                    informacion
                                )
 
                        }
                    );
 
                const resultado =
                    await respuesta.json();
 
 
                if (!respuesta.ok) {
 
                    throw new Error(
                        resultado.error
                    );
 
                }
 
                alert(
                    resultado.mensaje
                );
 
            }
            catch (error) {
 
                console.error(error);
 
                alert(
                    "Error al guardar."
                );
 
            }
        }
    );