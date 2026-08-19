# Rede — Cloud Security Lab

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Adicionada `AzureBastionSubnet` (`10.10.40.0/26`) para suportar acesso via Azure Bastion. |
| 2026-01 | Criação da VNet dedicada e segmentação inicial em `SNET-MANAGEMENT`, `SNET-SECURITY` e `SNET-WORKLOAD`. |

</details>

## 🎯 Objetivo

Construir uma rede segmentada para o laboratório, permitindo testar na prática isolamento, controle de tráfego e diferentes formas de acesso aos recursos.

## 🌐 Estado Atual

- **VNet:** `VNET-CLOUD-SECURITY`
- **CIDR:** `10.10.0.0/16`
- **Região:** `Brazil South`

A VNet é dividida por função:

| Subnet | Bloco CIDR | Função |
|---|---|---|
| `SNET-MANAGEMENT` | `10.10.10.0/24` | Administração e gerenciamento |
| `SNET-SECURITY` | `10.10.20.0/24` | Servidores e componentes de segurança |
| `SNET-WORKLOAD` | `10.10.30.0/24` | Cargas de trabalho futuras |
| `AzureBastionSubnet` | `10.10.40.0/26` | Acesso administrativo via Azure Bastion |

## 🗺️ Visão da VNet

![VNET-CLOUD-SECURITY](../04-evidencias/rede/vnet-cloud-security.png)

## 🛡️ Network Security Groups (NSGs)

Cada subnet possui um NSG dedicado:

- `NSG-MANAGEMENT`
- `NSG-SECURITY`
- `NSG-WORKLOAD`

Os NSGs são utilizados para controlar a comunicação entre os segmentos e reduzir acessos desnecessários.

## 🧪 Experimentos e Aprendizados

Novos experimentos, erros, decisões ou descobertas relevantes são registrados aqui conforme surgirem.

### Exemplo

**O que mudou:** descreva a alteração realizada.

**Por que:** explique o problema ou necessidade que motivou a mudança.

**Resultado:** registre como a alteração foi validada e o que foi aprendido.

---

[← Retornar ao Início do Laboratório](../README.md)
