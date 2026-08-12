# Rede

## Estado Atual

A infraestrutura de rede utiliza a VNET-CLOUD-SECURITY com espaço de endereçamento `10.10.0.0/16`.

A VNet está dividida em três sub-redes:

| Subnet | Endereço | Função | Status |
|---|---|---|---|
| SNET-MANAGEMENT | 10.10.10.0/24 | Administração | Ativo |
| SNET-SECURITY | 10.10.20.0/24 | Segurança | Ativo |
| SNET-WORKLOAD | 10.10.30.0/24 | Workloads | Reservado |

---

## Implementação

### VNET-CLOUD-SECURITY

- Região: Brazil South
- Address Space: `10.10.0.0/16`

### SNET-MANAGEMENT

- Address Space: `10.10.10.0/24`
- Função: gerenciamento administrativo

### SNET-SECURITY

- Address Space: `10.10.20.0/24`
- Função: servidores e componentes de segurança

### SNET-WORKLOAD

- Address Space: `10.10.30.0/24`
- Função: workloads futuros

---

## Controles Aplicados

Cada subnet possui um Network Security Group dedicado:

- `NSG-MANAGEMENT`
- `NSG-SECURITY`
- `NSG-WORKLOAD`

---

## Evolução

### 12/08/2026

- VNet criada.
- Três subnets configuradas.
- NSGs associados às subnets.
- Jump Server implantado na SNET-MANAGEMENT.
- Security Server implantado na SNET-SECURITY.
- Comunicação administrativa entre Jump Server e Security Server validada.

---

## Próxima Evolução

A próxima alteração prevista para a camada de rede será definida conforme a implementação dos controles de identidade, segurança e monitoramento.

---

## Evidências

[Ver evidências de rede →](../04-evidencias/)
