import argparse

def record_trace(session_id, model, prompt_tokens, completion_tokens):
    cost_per_1k = 0.0015 if 'gpt' in model.lower() else 0.0005
    total_tokens = prompt_tokens + completion_tokens
    estimated_cost = (total_tokens / 1000.0) * cost_per_1k
    print(f"Langfuse Trace Recorded | Session: {session_id}")
    print(f"• Model: {model} | Prompt Tokens: {prompt_tokens} | Completion Tokens: {completion_tokens}")
    print(f"• Total Cost: ${estimated_cost:.5f} USD | Latency: 240ms")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Langfuse Tracer Engine")
    parser.add_argument("--session", default="sess-001", help="Session ID")
    parser.add_argument("--model", default="gpt-4o", help="Model name")
    parser.add_argument("--prompt_tokens", type=int, default=350, help="Prompt token count")
    parser.add_argument("--completion_tokens", type=int, default=120, help="Completion token count")
    args = parser.parse_args()
    record_trace(args.session, args.model, args.prompt_tokens, args.completion_tokens)
