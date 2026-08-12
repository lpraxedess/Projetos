# Controle de Acesso — Cloud Security Lab

## Objetivo

Evoluir progressivamente os controles de acesso do ambiente, começando pelos controles de rede e avançando para controles de identidade, autenticação e autorização.

---

## Evolução do Controle de Acesso

### Etapa 01 — Controle de acesso pela rede

Na primeira etapa, o controle de acesso administrativo foi implementado principalmente através dos Network Security Groups (NSGs).

O acesso ao ambiente foi segmentado por subnet, permitindo:

- RDP externo somente para o ambiente de gerenciamento;
- RDP interno entre `SNET-MANAGEMENT` e `SNET-SECURITY`;
- ausência de acesso administrativo direto da Internet ao servidor de segurança.

Essa etapa estabeleceu o controle de acesso no nível de rede.

![NSGs do ambiente](../04-evidencias/controle-acesso/nsg-cloud-security.png)

---

### Etapa 02 — Controle de acesso baseado em identidade

Com a estrutura de rede estabelecida, o próximo nível de controle passou a ser a identidade.

Foram criadas contas com finalidades diferentes no Microsoft Entra ID:

- `luiz.admin` — administração de identidade;
- `luiz.azure.admin` — administração do Azure;
- `luiz.azure.reader` — acesso de leitura;
- `lab.breakglass01` — conta de emergência;
- `lab.breakglass02` — conta de emergência.

![Identidades do Microsoft Entra ID](../04-evidencias/controle-acesso/identidades-entra.png)

---

### Etapa 03 — Evolução para Azure RBAC

A próxima evolução é substituir o uso amplo da função `Owner` por funções específicas de acordo com a necessidade de cada identidade.

O objetivo é aplicar o princípio do menor privilégio e reduzir permissões administrativas permanentes.

![IAM da assinatura](../04-evidencias/controle-acesso/iam-assinatura.png)

---

## Modelo de Evolução

Controle de acesso
       │
       ├── 01. Rede
       │      └── NSGs
       │
       ├── 02. Identidade
       │      └── Microsoft Entra ID
       │
       ├── 03. Autorização
       │      └── Azure RBAC
       │
       ├── 04. Autenticação
       │      └── MFA
       │
       └── 05. Privilégios
              └── PIM / menor privilégio

## Estado Atual

| Controle | Estado |
|---|---|
| Segmentação de rede | Implementado |
| NSGs | Implementado |
| Microsoft Entra ID | Implementado |
| Separação de identidades | Implementado |
| Azure RBAC | Em evolução |
| MFA | Próxima etapa |
| PIM | Planejado |

## Próxima Etapa

A próxima evolução será revisar as atribuições atuais de `Owner` e implementar Azure RBAC com permissões mais específicas e escopo reduzido.
