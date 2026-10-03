class SolarCard extends HTMLElement {
 
    constructor() {
 
        super();
 
        this.attachShadow({
            mode: "open"
        });
 
    }
 
 
    connectedCallback() {
 
        this.render();
 
        this.loadData();
 
    }
 
 
    render() {
 
        this.shadowRoot.innerHTML = `
           
            <style>
 
                .card {
                    background: #111827;
                    color: white;
                    border-radius: 20px;
                    padding: 28px;
                    box-shadow:
                        0 15px 40px
                        rgba(0, 0, 0, 0.20);
 
                    animation:
                        slideIn 0.8s ease-out;
                }
 
 
                .header {
                    display: flex;
                    align-items: center;
                    gap: 15px;
                    margin-bottom: 20px;
                }
 
 
                .icon {
                    width: 50px;
                    height: 50px;
 
                    display: flex;
                    align-items: center;
                    justify-content: center;
 
                    border-radius: 50%;
 
                    background:
                        linear-gradient(
                            135deg,
                            #facc15,
                            #f97316
                        );
 
                    font-size: 25px;
 
                    animation:
                        pulse 2s infinite;
                }
 
 
                h2 {
                    margin: 0;
                }
 
 
                .subtitle {
                    color: #9ca3af;
                    margin-top: 4px;
                }
 
 
                .loading {
                    color: #facc15;
                    padding: 20px 0;
                }
 
 
                .values {
                    display: grid;
                    grid-template-columns:
                        repeat(
                            auto-fit,
                            minmax(160px, 1fr)
                        );
 
                    gap: 15px;
                }
 
 
                .value {
                    background: #1f2937;
                    border-radius: 12px;
                    padding: 18px;
 
                    animation:
                        fadeUp 0.6s ease-out;
                }
 
 
                .date {
                    color: #9ca3af;
                    font-size: 0.85rem;
                }
 
 
                .number {
                    font-size: 1.8rem;
                    font-weight: bold;
                    margin-top: 8px;
                }
 
 
                .error {
                    color: #f87171;
                }
 
 
                @keyframes slideIn {
 
                    from {
                        opacity: 0;
                        transform:
                            translateY(40px);
                    }
 
                    to {
                        opacity: 1;
                        transform:
                            translateY(0);
                    }
 
                }
 
 
                @keyframes fadeUp {
 
                    from {
                        opacity: 0;
                        transform:
                            translateY(20px);
                    }
 
                    to {
                        opacity: 1;
                        transform:
                            translateY(0);
                    }
 
                }
 
 
                @keyframes pulse {
 
                    0%, 100% {
                        transform: scale(1);
                    }
 
                    50% {
                        transform: scale(1.15);
                    }
 
                }
 
            </style>
 
 
            <article class="card">
 
                <div class="header">
 
                    <div class="icon">
                        ☀️
                    </div>
 
                    <div>
 
                        <h2>
                            Radiación solar
                        </h2>
 
                        <div class="subtitle">
                            NASA POWER
                        </div>
 
                    </div>
 
                </div>
 
 
                <div id="content">
 
                    <div class="loading">
                        Consultando datos satelitales...
                    </div>
 
                </div>
 
            </article>
        `;
    }
 
 
    async loadData() {
 
        try {
 
            const response =
                await fetch("/api/solar");
 
 
            if (!response.ok) {
 
                throw new Error(
                    "Error HTTP"
                );
 
            }
 
 
            const result =
                await response.json();
 
 
            this.displayData(result);
 
 
        } catch (error) {
 
            this.showError();
 
            console.error(error);
 
        }
 
    }
 
 
    displayData(result) {
 
        const content =
            this.shadowRoot.querySelector(
                "#content"
            );
 
 
        const entries =
            Object.entries(result.data);
 
 
        content.innerHTML = `
 
            <div class="values">
 
                ${entries.map(
                    ([date, value], index) => `
 
                    <div
                        class="value"
                        style="
                            animation-delay:
                            ${index * 0.12}s
                        "
                    >
 
                        <div class="date">
                            ${this.formatDate(date)}
                        </div>
 
                        <div class="number">
                            ${Number(value).toFixed(2)}
                        </div>
 
                        <div class="date">
                            kWh/m²/day
                        </div>
 
                    </div>
 
                `
                ).join("")}
 
            </div>
 
        `;
 
    }
 
 
    formatDate(date) {
 
        return `${date.substring(0, 4)}-
                ${date.substring(4, 6)}-
                ${date.substring(6, 8)}`;
 
    }
 
 
    showError() {
 
        const content =
            this.shadowRoot.querySelector(
                "#content"
            );
 
        content.innerHTML = `
            <div class="error">
                No fue posible cargar
                los datos solares.
            </div>
        `;
 
    }
 
}
 
 
customElements.define(
    "solar-card",
    SolarCard
);
 