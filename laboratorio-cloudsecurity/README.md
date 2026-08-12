# Laboratório — Cloud Security

Laboratório pessoal desenvolvido em Microsoft Azure para prática de Segurança da Informação, Cloud Security e Identity and Access Management (IAM).

## Objetivo

Desenvolver experiência prática em Segurança da Informação, Microsoft Azure, Cloud Security e Identity and Access Management (IAM).

## Arquitetura

### Rede

| Recurso | Configuração |
|---|---|
| Resource Group | RG-CLOUD-SECURITY-LAB |
| Região | Brazil South |
| VNet | VNET-CLOUD-SECURITY |
| Espaço de endereçamento | 10.10.0.0/16 |

### Sub-redes

| Sub-rede | CIDR | Função |
|---|---|---|
| SNET-MANAGEMENT | 10.10.10.0/24 | Administração |
| SNET-SECURITY | 10.10.20.0/24 | Segurança |
| SNET-WORKLOAD | 10.10.30.0/24 | Cargas de trabalho |

### Network Security Groups

| NSG | Sub-rede | Função |
|---|---|---|
| NSG-MANAGEMENT | SNET-MANAGEMENT | Controle de acesso administrativo |
| NSG-SECURITY | SNET-SECURITY | Controle de acesso aos recursos de segurança |
| NSG-WORKLOAD | SNET-WORKLOAD | Controle de acesso às cargas de trabalho |

## Máquinas Virtuais

### JUMP-SERVER-01

- Sistema operacional: Windows Server 2025 Datacenter: Azure Edition
- Tamanho: Standard D2als_v6
- vCPUs: 2
- Sub-rede: SNET-MANAGEMENT
- IP privado: 10.10.10.4
- NSG: NSG-MANAGEMENT
- Função: Jump Server para administração dos recursos internos

## Validação

### JUMP-SERVER-01

```text
Hostname: JUMP-SERVER-01
IPv4: 10.10.10.4
Máscara: 255.255.255.0
Gateway: 10.10.10.1
Usuário: jump-server-01\labadmin
