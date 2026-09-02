import argparse, subprocess, json, sys

def run_unlighthouse(site_url, samples=5):
    """
    Integración oficial con Unlighthouse CLI (GitHub: https://github.com/harlan-zw/unlighthouse)
    """
    cmd = ["npx", "-y", "unlighthouse", "--site", site_url, "--samples", str(samples), "--ci"]
    print(f"=== EJECUTANDO UNLIGHTHOUSE EN REAL: {' '.join(cmd)} ===")
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return {
            "Status": "Success" if res.returncode == 0 else "Failed",
            "Repo": "https://github.com/harlan-zw/unlighthouse",
            "Output": res.stdout[:500],
            "Stderr": res.stderr[:300]
        }
    except Exception as e:
        return {"Status": "Error", "Message": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unlighthouse CLI Audit (https://github.com/harlan-zw/unlighthouse)")
    parser.add_argument("--site", required=True, help="URL del sitio a auditar")
    parser.add_argument("--samples", type=int, default=5, help="Número de páginas a muestrear")
    args = parser.parse_args()
    print(json.dumps(run_unlighthouse(args.site, args.samples), indent=2))
