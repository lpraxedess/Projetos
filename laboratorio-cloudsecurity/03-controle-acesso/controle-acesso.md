# Controle de Acesso — Cloud Security Lab

## Estado Atual

O controle de acesso da infraestrutura utiliza Network Security Groups (NSGs) associados aos ambientes de gerenciamento, segurança e workloads.

Os NSGs foram criados de acordo com a segmentação da rede e serão utilizados para controlar o tráfego entre os diferentes ambientes.

## NSGs Implementados

| NSG | Subnet | Função |
|---|---|---|
| `NSG-MANAGEMENT` | `SNET-MANAGEMENT` | Controle do ambiente de administração |
| `NSG-SECURITY` | `SNET-SECURITY` | Controle dos servidores de segurança |
| `NSG-WORKLOAD` | `SNET-WORKLOAD` | Controle dos workloads futuros |

## Arquitetura de Acesso

O modelo de administração utilizado no laboratório segue o fluxo:

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

O `SECURITY-SERVER-01` não possui IP público.

O acesso administrativo ao servidor interno ocorre através do `JUMP-SERVER-01`.

## Evidência

Abaixo está a evidência dos Network Security Groups criados no ambiente do laboratório.

![Network Security Groups — Cloud Security Lab](../04-evidencias/controle-acesso/nsg-cloud-security.png)

## Status

Controle de acesso inicial implementado.

### Próximas evoluções

- Microsoft Entra ID
- RBAC
- MFA
- Princípio do menor privilégio
- Hardening
- Monitoramento e auditoria

[Retornar ao Laboratório →](../README.md)
