# ☁️ Cloud Security & IAM Lab — Microsoft Azure

Laboratório prático de **Cloud Security, IAM e infraestrutura no Microsoft Azure**, desenvolvido de forma incremental conforme minha evolução técnica.

> **Explore o laboratório:** escolha uma área abaixo para ver sua implementação, evolução, decisões, testes e evidências.

---

## 🧭 Laboratório

| Área | O que você encontra | Status |
|---|---|---|
| 🏗️ **[Arquitetura](./01-arquitetura/arquitetura.md)** | Estrutura do ambiente, decisões arquiteturais e evolução | ✅ Concluído |
| 🌐 **[Rede](./02-rede/rede.md)** | VNet, subnets, NSGs, segmentação e controles de tráfego | ✅ Concluído |
| 🔐 **[Controle de Acesso](./03-controle-acesso/controle-acesso.md)** | RBAC, MFA, Bastion e administração do ambiente | ✅ Concluído |
| 📸 **[Evidências](./04-evidencias/)** | Evidências das configurações e validações realizadas | 🔄 Em evolução |
| 👤 **[Identidade / Entra ID](./05-identidade/entra-id.md)** | Identidades, funções, grupos e IAM | ✅ Concluído |
| 🛡️ **[Governança / Azure Policy](./06-governanca/azure-policy.md)** | Policies, enforcement e controles preventivos | ✅ Concluído |
| 🔑 **07 — Federação / SSO** | Federação e Single Sign-On | ⏳ Planejado |
| 🔒 **08 — Criptografia** | Proteção de dados, Key Vault e secrets | ⏳ Planejado |
| 🚨 **09 — Resposta a Incidentes** | Investigação, contenção e resposta | ⏳ Planejado |
| ⚙️ **10 — DevSecOps / IaC** | Infraestrutura como código, automação e segurança | ⏳ Planejado |

---

## 🗺️ Visão rápida do ambiente

```text
                         MICROSOFT AZURE
                                │
                                ▼
                    ┌────────────────────┐
                    │ VNET-CLOUD-SECURITY│
                    │     10.10.0.0/16   │
                    └─────────┬──────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
    MANAGEMENT            SECURITY             WORKLOAD
    10.10.10.0/24        10.10.20.0/24        10.10.30.0/24
          │                   │                   │
          └───────────────┬───┴───────────────────┘
                          │
                    Azure Bastion
                    10.10.40.0/26

     Entra ID → IAM / RBAC / MFA
     NSGs     → Segmentação
     Policy   → Governança / Enforcement
```

---

## 📈 Evolução

O laboratório evolui conforme novos conhecimentos são aplicados. Mudanças relevantes ficam registradas dentro dos respectivos módulos.

### Principais mudanças já realizadas

| Evolução | Resultado |
|---|---|
| **Public IP → Azure Bastion** | Redução da exposição administrativa e remoção do RDP direto pela Internet |
| **Owner → Contributor** | Redução do escopo de privilégio administrativo |
| **Sem enforcement → Azure Policy** | Controle preventivo sobre configuração de recursos |
| **IAM inicial → identidade segmentada** | Separação de funções e aplicação de menor privilégio |

---

## 🧪 Como o laboratório é desenvolvido

A documentação de cada área acompanha o desenvolvimento real do ambiente. Quando relevante, são registrados **erros, dificuldades, decisões, mudanças, testes e resultados**.

Não é necessário documentar cada operação: o foco é registrar aquilo que ajuda a entender **como o laboratório evoluiu e o que foi aprendido no processo**.

---

## 🛠️ Tecnologias

**Cloud:** Microsoft Azure  
**Identity:** Microsoft Entra ID  
**Network:** VNet, Subnets, NSGs, Azure Bastion  
**Governance:** Azure Policy  
**Compute:** Windows Server  
**Security:** IAM, RBAC, MFA, Network Segmentation, Hardening

---

## 🚧 Próximas etapas

**Federação / SSO → Criptografia → Monitoramento → Detecção → Resposta a Incidentes → Defender → IaC → DevSecOps**

---

## 📌 Objetivo

Este é um **laboratório de estudo e desenvolvimento técnico**, não um ambiente produtivo. A infraestrutura é construída, modificada e expandida conforme novos conceitos são estudados e aplicados.

[← Voltar para os projetos](../README.md)
