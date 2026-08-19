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

## 📝 Observações

>

---

[← Controle de Acesso](../03-controle-acesso/controle-acesso.md) · [↑ Laboratório](../README.md) · [Governança →](../06-governanca/azure-policy.md)
