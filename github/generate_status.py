#!/usr/bin/env python3
"""
Gera as tabelas de status do laboratório a partir de .github/status.yml
e injeta o resultado nos arquivos README entre marcadores especiais.

Marcadores esperados nos README:
    <!-- STATUS:START -->
    ... (tabela "Estado do Projeto" - gerada automaticamente) ...
    <!-- STATUS:END -->

    <!-- BACKLOG:START -->
    ... (tabela detalhada de todos os itens - gerada automaticamente) ...
    <!-- BACKLOG:END -->

Não edite o conteúdo entre os marcadores manualmente - ele será sobrescrito.
"""

import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
STATUS_FILE = REPO_ROOT / ".github" / "status.yml"

# Arquivos README que devem receber as tabelas geradas automaticamente
TARGET_READMES = [
    REPO_ROOT / "Projetos" / "laboratorio-cloudsecurity" / "README.md",
]

# Prioridade de "gravidade" para decidir o status agregado de uma área
STATUS_SEVERITY = {
    "Bloqueado": 4,
    "Em andamento": 3,
    "Planejado": 2,
    "Concluído": 1,
}

STATUS_EMOJI = {
    "Concluído": "✅",
    "Em andamento": "🔄",
    "Em evolução": "🔄",
    "Planejado": "📋",
    "Bloqueado": "🚧",
}


def load_data():
    with open(STATUS_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f)


def compute_area_status(items_in_area):
    """Deriva o status da área a partir dos itens que ela contém."""
    statuses = {i["status"] for i in items_in_area}
    if len(statuses) == 1:
        return statuses.pop()
    if "Bloqueado" in statuses:
        return "Bloqueado"
    if "Em andamento" in statuses:
        return "Em andamento"
    if "Concluído" in statuses and ("Planejado" in statuses or "Em andamento" in statuses):
        return "Em evolução"
    return max(statuses, key=lambda s: STATUS_SEVERITY.get(s, 0))


def build_area_table(data):
    items = data["items"]
    area_docs = data.get("area_docs", {})

    areas = {}
    for i in items:
        areas.setdefault(i["area"], []).append(i)

    lines = [
        "| Área | Status | Acompanhar |",
        "|---|---|---|",
    ]
    for area, area_items in areas.items():
        status = compute_area_status(area_items)
        emoji = STATUS_EMOJI.get(status, "")
        doc = area_docs.get(area)
        link = f"[Ver {area.lower()} →]({doc})" if doc else "Próximo"
        lines.append(f"| {area} | {emoji} {status} | {link} |")

    return "\n".join(lines)


def build_backlog_table(data):
    items = sorted(
        data["items"],
        key=lambda i: (STATUS_SEVERITY.get(i["status"], 0) * -1, i["area"]),
    )

    lines = [
        "| Item | Área | Status | Prioridade | Observação |",
        "|---|---|---|---|---|",
    ]
    for i in items:
        emoji = STATUS_EMOJI.get(i["status"], "")
        obs = i.get("bloqueio") or i.get("referencia") or ""
        lines.append(
            f"| {i['item']} | {i['area']} | {emoji} {i['status']} | "
            f"{i.get('prioridade', '-')} | {obs} |"
        )

    return "\n".join(lines)


def inject_block(content: str, start_marker: str, end_marker: str, new_block: str) -> str:
    start = content.find(start_marker)
    end = content.find(end_marker)
    if start == -1 or end == -1:
        print(f"  ⚠️  Marcadores '{start_marker}' não encontrados - pulando.")
        return content

    before = content[: start + len(start_marker)]
    after = content[end:]
    return f"{before}\n{new_block}\n{after}"


def main():
    data = load_data()
    area_table = build_area_table(data)
    backlog_table = build_backlog_table(data)

    for readme_path in TARGET_READMES:
        if not readme_path.exists():
            print(f"⚠️  Arquivo não encontrado: {readme_path}")
            continue

        content = readme_path.read_text(encoding="utf-8")
        original = content

        content = inject_block(content, "<!-- STATUS:START -->", "<!-- STATUS:END -->", area_table)
        content = inject_block(content, "<!-- BACKLOG:START -->", "<!-- BACKLOG:END -->", backlog_table)

        if content != original:
            readme_path.write_text(content, encoding="utf-8")
            print(f"✅ Atualizado: {readme_path}")
        else:
            print(f"ℹ️  Sem mudanças: {readme_path}")


if __name__ == "__main__":
    main()
