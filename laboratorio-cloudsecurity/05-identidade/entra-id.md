# Microsoft Entra ID — Cloud Security Lab

## Objetivo
Centralizar a autenticação e autorização do laboratório, eliminando dependências de contas locais e aplicando o princípio do menor privilégio.

## Status Atual
Implementado. A estrutura de identidades, MFA e RBAC foi validada e está ativa no ambiente.

## Resumo das Implementações
- **Identidades:** Segregação entre contas administrativas, leitura e emergência.
- **RBAC:** Implementação de funções `Contributor` e `Reader` no escopo do `RG-CLOUD-SECURITY-LAB`.
- **MFA:** Camada de proteção adicional configurada para contas administrativas.

Para detalhes completos da implementação e a matriz de acesso atual, consulte a documentação de controle de acesso:

[Ver detalhes em Controle de Acesso →](../03-controle-acesso/controle-acesso.md)

ou

[Retornar ao Laboratório →](../README.md)
