import express from "express";
import path from "path";
import { fileURLToPath } from "url";
 
const app = express();
const PORT = 3000;
 
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
 
// Servir archivos estáticos
app.use(express.static(path.join(__dirname, "public")));
 
/*
 * Coordenadas de San José, Costa Rica.
 * Puedes cambiarlas por cualquier otra ubicación.
 */
const LATITUDE = 9.9281;
const LONGITUDE = -84.0907;
 
 
/*
 * ============================================================
 * MICROSERVICIO 1
 * NASA POWER
 *
 * Devuelve radiación solar.
 *
 * Los datos solares de POWER proceden de observaciones
 * satelitales y son procesados para estimar la radiación
 * en superficie.
 * ============================================================
 */
app.get("/api/solar", async (req, res) => {
 
    try {
 
        const today = new Date();
 
        // Usamos una fecha reciente.
        // NASA POWER puede tener cierta latencia para datos
        // observacionales.
        const endDate = new Date(today);
        endDate.setDate(endDate.getDate() - 5);
 
        const startDate = new Date(endDate);
        startDate.setDate(startDate.getDate() - 2);
 
        const formatDate = (date) => {
            return date.toISOString().slice(0, 10).replaceAll("-", "");
        };
 
        const start = formatDate(startDate);
        const end = formatDate(endDate);
 
        const url =
            `https://power.larc.nasa.gov/api/temporal/daily/point` +
            `?parameters=ALLSKY_SFC_SW_DWN` +
            `&community=RE` +
            `&longitude=${LONGITUDE}` +
            `&latitude=${LATITUDE}` +
            `&start=${start}` +
            `&end=${end}` +
            `&format=JSON`;
 
        const response = await fetch(url);
 
        if (!response.ok) {
            throw new Error(
                `NASA POWER respondió HTTP ${response.status}`
            );
        }
 
        const data = await response.json();
 
        res.json({
            source: "NASA POWER",
            latitude: LATITUDE,
            longitude: LONGITUDE,
            parameter: "ALLSKY_SFC_SW_DWN",
            unit: "kWh/m²/day",
            data: data.properties.parameter.ALLSKY_SFC_SW_DWN
        });
 
    } catch (error) {
 
        console.error("Error NASA POWER:", error);
 
        res.status(500).json({
            error: "No fue posible obtener los datos solares"
        });
    }
});
 
 
/*
 * ============================================================
 * MICROSERVICIO 2
 * NASA GIBS
 *
 * Obtiene una imagen satelital MODIS.
 *
 * En lugar de exponer directamente GIBS al navegador,
 * Express actúa como proxy.
 * ============================================================
 */
app.get("/api/satellite-image", async (req, res) => {
 
    try {
 
        /*
         * GIBS / MODIS Terra
         *
         * Usamos WMS 1.1.1 porque permite trabajar
         * con EPSG:4326 utilizando el BBOX como:
         *
         * minLon,minLat,maxLon,maxLat
         */
 
        const date = new Date();
 
        /*
         * MODIS no necesariamente tiene disponible
         * información del día actual.
         *
         * Utilizamos una fecha de unos días atrás.
         */
 
 
const dateString = "2026-08-24";
/*         date.setDate(date.getDate() - 4);
 
        const dateString =
            date.toISOString().slice(0, 10); */
 
 
 
 
        /*
         * Costa Rica
         *
         * minLon = -86
         * minLat = 8
         * maxLon = -82.5
         * maxLat = 12
         */
 
        const bbox =
            "-86,8,-82.5,12";
 
 
        const params = new URLSearchParams({
 
            service: "WMS",
 
            version: "1.1.1",
 
            request: "GetMap",
 
            layers:
                "MODIS_Terra_CorrectedReflectance_TrueColor",
 
            styles: "",
 
            srs: "EPSG:4326",
 
            bbox: bbox,
 
            width: "900",
 
            height: "500",
 
            format: "image/jpeg",
 
            time: dateString
 
        });
 
 
        const url =
            "https://gibs.earthdata.nasa.gov" +
            "/wms/epsg4326/best/wms.cgi?" +
            params.toString();
 
 
        console.log(
            "Consultando NASA GIBS:"
        );
 
        console.log(url);
 
 
        const response =
            await fetch(url);
 
 
        if (!response.ok) {
 
            throw new Error(
                `NASA GIBS respondió HTTP ${response.status}`
            );
 
        }
 
 
        const image =
            await response.arrayBuffer();
 
 
        res.set(
            "Content-Type",
            "image/jpeg"
        );
 
 
        res.send(
            Buffer.from(image)
        );
 
 
    } catch (error) {
 
        console.error(
            "Error NASA GIBS:",
            error
        );
 
 
        res.status(500).send(
            "No fue posible obtener la imagen satelital"
        );
 
    }
 
});
 
 
/*
 * Ruta principal
 */
app.get("/", (req, res) => {
 
    res.sendFile(
        path.join(__dirname, "public", "index.html")
    );
});
 
 
app.listen(PORT, () => {
 
    console.log(
        `Servidor ejecutándose en http://localhost:${PORT}`
    );
 
});