# Gerenciamento

## Monitoramento e gestão de atualizações WSUS

Este projeto documenta a criação de uma camada de observabilidade para o **WSUS (Windows Server Update Services)**, utilizando **PowerShell, Telegraf, InfluxDB e Grafana**.

O objetivo foi transformar as informações operacionais do WSUS em métricas históricas e painéis de acompanhamento, permitindo uma visão mais clara da situação das máquinas e das atualizações aprovadas.

### Arquitetura

```text
WSUS
  │
  ├── PowerShell / PoshWSUS
  │       │
  │       └── Coleta de status e conformidade
  │
  └── Telegraf
          │
          └── InfluxDB
                  │
                  └── Grafana
```

### Informações coletadas

O script PowerShell consulta o WSUS e consolida informações como:

- quantidade total de máquinas;
- máquinas conformes;
- máquinas com atualizações pendentes;
- máquinas com falhas de atualização;
- máquinas aguardando reinicialização;
- máquinas em estado desconhecido;
- máquinas sem reporte há mais de 3 dias;
- resultado da última sincronização dos clientes;
- atualizações pendentes por máquina;
- KB, título e estado das atualizações pendentes.

Os dados são enviados ao InfluxDB em três medições principais:

- `wsus-stats` — indicadores consolidados do ambiente;
- `wsus-machines` — situação individual das máquinas;
- `wsus-updates` — atualizações que exigem atenção.

### Grafana

O Grafana utiliza essas métricas para disponibilizar painéis de acompanhamento, incluindo:

- visão geral de conformidade do ambiente;
- máquinas sem reporte há mais de 3 dias;
- atualizações pendentes por máquina;
- evolução das máquinas pendentes e com falha;
- acompanhamento do estado de sincronização.

### Benefício

O WSUS possui informações de conformidade e atualização, mas sua utilização operacional pode ficar limitada quando é necessário acompanhar tendências, comparar períodos e identificar rapidamente máquinas que exigem intervenção.

A solução adiciona uma camada de observabilidade sobre os dados existentes no WSUS, permitindo transformar informações pontuais em indicadores, histórico e visualizações centralizadas.

### Tecnologias

- Windows Server
- WSUS
- PowerShell
- PoshWSUS
- Telegraf 1.39.3
- InfluxDB 1.12.4
- Grafana

### Evidência

Abaixo pode ser inserida a captura de tela do dashboard utilizado para demonstrar a solução em funcionamento.

```text
[ INSERIR PRINT DO DASHBOARD AQUI ]
```

### Observação

A coleta é executada pelo Telegraf em intervalo configurável, permitindo atualizar periodicamente os indicadores e manter o histórico no InfluxDB.
