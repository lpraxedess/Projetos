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

## 🎯 Objetivo

A minha proposta nesta etapa foi evoluir progressivamente os mecanismos de acesso ao ambiente, partindo de premissas de rede e avançando de forma estruturada para camadas robustas de identidade, autenticação, autorização e aplicação do princípio do menor privilégio.

---

## 🗺️ Modelo de Acesso Atual

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

A administração direta dos servidores internos via Internet foi completamente eliminada. Hoje, o **Azure Bastion** atua como o único ponto de entrada administrativo, acessado de forma segura via navegador (`HTTPS/443`), mantendo o `SECURITY-SERVER-01` confinado em rede estritamente privada e sem IP público. 

Abaixo, detalho como alcancei este padrão, etapa por etapa.

---

## 🏗️ Etapa 01 — Controle de Acesso via Rede

Na primeira fase, estabeleci o perímetro de segurança primário utilizando Network Security Groups (NSGs).

A segmentação por subnet garantiu:
* Tráfego RDP externo restrito exclusivamente ao segmento de gerenciamento.
* Conectividade RDP interna limitada entre `SNET-MANAGEMENT` e `SNET-SECURITY`.
* Ausência total de rotas de acesso administrativo direto da Internet para os servidores de segurança.

![NSGs do ambiente](../04-evidencias/controle-acesso/nsg-cloud-security.png)

---

## 🪪 Etapa 02 — Identidade como Perímetro

Com a fundação de rede validada, passei a estruturar o controle baseado em identidades dedicadas no **Microsoft Entra ID**:

* `luiz.admin` — Administração dedicada de identidades.
* `luiz.azure.admin` — Administração de recursos no Azure.
* `luiz.azure.reader` — Permissões estritas de leitura.
* `lab.breakglass01` — Conta de acesso emergencial (*break-glass*).
* `lab.breakglass02` — Conta de acesso emergencial (*break-glass*).

Esta segregação garante isolamento absoluto entre funções operacionais, auditoria e recuperação de desastres.

---

## 🔐 Etapa 03 — Governança de Autorização via Azure RBAC

Para controlar o acesso aos recursos do Azure com precisão, adotei o modelo de Role-Based Access Control (RBAC).

Como marco inicial, atribuí a função de `Leitor` (Reader) à identidade `luiz.azure.reader` escopo estrito ao grupo de recursos `RG-CLOUD-SECURITY-LAB`, evitando privilégios amplos em nível de assinatura.

![Azure RBAC — Reader no Resource Group](../04-evidencias/controle-acesso/rbac-reader-resource-group.png)

### Matriz Inicial de Autorização

| Identidade | Função | Escopo | Estado |
|---|---|---|---|
| `luiz.azure.reader` | Leitor | `RG-CLOUD-SECURITY-LAB` | Implementado |
| `luiz.azure.admin` | Contributor | `RG-CLOUD-SECURITY-LAB` | Implementado |
| `lab.breakglass01` | Global Administrator | Microsoft Entra ID | Reservado para Emergência |
| `lab.breakglass02` | Global Administrator | Microsoft Entra ID | Reservado para Emergência |

---

## 📉 Etapa 04 — Minimização de Privilégios Administrativos

Após validar o comportamento do ambiente com o perfil de `Contributor` limitado ao grupo de recursos, **removi a atribuição de `Owner`** que antes recaía diretamente sobre a assinatura principal para a conta `luiz.azure.admin`.

* **Estado Anterior:** `luiz.azure.admin → Owner → Azure subscription`
* **Estado Atual:** `luiz.azure.admin → Contributor → RG-CLOUD-SECURITY-LAB`

Essa alteração restringe o raio de impacto de eventuais incidentes e consolida o menor privilégio prático.

![RBAC administrativo — escopo do Resource Group](../04-evidencias/controle-acesso/rbac-admin-final.png)

---

## 🛡️ Etapa 05 — Camada de Autenticação Multifator (MFA)

Para mitigar riscos associados a credenciais comprometidas, implementei o segundo fator de autenticação nas contas administrativas:

* `luiz.admin` — Validação via Software OATH/TOTP.
* `luiz.azure.admin` — Validação via Microsoft Authenticator.

![MFA — luiz.admin](../04-evidencias/controle-acesso/mfa-luiz-admin.png)

![MFA — luiz.azure.admin](../04-evidencias/controle-acesso/mfa-luiz-azure-admin.png)

> **Nota de Contexto:** Como o tenant atual não possui licenciamento para o uso do *Microsoft Entra Conditional Access*, políticas avançadas baseadas em risco, dispositivo ou localização geográfica permanecem guardadas para expansões futuras.

---

## ⏳ Etapa 06 — Avaliação de Privileged Access Management (PIM)

Conduzi uma avaliação para implementar o *Microsoft Entra Privileged Identity Management (PIM)* visando controle Just-In-Time (JIT) de acessos elevados.

A verificação no portal apontou que os recursos completos do PIM exigem licenças específicas (Entra ID P2 ou Governance), indisponíveis no tier atual do tenant. Por esse motivo, a iniciativa foi documentada como **Planejada** para momentos de upgrade de infraestrutura, mantendo a governança baseada no Azure RBAC padrão.

![Licenciamento para Microsoft Entra PIM](../04-evidencias/controle-acesso/pim-licenciamento.png)

---

## 🚪 Etapa 07 — Blindagem de Perímetro com Azure Bastion

O marco conclusivo desta fase consistiu em banir qualquer exposição direta de IPs públicos em servidores voltados a tarefas administrativas.

* **Isolamento de NIC:** Remoção completa do IP público associado ao `JUMP-SERVER-01`.
* **Subnet Dedicada:** Alocação da `AzureBastionSubnet` (`10.10.40.0/26`) dentro da `VNET-CLOUD-SECURITY`.
* **Serviço:** Instalação do Azure Bastion (modo *Basic*, região *Brazil South*).
* **Integração de Identidade:** Aplicação da extensão `AADLoginForWindows` combinada à permissão `Virtual Machine User Login` via IAM.

O acesso ocorre estritamente via portal web em sessões seguras encapsuladas em HTTPS (`443`).

---

## 📈 Resumo da Trilha de Evolução

[01. Rede (NSGs)] ➡️ [02. Identidade (Entra ID)] ➡️ [03. Autorização (RBAC)] ➡️ [04. Menor Privilégio] ➡️ [05. Autenticação (MFA)] ➡️ [06. PIM (Planejado)] ➡️ [07. Azure Bastion]

---

## 📊 Status Consolidado dos Controles

| Mecanismo / Controle | Status |
|---|---|
| Segmentação de Rede | ✅ Implementado |
| Network Security Groups (NSGs) | ✅ Implementado |
| Microsoft Entra ID Core | ✅ Implementado |
| Segregação de Contas | ✅ Implementado |
| Azure RBAC | ✅ Implementado |
| Minimização de Escopo | ✅ Implementado |
| Multi-Factor Authentication (MFA) | ✅ Implementado |
| Conditional Access | ❌ Indisponível (Licenciamento) |
| Privileged Identity Management (PIM) | ⏳ Planejado (Licenciamento) |
| Azure Bastion (Sem IP Público) | ✅ Implementado |

---

## ⏭️ Próximos Passos

Superada a fase de blindagem de acessos e identidades, a próxima frente natural do laboratório migra para a **Governança Preventiva** através do **Azure Policy**, assegurando que os recursos criados obedeçam a parâmetros automáticos de conformidade corporativa.

[← Retornar ao Início do Laboratório](../README.md)
