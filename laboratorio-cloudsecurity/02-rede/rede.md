# Rede — Cloud Security Lab

## Estado Atual

A infraestrutura utiliza uma Virtual Network dedicada ao laboratório:

- VNet: `VNET-CLOUD-SECURITY`
- Endereço: `10.10.0.0/16`
- Região: `Brazil South`

A rede foi dividida em subnets de acordo com a função de cada ambiente.

## VNet

![VNET-CLOUD-SECURITY](../04-evidencias/rede/vnet-cloud-security.png)

## Subnets

A VNet foi segmentada em três subnets:

![Subnets da VNET-CLOUD-SECURITY](../04-evidencias/rede/subnet-cloud-security.png)

| Subnet | Endereço | Função |
|---|---|---|
| `SNET-MANAGEMENT` | `10.10.10.0/24` | Administração |
| `SNET-SECURITY` | `10.10.20.0/24` | Servidores de segurança |
| `SNET-WORKLOAD` | `10.10.30.0/24` | Workloads futuros |

## Network Security Groups

Cada subnet possui um Network Security Group dedicado:

- `NSG-MANAGEMENT`
- `NSG-SECURITY`
- `NSG-WORKLOAD`

Os NSGs serão utilizados para controlar o tráfego entre os diferentes ambientes e limitar a exposição dos recursos.
