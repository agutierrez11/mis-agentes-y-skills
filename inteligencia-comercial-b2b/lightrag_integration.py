# ==============================================================================
# LIGHTRAG INTEGRATION HELPER FOR INTELLIGENTIAL CPS COPILOT (OBSIDIAN VAULT INGEST)
# ==============================================================================
import os
import asyncio
import glob

def init_lightrag_local(working_dir="./cps_lightrag_store"):
    """
    Inicializa el motor LightRAG con Ollama Local (http://localhost:11434)
    Soporta GraphRAG de doble nivel (Low-Level & High-Level Knowledge Graph)
    """
    try:
        from lightrag import LightRAG, QueryParam
        from lightrag.llm import ollama_model_complete, ollama_embedding
        
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)

        rag = LightRAG(
            working_dir=working_dir,
            llm_model_func=ollama_model_complete,
            llm_model_name="llama3.1",
            embedding_func=ollama_embedding,
            embedding_model_name="nomic-embed-text",
        )
        return rag
    except ImportError:
        print("[Warning]: lightrag-hku no esta instalado. Usando fallback heuristico local.")
        return None

def ingest_obsidian_vault(rag_instance, vault_dir="./obsidian_vault"):
    """Ingesta todos los archivos Markdown (.md) de la boveda de Obsidian en LightRAG"""
    if rag_instance is None:
        print("[Warning]: Instancia LightRAG no disponible para ingesta.")
        return False
        
    if not os.path.exists(vault_dir):
        print(f"[Error]: La boveda de Obsidian no existe en {vault_dir}")
        return False

    md_files = glob.glob(os.path.join(vault_dir, "**/*.md"), recursive=True)
    print(f"[LightRAG Ingest]: Ingestando {len(md_files)} documentos Markdown de la boveda...")
    
    total_chars = 0
    for file_path in md_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if len(content.strip()) > 50:
                    rag_instance.insert(content)
                    total_chars += len(content)
        except Exception as e:
            print(f"Error ingestando {file_path}: {e}")
            
    print(f"[LightRAG Ingest OK]: {len(md_files)} archivos ({total_chars:,} caracteres) procesados en el grafo.")
    return True

def query_lightrag_cps(rag_instance, user_query, mode="hybrid"):
    """
    Consulta al Grafo de Conocimiento de LightRAG
    Modos: 'hybrid' (Grafo Dual + Vectores), 'local' (Detalles), 'global' (Conceptos CPS)
    """
    if rag_instance is None:
        return "[LightRAG no activo - usando Fallback de Reglas Heurísticas]"
    
    try:
        from lightrag import QueryParam
        result = rag_instance.query(user_query, param=QueryParam(mode=mode))
        return result
    except Exception as e:
        return f"[Error en Inferencia LightRAG: {str(e)}]"

if __name__ == "__main__":
    print("=== MÓDULO DE INTEGRACIÓN DE LIGHTRAG CON OBSIDIAN VAULT ===")
    rag = init_lightrag_local()
    if rag:
        ingest_obsidian_vault(rag)
