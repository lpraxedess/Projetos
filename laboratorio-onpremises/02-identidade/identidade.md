# Identidade & Integração Híbrida — Active Directory & Microsoft Entra Connect

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Implementação do Active Directory no Windows Server 2025 e execução da sincronização híbrida via Microsoft Entra Connect. |

</details>

## 🎯 Por que estruturar a Identidade Híbrida no Lab?

Em ambientes corporativos reais, a grande maioria das empresas não vive 100% na nuvem ou 100% on-premises — o modelo híbrido é a realidade do dia a dia. No meu laboratório, eu fiz questão de replicar esse cenário: centralizar a gestão de identidades no Active Directory local (Windows Server 2025) e estender esse controle para a nuvem através do **Microsoft Entra Connect**.

Assim, consigo simular o ciclo de vida real de um usuário ou máquina: criar o objeto no AD local, propagar as políticas de grupo (GPOs) e ver a sincronização refletir diretamente no Microsoft Entra ID.

---

## ⚙️ O que foi feito na prática

1. **Estrutura Local (AD DS):** 
   * Subida do Active Directory no Windows Server 2025.
   * Organização de usuários, grupos e computadores da infraestrutura.
2. **Integração Híbrida (Entra Connect):**
   * Instalação e configuração do Microsoft Entra Connect no servidor do domínio.
   * Validação do fluxo de sincronização de diretórios (password hash sync e provisionamento de objetos).
3. **Consolidação na Nuvem:**
   * Garantia de que os usuários e computadores criados on-premises aparecem no painel do Entra ID devidamente sinalizados com o status de sincronização local habilitada (`DirSync`).

---

## 📊 Evidências da Integração

Os prints abaixo demonstram o sucesso do processo e o resultado da sincronização refletida no tenant:

### 🟢 Conclusão do Assistente de Instalação do Entra Connect
> *Evidência do término bem-sucedido da configuração de sincronização híbrida.*

![Conclusão da Integração do Entra Connect](../evidencias/identidade/integracao-concluida.png)

---

### 👥 Usuários Sincronizados no Microsoft Entra ID
> *Visão no portal da nuvem mostrando os usuários e o status de sincronização local habilitada.*

![Usuários Sincronizados no Entra ID](../evidencias/identidade/sincronizacao-realizada.png)

---

## ⏭️ Próximos Passos

* Validar políticas de acesso condicional (*Conditional Access*) baseadas nas identidades sincronizadas.
* Testar cenários de desprovisionamento (ex: desativar usuário no AD local e acompanhar a remoção de acesso na nuvem).

---

[← Retornar ao Início do Lab On-Premises](../README.md)
