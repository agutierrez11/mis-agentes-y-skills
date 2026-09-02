import argparse, json

def banana_geo_format(markdown_content):
    """
    Formateador GEO (Generative Engine Optimization) para visibilidad en resúmenes de IA.
    """
    has_tables = "|" in markdown_content
    has_bullet = "-" in markdown_content or "*" in markdown_content
    word_count = len(markdown_content.split())
    
    score = 100
    suggestions = []
    
    if not has_tables:
        score -= 20
        suggestions.append("Agrega al menos 1 tabla Markdown para que los LLMs la extraigan como respuesta directa.")
    if word_count < 300:
        score -= 15
        suggestions.append("Amplía el contenido a más de 300 palabras con contexto semántico.")
        
    return {
        "GEO_Score": score,
        "Word_Count": word_count,
        "Has_Tables": has_tables,
        "Suggestions": suggestions
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True)
    args = parser.parse_args()
    print(json.dumps(banana_geo_format(args.text), indent=2, ensure_ascii=False))
