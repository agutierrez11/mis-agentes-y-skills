---
name: osintgraph-neo4j-mining
description: Arquitectura de base de datos orientada a grafos (Neo4j y consultas Cypher) inspirada en Osintgraph para minería de relaciones sociales, cálculo de puentes de 2º y 3er grado y descubrimiento de influencias B2B.
---

# 🕸️ Osintgraph & Neo4j Relationship Intelligence

## 📌 Propósito y Visión General
Esta Skill establece los patrones de arquitectura de datos en **Neo4j** (usando el lenguaje de consulta **Cypher**) inspirados en el proyecto *Osintgraph*. Permite modelar redes relacionales complejas (contactos, empresas, interacciones y puentes de confianza) para responder consultas de alta velocidad que serían ineficientes en SQL tradicional.

---

## 🎯 Casos de Uso Core

### 1. Minería de Puentes Cálidos (Radar Comercial)
Resolver en milisegundos preguntas como:
- *¿Quién en la red de Antonio tiene una relación de 1er grado con una persona que trabaje en la empresa objetivo X y que a su vez conozca a un decision maker en España?*

### 2. Análisis OSINT y Agrupación de Afinidades (Célula de Agentes)
- Mapear grupos de intereses, experiencia previa compartida (ej: ex-colegas de Everis/Falabella) y clústeres de cuentas objetivo.

---

## 🛠️ Esquema del Grafo en Neo4j (Cypher Protocol)

### Modelado de Nodos y Relaciones
```cypher
// Nodos Core
CREATE (u:User {id: "antonio", name: "Antonio Gutiérrez", role: "Owner"})
CREATE (c:Contact {id: "marc_garcia", name: "Marc García", position: "VP of Sales", city: "Madrid"})
CREATE (comp:Company {id: "klarna", name: "Klarna", sector: "FinTech"})

// Relaciones
CREATE (u)-[:OWNS_BOVEDA]->(c)
CREATE (c)-[:WORKS_AT {since: "2023-09", status: "Active"}]->(comp)
CREATE (u)-[:HAS_INTERACTION {dms_sent: 12, engagement_score: 95}]->(c)
```

### Consulta de Búsqueda de Puentes de 2º Grado (Cypher Query)
```cypher
// Buscar puentes de confianza cálidos hacia la empresa 'Klarna'
MATCH (me:User {id: "antonio"})-[:OWNS_BOVEDA]->(bridge:Contact)-[:WORKS_AT {status: "Active"}]->(targetComp:Company {name: "Klarna"})
WHERE bridge.engagement_score > 75
RETURN bridge.name AS ContactoCalido, 
       bridge.position AS CargoActual, 
       bridge.engagement_score AS ScoreConfianza
ORDER BY bridge.engagement_score DESC
LIMIT 10;
```

---

## 🚀 Integración Backend (Python / FastAPI / Neo4j Driver)
```python
from neo4j import GraphDatabase

class RelationshipGraphEngine:
    def __init__(self, uri, auth):
        self.driver = GraphDatabase.driver(uri, auth=auth)

    def find_warm_bridges(self, owner_id: str, target_company: str):
        query = """
        MATCH (u:User {id: $owner_id})-[:OWNS_BOVEDA]->(c:Contact)-[:WORKS_AT {status: 'Active'}]->(comp:Company)
        WHERE toLower(comp.name) CONTAINS toLower($target_company)
        RETURN c.name AS name, c.position AS position, c.city AS city
        """
        with self.driver.session() as session:
            result = session.run(query, owner_id=owner_id, target_company=target_company)
            return [record.data() for record in result]
```
