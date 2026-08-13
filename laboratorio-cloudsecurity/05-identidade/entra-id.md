# Microsoft Entra ID — Cloud Security Lab

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-02 | Validada estrutura de RBAC (`Contributor`/`Reader`) no escopo do Resource Group. |
| 2026-02 | Configurado MFA para contas administrativas. |
| 2026-01 | Criação das identidades segregadas: administração, leitura e contas de emergência (break glass). |

</details>

## Objetivo

Meu objetivo aqui é centralizar a autenticação e autorização do laboratório, eliminando dependências de contas locais e aplicando o princípio do menor privilégio.

## Status Atual

A estrutura de identidades, MFA e RBAC já está validada e ativa no ambiente. Como essa é minha área de especialização dentro do laboratório, sigo aprofundando os controles além do que já foi implementado.

## Resumo das Implementações

- **Identidades:** segregação entre contas administrativas, leitura e emergência.
- **RBAC:** funções `Contributor` e `Reader` implementadas no escopo do `RG-CLOUD-SECURITY-LAB`.
- **MFA:** camada de proteção adicional configurada para contas administrativas.

**Próximo passo:** evoluir para Privileged Access Management (PAM), federação e SSO, expandindo o escopo de IAM do laboratório.

Para detalhes completos da implementação e a matriz de acesso atual, consulte a documentação de controle de acesso:

[Ver detalhes em Controle de Acesso →](../03-controle-acesso/controle-acesso.md)

[Retornar ao Laboratório →](../README.md)
