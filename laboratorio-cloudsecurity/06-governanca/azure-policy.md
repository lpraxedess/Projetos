# Governança e Conformidade — Azure Policy

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Validado bloqueio preventivo via Azure Policy em tentativa de criação de recurso sem a tag `Ambiente`. |
| 2026-03 | Implementada política de tag obrigatória (`Ambiente`) no escopo do Resource Group. |

</details>

## 🎯 Objetivo

Aqui começo a transformar requisitos de segurança e organização em controles que o próprio Azure consegue aplicar. O primeiro experimento foi usar o **Azure Policy** para exigir uma tag obrigatória nos recursos do laboratório.

## 🛠️ Implementação da Política de Tags

Configurei uma política personalizada para exigir a tag `Ambiente` nos recursos provisionados no `RG-CLOUD-SECURITY-LAB`.

### Definição da Política

Utilizei o modo `All` para analisar operações de criação ou modificação no nível de controle:

```json
{
  "mode": "All",
  "policyRule": {
    "if": {
      "field": "tags['Ambiente']",
      "exists": "false"
    },
    "then": {
      "effect": "deny"
    }
  },
  "parameters": {}
}
```

## 🧪 Validação

Tentei provisionar a conta de armazenamento `testesemtag` sem a tag obrigatória. O Azure Policy bloqueou a operação com `RequestDisallowedByPolicy`.

Isso validou que o controle está atuando preventivamente no *Management Plane*, antes da criação do recurso.

![Atribuição da política no Resource Group](../04-evidencias/governanca/politica-atribuida-rg-lab.png)

![Bloqueio preventivo de criação por falta de tag](../04-evidencias/governanca/politica-exigencia-tag-criacao-recurso.png)

## 🧠 O que este experimento mostrou

O principal aprendizado foi perceber na prática a diferença entre identificar um problema depois que um recurso existe e impedir que uma configuração fora do padrão seja criada.

Novos experimentos de governança serão registrados aqui conforme forem realizados.

---

[← Retornar ao Início do Laboratório](../README.md)
