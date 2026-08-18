# Arquitetura — Cloud Security Lab

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Removido IP público do `JUMP-SERVER-01`; adicionada `AzureBastionSubnet` (`10.10.40.0/26`). |
| 2026-01 | Definição inicial da arquitetura: VNet única segmentada em três subnets por função. |

</details>

## 🌐 Visão Geral

Estruturei este laboratório no **Microsoft Azure** com um objetivo claro desde o início: separar os diferentes níveis de infraestrutura e reduzir ao máximo a exposição dos recursos.

Para alcançar esse isolamento, optei por uma Virtual Network dedicada, dividida em subnets com funções bem específicas, garantindo que cada componente cumpra um papel isolado dentro do ambiente.

---

## 🏗️ Estrutura de Rede

A infraestrutura está organizada conforme a tabela abaixo:

| Componente | Bloco CIDR | Função |
|---|---|---|
| `VNET-CLOUD-SECURITY` | `10.10.0.0/16` | Rede principal do laboratório |
| `SNET-MANAGEMENT` | `10.10.10.0/24` | Administração |
| `SNET-SECURITY` | `10.10.20.0/24` | Servidores de segurança |
| `SNET-WORKLOAD` | `10.10.30.0/24` | Workloads futuros |
| `AzureBastionSubnet` | `10.10.40.0/26` | Acesso seguro via Azure Bastion (sem exposição pública) |

---

## 🔒 Modelo de Acesso

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

Priorizei garantir que a administração dos servidores internos **nunca** seja feita de forma direta pela Internet. 

* O **Azure Bastion** atua como o único ponto de entrada administrativo, acessado de forma segura via navegador (`HTTPS/443`).
* O `SECURITY-SERVER-01` permanece isolado em rede estritamente privada, completamente desprovido de IP público.

---

## 🧩 Segmentação por Subnet

Dividi as subnets por função para aplicar controles granulares de acordo com o escopo de cada ambiente:

* **Management:** Recursos voltados à administração e suporte da infraestrutura.
* **Security:** Servidores e componentes de monitoramento/segurança.
* **Workload:** Camada reservada para aplicações e serviços futuros.

---

## 🛡️ Decisões de Arquitetura & Segurança

As premissas que guiaram a construção deste ambiente foram:

* Segmentação rígida da rede por função.
* Eliminação de qualquer exposição direta à Internet.
* Centralização administrativa por meio de um Jump Server.
* Ausência de IPs públicos em servidores internos.
* Controle restrito de tráfego via Network Security Groups (NSGs).
* Flexibilidade estrutural para expansão de controles baseados em identidade (IAM).

---

## 📷 Evidência Real

Validação visual da arquitetura de rede em ambiente real:

![Arquitetura de Rede — Cloud Security Lab](../04-evidencias/arquitetura/arquitetura-cloud-security.png)

---

## 📌 Status

> **Implementado e Validado.** As próximas evoluções serão incorporadas conforme novos controles de segurança forem adicionados ao laboratório.

[← Retornar ao Início do Laboratório](../README.md)
