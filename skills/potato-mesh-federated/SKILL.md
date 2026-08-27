---
name: potato-mesh-federated
description: Arquitectura de sincronización federada, local-first y protocolo P2P inspirada en Potato Mesh para redes de bóvedas privadas, descubrimiento sin servidor central y Sovereign Agent Mesh (SAM).
---

# 🌐 Potato Mesh & Federated Local-First Architecture

## 📌 Propósito y Visión General
Esta Skill abstrae los patrones de arquitectura **local-first, federados y descentralizados (P2P)** inspirados en el proyecto *Potato Mesh*. Define cómo estructurar sistemas donde los datos sensibles residen exclusivamente en dispositivos o nodos locales (Zero-Knowledge) y se comunican mediante protocolos federados sin depender de una base de datos cloud centralizada.

---

## 🎯 Casos de Uso Core

### 1. Bóvedas Privadas Federadas (Radar Comercial - BYOD)
- Cada vendedor posee un nodo/bóveda local encriptada con su patrimonio de contactos de LinkedIn.
- **Protocolo de Descubrimiento Federado**: Cuando el Vendedor A busca un contacto en Klarna, el sistema consulta de forma anónima a las bóvedas de los Vendedores B y C:
  - *Respuesta anonimizada*: `"Nodo B tiene 1 contacto activo con score 95"`.
  - *Acción*: El Vendedor A solicita la introducción cálida mediante una señal federada P2P aprobada por el Vendedor B.

### 2. Sovereign Agent Mesh / SAM (Célula de Agentes Antigravity)
- Conectar agentes de IA en diferentes terminales o servidores locales mediante mensajería mesh/P2P sin pasar por servidores centrales de terceros.

---

## 🛠️ Patrón de Arquitectura (Federated Node Protocol)

### Diagrama de Comunicación P2P (Bóvedas Privadas)
```
  [ Bóveda Vendedor A (Local) ] ◄──(Señal Federada Anonimizada)──► [ Bóveda Vendedor B (Local) ]
                 │                                                            │
                 ▼                                                            ▼
      (Silo Privado Encriptado)                                  (Silo Privado Encriptado)
```

### Especificación de Mensaje de Descubrimiento Anónimo (P2P Handshake)
```json
{
  "protocol": "radar-federated-v1",
  "action": "QUERY_WARM_BRIDGE",
  "query_hash": "a8f9c0e2b1d3", // Hash de la empresa objetivo (ej: "klarna")
  "requester_node_id": "node_antonio_01",
  "signature": "eddsa_sig_..."
}
```

### Respuesta del Nodo Federado (Zero-Knowledge Response)
```json
{
  "responder_node_id": "node_giovanna_02",
  "match_found": true,
  "match_count": 1,
  "highest_engagement_score": 98,
  "bounty_eligible": true,
  "bounty_amount_usd": 150
}
```

---

## 🛡️ Principios Universales de Seguridad
1. **Zero Centralized Storage**: Las conversaciones y chats privados jamás se consolidan en una base de datos compartida.
2. **Opt-in Referral Approval**: El dueño de la bóveda receptora debe presionar individualmente "Aprobar Introducción" antes de revelar la identidad del contacto.
3. **Firmas Criptográficas Ed25519**: Toda comunicación entre nodos federados debe estar firmada criptográficamente para evitar suplantaciones.
