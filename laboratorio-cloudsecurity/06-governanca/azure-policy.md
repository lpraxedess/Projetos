# Governança e Conformidade — Azure Policy

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Validado bloqueio preventivo via Azure Policy em tentativa de criação de recurso sem tag `Ambiente`. |
| 2026-03 | Implementada política de tag obrigatória (`Ambiente`) no escopo do Resource Group. |

</details>

## Objetivo

Meu objetivo aqui foi evoluir o laboratório do controle de acesso reativo para o controle preventivo de conformidade, utilizando o **Azure Policy** para garantir que todos os recursos sigam padrões organizacionais — nesse caso, a exigência de tags obrigatórias.

---

## Implementação da Política de Tags

Implementei uma política para exigir a presença obrigatória da tag `Ambiente` em qualquer recurso criado dentro do escopo do laboratório (`RG-CLOUD-SECURITY-LAB`).

### Definição da Política (JSON)

Usei o modo `All` para garantir que o motor do Azure Policy intercepte todas as requisições de criação (`PUT/PATCH`) no momento da submissão:

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

## Validação e Evidências

Para testar o controle, tentei criar uma conta de armazenamento (`testesemtag`) sem a tag obrigatória, e a criação foi bloqueada preventivamente pelo Azure Policy — confirmando a eficácia do controle.

**Nota:** o erro `RequestDisallowedByPolicy` confirma que o Azure interceptou a requisição e negou a operação antes mesmo da criação do recurso.

![politica](../04-evidencias/governanca/politica-atribuida-rg-lab.png)

![politica barrando](../04-evidencias/governanca/politica-exigencia-tag-criacao-recurso.png)

[Retornar ao Laboratório →](../README.md)
