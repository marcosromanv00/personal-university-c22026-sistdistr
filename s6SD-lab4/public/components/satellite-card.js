class SatelliteCard extends HTMLElement {
 
    constructor() {
 
        super();
 
        this.attachShadow({
            mode: "open"
        });
 
    }
 
 
    connectedCallback() {
 
        this.render();
 
        this.loadImage();
 
    }
 
 
    render() {
 
        this.shadowRoot.innerHTML = `
 
            <style>
 
                .card {
                    background: white;
                    border-radius: 20px;
                    overflow: hidden;
 
                    box-shadow:
                        0 15px 40px
                        rgba(0, 0, 0, 0.18);
 
                    animation:
                        zoomIn 0.9s ease-out;
                }
 
 
                .header {
                    padding: 24px;
 
                    display: flex;
                    align-items: center;
 
                    gap: 15px;
                }
 
 
                .icon {
                    font-size: 40px;
 
                    animation:
                        float 3s ease-in-out infinite;
                }
 
 
                h2 {
                    margin: 0;
                    color: #111827;
                }
 
 
                .subtitle {
                    margin-top: 5px;
                    color: #6b7280;
                }
 
 
                .image-container {
                    position: relative;
 
                    background: #111827;
 
                    min-height: 300px;
 
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
 
 
                img {
                    width: 100%;
                    display: block;
 
                    opacity: 0;
 
                    transition:
                        opacity 0.8s ease;
 
                }
 
 
                img.loaded {
                    opacity: 1;
                }
 
 
                .loading {
                    position: absolute;
 
                    color: white;
 
                    animation:
                        pulse 1.5s infinite;
                }
 
 
                .footer {
                    padding: 18px 24px;
 
                    color: #6b7280;
 
                    font-size: 0.9rem;
                }
 
 
                @keyframes zoomIn {
 
                    from {
                        opacity: 0;
                        transform:
                            scale(0.92);
                    }
 
                    to {
                        opacity: 1;
                        transform:
                            scale(1);
                    }
 
                }
 
 
                @keyframes float {
 
                    0%, 100% {
                        transform:
                            translateY(0);
                    }
 
                    50% {
                        transform:
                            translateY(-8px);
                    }
 
                }
 
 
                @keyframes pulse {
 
                    0%, 100% {
                        opacity: 0.5;
                    }
 
                    50% {
                        opacity: 1;
                    }
 
                }
 
            </style>
 
 
            <article class="card">
 
                <div class="header">
 
                    <div class="icon">
                        🛰️
                    </div>
 
                    <div>
 
                        <h2>
                            Imagen satelital
                        </h2>
 
                        <div class="subtitle">
                            NASA GIBS / MODIS Terra
                        </div>
 
                    </div>
 
                </div>
 
 
                <div class="image-container">
 
                    <div
                        id="loading"
                        class="loading"
                    >
                        Descargando imagen satelital...
                    </div>
 
                    <img
                        id="satelliteImage"
                        alt="Imagen satelital de Costa Rica"
                    >
 
                </div>
 
 
                <div class="footer">
 
                    Visualización de observaciones
                    de la Tierra mediante NASA GIBS.
 
                </div>
 
            </article>
        `;
    }
 
 
    async loadImage() {
 
        const image =
            this.shadowRoot.querySelector(
                "#satelliteImage"
            );
 
        const loading =
            this.shadowRoot.querySelector(
                "#loading"
            );
 
 
        try {
            //***************************ojo explicar */
            const response =
                await fetch(
                    "/api/satellite-image"
                );
 
 
            if (!response.ok) {
 
                const errorText =
                    await response.text();
 
                throw new Error(
                    errorText ||
                    `HTTP ${response.status}`
                );
 
            }
 
 
            /*
             * Convertimos la respuesta
             * en Blob.
             */
 
            const blob =
                await response.blob();
 
 
            /*
             * Creamos una URL temporal
             * para mostrar la imagen.
             */
 
            const imageUrl =
                URL.createObjectURL(blob);
 
 
            image.src = imageUrl;
 
 
            image.onload = () => {
 
                loading.style.display =
                    "none";
 
                image.classList.add(
                    "loaded"
                );
 
            };
 
 
        } catch (error) {
 
            loading.textContent =
                "No fue posible cargar la imagen.";
 
            console.error(error);
 
        }
 
    }
 
}
 
 
customElements.define(
    "satellite-card",
    SatelliteCard
);
 