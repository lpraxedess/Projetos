# Arquitetura — Cloud Security Lab

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Removido IP público do JUMP-SERVER-01; adicionada AzureBastionSubnet (10.10.40.0/26). |
| 2026-01 | Definição inicial da arquitetura: VNet única segmentada em três subnets por função. |

</details>

## Visão Geral

Estruturei este laboratório no Microsoft Azure com um objetivo claro desde o início: separar os diferentes níveis de infraestrutura e reduzir ao máximo a exposição dos recursos.

Para isso, optei por uma Virtual Network dedicada, dividida em subnets com funções bem específicas — cada uma isolando um tipo de responsabilidade dentro do ambiente.

## Estrutura

A infraestrutura ficou organizada da seguinte forma:

| Componente | Endereço | Função |
|---|---|---|
| `VNET-CLOUD-SECURITY` | `10.10.0.0/16` | Rede principal do laboratório |
| `SNET-MANAGEMENT` | `10.10.10.0/24` | Administração |
| `SNET-SECURITY` | `10.10.20.0/24` | Servidores de segurança |
| `SNET-WORKLOAD` | `10.10.30.0/24` | Workloads futuros |
| `AzureBastionSubnet` | `10.10.40.0/26` | Acesso via Azure Bastion (sem exposição pública) |

## Modelo de Acesso

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

Um dos pontos que priorizei foi garantir que a administração dos servidores internos nunca fosse feita diretamente pela Internet. Hoje, o `Azure Bastion` é o único ponto de entrada administrativo, acessado via navegador (HTTPS/443), e o `SECURITY-SERVER-01` permanece isolado na rede privada, sem IP público.

## Segmentação

Dividi as subnets por função justamente para poder aplicar controles diferentes de acordo com o que cada ambiente representa:

- ### Management: onde ficam os recursos que uso para administrar a infraestrutura.
- ### Security: reservada para os servidores e componentes ligados diretamente à segurança.
- ### Workload: deixei reservada para aplicações e outros workloads que devo adicionar conforme o laboratório evoluir.

## Decisões de Segurança

Ao longo da construção dessa arquitetura, as decisões que guiei foram:

- Segmentar a rede por função.
- Reduzir ao máximo a exposição direta à Internet.
- Centralizar a administração através de um Jump Server.
- Manter os servidores internos sem IP público.
- Controlar toda comunicação através de Network Security Groups.
- Deixar espaço para evoluir os controles com base em identidade no futuro.

## Evidência

A imagem abaixo é a evidência da arquitetura atual, validada em ambiente real:

![Arquitetura de Rede — Cloud Security Lab](../04-evidencias/arquitetura/arquitetura-cloud-security.png)

## Status

A arquitetura inicial já está implementada e validada. As próximas evoluções vão sendo incorporadas conforme adiciono novos controles de segurança ao laboratório.

[Retornar ao Laboratório →](../README.md)
