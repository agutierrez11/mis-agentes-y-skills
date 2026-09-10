---
name: multi-llm-consensus
description: Use when arbitrating critical architectural decisions, code reviews, or business strategies across multiple models with forced adversarial challenges and calibrated confidence scoring.
---

# Multi-LLM Consensus Engine

Inspired by Michael Sitarzewski's `msitarzewski/duh` and Andrej Karpathy's LLM Council, this skill arbitrates and stress-tests critical decisions through a 4-phase adversarial consensus protocol:

```
PROPOSE  -->  CHALLENGE  -->  REVISE  -->  COMMIT
```

1. **Propose**: Drafts an initial high-quality solution or technical blueprint.
2. **Adversarial Challenge (Forced Dissent)**: A devil's advocate model identifies edge cases, security vulnerabilities, latency bottlenecks, and operational friction (anti-sycophancy mode).
3. **Revise**: The proposer is forced to harden the solution by directly incorporating solutions to every valid objection.
4. **Commit**: Synthesizes the final hardened decision with epistemic confidence metrics.

## CLI Usage

Run the consensus CLI tool in `scripts/consensus_engine.py`:

```bash
# 1. Deliberate any architecture or commercial strategy question
python C:\Users\Antonio\.gemini\config\skills\multi-llm-consensus\scripts\consensus_engine.py "Arquitectura de switch transaccional ISO 20022 con alta concurrencia"

# 2. Output structured JSON for agent pipelines
python C:\Users\Antonio\.gemini\config\skills\multi-llm-consensus\scripts\consensus_engine.py "Estrategia de compensacion y comisiones en SmartPOS" --json

# 3. Deterministic offline mode (no API key required)
python C:\Users\Antonio\.gemini\config\skills\multi-llm-consensus\scripts\consensus_engine.py "Migracion de base24 a microservicios" --offline
```
