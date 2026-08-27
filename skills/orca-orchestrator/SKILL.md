# 🐋 Orca Agent Orchestrator & Parallel ADE (`orca-orchestrator`)

Esta skill proporciona pautas y patrones para orquestar múltiples agentes de IA (Claude Code, Gemini, Codex, Cursor CLI) en paralelo utilizando el entorno **[stablyai/orca](https://github.com/stablyai/orca)** (Agent Development Environment).

---

## 📌 ¿Cuándo usar esta Skill?
- Al ejecutar **experimentos en paralelo** o competir enfoques entre distintos agentes.
- Para aislar cambios de código complejos mediante **Git Worktrees** antes de mergear a `main`.
- Cuando se requiera coordinar una flota de subagentes agénticos asignando tareas por ramas o repositorios independientes.

---

## 🛠️ Arquitectura de Orquestación Orca

```
              [ Orca ADE Control Plane ]
                         │
     ┌───────────────────┼───────────────────┐
     ▼                   ▼                   ▼
[ Git Worktree A ]  [ Git Worktree B ]  [ Git Worktree C ]
  Agent: Claude       Agent: Gemini       Agent: Custom CLI
  Feature: Backend    Feature: UI/UX      Feature: Tests
```

---

## ⚙️ Reglas de Aislamiento y Trabajo Paralelo

1. **Uso Estricto de Worktrees:**
   - Crear ramas/worktrees temporales (`git worktree add ../feature-branch feature-branch`) para cada ejecución de agente en Orca.
2. **Evaluación Comparativa (Multi-Agent Benchmark):**
   - Comparar diffs y métricas entre worktrees antes de unificar cambios en la rama principal.
3. **Sincronización CI/CD:**
   - Una vez validada la solución ganadora en Orca, ejecutar los tests automáticos, linter y realizar `git commit` + `git push` a `main`.
