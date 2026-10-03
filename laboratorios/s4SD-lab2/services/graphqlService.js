// ======================================================
// SERVICIO PARA REALIZAR LLAMADAS A APIs GRAPHQL
// ======================================================
 
 
// ======================================================
// 1. API GRAPHQL DE PAÍSES
// ======================================================
 
const COUNTRIES_API =
    "https://countries.trevorblades.com/";
 
 
// ======================================================
// 2. API GRAPHQL DE RICK AND MORTY
// ======================================================
 
const RICK_MORTY_API =
    "https://rickandmortyapi.com/graphql";
 
 
// ======================================================
// FUNCIÓN 1
// Obtener información de países
// ======================================================
 
async function obtenerPaises() {
 
    // ----------------------------------------------
    // CONSULTA GRAPHQL
    // ----------------------------------------------
 
    const query = `
        query {
            countries {
                code
                name
                emoji
                capital
                currency
            }
        }
    `;
 
 
    // ----------------------------------------------
    // LLAMADA HTTP POST AL SERVIDOR GRAPHQL
    // ----------------------------------------------
 
    const respuesta = await fetch(COUNTRIES_API, {
 
        method: "POST",
 
        headers: {
            "Content-Type": "application/json"
        },
 
        body: JSON.stringify({
            query: query
        })
    });
 
 
    // ----------------------------------------------
    // Convertir respuesta a JSON
    // ----------------------------------------------
 
    const resultado = await respuesta.json();
 
 
    // ----------------------------------------------
    // Verificar errores GraphQL
    // ----------------------------------------------
 
    if (resultado.errors) {
 
        console.error(resultado.errors);
 
        throw new Error(
            "Error en la consulta GraphQL de países"
        );
    }
 
 
    // ----------------------------------------------
    // Retornar solamente los datos
    // ----------------------------------------------
 
    return resultado.data.countries;
}
 
 
// ======================================================
// FUNCIÓN 2
// Obtener personajes de Rick and Morty
// ======================================================
 
async function obtenerPersonajes() {
 
    // ----------------------------------------------
    // CONSULTA GRAPHQL
    // ----------------------------------------------
 
    const query = `
        query {
            characters(page: 1) {
                info {
                    count
                }
 
                results {
                    id
                    name
                    status
                    species
                    gender
                    image
                }
            }
        }
    `;
 
 
    // ----------------------------------------------
    // LLAMADA HTTP POST AL SERVIDOR GRAPHQL
    // ----------------------------------------------
 
    const respuesta = await fetch(RICK_MORTY_API, {
 
        method: "POST",
 
        headers: {
            "Content-Type": "application/json"
        },
 
        body: JSON.stringify({
            query: query
        })
    });
 
 
    // ----------------------------------------------
    // Convertir respuesta a JSON
    // ----------------------------------------------
 
    const resultado = await respuesta.json();
 
 
    // ----------------------------------------------
    // Verificar errores GraphQL
    // ----------------------------------------------
 
    if (resultado.errors) {
 
        console.error(resultado.errors);
 
        throw new Error(
            "Error en la consulta GraphQL de personajes"
        );
    }
 
 
    // ----------------------------------------------
    // Retornar datos
    // ----------------------------------------------
 
    return resultado.data.characters;
}
 
 
module.exports = {
    obtenerPaises,
    obtenerPersonajes
};