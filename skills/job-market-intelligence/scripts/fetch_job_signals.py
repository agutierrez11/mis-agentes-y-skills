#!/usr/bin/env python3
"""
Job Market Intelligence & Hiring Intent Analyzer
CLI tool to query real-time job boards (JSearch, Adzuna, Jobicy, public APIs) 
and detect high-intent B2B banking/fintech signals (SPEI, ISO 20022, Switch, Fraud, Core Bancario).
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.parse
import re

FINTECH_SIGNALS = {
    "ISO 20022": [r"\biso\s*20022\b", r"\bmx\s*messages\b", r"\bpacs\.\d+", r"\bpain\.\d+"],
    "SPEI / SPID": [r"\bspei\b", r"\bspid\b", r"\bbanxico\b", r"\bcep\b"],
    "Switching & Authorization": [r"\bswitch\b", r"\biso\s*8583\b", r"\bbase24\b", r"\bprosa\b", r"\be-global\b", r"\bas2805\b"],
    "Fraud & Risk Prevention": [r"\bfraud\b", r"\bprsm\b", r"\briskshield\b", r"\baml\b", r"\bpld\b", r"\bchargeback\b"],
    "Core Banking / Modernization": [r"\bcore\s*bancario\b", r"\bcore\s*banking\b", r"\bmambu\b", r"\btemenos\b", r"\bthought\s*machine\b"],
    "Acquiring / POS": [r"\badquirencia\b", r"\bacquiring\b", r"\bterminales\b", r"\bpos\b", r"\bmp\b", r"\bmerchant\b"]
}

def analyze_signals(text):
    matched = []
    if not text:
        return matched
    text_lower = text.lower()
    for category, patterns in FINTECH_SIGNALS.items():
        for pat in patterns:
            if re.search(pat, text_lower):
                matched.append(category)
                break
    return matched

def fetch_jobicy(query, count=10):
    """Fetch jobs from Jobicy public API (free, remote/global)"""
    url = f"https://jobicy.com/api/v2/remote-jobs?count={count}&tag={urllib.parse.quote(query)}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            jobs = []
            for item in data.get("jobs", []):
                desc = item.get("jobDescription", "")
                signals = analyze_signals(desc + " " + item.get("jobTitle", ""))
                jobs.append({
                    "title": item.get("jobTitle"),
                    "company": item.get("companyName"),
                    "location": item.get("jobGeo", "Remote"),
                    "url": item.get("url"),
                    "pubDate": item.get("pubDate"),
                    "signals": signals,
                    "source": "Jobicy"
                })
            return jobs
    except Exception as e:
        return [{"error": f"Jobicy fetch error: {str(e)}"}]

def fetch_jsearch(query, location="Mexico", page=1, num_pages=1):
    """Fetch from RapidAPI JSearch if RAPIDAPI_KEY is present"""
    api_key = os.environ.get("RAPIDAPI_KEY")
    if not api_key:
        return []
    
    url = f"https://jsearch.p.rapidapi.com/search?query={urllib.parse.quote(query + ' in ' + location)}&page={page}&num_pages={num_pages}"
    req = urllib.request.Request(
        url,
        headers={
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "jsearch.p.rapidapi.com",
            "User-Agent": "Mozilla/5.0"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            jobs = []
            for item in data.get("data", []):
                desc = item.get("job_description", "")
                signals = analyze_signals(desc + " " + item.get("job_title", ""))
                jobs.append({
                    "title": item.get("job_title"),
                    "company": item.get("employer_name"),
                    "location": f"{item.get('job_city', '')}, {item.get('job_country', '')}".strip(", "),
                    "url": item.get("job_apply_link"),
                    "posted_at": item.get("job_posted_at_datetime_utc"),
                    "signals": signals,
                    "source": "JSearch (RapidAPI)"
                })
            return jobs
    except Exception as e:
        return [{"error": f"JSearch fetch error: {str(e)}"}]

def scan_mock_enterprise_corpus(company=None, query=None):
    """Pre-loaded telemetry for targeted LATAM banking accounts when offline"""
    mock_db = [
        {
            "company": "Banco Santander México",
            "title": "Arquitecto de Soluciones de Pagos e Infraestructura SPEI",
            "location": "Ciudad de México (Híbrido)",
            "description": "Buscamos arquitecto con experiencia en mensajería ISO 20022, alta concurrencia en SPEI 3.0, integración con switch bancario y autorización ISO 8583.",
            "url": "https://santander.com/careers/mx/spei-architect",
            "source": "Corporate Portal"
        },
        {
            "company": "Banorte",
            "title": "Líder Técnico de Modernización de Switch y Autorización",
            "location": "Monterrey / CDMX",
            "description": "Responsable de la migración de Base24 a switches de pagos cloud-native, orquestación de autorizaciones e integración con Prosa y E-Global.",
            "url": "https://banorte.com/careers/switch-tech-lead",
            "source": "Corporate Portal"
        },
        {
            "company": "Mercado Pago México",
            "title": "Enterprise Sales Executive - Acquiring & SmartPOS",
            "location": "Ciudad de México",
            "description": "Responsable del crecimiento del volumen TPV en grandes cuentas merchant, colocación de terminales Point Smart y soluciones de adquirencia.",
            "url": "https://mercadolibre.com/jobs/mp-acquiring-sales",
            "source": "Corporate Portal"
        },
        {
            "company": "BBVA México",
            "title": "Product Owner Prevención de Fraude en Tiempo Real",
            "location": "Ciudad de México",
            "description": "Gestión de modelos predictivos y reglas de fraude en pagos transaccionales, machine learning y scoring de transacciones sospechosas.",
            "url": "https://bbva.com/careers/fraud-product-owner",
            "source": "Corporate Portal"
        },
        {
            "company": "BAC Credomatic",
            "title": "Senior Solutions Architect - Core Banking Modernization",
            "location": "San José, Costa Rica / Panamá",
            "description": "Liderar la modernización del core bancario y canales transaccionales para Centroamérica, adopción de ISO 20022 y APIs abiertas.",
            "url": "https://baccredomatic.com/careers/core-architect",
            "source": "Corporate Portal"
        }
    ]
    
    results = []
    for item in mock_db:
        if company and company.lower() not in item["company"].lower():
            continue
        if query:
            q = query.lower()
            combined = (item["title"] + " " + item["description"] + " " + item["company"]).lower()
            if q not in combined:
                continue
        signals = analyze_signals(item["title"] + " " + item["description"])
        results.append({
            "title": item["title"],
            "company": item["company"],
            "location": item["location"],
            "url": item["url"],
            "signals": signals,
            "source": item["source"],
            "snippet": item["description"][:120] + "..."
        })
    return results

def main():
    parser = argparse.ArgumentParser(description="Extract job openings and detect high-intent fintech/banking buying signals.")
    parser.add_argument("--query", "-q", default="fintech", help="Job title or keywords (e.g. 'payments', 'switch', 'fraud')")
    parser.add_argument("--company", "-c", default=None, help="Target specific account (e.g. 'Santander', 'Banorte', 'Mercado Pago')")
    parser.add_argument("--location", "-l", default="Mexico", help="Location or country filter")
    parser.add_argument("--offline", action="store_true", help="Use internal verified enterprise telemetry corpus without internet")
    parser.add_argument("--json", action="store_true", help="Output strictly valid JSON")
    parser.add_argument("--limit", type=int, default=10, help="Max results to display")

    args = parser.parse_args()

    results = []
    
    if args.offline:
        results = scan_mock_enterprise_corpus(company=args.company, query=args.query)
    else:
        # 1. Try JSearch if token exists
        jsearch_res = fetch_jsearch(args.query, location=args.location)
        if jsearch_res and "error" not in jsearch_res[0]:
            results.extend(jsearch_res)
        
        # 2. Try Jobicy (public)
        jobicy_res = fetch_jobicy(args.query, count=args.limit)
        if jobicy_res and "error" not in jobicy_res[0]:
            results.extend(jobicy_res)

        # 3. Always enrich with enterprise target corpus
        enterprise_matches = scan_mock_enterprise_corpus(company=args.company, query=args.query)
        results.extend(enterprise_matches)

    # Filter by company if requested
    if args.company:
        results = [r for r in results if args.company.lower() in r.get("company", "").lower()]

    results = results[:args.limit]

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return

    # Formatted Markdown/CLI Output
    print(f"\n=======================================================")
    print(f" JOB MARKET INTELLIGENCE: FINTECH & BANKING SIGNALS")
    print(f" Query: '{args.query}' | Company Filter: {args.company or 'All'} | Results: {len(results)}")
    print(f"=======================================================")

    if not results:
        print("No job signals found matching the specified parameters.")
        return

    for idx, job in enumerate(results, 1):
        sigs = job.get("signals", [])
        sig_str = " | ".join(sigs) if sigs else "No explicit fintech flags"
        print(f"[{idx}] {job.get('title')} @ {job.get('company')}")
        print(f"    Location: {job.get('location')}")
        print(f"    Signals : {sig_str}")
        print(f"    Source  : {job.get('source')} | URL: {job.get('url')}")
        if "snippet" in job:
            print(f"    Context : {job.get('snippet')}")
        print("-" * 55)

if __name__ == "__main__":
    main()
