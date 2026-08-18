<div align="center">

# ☁️ Cloud Security & IAM Lab — Microsoft Azure

> **Meu laboratório prático de segurança em nuvem e gestão de identidades**  

<p align="center">
  <img src="https://img.shields.io/badge/Cloud-Microsoft%20Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white" alt="Azure">
  <img src="https://img.shields.io/badge/Core-IAM%20%2F%20Entra%20ID-00A4EF?style=for-the-badge&logo=microsoft&logoColor=white" alt="Entra ID">
  <img src="https://img.shields.io/badge/Status-Em%20Evolução%20Ativa-107C10?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Foco-Segurança%20%2F%20IAM-FFB900?style=for-the-badge" alt="Focus">
</p>

</div>

---

## 👋 Sobre este Laboratório

Criei este repositório para colocar a mão na massa e documentar a construção do meu laboratório de **Cloud Security e IAM** no **Microsoft Azure**. 

Meu foco principal é **IAM (Gestão de Identidade e Acesso)**, mas sei que para ser um profissional de segurança completo, preciso entender a fundo como a infraestrutura e as redes funcionam por trás dos panos, apesar de ter sempre trabalhado em ambientes hibridos quero aprofundar meus conhecimentos em cloud. Por isso, construí o ambiente de forma incremental: comecei estruturando a rede do zero, criei camadas rígidas de controle de acesso, centralizei as identidades e implementei governança. 

Aqui você vai encontrar exatamente o histórico prático de tudo o que estou estudando, testando e validando no dia a dia.

---

## 📂 O que já construí e meus próximos passos

| Área do Laboratório | O que fiz / O que abrange | Status |
|---|---|---|
| [Arquitetura](./01-arquitetura/arquitetura.md) | Desenho e segmentação inicial da infraestrutura (Management, Security, Workload). | ✅ **Concluído** |
| [Rede](./02-rede/rede.md) | Configuração de VNets, subnets dedicadas e Network Security Groups (NSGs). | ✅ **Concluído** |
| [Controle de Acesso](./03-controle-acesso/controle-acesso.md) | Aplicação de RBAC, MFA, Azure Bastion e remoção de IPs públicos. | ✅ **Concluído** |
| [Identidade & IAM](./05-identidade/entra-id.md) | Centralização no Microsoft Entra ID e separação de contas por função. | ✅ **Concluído** |
| [Governança](./06-governanca/azure-policy.md) | Criação de regras preventivas com Azure Policy para controle de conformidade. | ✅ **Concluído** |
| Federação e SSO | Próximos testes com B2B/B2C, federação de identidades e Single Sign-On. | ⏳ *Em breve* |
| Criptografia | Gestão de chaves, Key Vault e proteção de dados em repouso e trânsito. | ⏳ *Planejado* |
| Resposta a Incidentes | Simulação de investigação e análise forense baseada nos logs da nuvem. | ⏳ *Planejado* |
| DevSecOps / IaC | Práticas de infraestrutura como código com validação de segurança antes do deploy. | ⏳ *Planejado* |
| Monitoramento | Coleta de logs, centralização e visibilidade do que acontece no ambiente. | ⏳ *Planejado* |
| Detecção | Criação de alertas e detecção de comportamentos anômalos. | ⏳ *Planejado* |
| Microsoft Defender | Proteção avançada de workloads e postura de segurança com o Defender for Cloud. | ⏳ *Planejado* |
