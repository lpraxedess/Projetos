# Cloud Security Lab — Microsoft Azure

> Laboratório prático de Cloud Security desenvolvido de forma incremental, com foco em segmentação de rede, controle de acesso, redução de exposição e evolução dos controles de segurança — com aprofundamento contínuo em Identity and Access Management (IAM).

---

## Visão Geral

Este projeto documenta a construção de um ambiente de Cloud Security no Microsoft Azure.

O laboratório está sendo desenvolvido passo a passo. Cada área possui seu próprio histórico de evolução, disponível no respectivo documento.

Meu foco de especialização é IAM, mas entendo que conhecimento sólido em todas as frentes de Cloud Security é necessário para atuar com profundidade — por isso o laboratório evolui em múltiplas áreas, cada uma no seu devido tempo.

---

## Áreas do Laboratório

Cada frente abaixo representa um tema que venho desenvolvendo dentro do laboratório. O resumo aqui é só o ponto de partida — o histórico completo de decisões, ajustes e evolução de cada uma fica documentado na área específica.

### 🏗️ Arquitetura
Foquei em desenhar uma estrutura que já nasce segmentada, separando o que é gerenciamento, o que é segurança e o que é workload — reduzindo a superfície de ataque desde a concepção do ambiente, não como um ajuste posterior.

[Ver evolução completa →](./01-arquitetura/arquitetura.md)

### 🌐 Rede
Em redes, foquei na estruturação e arquitetura da conexão entre as máquinas, aplicando boas práticas de segurança para garantir uma estrutura e conexão segura entre os ambientes.

[Ver evolução completa →](./02-rede/rede.md)

### 🔐 Controle de Acesso
Aqui o foco foi evoluir o acesso administrativo de forma progressiva — começando pelo controle via rede (NSGs e Jump Server), avançando para autorização (RBAC) e autenticação (MFA), até eliminar completamente a exposição pública com Azure Bastion.

[Ver evolução completa →](./03-controle-acesso/controle-acesso.md)

### 🪪 Identidade & IAM — *área de especialização*
Esta é a frente onde aprofundo mais — centralização da autenticação no Microsoft Entra ID, separação de contas por função, e evolução contínua para Privileged Access Management (PAM), federação e princípio do menor privilégio em todos os níveis.

[Ver evolução completa →](./05-identidade/entra-id.md)

### 📋 Governança
Foquei em sair de um controle apenas reativo para um controle preventivo — usando Azure Policy pra garantir que os recursos sigam padrões definidos antes mesmo de serem criados, não depois.

[Ver evolução completa →](./06-governanca/azure-policy.md)

### 🔑 Federação e SSO — *Em Desenvolvimento*
O objetivo será aprofundar o que começou em Identidade, indo além da estrutura básica de contas — trabalhando federação entre provedores, Single Sign-On e cenários de colaboração externa (B2B/B2C).

### 🔒 Criptografia e Proteção de Dados — *Em Desenvolvimento*
O objetivo será trabalhar a proteção de dados em repouso e em trânsito, gestão de chaves e segredos com Azure Key Vault, e controlar quem tem permissão de acessar cada camada de criptografia.

### 🛡️ Hardening — *Em Desenvolvimento*
O objetivo será reduzir a superfície de ataque nos próprios servidores, aplicando benchmarks de configuração segura no nível do sistema operacional.

### 📊 Monitoramento — *Em Desenvolvimento*
O objetivo será dar visibilidade sobre o que acontece dentro do ambiente — logs, alertas e detecção de comportamento anômalo.

### 🕵️ Resposta a Incidentes — *Em Desenvolvimento*
O objetivo será estruturar um processo de investigação e resposta a partir do que for detectado no Monitoramento — da identificação à contenção, documentando cada cenário como um caso de estudo.

### ⚙️ DevSecOps / Infraestrutura como Código — *Em Desenvolvimento*
O objetivo será aplicar segurança desde o provisionamento do ambiente, usando Infraestrutura como Código com validações de segurança antes do deploy, ao invés de corrigir depois que o recurso já existe.

[Retornar aos Projetos →](../README.md)
