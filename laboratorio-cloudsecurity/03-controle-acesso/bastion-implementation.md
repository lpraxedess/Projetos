# Implementação do Azure Bastion

> **Nota de contexto:** esta implementação ocorreu após a etapa de Governança (Azure Policy), mas foi organizada aqui por ser tematicamente um controle de acesso.

Para eliminar a exposição direta do Jump Server à internet, implementamos o **Azure Bastion**. Esta solução permite acesso via navegador (HTTPS/443), eliminando a necessidade de IPs públicos nas máquinas virtuais.

## Arquitetura de Acesso
- **Isolamento:** O IP público foi removido da placa de rede (NIC) do `JUMP-SERVER-01`.
- **Subnet Dedicada:** Criada a subnet `AzureBastionSubnet` na VNet `VNET-CLOUD-SECURITY` (bloco 10.10.40.0/26).
- **Serviço:** Azure Bastion em modo *Basic* na região `Brazil South`.

## Configurações Técnicas
- **IAM:** Atribuída a função `Virtual Machine User Login` à conta de leitura, garantindo conformidade de acesso.
- **Extensão:** Instalação da extensão `AADLoginForWindows` para suporte a identidades do Microsoft Entra ID.
- **Segurança:** O acesso é realizado de forma privada, mantendo o tráfego RDP interno à rede virtual.

## Validação
O acesso é realizado via Portal do Azure > Virtual Machines > JUMP-SERVER-01 > Connect > Bastion. O login é validado através de credenciais locais, assegurando que o ambiente de laboratório está operando dentro dos padrões de segurança corporativos.

[Retornar ao Laboratório →](../README.md)

