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

Após estabelecer os controles de acesso no nível de rede e estruturar as identidades no Microsoft Entra ID, o controle de acesso passou a ser tratado também no nível de autorização dos recursos Azure.

Como primeiro passo, a identidade `luiz.azure.reader` recebeu a função `Leitor` no escopo do `RG-CLOUD-SECURITY-LAB`.

A atribuição foi realizada no nível do grupo de recursos, evitando conceder permissões de leitura em toda a assinatura.

![Azure RBAC — Reader no Resource Group](../04-evidencias/controle-acesso/rbac-reader-resource-group.png)

Essa alteração representa a evolução de um modelo baseado em permissões amplas para um modelo baseado em função e escopo.

O objetivo é aplicar progressivamente o princípio do menor privilégio, concedendo a cada identidade somente as permissões necessárias para sua finalidade.

### Estado atual do RBAC

| Identidade | Função | Escopo | Estado |
|---|---|---|---|
| `luiz.azure.reader` | Leitor | `RG-CLOUD-SECURITY-LAB` | Implementado |
| `luiz.azure.admin` | Proprietário | Assinatura | Em revisão |
| `lab.breakglass01` | Administrador Global | Entra ID | Mantido para emergência |
| `lab.breakglass02` | Administrador Global | Entra ID | Mantido para emergência |

A configuração atual ainda possui permissões administrativas amplas que serão revisadas nas próximas etapas.

---
### Etapa 04 — Redução do privilégio administrativo

Após validar a atribuição de `Contributor` no `RG-CLOUD-SECURITY-LAB`, a atribuição de `Owner` que existia diretamente na assinatura foi removida da identidade `luiz.azure.admin`.

A conta permanece com capacidade administrativa sobre os recursos necessários ao laboratório, porém o escopo foi reduzido para o grupo de recursos.

Essa alteração reduz o impacto potencial de uma utilização indevida da conta e aproxima o ambiente do princípio do menor privilégio.

![RBAC administrativo — escopo do Resource Group](../04-evidencias/controle-acesso/rbac-admin-final.png)

Estado anterior:

`luiz.azure.admin → Owner → Azure subscription 1`

Estado atual:

`luiz.azure.admin → Contributor → RG-CLOUD-SECURITY-LAB`

### Matriz de Acesso

A definição das permissões será baseada na função de cada identidade e no princípio do menor privilégio.

| Identidade | Função | Escopo | Permissão |
|---|---|---|---|
| `luiz.azure.admin` | Administração Azure | Resource Group | Administração dos recursos do laboratório |
| `luiz.azure.reader` | Leitura | Resource Group | Somente leitura |
| `luiz.admin` | Administração de identidade | Microsoft Entra ID | Administração de identidades |
| `lab.breakglass01` | Emergência | Conforme necessidade | Acesso emergencial |
| `lab.breakglass02` | Emergência | Conforme necessidade | Acesso emergencial |

O objetivo é evitar a utilização de permissões administrativas mais amplas do que o necessário.

As atribuições serão aplicadas preferencialmente no menor escopo possível, reduzindo a superfície de privilégio do ambiente.

## Modelo de Evolução
```text
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
```
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

A próxima evolução será implementar MFA para as identidades administrativas do ambiente, adicionando uma camada de proteção além das credenciais.

Após a validação do MFA, o laboratório avançará para controles de privilégio e administração just-in-time com PIM.

[Retornar ao Laboratório →](../README.md)
