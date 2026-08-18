# Arquitetura — On-Premises Lab

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Configuração da rede interna no VirtualBox e distribuição das máquinas virtuais. |

</details>

## 🌐 Visão Geral

O laboratório simula uma rede corporativa híbrida localmente utilizando **VirtualBox**. A topologia foi desenhada para separar serviços de infraestrutura crítica, servidores de segurança e estações de trabalho, permitindo simular tráfego interno, políticas de domínio e monitoramento de perímetro.

---

## 🏗️ Stack Tecnológica

* **Hipervisor:** Oracle VirtualBox
* **Serviços de Diretório & Infra:** Windows Server 2025 (Active Directory, DNS, WSUS)
* **Sincronização Cloud:** Microsoft Entra Connect (integrando o AD local com o tenant Azure)
* **Segurança & Monitoramento:** Rocky Linux rodando **Wazuh** (SIEM/EDR) e **Suricata** (IDS/IPS)
* **Ofensivo / Validação:** Kali Linux

---

## 🔒 Topologia de Rede (Conceitual)

* **Rede Interna (Internal Network):** Isola os servidores de domínio e os agentes de monitoramento.
* **Modo Bridge / NAT:** Utilizado para conectividade pontual de atualizações (WSUS) e sincronização com o Microsoft Entra ID.

---

[← Retornar ao Início do Lab On-Premises](../README.md)
