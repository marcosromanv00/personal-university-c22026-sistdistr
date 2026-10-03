/**
 * Welcome to Cloudflare Workers!
 *
 * This is a template for a Scheduled Worker: a Worker that can run on a
 * configurable interval:
 * https://developers.cloudflare.com/workers/platform/triggers/cron-triggers/
 *
 * - Run `npm run dev` in your terminal to start a development server
 * - Run `curl "http://localhost:8787/__scheduled?cron=*+*+*+*+*"` to see your worker in action
 * - Run `npm run deploy` to publish your worker
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */

/* export default {
	async fetch(req) {
		const url = new URL(req.url)
		url.pathname = "/__scheduled";
		url.searchParams.append("cron", "* * * * *");
		return new Response(`To test the scheduled handler, ensure you have used the "--test-scheduled" then try running "curl ${url.href}".`);
	},
	// The scheduled handler is invoked at the interval set in our wrangler.jsonc's
	// [[triggers]] configuration.
	async scheduled(event, env, ctx) {
		// A Cron Trigger can make requests to other endpoints on the Internet,
		// publish to a Queue, query a D1 Database, and much more.
		//
		// We'll keep it simple and make an API call to a Cloudflare API:
		let resp = await fetch('https://api.cloudflare.com/client/v4/ips');
		let wasSuccessful = resp.ok ? 'success' : 'fail';

		// You could store this result in KV, write to a D1 Database, or publish to a Queue.
		// In this template, we'll just log the result:
		console.log(`trigger fired at ${event.cron}: ${wasSuccessful}`);
	},
}; */

// =====================================================
// CLOUDFLARE WORKER
//
// IMPLEMENTACIÓN FaaS
// =====================================================

// =====================================================
// FUNCIÓN PRINCIPAL DEL WORKER
// =====================================================

// Cloudflare ejecuta esta función cuando ocurre
// un evento HTTP.
//
// ================================================
// PUNTO 1:
//
// ENFOQUE BASADO EN EVENTOS
//
// fetch(request) se ejecuta como respuesta a
// un EVENTO HTTP.
// ================================================

export default {

    // =================================================
    // EVENTO HTTP
    // =================================================

    async fetch(request, env, ctx) {

        // Creamos un objeto URL para conocer
        // qué endpoint fue solicitado.
        const url = new URL(request.url);


        // =============================================
        // CONFIGURACIÓN CORS
        // =============================================

        // Permitimos que nuestro frontend Express
        // pueda llamar al Worker.
        const headers = {
            "Content-Type":
                "application/json",
            "Access-Control-Allow-Origin":
                "*"
        };


        // =============================================
        // PUNTO 1
        //
        // EVENT-DRIVEN
        // =============================================

        // Si ocurre una solicitud HTTP hacia:
        //
        // /evento
        //
        // el evento dispara esta respuesta.
        if (url.pathname === "/evento") {

            console.log(
                "EVENTO HTTP RECIBIDO"
            );

            return new Response(

                JSON.stringify({

                    tipo:
                        "EVENTO",

                    mensaje:
                        "El evento HTTP disparó " +
                        "correctamente una función FaaS",

                    fecha:
                        new Date().toISOString()

                }),

                {
                    headers
                }

            );

        }


        // =============================================
        // PUNTO 2
        //
        // PROPIEDADES DE LAS FUNCIONES
        // =============================================

        // Cada endpoint representa una responsabilidad
        // específica.
        //
        // La función se ejecuta bajo demanda.
        //
        // No mantiene una sesión propia entre
        // ejecuciones.
        if (url.pathname === "/funcion") {

            // Ejecutamos una función independiente.
            const resultado =
                procesarFuncion();

            return new Response(

                JSON.stringify({

                    tipo:
                        "FUNCIÓN FaaS",

                    mensaje:
                        resultado,

                    propiedades: [
                        "Independiente",
                        "Bajo demanda",
                        "Sin estado persistente",
                        "Responsabilidad específica"
                    ]

                }),

                {
                    headers
                }

            );

        }


        // =============================================
        // RESPUESTA POR DEFECTO
        // =============================================

        return new Response(

            JSON.stringify({

                mensaje:
                    "FaaS Event Manager activo",

                endpoints: [
                    "/evento",
                    "/funcion"
                ]

            }),

            {
                headers
            }

        );

    },



    // =================================================
    // PUNTO 3
    //
    // DISPARADORES Y PLANIFICADORES
    // =================================================

    // scheduled() NO es ejecutado por un usuario.
    //
    // Es ejecutado automáticamente por Cloudflare
    // cuando se cumple una expresión Cron.
    //
    // Ejemplo:
    //
    // */5 * * * *
    //
    // Ejecutar cada 5 minutos.

    async scheduled(
        controller,
        env,
        ctx
    ) {

        console.log(
            "================================="
        );

        console.log(
            "⏰ CRON TRIGGER ACTIVADO"
        );

        console.log(
            "Hora de ejecución:",
            new Date().toISOString()
        );

        console.log(
            "================================="
        );


        // =============================================
        // FUNCIÓN PROGRAMADA
        // =============================================

        // ctx.waitUntil permite asociar trabajo
        // asíncrono al evento programado.

        ctx.waitUntil(
            ejecutarTareaProgramada()
        );

    }

};



// =====================================================
// PUNTO 2
//
// FUNCIÓN INDEPENDIENTE
// =====================================================

// Esta función tiene una única responsabilidad:
//
// Procesar una operación FaaS.

function procesarFuncion() {

    return (
        "La función independiente fue ejecutada " +
        "correctamente en Cloudflare Workers."
    );

}



// =====================================================
// PUNTO 3
//
// FUNCIÓN EJECUTADA POR EL PLANIFICADOR
// =====================================================

async function ejecutarTareaProgramada() {

    console.log(
        "Tarea automática ejecutándose..."
    );

    // Simulación de una tarea automática.
    //
    // En una aplicación real podría:
    //
    // - Consultar una API
    // - Limpiar datos
    // - Crear un reporte
    // - Enviar notificaciones
    // - Actualizar información

    console.log(
        "Tarea automática finalizada."
    );

}
