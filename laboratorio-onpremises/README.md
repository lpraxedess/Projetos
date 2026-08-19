# 🛡️ On-Premises & Blue Team Lab

Meu laboratório prático de infraestrutura tradicional, identidade híbrida, hardening e monitoramento de segurança.

## 🎯 Objetivo

Aqui é onde aplico na prática conhecimentos de infraestrutura e segurança em um ambiente local. Construo, testo e modifico a estrutura conforme avanço, usando o laboratório para validar configurações, observar resultados e registrar decisões e descobertas relevantes.

## 🔄 Fluxo do Laboratório

```text
Arquitetura → Identidade → Gerenciamento → Hardening → Monitoramento
                                                   ↓
                                           Resposta a Incidentes
```

A sequência representa uma linha de evolução, mas o laboratório não é linear: áreas já desenvolvidas podem ser revisitadas sempre que novos testes ou mudanças na arquitetura exigirem.

## Laboratório

| Área | O que é tratado |
|---|---|
| 🏗️ **[Arquitetura](./01-arquitetura/arquitetura.md)** | Topologia, segmentação, conectividade e organização das máquinas virtuais |
| 👤 **[Identidade](./02-identidade/identidade.md)** | Active Directory, DNS, organização de identidades e integração com Microsoft Entra ID |
| ⚙️ **Gerenciamento** | WSUS, atualizações, patches e correções de segurança |
| 🛡️ **[Hardening](./04-hardening/hardening.md)** | CIS Benchmarks, análise de aplicabilidade, automação e validação de postura |
| 📊 **Monitoramento** | Wazuh, Suricata, logs, eventos e detecção |
| 🚨 **Resposta a Incidentes** | Simulação de ataques, triagem, investigação e resposta |

> **Nota:** As áreas sem link ainda não possuem documentação desenvolvida. Elas permanecem na tabela para mostrar os próximos temas do laboratório.

[← Voltar aos Laboratórios](../README.md)
