<div align="center">

# 🛡️ On-Premises & Blue Team Lab

> **Meu laboratório prático de infraestrutura tradicional, hardening, diretórios e monitoramento de segurança**  

<p align="center">
  <img src="https://img.shields.io/badge/Stack-Active%20Directory%20%2F%20WSUS-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Server">
  <img src="https://img.shields.io/badge/SIEM-%20Wazuh%20%2F%20Suricata-005571?style=for-the-badge&logo=security&logoColor=white" alt="Wazuh">
  <img src="https://img.shields.io/badge/Virtualização-VirtualBox-DE0000?style=for-the-badge&logo=virtualbox&logoColor=white" alt="VirtualBox">
  <img src="https://img.shields.io/badge/Status-Em%20Evolução%20Ativa-107C10?style=for-the-badge" alt="Status">
</p>

</div>

---

## 👋 Sobre este Laboratório

Criei este ambiente em **VirtualBox** para simular uma infraestrutura corporativa tradicional (*On-Premises*) e integrá-la ao ecossistema de nuvem. O objetivo é praticar cenários reais de administração de sistemas, implementação de diretórios, aplicação de frameworks de hardening baseados em **CIS Benchmarks**, além de monitoramento ativo de ameaças com **Wazuh** e **Suricata**.

---
    
## 📂 O que já construí e meus próximos passos


| Área do Laboratório | O que fiz / O que abrange | Status |
|---|---|---|
| [Arquitetura](./01-arquitetura/arquitetura.md) | Desenho da rede virtual, topologia no VirtualBox e comunicação entre VMs. | ✅ **Concluído** |
| [Identidade & Diretório](./02-identidade-diretorio/active-directory-entra-connect.md) | Windows Server 2025, Active Directory, WSUS e sincronização via Microsoft Entra Connect. | ✅ **Concluído** |
| [Hardening & Compliance](./03-hardening-compliance/cis-benchmarks-scripts.md) | Scripts automatizados baseados em CIS Benchmarks e validação de postura de segurança. | ✅ **Concluído** |
| [Monitoramento & SOC](./04-monitoramento-soc/wazuh-suricata.md) | Implementação do Wazuh (SIEM/XDR) e Suricata (IDS/IPS) no Rocky Linux. | ✅ **Concluído** |
| Resposta a Incidentes | Simulação de ataques e triagem de alertas no SOC on-premises. | ⏳ *Planejado* |

---

[← Retornar ao Início Geral dos Laboratórios](../README.md)
