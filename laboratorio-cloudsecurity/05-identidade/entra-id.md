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

## 🧪 Experimentos e Aprendizados

> Esta seção registra o processo de aprendizagem. Novos experimentos devem ser adicionados quando uma implementação gerar um erro, descoberta ou decisão técnica relevante.

### Problema

Descreva o que você tentou implementar ou investigar.

### Erro

Registre o comportamento inesperado, mensagem de erro ou resultado diferente do esperado.

### Investigação

Registre as hipóteses, testes, documentação consultada e evidências utilizadas para encontrar a causa.

### Correção

Descreva a alteração realizada e o motivo técnico da solução escolhida.

### Resultado

Explique como a solução foi validada tecnicamente.

### Aprendizado

Registre o conceito de identidade, autenticação ou autorização consolidado com o experimento.

### Próximo passo

Registre o que ainda precisa ser estudado, testado ou melhorado.

---

## 🔮 Próximos Passos

Como evolução planejada, pretendo avançar para conceitos de *Privileged Access Management (PAM)*, federação e SSO para expandir o escopo de IAM do laboratório.

> Para detalhes granulares de implementação, evidências e matriz de acesso completa, consulte a documentação dedicada:
>
> [Ver detalhes em Controle de Acesso →](../03-controle-acesso/controle-acesso.md)

---

[← Retornar ao Início do Laboratório](../README.md)
