# Microsoft Entra ID — Cloud Security Lab

## Objetivo

Evoluir o controle de acesso do laboratório utilizando identidade como parte central da segurança.

A etapa tem como objetivo substituir a dependência exclusiva de contas locais por controles baseados em identidade, permitindo aplicar autenticação, autorização e princípio do menor privilégio.

## Planejamento

Nesta etapa serão trabalhados:

- Microsoft Entra ID
- Identidades administrativas
- RBAC
- MFA
- Princípio do menor privilégio
- Controle de acesso aos recursos Azure

## Modelo de Acesso

O modelo de segurança será evoluído de:

    Usuário
       |
       v
    Jump Server
       |
       v
    Recursos Azure

para um modelo em que a identidade também participa do controle:

    Usuário
       |
       v
    Microsoft Entra ID
       |
       | Autenticação
       v
    Autorização / RBAC
       |
       v
    Recursos Azure

## Estado Atual

Microsoft Entra ID ainda não foi implementado como mecanismo de autenticação administrativa do laboratório.

Status: **Próximo**

## Próximas Implementações

1. Criar ou utilizar uma identidade administrativa adequada.
2. Avaliar o acesso aos recursos através do Microsoft Entra ID.
3. Implementar RBAC.
4. Configurar MFA.
5. Aplicar o princípio do menor privilégio.
6. Validar o acesso.
7. Registrar as evidências.

## Evidências

As evidências desta etapa serão adicionadas após a implementação dos controles.

[Retornar ao Laboratório →](../README.md)
