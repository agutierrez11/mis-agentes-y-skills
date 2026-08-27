---
name: livecharts2-data-viz
description: Arquitectura e integración de gráficos y mapas interactivos de alto rendimiento en tiempo real (charts 2D/3D, gauges, heatmaps, mapas geográficos) basados en LiveCharts2 (SkiaSharp engine) para dashboards financieros, analítica B2B y telemetría de pagos.
---

# 📊 LiveCharts2 High-Performance Data Visualization & Telemetry Engine

Skill para el diseño, implementación y optimización de tableros analíticos, gráficos financieros, velocímetros/gauges multi-métrica, mapas de calor y mapas coropléticos inspirados en la arquitectura multitrama y motor SkiaSharp de LiveCharts2.

---

## 🚀 Cuándo Utilizar esta Skill

Invoca esta skill cuando el proyecto requiera:
- **Dashboards FinTech & Telemetría en Tiempo Real:** Monitor de transacciones por segundo (TPS), volumen procesado ($ MXN / USD), tasa de autorización y latencia de pasarelas de pago.
- **Gráficos Financieros Multieje:** Comparativas de comisiones de SOFOMEs, agregadores y pasarelas con múltiples ejes Y (Porcentaje % vs Monto Fijo $).
- **Gauges & Indicadores de Performance:** Velocímetros circulares y radiales para métricas de riesgo, salud de API y densidad de aceptación de pagos.
- **Mapas Geográficos Coropléticos:** Distribución geográfica de densidad de adquirencia, SOFOMEs y adquirentes por estado en México y LATAM.
- **Heatmaps de Actividad Comercial:** Matrices de volumen de cobro por hora del día y día de la semana.

---

## 📐 Principios de Diseño para Dashboards FinTech

1. **Jerarquía Visual y Contraste Alto:**
   - Usa fondos oscuros (`#0B0F19`, `#030712`) con trazos fosforescentes / gradientes HSL (`#10B981` verde éxito, `#F59E0B` advertencia, `#EF4444` rechazo, `#6366F1` volumen).
2. **Animaciones Suaves sin Bloquear el Hilo Principal:**
   - Interpolación fluida de puntos en tiempo real (transición easing cubic-bezier a 60 FPS).
3. **Tooltips Interactivos Contextuales:**
   - Formateo automático de divisas (`$1,250,000 MXN`), porcentajes (`2.95% + $3.00`) y desgloses de IVA/comisión en hover.

---

## 💻 Patrón de Código: Dashboard FinTech con Recharts / Chart.js + Tailwind

Ejemplo de implementación equivalente en ecosistemas Web React / TypeScript:

```tsx
import React from "react";
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

interface TelemetryData {
  time: string;
  volume: number;
  approved: number;
}

const data: TelemetryData[] = [
  { time: "00:00", volume: 45000, approved: 98.2 },
  { time: "04:00", volume: 12000, approved: 99.1 },
  { time: "08:00", volume: 185000, approved: 97.4 },
  { time: "12:00", volume: 340000, approved: 96.8 },
  { time: "16:00", volume: 290000, approved: 98.0 },
  { time: "20:00", volume: 160000, approved: 98.5 },
];

export function PaymentTelemetryChart() {
  return (
    <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 shadow-2xl">
      <div className="flex justify-between items-center mb-4">
        <div>
          <h3 className="text-lg font-bold text-white font-outfit">Volumen Transaccionado en Tiempo Real</h3>
          <p className="text-xs text-slate-400">Telemetría procesada vía Pasarelas LATAM</p>
        </div>
        <span className="px-3 py-1 text-xs font-semibold text-emerald-400 bg-emerald-950/60 border border-emerald-800/50 rounded-full animate-pulse">
          ● EN VIVO
        </span>
      </div>

      <div className="h-64 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data}>
            <defs>
              <linearGradient id="volumeGrad" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#6366f1" stopOpacity={0.4}/>
                <stop offset="95%" stopColor="#6366f1" stopOpacity={0.0}/>
              </linearGradient>
            </defs>
            <XAxis dataKey="time" stroke="#64748b" fontSize={12} tickLine={false} />
            <YAxis stroke="#64748b" fontSize={12} tickFormatter={(val) => `$${val/1000}k`} tickLine={false} />
            <Tooltip
              contentStyle={{ backgroundColor: "#0f172a", borderColor: "#334155", borderRadius: "12px" }}
              formatter={(value: any) => [`$${Number(value).toLocaleString()} MXN`, "Volumen"]}
            />
            <Area type="monotone" dataKey="volume" stroke="#818cf8" strokeWidth={3} fillOpacity={1} fill="url(#volumeGrad)" />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
```

---

## ⚡ Reglas de Desempeño y Escalabilidad
1. **Muestreo de Puntos Dinámico (Downsampling):** Para datasets de más de 5,000 puntos en tiempo real, aplica algoritmos de muestreo LTTB (Largest-Triangle-Three-Buckets) para mantener el renderizado en bajo consumo de CPU.
2. **Buffer Circular de Memoria:** Mantén arreglos de tamaño fijo (`RingBuffer`) para streamings en vivo en lugar de re-asignar memoria continuamente.
