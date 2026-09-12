// =====================================================
// CONFIGURACIÓN
// =====================================================
 
// IMPORTANTE:
//
// Después de desplegar Cloudflare Worker,
// reemplazar esta URL.
//
// Ejemplo:
//
// https://faas-worker.usuario.workers.dev
 
const WORKER_URL =
    "https://cloud-worker.fullengineer90253.workers.dev";
 
 
// =====================================================
// ELEMENTOS HTML
// =====================================================
 
const resultado =
    document.getElementById("resultado");
 
const mensaje =
    document.getElementById("mensaje");
 
 
// =====================================================
// MOSTRAR RESULTADO CON ANIMACIÓN
// =====================================================
 
function mostrarMensaje(texto) {
 
    // Cambiamos el mensaje.
    mensaje.textContent = texto;
 
 
    // Quitamos la animación anterior.
    resultado.classList.remove("animar");
 
 
    // Esta línea obliga al navegador
    // a reiniciar la animación.
    void resultado.offsetWidth;
 
 
    // Agregamos nuevamente la animación.
    resultado.classList.add("animar");
 
}
 
 
 
// =====================================================
// PUNTO 1
//
// ENFOQUE BASADO EN EVENTOS
// =====================================================
 
async function ejecutarEvento() {
 
    try {
 
        mostrarMensaje(
            "Evento enviado al Cloud..."
        );
 
 
        // =============================================
        // EVENTO HTTP
        //
        // El fetch genera una solicitud HTTP.
        //
        // Esa solicitud funciona como un EVENTO
        // que dispara el Cloudflare Worker.
        // =============================================
 
        const respuesta =
            await fetch(
                `${WORKER_URL}/evento`
            );
 
 
        const datos =
            await respuesta.json();
 
 
        mostrarMensaje(
            `${datos.mensaje}`
        );
 
    }
    catch (error) {
 
        mostrarMensaje(
            "Error conectando con Cloud FaaS"
        );
 
    }
 
}
 
 
 
// =====================================================
// PUNTO 2
//
// PROPIEDADES DE LAS FUNCIONES
// =====================================================
 
async function ejecutarFuncion() {
 
    try {
 
        mostrarMensaje(
            "Ejecutando función independiente..."
        );
 
 
        // Esta llamada activa otra función
        // o comportamiento independiente
        // dentro del Worker.
 
        const respuesta =
            await fetch(
                `${WORKER_URL}/funcion`
            );
 
 
        const datos =
            await respuesta.json();
 
 
        mostrarMensaje(
            `${datos.mensaje}`
        );
 
    }
    catch (error) {
 
        mostrarMensaje(
            "Error ejecutando la función"
        );
 
    }
 
}
 
 
 
// =====================================================
// PUNTO 3
//
// TRIGGERS Y PLANIFICADORES
// =====================================================
 
function mostrarScheduler() {
 
    // Esta parte explica al usuario que existe
    // una función programada en Cloudflare.
 
    mostrarMensaje(
 
        "Existe un Cron Trigger configurado. " +
 
        "Cloudflare ejecutará automáticamente " +
 
        "la función scheduled() según el horario."
 
    );
 
}