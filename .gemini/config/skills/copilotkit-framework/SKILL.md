---
name: copilotkit-framework
description: Desarrollo e integración de copilotos de IA en aplicaciones web (React/Next.js) con Generative UI y el protocolo AG-UI usando CopilotKit (copilotkit/copilotkit).
---

# ⚡ CopilotKit — In-App AI Copilots & Generative UI

Esta habilidad proporciona patrones de arquitectura para construir Copilotos de IA integrados dentro de aplicaciones web utilizando **CopilotKit** (`github.com/copilotkit/copilotkit`).

## 🚀 Conceptos Core
1. **In-App Chatbot & Sidebars:** Asistentes de IA contextuales que leen el estado interno de la aplicación React.
2. **Generative UI:** La IA no solo responde con texto, sino que genera componentes de React interactivos (tablas, gráficos, formularios) dentro de la interfaz en tiempo real.
3. **AG-UI Protocol:** Conecta agentes de LangGraph, CrewAI o Python backend directamente con la UI del cliente.

## 🛠️ Instalación rápida en React/Next.js
```bash
npm install @copilotkit/react-core @copilotkit/react-ui
```

## 💻 Patrón de Código React
```tsx
import { CopilotKit } from "@copilotkit/react-core";
import { CopilotSidebar } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";

export default function App() {
  return (
    <CopilotKit publicApiKey="TU_API_KEY">
      <CopilotSidebar defaultOpen={true} labels={{ title: "Asistente Financiero Copilot" }}>
        <YourMainApplication />
      </CopilotSidebar>
    </CopilotKit>
  );
}
```
