# Arquitetura — On-Premises Lab

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Configuração da rede interna no VirtualBox e distribuição das máquinas virtuais. |

</details>

## 🎯 Objetivo

Aqui defino a estrutura do ambiente local e as decisões que permitem testar infraestrutura, identidade e segurança em um cenário on-premises.

## 🌐 Visão Geral

O laboratório simula uma infraestrutura corporativa local utilizando **VirtualBox**, com separação entre serviços de infraestrutura, servidores de segurança e estações de trabalho. A rede foi pensada para permitir testes de comunicação interna, políticas de domínio, integração híbrida e monitoramento.

## 🔒 Topologia de Rede

- **Rede Interna (Internal Network):** utilizada para manter a comunicação principal entre os componentes do laboratório isolada do ambiente externo.
- **Bridge / NAT:** utilizados quando um recurso precisa de conectividade externa, como atualizações e sincronização com o Microsoft Entra ID.

A separação entre rede interna e conectividade externa permite testar diferentes cenários sem transformar o laboratório em uma rede totalmente exposta.

## 🧩 Componentes do Ambiente

- **VirtualBox:** camada de virtualização.
- **Windows Server 2025:** Active Directory, DNS e WSUS.
- **Microsoft Entra Connect:** integração entre o Active Directory local e o Microsoft Entra ID.
- **Rocky Linux:** base para Wazuh e Suricata.
- **Kali Linux:** validação e simulação de cenários ofensivos.

## 📝 Observações

>

---

[← Laboratório](../README.md) · [Identidade →](../02-identidade/identidade.md)
