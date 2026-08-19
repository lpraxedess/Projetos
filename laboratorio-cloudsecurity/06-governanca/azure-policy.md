# Governança e Conformidade — Azure Policy

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Validado bloqueio preventivo via Azure Policy em tentativa de criação de recurso sem a tag `Ambiente`. |
| 2026-03 | Implementada política de tag obrigatória (`Ambiente`) no escopo do Resource Group. |

</details>

## 🎯 Objetivo

O objetivo desta etapa foi evoluir o laboratório de uma abordagem de controle estritamente reativa para mecanismos de governança preventiva. Utilizei o **Azure Policy** para garantir conformidade automatizada e padronização organizacional, focando inicialmente na obrigatoriedade de tags em recursos.

---

## 🛠️ Implementação da Política de Tags

Configurei uma política personalizada para exigir a presença obrigatória da tag `Ambiente` em qualquer recurso provisionado no escopo do grupo de recursos do laboratório (`RG-CLOUD-SECURITY-LAB`).

### Definição da Política

Utilizei o modo `All` para assegurar que o motor do Azure Policy analise e intercepte requisições de criação ou modificação (`PUT/PATCH`) no nível de controle:

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

---

## 🧪 Validação e Evidências

Para testar o controle preventivo, tentei provisionar uma conta de armazenamento (`testesemtag`) omitindo a tag obrigatória. O Azure Policy interceptou a submissão e bloqueou o provisionamento de forma síncrona.

> **Nota Técnica:** O retorno do código de erro `RequestDisallowedByPolicy` evidencia que o motor de conformidade atuou na camada de controle (*Management Plane*), negando a operação antes que qualquer infraestrutura fosse alocada.

![Atribuição da política no Resource Group](../04-evidencias/governanca/politica-atribuida-rg-lab.png)

![Bloqueio preventivo de criação por falta de tag](../04-evidencias/governanca/politica-exigencia-tag-criacao-recurso.png)

---

## 🧠 Experimentos e Aprendizados

> Esta seção registra o processo de aprendizagem. Novos experimentos devem ser adicionados quando uma implementação gerar um erro, descoberta ou decisão técnica relevante.

### Problema

Descreva o que você tentou implementar ou investigar.

### Erro

Registre o comportamento inesperado, mensagem de erro ou resultado diferente do esperado.

### Investigação

Registre as hipóteses, testes, documentação consultada e evidências utilizadas para encontrar a causa.

### Correção

Descreva a alteração realizada na Policy ou no ambiente.

### Resultado

Explique como a política foi validada, incluindo evidências do comportamento esperado.

### Aprendizado

Registre o conceito de governança, compliance ou Azure Policy consolidado com o experimento.

### Próximo passo

Registre o próximo controle ou cenário que pretende testar.

---

[← Retornar ao Início do Laboratório](../README.md)
