# Laboratório — Cloud Security

Laboratório prático desenvolvido em Microsoft Azure com foco em Cloud Security, IAM, controle de acesso, segmentação de rede e hardening.

O projeto está sendo construído de forma incremental. A ideia é registrar não apenas o resultado final, mas também como a infraestrutura foi planejada, quais decisões foram tomadas, quais problemas surgiram e como foram resolvidos.

## Objetivo

Construir um ambiente de laboratório que permita praticar, de forma próxima a um cenário real, conceitos de Segurança da Informação, Microsoft Azure, Cloud Security e Identity and Access Management (IAM).

## Arquitetura

O ambiente utiliza uma Virtual Network dedicada, com o espaço de endereçamento `10.10.0.0/16`.

A rede foi dividida em três sub-redes, cada uma com uma finalidade específica:

- `SNET-MANAGEMENT` — `10.10.10.0/24`
- `SNET-SECURITY` — `10.10.20.0/24`
- `SNET-WORKLOAD` — `10.10.30.0/24`

A separação permite manter a administração, os componentes de segurança e os workloads em segmentos diferentes.

## Implementação

### 1. Estrutura de rede

Foi criada a `VNET-CLOUD-SECURITY` e as sub-redes foram associadas a Network Security Groups próprios:

- `NSG-MANAGEMENT`
- `NSG-SECURITY`
- `NSG-WORKLOAD`

Desde o início, a comunicação entre os segmentos foi pensada de acordo com a função de cada rede, evitando liberar acesso desnecessário.

### 2. Jump Server

O `JUMP-SERVER-01` foi criado na `SNET-MANAGEMENT`.

Ele possui um IP público e funciona como ponto de entrada para a administração dos recursos privados do laboratório.

O fluxo de acesso é:

```text
Máquina administrativa
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

Dessa forma, os servidores internos não precisam ficar diretamente expostos à Internet.

### 3. Security Server

O `SECURITY-SERVER-01` foi criado na `SNET-SECURITY`.

Seu endereço é `10.10.20.4` e a máquina não possui IP público.

O acesso administrativo foi realizado através do `JUMP-SERVER-01`, validando na prática o modelo de administração centralizada por Jump Server.

### 4. Controle de acesso

O tráfego entre as sub-redes é controlado pelos Network Security Groups.

O modelo adotado até aqui é:

```text
Acesso administrativo
        |
        v
Jump Server
        |
        v
Recursos privados
```

Em vez de permitir que cada servidor interno seja acessado diretamente pela Internet, o acesso administrativo passa primeiro pelo ambiente de gerenciamento.

## O que já foi validado

- VNet criada e organizada por função.
- Sub-redes de Management, Security e Workload implementadas.
- NSGs criados e associados às respectivas sub-redes.
- Jump Server implementado.
- Security Server implementado sem IP público.
- Acesso RDP ao Jump Server validado.
- Acesso RDP do Jump Server para o Security Server validado.
- Comunicação entre os segmentos validada de acordo com as regras configuradas.

## Decisões de segurança

Durante a construção do laboratório, algumas decisões foram tomadas para aproximar o ambiente de uma infraestrutura corporativa:

- Separação da rede por função.
- Controle de tráfego utilizando NSGs.
- Administração centralizada através de Jump Server.
- Servidores internos sem exposição pública.
- Restrição do acesso administrativo à rede de gerenciamento.
- Uso do menor nível de exposição possível para os recursos internos.

## Evolução do projeto

O laboratório ainda está em construção.

As próximas etapas serão adicionadas conforme forem implementadas e validadas, incluindo:

- Microsoft Entra ID
- RBAC
- Hardening dos servidores
- Monitoramento
- Logs e auditoria
- Detecção de eventos de segurança
- Controles adicionais de Cloud Security

A intenção é que este README acompanhe a evolução do laboratório e permita entender rapidamente o estado atual do ambiente sem precisar consultar cada arquivo individualmente.

## Documentação

Os detalhes técnicos e as evidências das implementações estão organizados nas seguintes seções:

- [Arquitetura](./01-arquitetura/arquitetura.md)
- [Rede](./02-rede/rede.md)
- [Controle de Acesso](./03-controle-acesso/controle-acesso.md)
- [Evidências](./04-evidencias/)
