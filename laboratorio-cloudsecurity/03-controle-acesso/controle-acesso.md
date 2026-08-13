# Controle de Acesso — Cloud Security Lab

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Etapa 07 — Implementado Azure Bastion, eliminando IP público do Jump Server. |
| 2026-02 | Etapa 06 — Avaliado Microsoft Entra PIM; mantido como planejado por limitação de licenciamento. |
| 2026-02 | Etapa 05 — Configurado MFA para contas administrativas (`luiz.admin`, `luiz.azure.admin`). |
| 2026-02 | Etapa 04 — Removida atribuição de Owner na assinatura; reduzido escopo para Contributor no Resource Group. |
| 2026-01 | Etapa 03 — Implementado Azure RBAC com função Leitor no escopo do Resource Group. |
| 2026-01 | Etapa 02 — Criadas identidades segregadas por função no Microsoft Entra ID. |
| 2026-01 | Etapa 01 — Implementado controle de acesso via NSGs e Jump Server. |

</details>

## Objetivo

Minha ideia aqui foi evoluir progressivamente os controles de acesso do ambiente, começando pelos controles de rede e avançando para controles de identidade, autenticação, autorização e menor privilégio.

## Modelo de Acesso Atual

<div align="center">

```mermaid
flowchart LR
    A(["💻 Admin"])-->|HTTPS 443| B(["🔒 Bastion"])
    B --> C(["🖥️ JUMP-SERVER-01"])
    C -->|RDP interno| D(["🛡️ SECURITY-SERVER-01"])
    classDef external fill:#1e3a5f,stroke:#60a5fa,stroke-width:2px,color:#e0f2fe
    classDef bastion fill:#5a3a1e,stroke:#fb923c,stroke-width:2px,color:#fed7aa
    classDef server fill:#1e4620,stroke:#4ade80,stroke-width:2px,color:#dcfce7
    classDef secure fill:#4c1d1d,stroke:#f87171,stroke-width:2px,color:#fecaca
    class A external
    class B bastion
    class C server
    class D secure
```

</div>

Hoje a administração dos servidores internos não é feita diretamente pela Internet. O `Azure Bastion` é meu ponto de entrada administrativo, acessado via navegador (HTTPS/443), e o `SECURITY-SERVER-01` permanece na rede privada, sem IP público. Abaixo, conto como cheguei até esse estado, etapa por etapa.

---

## Etapa 01 — Controle de acesso pela rede

Na primeira etapa, implementei o controle de acesso administrativo principalmente através dos Network Security Groups (NSGs).

Segmentei o acesso ao ambiente por subnet, permitindo:

- RDP externo somente para o ambiente de gerenciamento;
- RDP interno entre `SNET-MANAGEMENT` e `SNET-SECURITY`;
- ausência de acesso administrativo direto da Internet ao servidor de segurança.

Essa etapa estabeleceu o controle de acesso no nível de rede.

![NSGs do ambiente](../04-evidencias/controle-acesso/nsg-cloud-security.png)

---

## Etapa 02 — Controle de acesso baseado em identidade

Com a estrutura de rede estabelecida, o próximo nível de controle que trabalhei foi a identidade.

Criei contas com finalidades diferentes no Microsoft Entra ID:

- `luiz.admin` — administração de identidade;
- `luiz.azure.admin` — administração do Azure;
- `luiz.azure.reader` — acesso de leitura;
- `lab.breakglass01` — conta de emergência;
- `lab.breakglass02` — conta de emergência.

Essa separação me permite diferenciar funções administrativas, leitura e acesso emergencial.

---

## Etapa 03 — Evolução para Azure RBAC

Depois de estabelecer os controles de acesso no nível de rede e estruturar as identidades no Microsoft Entra ID, passei a tratar o controle de acesso também no nível de autorização dos recursos Azure.

Como primeiro passo, atribuí a função `Leitor` à identidade `luiz.azure.reader`, no escopo do `RG-CLOUD-SECURITY-LAB`.

Fiz essa atribuição no nível do grupo de recursos, evitando conceder permissões de leitura em toda a assinatura.

![Azure RBAC — Reader no Resource Group](../04-evidencias/controle-acesso/rbac-reader-resource-group.png)

Essa mudança representa a evolução de um modelo baseado em permissões amplas para um modelo baseado em função e escopo.

Meu objetivo é aplicar progressivamente o princípio do menor privilégio, concedendo a cada identidade somente as permissões necessárias para sua finalidade.

### Estado atual do RBAC

| Identidade | Função | Escopo | Estado |
|---|---|---|---|
| `luiz.azure.reader` | Leitor | `RG-CLOUD-SECURITY-LAB` | Implementado |
| `luiz.azure.admin` | Contributor | `RG-CLOUD-SECURITY-LAB` | Implementado |
| `lab.breakglass01` | Administrador Global | Entra ID | Mantido para emergência |
| `lab.breakglass02` | Administrador Global | Entra ID | Mantido para emergência |

As permissões administrativas amplas que existiam anteriormente foram reduzidas conforme a finalidade de cada identidade.

---

## Etapa 04 — Redução do privilégio administrativo

Depois de validar a atribuição de `Contributor` no `RG-CLOUD-SECURITY-LAB`, removi a atribuição de `Owner` que existia diretamente na assinatura da identidade `luiz.azure.admin`.

A conta permanece com capacidade administrativa sobre os recursos necessários ao laboratório, mas reduzi o escopo para o grupo de recursos.

Essa mudança reduz o impacto potencial de uma utilização indevida da conta e aproxima o ambiente do princípio do menor privilégio.

![RBAC administrativo — escopo do Resource Group](../04-evidencias/controle-acesso/rbac-admin-final.png)

Estado anterior:

`luiz.azure.admin → Owner → Azure subscription 1`

Estado atual:

`luiz.azure.admin → Contributor → RG-CLOUD-SECURITY-LAB`

### Matriz de Acesso

Defini as permissões com base na função de cada identidade e no princípio do menor privilégio.

| Identidade | Função | Escopo | Permissão |
|---|---|---|---|
| `luiz.azure.admin` | Administração Azure | Resource Group | Administração dos recursos do laboratório |
| `luiz.azure.reader` | Leitura | Resource Group | Somente leitura |
| `luiz.admin` | Administração de identidade | Microsoft Entra ID | Administração de identidades |
| `lab.breakglass01` | Emergência | Conforme necessidade | Acesso emergencial |
| `lab.breakglass02` | Emergência | Conforme necessidade | Acesso emergencial |

Aplico as atribuições preferencialmente no menor escopo possível, reduzindo a superfície de privilégio do ambiente.

---

## Etapa 05 — Autenticação multifator

Com a estrutura de identidade e autorização estabelecida, adicionei uma camada extra de proteção às contas administrativas por meio da autenticação multifator.

Configurei métodos de autenticação no Microsoft Entra ID:

- `luiz.admin` — Software OATH/TOTP;
- `luiz.azure.admin` — Microsoft Authenticator.

O MFA adiciona um segundo fator de autenticação além das credenciais, reduzindo o impacto de um eventual comprometimento de senha.

![MFA — luiz.admin](../04-evidencias/controle-acesso/mfa-luiz-admin.png)

![MFA — luiz.azure.admin](../04-evidencias/controle-acesso/mfa-luiz-azure-admin.png)

> **Nota:** o tenant não possui licenciamento suficiente para utilizar o Microsoft Entra Conditional Access neste momento. Por isso, políticas baseadas em risco, aplicativo, dispositivo e localização permanecem como evolução futura.

---

## Etapa 06 — Avaliação de gerenciamento de privilégios

Depois de implementar o menor privilégio e o MFA, avaliei a utilização do Microsoft Entra Privileged Identity Management (PIM) para controle de acessos administrativos privilegiados e acesso just-in-time.

Durante a avaliação, o portal Microsoft Entra me informou que o tenant não possui atualmente o licenciamento necessário para utilizar todos os recursos do PIM.

Por isso, não registrei o PIM como controle implementado.

A decisão que tomei foi manter o PIM como evolução planejada e continuar aplicando o princípio do menor privilégio através do Azure RBAC disponível no ambiente.

**Estado:** Planejado — dependente de licenciamento Microsoft Entra ID P2 ou Microsoft Entra ID Governance.

![Licenciamento para Microsoft Entra PIM](../04-evidencias/controle-acesso/pim-licenciamento.png)

---

## Etapa 07 — Eliminação de exposição pública (Azure Bastion)

Com os controles de identidade, autorização e conformidade já estabelecidos, o último passo dessa fase foi eliminar completamente a exposição direta de IP público na infraestrutura administrativa.

*Nota: essa implementação ocorreu depois da etapa de Governança (Azure Policy), mas mantenho ela aqui por ser tematicamente um controle de acesso.*

Para isso, implementei o **Azure Bastion**, que permite acesso via navegador (HTTPS/443), eliminando a necessidade de IPs públicos nas máquinas virtuais.

### Arquitetura de Acesso

- **Isolamento:** removi o IP público da placa de rede (NIC) do `JUMP-SERVER-01`.
- **Subnet dedicada:** criei a subnet `AzureBastionSubnet` na VNet `VNET-CLOUD-SECURITY` (bloco `10.10.40.0/26`).
- **Serviço:** Azure Bastion em modo *Basic*, na região `Brazil South`.

### Configurações Técnicas

- **IAM:** atribuí a função `Virtual Machine User Login` à conta de leitura, garantindo conformidade de acesso.
- **Extensão:** instalei a extensão `AADLoginForWindows` para suportar identidades do Microsoft Entra ID.
- **Segurança:** o acesso é feito de forma privada, mantendo o tráfego RDP interno à rede virtual.

### Validação

Acesso via Portal do Azure → Virtual Machines → JUMP-SERVER-01 → Connect → Bastion. O login é validado através de credenciais locais, o que confirma que o ambiente está operando dentro dos padrões de segurança que defini para o laboratório.

O IP público foi removido do `JUMP-SERVER-01` e o acesso passou a ser feito via Azure Bastion, sem exposição de portas RDP à Internet.

---

## Modelo de Evolução

**Controle de acesso**

→ **01. Rede**
NSGs

→ **02. Identidade**
Microsoft Entra ID

→ **03. Autorização**
Azure RBAC

→ **04. Menor privilégio**
Redução de escopo

→ **05. Autenticação**
MFA

→ **06. Privilégios**
PIM — planejado conforme disponibilidade de licenciamento

→ **07. Exposição**
Azure Bastion — eliminação de IP público

---

## Estado Atual

| Controle | Estado |
|---|---|
| Segmentação de rede | Implementado |
| NSGs | Implementado |
| Microsoft Entra ID | Implementado |
| Separação de identidades | Implementado |
| Azure RBAC | Implementado |
| Redução de privilégios | Implementado |
| MFA | Implementado |
| Conditional Access | Não disponível — licenciamento |
| PIM | Planejado — licenciamento |
| Azure Bastion | Implementado |

---

## Próxima Etapa

Como o PIM depende de um licenciamento que não está disponível no tenant atual, a próxima evolução prática do laboratório será trabalhar controles de governança e conformidade usando os recursos disponíveis no Azure.

A próxima etapa será o **Azure Policy**, começando pela criação de uma política simples e controlada para demonstrar governança preventiva sobre os recursos do laboratório.

O objetivo é evoluir do controle de acesso para o controle de conformidade, demonstrando que os recursos não apenas possuem permissões adequadas, mas também precisam obedecer a regras definidas pelo ambiente.

---

[Retornar ao Laboratório →](../README.md)
