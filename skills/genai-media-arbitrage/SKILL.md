---
name: genai-media-arbitrage
description: Use when calculating cost arbitrage, evaluating generation pricing, or routing inference across video/image AI models (Veo 3.1, Sora 2, Runway, Flux Pro) between direct providers and low-cost brokers.
---

# GenAI Media Arbitrage Engine

This skill calculates real-time cost arbitrage and brokers multi-model generation requests for video and image foundation models (Sora 2 Turbo/Standard, Google Veo 3.1, Runway Aleph/Gen-3, Flux 1.1 Pro, Midjourney). 

By routing inference via gateway brokers (such as Kie.ai, Fal.ai, Together, Replicate pool batches) instead of paying full retail direct API margins, workloads achieve **70% to 78.6% cost reduction**.

## Quick Start / CLI Execution

Execute the built-in CLI tool located in `scripts/media_arbitrage_client.py`:

```bash
# 1. Compare full arbitrage spectrum across all supported models
python C:\Users\Antonio\.gemini\config\skills\genai-media-arbitrage\scripts\media_arbitrage_client.py --compare-all

# 2. Calculate savings for a specific model (e.g. Sora 2 Turbo for 30 seconds of video)
python C:\Users\Antonio\.gemini\config\skills\genai-media-arbitrage\scripts\media_arbitrage_client.py --model sora-2-turbo --units 30

# 3. Calculate image generation batch arbitrage (e.g. 500 images on Flux 1.1 Pro)
python C:\Users\Antonio\.gemini\config\skills\genai-media-arbitrage\scripts\media_arbitrage_client.py --model flux-1.1-pro --units 500

# 4. Output JSON for automated pricing calculators or agent pipelines
python C:\Users\Antonio\.gemini\config\skills\genai-media-arbitrage\scripts\media_arbitrage_client.py --model veo-3.1 --units 60 --json
```

## Model Benchmark Matrix

| Model | Media Type | Direct Retail | Broker Router | Arbitrage Margin |
| :--- | :--- | :--- | :--- | :--- |
| **Sora 2 Turbo** | Video (1080p) | $0.20 / sec | $0.045 / sec | **-77.5%** |
| **Sora 2 Standard** | Video (1080p) | $0.40 / sec | $0.089 / sec | **-77.8%** |
| **Google Veo 3.1** | Video (4K/1080p) | $0.35 / sec | $0.075 / sec | **-78.6%** |
| **Runway Aleph** | Video (1080p) | $0.25 / sec | $0.060 / sec | **-76.0%** |
| **Flux 1.1 Pro** | Image (2K) | $0.05 / img | $0.015 / img | **-70.0%** |
| **Midjourney v6.1** | Image (1K) | $0.04 / img | $0.012 / img | **-70.0%** |

## Integration with Agent Swarms

When building video pipelines, marketing automations, or dynamic B2B video generation, agents invoke this skill to pick the most cost-effective generation route before firing outbound requests.
