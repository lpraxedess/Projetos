# ⚙️ Gerenciamento

Documentação das práticas de gerenciamento de atualizações, aplicação de patches e acompanhamento de conformidade no ambiente **On-Premises**.

## 🎯 Objetivo

Utilizar o WSUS como fonte de dados para construir uma camada de observabilidade que permita acompanhar, de forma centralizada, a situação das máquinas, atualizações pendentes, falhas e ausência de comunicação dos clientes.

A solução transforma informações operacionais do WSUS em métricas históricas e indicadores visuais, facilitando a identificação de máquinas que necessitam de intervenção.

## 🏗️ Solução

```text
                    ┌─────────────────┐
                    │      WSUS       │
                    │ Atualizações e  │
                    │   conformidade  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    PowerShell   │
                    │     PoshWSUS    │
                    │     Coleta      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Telegraf    │
                    │    Coleta /     │
                    │    Transporte   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    InfluxDB     │
                    │    Histórico    │
                    │    das métricas │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Grafana     │
                    │   Dashboards    │
                    │  e indicadores  │
                    └─────────────────┘
```

## 📊 Informações monitoradas

A coleta consolida informações relevantes do ambiente WSUS:

| Indicador | Descrição |
|---|---|
| 🖥️ **Total de máquinas** | Quantidade de clientes identificados pelo WSUS |
| ✅ **Conformes** | Máquinas sem atualizações que exigem atenção |
| 🟠 **Pendentes** | Máquinas com atualizações ainda não instaladas |
| 🔴 **Falhas** | Máquinas com atualizações em estado de falha |
| 🔄 **Reboot pendente** | Máquinas que necessitam de reinicialização |
| ❓ **Unknown** | Máquinas com estado de atualização desconhecido |
| 📡 **Sem reporte > 3 dias** | Clientes que não reportam ao WSUS há mais de três dias |
| 🔄 **Sincronização** | Resultado da última sincronização dos clientes |
| 📦 **Atualizações pendentes** | KB, título e estado das atualizações por máquina |

## 🗄️ Métricas no InfluxDB

Os dados são organizados em três medições:

### `wsus-stats`

Indicadores consolidados do ambiente, utilizados para números gerais e gráficos históricos.

### `wsus-machines`

Informações individuais das máquinas, incluindo:

- nome da máquina;
- status de conformidade;
- atualizações pendentes;
- falhas;
- reinicialização pendente;
- estado desconhecido;
- último reporte;
- resultado da última sincronização.

### `wsus-updates`

Detalhamento das atualizações que exigem atenção, relacionando:

- máquina;
- KB;
- atualização;
- estado;
- ID da atualização.

## 📈 Grafana

O dashboard permite visualizar a situação do ambiente de forma centralizada, incluindo:

- visão geral da conformidade;
- máquinas sem reporte há mais de 3 dias;
- atualizações pendentes por máquina;
- evolução das máquinas pendentes;
- evolução das máquinas com falha;
- acompanhamento da sincronização.

## 🔄 Funcionamento

O PowerShell consulta diretamente a API administrativa do WSUS e consolida os dados de conformidade e atualização.

O **Telegraf** executa o script periodicamente e envia as métricas para o **InfluxDB**, que mantém o histórico utilizado pelo **Grafana**.

O intervalo de coleta é configurável no `telegraf.conf`.

## 🧰 Tecnologias

| Tecnologia | Utilização |
|---|---|
| 🪟 **Windows Server** | Plataforma do ambiente |
| 🔄 **WSUS** | Gerenciamento de atualizações |
| 💻 **PowerShell** | Automação e coleta |
| 🔌 **PoshWSUS** | Integração com o WSUS |
| 📥 **Telegraf** | Coleta e envio das métricas |
| 🗄️ **InfluxDB** | Armazenamento das séries temporais |
| 📊 **Grafana** | Visualização e acompanhamento |

## 🖼️ Evidência

Dashboard desenvolvido para acompanhamento do ambiente WSUS:

> **Inserir aqui o print do dashboard.**

## 💡 Resultado

A solução adiciona uma camada de observabilidade ao WSUS, permitindo sair de uma visão predominantemente operacional e passar a acompanhar indicadores, histórico e situações que exigem intervenção em um único dashboard.

O objetivo não é substituir o WSUS, mas **ampliar a visibilidade sobre os dados que ele já disponibiliza**, facilitando o acompanhamento da saúde do ambiente e da conformidade das máquinas.

[← Voltar ao Laboratório](../README.md)
