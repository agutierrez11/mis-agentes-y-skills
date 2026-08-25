---
name: microsoft-data-formulator
description: Síntesis y transformación inteligente de datos interactiva con IA (basado en microsoft/data-formulator). Unifica pipelines de Pandas/Vega-Lite/JSON sin pérdida de atributos, preservando metadatos de enriquecimiento (HarvestAPI/Apify) y estado CRM.
---

# Microsoft Data Formulator — Data Transformation & Visualization Engine

Este skill implementa los principios de **microsoft/data-formulator** para el procesamiento, limpieza, enriquecimiento y visualización iterativa de datasets complejos (B2B Sales Intelligence, CSVs de LinkedIn, JSONs de Apify/HarvestAPI).

---

## 🛠️ Principios de Procesamiento de Datos

1. **Preservación de Esquema e Identidad (Schema Integrity):**
   - Al fusionar o transformar datasets, NUNCA eliminar banderas clave (`harvest_enriched`, `jobStatus`, `crmStatus`, `discardedFromPurge`, `whitelistedFromPurge`).
   - Cada transformación debe validar que el número total de registros antes y después sea coherente.

2. **Limpieza y Normalización Multilingüe:**
   - Normalizar caracteres y acentos (`Cancún` -> `cancun` -> `México`) para evitar falsos negativos en filtros de país o jerarquía.
   - Tratar de forma diferenciada campos vacíos (`null`) vs `Desconocido`.

3. **Visualización e Inteligencia de Relaciones (Vega-Lite / ECharts):**
   - Asegurar que todo gráfico o mapa GIS se alimente del dataset filtrado activo (`filteredContacts`), re-size dinámico de contenedores y refit de Leaflet/ECharts al cambiar de pestaña.

---

## 📋 Protocolo de Fusión de Bóvedas (Smart Merge)

```python
# Pipeline conceptual Data Formulator para Radar Comercial
def merge_vault_datasets(raw_zip_data, live_harvest_data, local_crm_state):
    # 1. Base primaria con de-duplicación por URL/ID
    unified = {c['id']: c for c in raw_zip_data}
    
    # 2. Inyección de Metadata en vivo (HarvestAPI / Apify)
    for h in live_harvest_data:
        if h['id'] in unified:
            unified[h['id']].update(h['metadata'])
            unified[h['id']]['harvest_enriched'] = True
            
    # 3. Preservación estricta de Depuración Dunbar / CRM State
    for disc_id in local_crm_state.get('discarded', []):
        if disc_id in unified:
            unified[disc_id]['crmStatus'] = 'Descartado'
            unified[disc_id]['discardedFromPurge'] = True
            
    return list(unified.values())
```
