# Cloud Security Lab — Microsoft Azure

> Laboratório prático de Cloud Security desenvolvido de forma incremental, com foco em segmentação de rede, controle de acesso, redução de exposição e evolução dos controles de segurança.

---

## Visão Geral

Este projeto documenta a construção de um ambiente de Cloud Security no Microsoft Azure.

O laboratório está sendo desenvolvido passo a passo. Cada etapa registra o estado atual do ambiente, as decisões tomadas, os ajustes realizados e as validações executadas.

A ideia é permitir acompanhar não apenas o resultado final, mas também a evolução da infraestrutura ao longo do projeto.

---

## Arquitetura Atual

```text
[ Máquina Administrativa ]
         │
         │ RDP
         │ Origem restrita por NSG
         ▼
┌────────────────────────────────────────────────────────────────┐
│ VNET-CLOUD-SECURITY (10.10.0.0/16)                             │
│                                                                │
│   ┌────────────────────────────────────────────────────────┐   │
│   │ SNET-MANAGEMENT (10.10.10.0/24)                        │   │
│   │ └── JUMP-SERVER-01 (10.10.10.4) [IP Público]           │   │
│   └───────────────────────────┬────────────────────────────┘   │
│                               │                                │
│                               │ RDP interno                    │
│                               │ Controlado por NSG             │
│                               ▼                                │
│   ┌────────────────────────────────────────────────────────┐   │
│   │ SNET-SECURITY (10.10.20.0/24)                          │   │
│   │ └── SECURITY-SERVER-01 (10.10.20.4) [Sem IP Público]   │   │
│   └────────────────────────────────────────────────────────┘   │
│                                                                │
│   ┌────────────────────────────────────────────────────────┐   │
│   │ SNET-WORKLOAD (10.10.30.0/24)                          │   │
│   │ └── [Reservada para Workloads Futuros]                 │   │
│   └────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────┘
```

---

## Estado do Projeto

| Área | Status | Acompanhar |
|---|---|---|
| Arquitetura | Concluído | [Ver arquitetura →](./01-arquitetura/arquitetura.md) |
| Rede | Concluído | [Ver rede →](./02-rede/rede.md) |
| Controle de Acesso | Concluído | [Ver controle de acesso →](./03-controle-acesso/controle-acesso.md) |
| Evidências | Em atualização | [Ver evidências →](./04-evidencias/) |
| Microsoft Entra ID | Concluído | — | [Ver identidade →](./05-identidade/entra-id.md) |
| RBAC | Planejado | Próximo |
| Hardening | Planejado | Próximo |
| Monitoramento | Planejado | Próximo |

---

## O que já foi construído

### Rede

A infraestrutura foi criada utilizando uma VNet dedicada:

`VNET-CLOUD-SECURITY — 10.10.0.0/16`

Com três sub-redes:

- `SNET-MANAGEMENT` — `10.10.10.0/24`
- `SNET-SECURITY` — `10.10.20.0/24`
- `SNET-WORKLOAD` — `10.10.30.0/24`

A rede foi segmentada de acordo com a função de cada ambiente.

[Ver evolução da rede →](./02-rede/rede.md)

### Controle de Acesso

Foram criados NSGs específicos para cada subnet:

- `NSG-MANAGEMENT`
- `NSG-SECURITY`
- `NSG-WORKLOAD`

Também foi implementado o `JUMP-SERVER-01` como ponto central de administração.

[Ver evolução do controle de acesso →](./03-controle-acesso/controle-acesso.md)

### Servidores

O ambiente atualmente possui:

- `JUMP-SERVER-01` — `10.10.10.4`
- `SECURITY-SERVER-01` — `10.10.20.4`

O `SECURITY-SERVER-01` não possui IP público.

O acesso administrativo ao servidor interno foi validado através do Jump Server.

---

## Validação Atual

O fluxo administrativo validado foi:

```text
Máquina Administrativa
        |
        | RDP
        v
JUMP-SERVER-01
10.10.10.4
        |
        | RDP
        v
SECURITY-SERVER-01
10.10.20.4
```

O acesso ao servidor interno não é realizado diretamente pela Internet.

As evidências das validações são armazenadas na pasta:

[Ver evidências →](./04-evidencias/)

---

## Próxima Etapa

### Microsoft Entra ID

A próxima etapa será evoluir o controle de identidade e acesso, trabalhando:

- Microsoft Entra ID
- RBAC
- MFA
- Princípio do menor privilégio
- Controles de acesso administrativos

---

## Documentação

| Área | Conteúdo |
|---|---|
| [Arquitetura](./01-arquitetura/arquitetura.md) | Estrutura e decisões arquiteturais |
| [Rede](./02-rede/rede.md) | VNet, subnets, endereçamento e evolução da rede |
| [Controle de Acesso](./03-controle-acesso/controle-acesso.md) | NSGs, Jump Server e fluxo administrativo |
| [Evidências](./04-evidencias/) | Capturas e evidências utilizadas pelas demais etapas |

---

## Stack

`Microsoft Azure` · `Virtual Network` · `Network Security Groups` · `Windows Server 2025` · `Microsoft Entra ID` · `RBAC` · `Cloud Security`
