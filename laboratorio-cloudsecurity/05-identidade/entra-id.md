# Microsoft Entra ID — Cloud Security Lab

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-02 | Validada estrutura de RBAC (`Contributor`/`Reader`) no escopo do Resource Group. |
| 2026-02 | Configurado MFA para contas administrativas. |
| 2026-01 | Criadas identidades segregadas para administração, leitura e acesso emergencial. |

</details>

## 🎯 Objetivo

Aqui concentro a parte de identidade do laboratório: criação e organização das contas, autenticação, autorização e aplicação do menor privilégio.

## 👤 Estrutura Atual

- **Identidades:** separação entre administração, leitura e contas de emergência (*break-glass*).
- **RBAC:** `Contributor` e `Reader` aplicados no escopo do `RG-CLOUD-SECURITY-LAB`.
- **MFA:** configurado para as contas administrativas.

## 🔐 Relação com o Controle de Acesso

A identidade é utilizada junto com as regras de acesso do ambiente. A documentação detalhada das permissões, escopos e do processo de evolução está em:

[Ver Controle de Acesso →](../03-controle-acesso/controle-acesso.md)

## 🧪 Experimentos e Aprendizados

Novos experimentos, erros, decisões ou descobertas relevantes são registrados aqui conforme surgirem.

### Exemplo

**O que mudou:** descreva a alteração realizada.

**Por que:** explique o problema ou necessidade que motivou a mudança.

**Resultado:** registre como a alteração foi validada e o que foi aprendido.

## 🔮 Próximos Passos

A evolução desta área deve avançar conforme o laboratório incorporar novos cenários de PAM, federação e SSO.

---

[← Retornar ao Início do Laboratório](../README.md)
