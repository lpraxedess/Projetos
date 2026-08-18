# Rede — Cloud Security Lab

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Adicionada `AzureBastionSubnet` (`10.10.40.0/26`) para suportar acesso via Azure Bastion. |
| 2026-01 | Criação da VNet dedicada e segmentação inicial em `SNET-MANAGEMENT`, `SNET-SECURITY` e `SNET-WORKLOAD`. |

</details>

## 🌐 Estado Atual

Para sustentar este laboratório com isolamento adequado, estruturei uma Virtual Network dedicada:

* **VNet:** `VNET-CLOUD-SECURITY`
* **Bloco CIDR:** `10.10.0.0/16`
* **Região:** `Brazil South`

Dividi esta rede em subnets segmentadas estritamente de acordo com a função e responsabilidade de cada ambiente.

---

## 🗺️ Visão da VNet

![VNET-CLOUD-SECURITY](../04-evidencias/rede/vnet-cloud-security.png)

---

## 📂 Segmentação de Subnets

Atualmente, a VNet está dividida em quatro subnets principais:

![Subnets da VNET-CLOUD-SECURITY](../04-evidencias/rede/subnet-cloud-security.png)

| Subnet | Bloco CIDR | Função |
|---|---|---|
| `SNET-MANAGEMENT` | `10.10.10.0/24` | Administração e gerenciamento do ambiente |
| `SNET-SECURITY` | `10.10.20.0/24` | Servidores e componentes de segurança |
| `SNET-WORKLOAD` | `10.10.30.0/24` | Camada reservada para cargas de trabalho futuras |
| `AzureBastionSubnet` | `10.10.40.0/26` | Acesso administrativo seguro via Azure Bastion |

---

## 🛡️ Network Security Groups (NSGs)

Para aplicar o controle de tráfego de forma granular, cada subnet conta com um NSG dedicado:

* `NSG-MANAGEMENT`
* `NSG-SECURITY`
* `NSG-WORKLOAD`

Utilizo os NSGs para restringir a comunicação lateral entre os ambientes e mitigar qualquer exposição desnecessária de recursos.

---

[← Retornar ao Início do Laboratório](../README.md)
