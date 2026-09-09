#!/usr/bin/env python3
"""
GenAI Media Arbitrage CLI Tool
Calculate pricing arbitrage across state-of-the-art video & image generation models (Veo 3.1, Sora 2, Runway Aleph, Flux 1.1 Pro)
and route requests across direct provider APIs vs. low-cost brokers (Kie.ai, Together, Replicate, Fal.ai).
"""

import argparse
import json
import os
import sys

# Reference pricing benchmark ($ / unit: second of video or per image generation)
MODEL_REGISTRY = {
    "sora-2-turbo": {
        "provider": "OpenAI / Sora",
        "type": "video",
        "direct_cost_per_sec": 0.20,
        "broker_cost_per_sec": 0.045, # e.g. Kie.ai / batch discounted router
        "broker_name": "Kie.ai / Batch Gateway",
        "resolution": "1080p",
        "max_duration_sec": 10
    },
    "sora-2-standard": {
        "provider": "OpenAI / Sora",
        "type": "video",
        "direct_cost_per_sec": 0.40,
        "broker_cost_per_sec": 0.089,
        "broker_name": "Kie.ai Gateway",
        "resolution": "1080p",
        "max_duration_sec": 20
    },
    "veo-3.1": {
        "provider": "Google DeepMind / Vertex AI",
        "type": "video",
        "direct_cost_per_sec": 0.35,
        "broker_cost_per_sec": 0.075,
        "broker_name": "Cloud Broker Pool",
        "resolution": "4K / 1080p",
        "max_duration_sec": 60
    },
    "runway-aleph": {
        "provider": "RunwayML Gen-3",
        "type": "video",
        "direct_cost_per_sec": 0.25,
        "broker_cost_per_sec": 0.060,
        "broker_name": "Fal.ai / Replicate",
        "resolution": "1080p",
        "max_duration_sec": 10
    },
    "flux-1.1-pro": {
        "provider": "Black Forest Labs",
        "type": "image",
        "direct_cost_per_img": 0.05,
        "broker_cost_per_img": 0.015,
        "broker_name": "Together.ai / Fal.ai",
        "resolution": "2048x2048",
        "max_duration_sec": 0
    },
    "midjourney-v6.1": {
        "provider": "Midjourney Direct",
        "type": "image",
        "direct_cost_per_img": 0.04,
        "broker_cost_per_img": 0.012,
        "broker_name": "Discord Bot API Gateway",
        "resolution": "1024x1024",
        "max_duration_sec": 0
    }
}

def calculate_arbitrage(model_key, units=10):
    """Compute direct vs broker costs and percentage savings"""
    info = MODEL_REGISTRY.get(model_key)
    if not info:
        return None
    
    is_video = info["type"] == "video"
    direct_unit_cost = info["direct_cost_per_sec"] if is_video else info["direct_cost_per_img"]
    broker_unit_cost = info["broker_cost_per_sec"] if is_video else info["broker_cost_per_img"]
    
    total_direct = direct_unit_cost * units
    total_broker = broker_unit_cost * units
    savings_usd = total_direct - total_broker
    savings_pct = (savings_usd / total_direct) * 100 if total_direct > 0 else 0
    
    return {
        "model": model_key,
        "type": info["type"],
        "provider": info["provider"],
        "broker_name": info["broker_name"],
        "units": units,
        "unit_label": "seconds" if is_video else "images",
        "direct_cost_total": round(total_direct, 4),
        "broker_cost_total": round(total_broker, 4),
        "net_savings_usd": round(savings_usd, 4),
        "arbitrage_savings_percent": round(savings_pct, 1)
    }

def main():
    parser = argparse.ArgumentParser(description="GenAI Media Arbitrage Engine - Compare direct vs broker costs for Video/Image AI models.")
    parser.add_argument("--model", "-m", choices=list(MODEL_REGISTRY.keys()), default=None, help="Target model key")
    parser.add_argument("--units", "-u", type=int, default=10, help="Number of seconds (video) or images generated")
    parser.add_argument("--compare-all", "-a", action="store_true", help="Compare arbitrage across all models in registry")
    parser.add_argument("--json", action="store_true", help="Output valid JSON")

    args = parser.parse_args()

    if args.compare_all or not args.model:
        summary_list = []
        for key in MODEL_REGISTRY:
            u = args.units if args.units else (10 if MODEL_REGISTRY[key]["type"] == "video" else 50)
            summary_list.append(calculate_arbitrage(key, units=u))
        
        if args.json:
            print(json.dumps(summary_list, indent=2, ensure_ascii=False))
            return
        
        print("\n" + "=" * 70)
        print(" GENAI MEDIA ARBITRAGE BENCHMARK (DIRECT vs. LOW-COST BROKERS)")
        print("=" * 70)
        print(f"{'Model':<18} | {'Type':<6} | {'Units':<7} | {'Direct ($)':<10} | {'Broker ($)':<10} | {'Arbitrage Savings':<15}")
        print("-" * 70)
        for s in summary_list:
            print(f"{s['model']:<18} | {s['type']:<6} | {s['units']} {s['unit_label'][:3]:<3} | ${s['direct_cost_total']:<9.2f} | ${s['broker_cost_total']:<9.2f} | -{s['arbitrage_savings_percent']:.1f}% (${s['net_savings_usd']:.2f})")
        print("=" * 70 + "\n")
        return

    # Single model calculation
    arb = calculate_arbitrage(args.model, units=args.units)
    if args.json:
        print(json.dumps(arb, indent=2, ensure_ascii=False))
        return

    print(f"\n=======================================================")
    print(f" ARBITRAGE REPORT: {args.model.upper()}")
    print(f"=======================================================")
    print(f" Type            : {arb['type'].capitalize()}")
    print(f" Provider Direct : {arb['provider']}")
    print(f" Broker Route    : {arb['broker_name']}")
    print(f" Volume          : {arb['units']} {arb['unit_label']}")
    print(f" Direct Cost     : ${arb['direct_cost_total']:.4f} USD")
    print(f" Broker Cost     : ${arb['broker_cost_total']:.4f} USD")
    print(f" Net Savings     : ${arb['net_savings_usd']:.4f} USD (-{arb['arbitrage_savings_percent']}%)")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
