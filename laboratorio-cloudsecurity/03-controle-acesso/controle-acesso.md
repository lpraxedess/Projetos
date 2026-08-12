# Controle de Acesso — Cloud Security Lab

## Estado Atual

O controle de acesso da infraestrutura é realizado através de Network Security Groups (NSGs), associados às subnets de acordo com sua função.

O objetivo é limitar a exposição dos servidores e permitir somente os fluxos necessários para administração.

## NSGs Implementados

| NSG | Subnet | Função |
|---|---|---|
| `NSG-MANAGEMENT` | `SNET-MANAGEMENT` | Controle do acesso administrativo |
| `NSG-SECURITY` | `SNET-SECURITY` | Proteção dos servidores de segurança |
| `NSG-WORKLOAD` | `SNET-WORKLOAD` | Controle dos workloads futuros |

---

## NSG-MANAGEMENT

O `NSG-MANAGEMENT` controla o acesso à subnet de gerenciamento.

### Regra administrativa

Foi configurada uma regra de entrada permitindo RDP:

| Regra | Porta | Protocolo | Origem | Ação |
|---|---:|---|---|---|
| `Allow-RDP-Admin` | `3389` | TCP | IP administrativo autorizado | Allow |

O acesso RDP externo é restrito à origem administrativa autorizada.

As demais conexões de entrada são bloqueadas pela regra padrão `DenyAllInBound`.

---

## NSG-SECURITY

O `NSG-SECURITY` controla o acesso à subnet onde está localizado o `SECURITY-SERVER-01`.

### Regra administrativa

O acesso RDP é permitido somente a partir da subnet de gerenciamento:

| Regra | Porta | Protocolo | Origem | Ação |
|---|---:|---|---|---|
| `Allow-RDP-From-Management` | `3389` | TCP | `10.10.10.0/24` | Allow |

Dessa forma, o `SECURITY-SERVER-01` não precisa aceitar conexões RDP diretamente da Internet.

O fluxo administrativo utilizado é:

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
