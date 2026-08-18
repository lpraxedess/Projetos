# Hardening & Compliance — Windows Server & CIS Benchmarks

<details>
<summary><strong>📜 Histórico de Evolução</strong></summary>

| Data | Alteração |
|---|---|
| 2026-03 | Análise de aplicabilidade e execução de script automatizado para hardening parcial do Windows Server com base nas recomendações CIS do Wazuh. |
| 2026-03 | Validação prática e captura de evidências (comparativo de pontuação de conformidade antes e depois). |

</details>

## 🎯 Por que e como eu faço o Hardening neste Lab?

Montar um laboratório é legal, mas deixá-lo seguro de verdade exige método. Aqui, eu quis trazer exatamente a mesma linha de raciocínio que sinto e aplico no meu dia a dia profissional: **nem tudo o que vem pronto em um framework ou baseline teórico é aplicável ou faz sentido em um ambiente corporativo real**. 

Quando puxei a auditoria inicial do **Wazuh** baseada nos **CIS Benchmarks**, vieram centenas de alertas. Antes de sair rodando qualquer script ou aceitando todas as recomendações cegamente, realizei uma análise criteriosa para validar o que realmente é aplicável ao contexto do meu laboratório (e que reflete o cuidado que devemos ter em produções reais para não quebrar sistemas ou travar aplicações).

---

## 🛠️ Minha Abordagem Prática

1. **Auditoria de Postura:** Deixei o Wazuh varrer o Windows Server para expor o cenário "cru" e entender onde estavam as maiores brechas de configuração.
2. **Filtro de Aplicabilidade:** Avaliei os pontos apontados, separando o que é crítico de ajustar (políticas de senha, auditoria de eventos, restrições de privilégio) daquilo que exigiria exceções controladas.
3. **Automação com Script:** Criei um script focado nos ajustes que passei pelo crivo da minha análise, garantindo agilidade e reprodutibilidade no ambiente.
4. **Validação:** Executei novamente o scan para medir o salto na pontuação de conformidade e certificar que o servidor ficou blindado, mas funcional.

---

## 📊 Evidências de Melhoria (Antes vs. Depois)

Os prints abaixo mostram o antes e o depois do ambiente após a aplicação dos ajustes que selecionei como aplicáveis:

### 🔴 Cenário Inicial (Antes do Hardening)
> *Visão da pontuação crua e dos alertas gerados pelas políticas padrão de instalação do sistema.*

![Pontuação Antes do Hardening](../evidencias/hardening/cis-pontuacao-antes.png)

---

### 🟢 Cenário Atual (Após o Hardening Aplicado e Filtrado)
> *Visão após rodar os ajustes validados, mostrando a subida expressiva na conformidade e a mitigação dos riscos reais.*

![Pontuação Depois do Hardening](../evidencias/hardening/cis-pontuacao-depois.png)

---

## ⏭️ Próximos Passos

* Avaliar novos pontos de melhoria nas políticas de auditoria.
* Levar essa mesma linha de raciocínio de "hardening com critério" para o meu ambiente Linux (Rocky Linux / Wazuh / Suricata).

---

[← Retornar ao Início do Lab On-Premises](../README.md)
