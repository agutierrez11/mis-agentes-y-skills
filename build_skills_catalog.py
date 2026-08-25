import os
import re

SKILLS_DIR = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\mis-agentes-y-skills\skills"
OUTPUT_MD = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\mis-agentes-y-skills\CATALOGO_SKILLS.md"
README_MD = r"c:\Users\Antonio\.gemini\antigravity-ide\scratch\mis-agentes-y-skills\README.md"

def parse_skill_md(skill_path):
    skill_md = os.path.join(skill_path, "SKILL.md")
    name = os.path.basename(skill_path)
    description = "Sin descripción provista."
    
    if os.path.exists(skill_md):
        try:
            with open(skill_md, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                
            # Parse YAML frontmatter if exists
            match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if match:
                yaml_text = match.group(1)
                desc_match = re.search(r"description:\s*(.+)", yaml_text, re.IGNORECASE)
                name_match = re.search(r"name:\s*(.+)", yaml_text, re.IGNORECASE)
                if desc_match:
                    description = desc_match.group(1).strip().strip('"\'')
                if name_match:
                    name = name_match.group(1).strip().strip('"\'')
            else:
                # Fallback to first paragraph
                lines = [l.strip() for l in content.split("\n") if l.strip() and not l.startswith("#")]
                if lines:
                    description = lines[0][:150] + "..." if len(lines[0]) > 150 else lines[0]
        except Exception as e:
            pass
            
    return name, description

def generate_catalog():
    if not os.path.exists(SKILLS_DIR):
        print("Skills dir not found!")
        return

    subdirs = sorted([d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))])
    total_count = len(subdirs)
    print(f"Encontradas {total_count} skills.")

    catalog = []
    catalog.append("# ⚡ CATÁLOGO MAESTRO DE SKILLS Y AGENTES DE IA")
    catalog.append(f"\n**Total de Skills Catalogadas y Disponibles:** `{total_count}` Skills Agénticas Especializadas\n")
    catalog.append("---")
    catalog.append("\n## 🔍 ÍNDICE ALFABÉTICO COMPLETO\n")
    catalog.append("| # | Nombre de la Skill / Agente | Descripción / Caso de Uso | Ruta de Acceso Directo |")
    catalog.append("| :-: | :--- | :--- | :--- |")

    for idx, dir_name in enumerate(subdirs, 1):
        skill_path = os.path.join(SKILLS_DIR, dir_name)
        name, description = parse_skill_md(skill_path)
        # Escape pipe chars in description
        clean_desc = description.replace("|", "\\|").replace("\n", " ")
        rel_link = f"[`{dir_name}`](./skills/{dir_name}/SKILL.md)"
        catalog.append(f"| {idx} | **{name}** | {clean_desc} | {rel_link} |")

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(catalog))
    print(f"Catálogo generado con éxito en: {OUTPUT_MD}")

    # Update README.md
    if os.path.exists(README_MD):
        with open(README_MD, "r", encoding="utf-8", errors="ignore") as f:
            readme_text = f.read()

        new_section = (
            f"## ⚡ SKILLS Y AGENTES EN ESTE REPOSITORIO (`./skills/`)\n\n"
            f"Este repositorio cuenta con **{total_count} Skills Agénticas Especializadas** en desarrollo web, "
            f"inteligencia comercial, ciencia de datos, DevOps, diseño UI/UX y aceleración con modelos de IA.\n\n"
            f"📘 **[`CATALOGO_SKILLS.md`](./CATALOGO_SKILLS.md)** — Consulta el catálogo completo indexado con descripciones y enlaces directos.\n\n"
            f"### Ejemplo de Skills Destacadas:\n"
            f"- 🎨 `awesome-claude-design`: Sistemas de diseño UI/UX premium (Linear, Stripe, Vercel).\n"
            f"- 🕵️ `agent-reach`: Scraping e inteligencia en tiempo real en +13 redes sociales.\n"
            f"- 🧠 `warden-agent-orchestrator`: Orquestación de agentes locales con deliberación multi-modelo.\n"
            f"- 📊 `ui-ux-pro-max`: Base de conocimientos de diseño UI, paletas y jerarquías de badges.\n"
            f"- 🤖 `deepseek-harness`: Harness para modelos DeepSeek y optimización de razonamiento.\n\n"
            f"*Ver el catálogo completo con las {total_count} skills en [CATALOGO_SKILLS.md](./CATALOGO_SKILLS.md).*\n"
        )

        if "## ??? SKILLS DISPONIBLES EN ESTE REPOSITORIO" in readme_text:
            readme_text = re.sub(
                r"## \?\?\? SKILLS DISPONIBLES EN ESTE REPOSITORIO.*$",
                new_section,
                readme_text,
                flags=re.DOTALL
            )
        elif "## ⚡ SKILLS Y AGENTES EN ESTE REPOSITORIO" in readme_text:
            readme_text = re.sub(
                r"## ⚡ SKILLS Y AGENTES EN ESTE REPOSITORIO.*$",
                new_section,
                readme_text,
                flags=re.DOTALL
            )
        else:
            readme_text += "\n\n" + new_section

        with open(README_MD, "w", encoding="utf-8") as f:
            f.write(readme_text)
        print("README.md actualizado exitosamente.")

if __name__ == "__main__":
    generate_catalog()
