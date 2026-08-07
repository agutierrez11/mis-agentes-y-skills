---
name: mapcn-gis-specialist
description: Diseña e integra mapas vectoriales interactivos, geolocalización de prospectos B2B y visualización espacial de datos comerciales usando MapLibre GL, TailwindCSS y mapcn.
---

# 🗺️ mapcn GIS & Geospatial Visualization Specialist

Esta skill enseña al agente de IA a integrar mapas interactivos vectoriales de alta fidelidad visual en aplicaciones React / Next.js utilizando la librería open-source **mapcn** (basada en MapLibre GL y estilizada con TailwindCSS).

---

## 🎨 1. Principios de Integración y Estética

* **Theme Awareness Nativo:** El mapa debe conmutar automáticamente entre tema claro y oscuro según las variables del sistema (`dark:` / `light:`).
* **Filtros por Capas:** Visualización de clientes, competidores o prospectos mediante marcadores animados y tooltips con métricas clave.

---

## 🛠️ 2. Patrón de Uso en React / Next.js

```tsx
import { Map, Marker, Popup } from "@/components/ui/map";

export function SalesTerritoryMap({ entities }) {
  return (
    <Map initialView={{ latitude: 23.6345, longitude: -102.5528, zoom: 5 }}>
      {entities.map(item => (
        <Marker key={item.id} latitude={item.lat} longitude={item.lng}>
          <Popup>
            <div className="p-2 text-xs font-mono">
              <p className="font-bold">{item.name}</p>
              <p className="text-emerald-500">MRR: ${item.mrr}</p>
            </div>
          </Popup>
        </Marker>
      ))}
    </Map>
  );
}
```
