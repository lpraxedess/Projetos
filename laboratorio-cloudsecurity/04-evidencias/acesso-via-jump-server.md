# Acesso à Security Server via Jump Server

## Objetivo

Validar que o acesso administrativo à infraestrutura de segurança ocorre através do Jump Server, sem exposição direta da máquina à Internet.

## Fluxo de acesso
```text
Máquina administrativa
        |
        | RDP
        v
JUMP-SERVER-01 (10.10.10.4)
        |
        | RDP
        v
SECURITY-SERVER-01 (10.10.20.4)
```
## Validação

Acesso realizado com sucesso:

- Jump Server: `JUMP-SERVER-01`
- IP: `10.10.10.4`
- Security Server: `SECURITY-SERVER-01`
- IP: `10.10.20.4`
- Protocolo: RDP
- Porta: TCP/3389
- IP público na Security Server: Não

## Controles de segurança

- `SECURITY-SERVER-01` não possui IP público.
- O acesso administrativo à infraestrutura ocorre através da `SNET-MANAGEMENT`.
- O acesso à `SNET-SECURITY` é controlado pelo `NSG-SECURITY`.
- O `JUMP-SERVER-01` atua como ponto de administração da infraestrutura.
- O acesso direto da Internet à `SECURITY-SERVER-01` não é permitido.

## Resultado

A comunicação administrativa entre o `JUMP-SERVER-01` e a `SECURITY-SERVER-01` foi validada com sucesso.
