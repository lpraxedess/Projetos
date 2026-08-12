# Controle de Acesso — Cloud Security Lab

## Estado Atual

O controle de acesso do ambiente Azure utiliza Microsoft Entra ID e Azure RBAC.

As permissões são aplicadas em diferentes níveis de escopo, permitindo evoluir posteriormente para o princípio do menor privilégio.

## Azure RBAC

Atualmente, a assinatura possui três atribuições com a função `Owner`.

| Identidade | Função | Escopo |
|---|---|---|
| `Luiz Henrique Praxedes da Silva` | Owner | Assinatura |
| `Luiz Henrique Praxedes da Silva` | Owner | Assinatura |
| `luiz.azure.admin` | Owner | Assinatura |

> O ambiente ainda está em fase de evolução. A configuração atual possui privilégios elevados para permitir a construção do laboratório. A redução desses privilégios será realizada nas próximas etapas, utilizando funções específicas e escopos mais restritos.

## Microsoft Entra ID

O ambiente possui identidades administrativas e contas destinadas a contingência:

| Identidade | Finalidade |
|---|---|
| `luiz.admin` | Administração do Microsoft Entra ID |
| `luiz.azure.admin` | Administração dos recursos Azure |
| `luiz.azure.reader` | Acesso somente leitura |
| `lab.breakglass01` | Conta de contingência |
| `lab.breakglass02` | Conta de contingência |

As contas `lab.breakglass01` e `lab.breakglass02` serão utilizadas como contas de emergência e deverão permanecer protegidas e com uso restrito.

## Próxima Evolução

A próxima etapa será reduzir a dependência da função `Owner` e implementar um modelo de acesso baseado em menor privilégio.

Serão avaliados:

- Azure RBAC
- Microsoft Entra ID
- MFA
- Microsoft Entra Privileged Identity Management (PIM)
- Separação entre contas administrativas e contas de uso diário
- Contas de emergência (*break glass*)
- Escopos específicos para cada função

## Evidência

A evidência do estado atual do RBAC está armazenada em:

`04-evidencias/controle-acesso/`

![IAM da assinatura Azure](../04-evidencias/controle-acesso/iam-assinatura.png)

![IAM do Resource Group](../04-evidencias/controle-acesso/iam-resource-group.png)
