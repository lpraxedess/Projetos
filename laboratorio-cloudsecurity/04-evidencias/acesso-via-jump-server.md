# Acesso à Security Server via Jump Server

## Objetivo

Validar que o acesso administrativo à infraestrutura de segurança ocorre através do Jump Server, sem exposição direta da máquina à Internet.

## Fluxo de acesso

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
