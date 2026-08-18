# Microsoft Entra ID — Cloud Security Lab

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-02 | Validada estrutura de RBAC (`Contributor`/`Reader`) no escopo do Resource Group. |
| 2026-02 | Configurado MFA para contas administrativas. |
| 2026-01 | Criação das identidades segregadas: administração, leitura e contas de emergência (break glass). |

</details>

## 🎯 Objetivo

O objetivo desta seção é centralizar a autenticação e autorização do laboratório, eliminando dependências de credenciais locais e aplicando o princípio do menor privilégio em nível de diretório.

---

## 📊 Status Atual

A estrutura de identidades, MFA e RBAC já se encontra validada e ativa no ambiente. Sendo uma das bases fundamentais do laboratório, a gestão de identidades atua em conjunto com as diretrizes de acesso.

---

## ⚙️ Resumo das Implementações

* **Identidades:** Segregação rígida entre funções administrativas, leitura e contas de emergência (*break-glass*).
* **RBAC:** Funções `Contributor` e `Reader` aplicadas estritamente no escopo do `RG-CLOUD-SECURITY-LAB`.
* **MFA:** Camada de autenticação multifator configurada e ativa para contas com privilégios.

---

## 🔮 Próximos Passos

Como evolução planejada, pretendo avançar para conceitos de *Privileged Access Management (PAM)*, federação e SSO para expandir o escopo de IAM do laboratório.

> Para detalhes granulares de implementação, evidências e matriz de acesso completa, consulte a documentação dedicada:
> 
> [Ver detalhes em Controle de Acesso →](../03-controle-acesso/controle-acesso.md)

---

[← Retornar ao Início do Laboratório](../README.md)
