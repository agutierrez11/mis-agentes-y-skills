# 🛠️ Playbook Técnico de Autenticación DNS & Entregabilidad B2B

**Diseñado para:** Intelligential  
**Propósito:** Eliminar la caída de correos/invitaciones en SPAM y garantizar que el 100% de los mensajes de ventas lleguen a la bandeja de entrada principal de los CEOs de SOFOMes.  
**Tiempo de Ejecución:** ~15 Minutos en el proveedor de DNS (Cloudflare, GoDaddy, Google Domains, etc.).

---

## 📋 Checklist de Configuración DNS (Paso a Paso)

### 1. Registro SPF (Sender Policy Framework)
Verifica que los servidores de Google o Microsoft tengan permiso explícito para enviar correos a nombre de `intelligential.tech`.

* **Tipo:** `TXT`
* **Nombre / Host:** `@` (o dejar en blanco según el proveedor DNS)
* **Valor (si usan Google Workspace):**  
  `v=spf1 include:_spf.google.com ~all`
* **Valor (si usan Microsoft 365 / Outlook):**  
  `v=spf1 include:spf.protection.outlook.com ~all`

---

### 2. Registro DKIM (Firma Digital Anti-Suplantación)
Firma digitalmente cada correo saliente para que los filtros de Gmail/Outlook sepan que el mensaje es auténtico y no fue alterado.

1. Entrar a la consola de administración de **Google Workspace** (`admin.google.com`) ➔ *Apps* ➔ *Google Workspace* ➔ *Gmail* ➔ *Autenticar correo (DKIM)*.
2. Hacer clic en **Generar nuevo registro**.
3. Copiar la clave generada e insertarla en el DNS:
   * **Tipo:** `TXT`
   * **Nombre / Host:** `google._domainkey`
   * **Valor:** *(Pegar la clave extensa generada por Google Workspace)*

---

### 3. Registro DMARC (Protección de Dominio y Reputación)
Instruye a los servidores receptores sobre cómo tratar correos que no pasen SPF/DKIM y otorga alta reputación inmediata.

* **Tipo:** `TXT`
* **Nombre / Host:** `_dmarc`
* **Valor (Modo Monitoreo Inicial):**  
  `v=DMARC1; p=none; rua=mailto:luis.fernando@intelligential.tech; pct=100`

---

### 4. Dominios Satélite & Warmup Automatizado (Para Prospección Outbound)

Dado que el equipo comercial es ágil y pequeño, **no se deben enviar correos masivos de prospección desde el dominio principal corporativo (`intelligential.tech`)** para evitar riesgos.

```
                  ┌─────────────────────────────────────────┐
                  │ DOMINIO PRINCIPAL (intelligential.tech) │
                  │  (Uso exclusivo: Cierre, Demos, Legal)  │
                  └────────────────────┬────────────────────┘
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
┌───────────────────────────┐                         ┌───────────────────────────┐
│ DOMINIO SATÉLITE OUTBOUND │                         │ DOMINIO SATÉLITE OUTBOUND │
│  (getintelligential.com)  │                         │    (intelligential.co)    │
└─────────────┬─────────────┘                         └─────────────┬─────────────┘
              │                                                     │
              └──────────────────┬──────────────────────────────────┘
                                 ▼
                     ┌───────────────────────┐
                     │ RED DE WARMUP AUTOM.  │
                     │ (Instantly / Lemlist) │
                     └───────────────────────┘
```

1. **Comprar 1 o 2 dominios satélite:**
   * **`getintelligential.com`** (🟢 DISPONIBLE — Opción #1 Recomendada para Outbound)
   * **`intelligential.co`** (🟢 DISPONIBLE — Opción corta ideal para correo saliente)
   * **`tryintelligential.com`** (🟢 DISPONIBLE — Opción SaaS para invitaciones a Demos)
   * **`intelligentialcore.com`** (🟢 DISPONIBLE — Opción técnica corporativa)

### 🛒 Dónde Comprar los Dominios Satélite (Registradores Verificados):

| Registrador | Enlace Directo | Precio Estimado | Ventaja Competitiva |
| :--- | :--- | :--- | :--- |
| **Cloudflare Registrar (🏆 Recomendado)** | [cloudflare.com/products/registrar](https://www.cloudflare.com/products/registrar/) | **~$9.77 USD / año** | Venta al costo estricto sin margen, WHOIS Privacy gratis e integración DNS en 1 clic. |
| **Namecheap** | [namecheap.com](https://www.namecheap.com) | **~$10.28 USD / año** | Panel intuitivo, PrivacyGuard gratis para siempre. |
| **GoDaddy** | [godaddy.com](https://www.godaddy.com) | **~$11.99 USD / año** | Registro estándar rápido. |

2. **Redirección Web:** Configurar una redirección HTTP 301 en el dominio satélite para que si alguien entra a `getintelligential.com` lo envíe automáticamente a `intelligential.tech`.
3. **Warmup Automático (14 Días):** Conectar las cuentas secundarias a herramientas como **Instantly.ai** o **Smartlead.ai** (envían y responden correos automáticos entre servidores de confianza durante 2 semanas para elevar la puntuación de entregabilidad a 99%).

---
*Playbook técnico preparado por Antonio Gutiérrez para la reunión del 27 de Julio.*
