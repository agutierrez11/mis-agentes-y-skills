---
name: job-market-intelligence
description: Use when extracting job openings, tracking hiring surges, or detecting B2B enterprise intent signals (ISO 20022, SPEI, switch, fraud, acquiring) across banks and fintechs.
---

# Job Market Intelligence & Enterprise Intent Signals

This skill extracts real-time and historical hiring telemetry across job boards, career portals, and financial institutions to detect strategic B2B intent signals. When banks or fintechs hire for specialized protocols (ISO 20022, SPEI 3.0, Base24, Real-Time Fraud, SmartPOS acquiring), it reveals internal modernization budgets and active procurement cycles.

## Quick Start / CLI Execution

Run the built-in CLI tool located in `scripts/fetch_job_signals.py`:

```bash
# 1. Search for specific technology intent across accounts
python C:\Users\Antonio\.gemini\config\skills\job-market-intelligence\scripts\fetch_job_signals.py --query "SPEI"

# 2. Target a specific financial institution
python C:\Users\Antonio\.gemini\config\skills\job-market-intelligence\scripts\fetch_job_signals.py --query "" --company "Santander"

# 3. Output clean JSON for pipeline ingestion
python C:\Users\Antonio\.gemini\config\skills\job-market-intelligence\scripts\fetch_job_signals.py --query "switch" --json

# 4. Offline / low-latency mode using curated LATAM banking corpus
python C:\Users\Antonio\.gemini\config\skills\job-market-intelligence\scripts\fetch_job_signals.py --query "fraud" --offline
```

## Intent Signal Detection Map

The engine automatically flags matches across 6 core payments domains:

1. **ISO 20022 / MX Messaging**: `pacs.008`, `pain.001`, `camt.053`, message transformations.
2. **SPEI / SPID / Banxico**: Banxico clearing, high-concurrency SPEI 3.0 gateways, CEP reconciliation.
3. **Switching & Authorization**: ISO 8583, Base24, ACI switch migration, Prosa, E-Global, AS2805.
4. **Fraud & Risk Prevention**: PRM, RiskShield, Falcon, real-time AML/PLD rules, chargeback defense.
5. **Core Banking Modernization**: Cloud-native cores (Mambu, Temenos, Thought Machine) vs. legacy mainframes.
6. **Acquiring / POS**: SmartPOS, terminal fleets, ISO acquiring, merchant acquiring solutions.

## Data Sources

- **JSearch (RapidAPI)**: Real-time global aggregations across LinkedIn, Indeed, Glassdoor, and ZipRecruiter (requires `RAPIDAPI_KEY` in environment if live querying).
- **Jobicy Remote Engine**: Native live REST API without credentials for global remote roles.
- **Enterprise Bank Telemetry**: Built-in benchmark corpus of top tier-1 LATAM financial institutions (Santander, Banorte, BBVA, Mercado Pago, BAC Credomatic).
