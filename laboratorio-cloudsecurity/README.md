<div align="center">

# ☁️ Cloud Security & IAM Lab — Microsoft Azure

> Laboratório prático para desenvolver, testar e consolidar conhecimentos em Cloud Security, IAM e infraestrutura Azure.

<p align="center">
  <img src="https://img.shields.io/badge/Cloud-Microsoft%20Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white" alt="Azure">
  <img src="https://img.shields.io/badge/Core-IAM%20%2F%20Entra%20ID-00A4EF?style=for-the-badge&logo=microsoft&logoColor=white" alt="Entra ID">
  <img src="https://img.shields.io/badge/Status-Em%20Evolução-107C10?style=for-the-badge" alt="Status">
</p>

</div>

---

## 🎯 Sobre o laboratório

Este ambiente é meu espaço de prática em **Cloud Security e IAM no Microsoft Azure**. A construção acontece de forma incremental: novos conceitos são estudados, implementados, testados e incorporados ao laboratório conforme minha evolução técnica.

O objetivo não é reproduzir um ambiente corporativo completo de uma vez, mas **aprender construindo**, aumentando gradualmente a complexidade e a maturidade dos controles.

Erros, dificuldades, decisões e mudanças relevantes também são documentados durante essa evolução.

---

## 🏗️ Arquitetura atual

```text
                         INTERNET
                            │
                            ▼
                    ┌───────────────┐
                    │ Azure Bastion  │
                    │   Acesso RDP   │
                    └───────┬───────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                    VNET-CLOUD-SECURITY                       │
│                       10.10.0.0/16                           │
│                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   MANAGEMENT    │  │    SECURITY     │  │   WORKLOAD   │ │
│  │ 10.10.10.0/24  │  │ 10.10.20.0/24  │  │10.10.30.0/24 │ │
│  │                 │  │                 │  │              │ │
│  │ Administração   │  │ Controles de    │  │ Recursos de  │ │
│  │ e Jump Server   │  │ segurança      │  │ trabalho     │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │                 AzureBastionSubnet                     │  │
│  │                    10.10.40.0/26                       │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘

        Microsoft Entra ID  →  IAM / RBAC / MFA
        Azure Policy        →  Governança / Enforcement
        NSGs                →  Segmentação / Controle de tráfego
```

---

## 📊 Evolução do laboratório

| Área | Situação | Resultado |
|---|---|---|
| Arquitetura | ✅ Concluído | Estrutura inicial da infraestrutura e segmentação |
| Rede | ✅ Concluído | VNet, subnets e NSGs |
| Controle de acesso | ✅ Concluído | RBAC, MFA e controles administrativos |
| Azure Bastion | ✅ Concluído | Administração sem exposição RDP direta à Internet |
| Identidade / IAM | ✅ Concluído | Microsoft Entra ID e separação de funções |
| Governança | ✅ Concluído | Azure Policy com enforcement |
| Federação / SSO | ⏳ Próximo | B2B/B2C, federação e SSO |
| Criptografia | ⏳ Planejado | Key Vault e proteção de dados |
| Monitoramento | ⏳ Planejado | Logs e visibilidade do ambiente |
| Detecção | ⏳ Planejado | Alertas e identificação de comportamentos anômalos |
| Resposta a incidentes | ⏳ Planejado | Investigação e resposta baseada em evidências |
| Microsoft Defender | ⏳ Planejado | Postura e proteção de workloads |
| DevSecOps / IaC | ⏳ Planejado | Automação e validação de segurança |

---

## 🔄 Principais evoluções

### Exposição administrativa

```text
ANTES
Internet → Public IP → RDP → Jump Server

DEPOIS
Admin → Azure Bastion → Private IP → Jump Server
```

**Objetivo:** reduzir a superfície de exposição e eliminar o acesso RDP diretamente pela Internet.

### Privilégios administrativos

```text
ANTES
Owner → Subscription

DEPOIS
Contributor → Resource Group
```

**Objetivo:** aplicar menor privilégio e limitar o escopo administrativo.

### Governança

```text
ANTES
Recurso sem tag → Provisionamento permitido

DEPOIS
Recurso sem tag → Azure Policy → DENY
```

**Objetivo:** transformar requisitos de governança em controles preventivos.

---

## 📂 Laboratório por etapa

| Módulo | Conteúdo | Status |
|---|---|---|
| [01 — Arquitetura](./01-arquitetura/arquitetura.md) | Desenho e organização da infraestrutura | ✅ |
| [02 — Rede](./02-rede/rede.md) | VNet, subnets e NSGs | ✅ |
| [03 — Controle de Acesso](./03-controle-acesso/controle-acesso.md) | RBAC, MFA, Bastion e acesso administrativo | ✅ |
| [04 — Evidências](./04-evidencias/) | Evidências visuais das implementações | 🔄 |
| [05 — Identidade](./05-identidade/entra-id.md) | Microsoft Entra ID e IAM | ✅ |
| [06 — Governança](./06-governanca/azure-policy.md) | Azure Policy e compliance | ✅ |
| 07 — Federação / SSO | Federação e Single Sign-On | ⏳ |
| 08 — Criptografia | Key Vault e proteção de dados | ⏳ |
| 09 — Resposta a Incidentes | Investigação e resposta | ⏳ |
| 10 — DevSecOps / IaC | Automação e segurança no ciclo de entrega | ⏳ |

---

## 🧪 Evidências e validações

O laboratório prioriza evidências práticas para demonstrar que os controles foram realmente implementados e testados.

- Configurações do Azure Portal
- Testes de acesso
- Testes de bloqueio por Azure Policy
- RBAC e permissões
- MFA e identidade
- NSGs e segmentação
- Evolução da arquitetura

[📁 Acessar evidências](./04-evidencias/)

---

## 🛠️ Stack atual

**Cloud:** Microsoft Azure  
**Identity:** Microsoft Entra ID  
**Network:** VNet, Subnets, NSGs, Azure Bastion  
**Governance:** Azure Policy  
**Compute:** Windows Server  
**Security:** IAM, RBAC, MFA, Network Segmentation, Hardening

---

## 🚧 Próximos passos

A evolução planejada é gradual, priorizando conhecimento antes de adicionar novas tecnologias:

1. Federação / SSO
2. Key Vault e criptografia
3. Monitoramento e logging
4. Detecção e resposta
5. Microsoft Defender
6. IaC
7. DevSecOps
8. Automação e testes de segurança

---

## 📌 Observação

Este laboratório é desenvolvido exclusivamente para **estudo, prática e evolução técnica**. As implementações representam experimentos controlados e não ambientes produtivos.

[← Voltar para os Laboratórios](../README.md)
