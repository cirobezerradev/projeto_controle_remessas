# **Sistema de Controle de Remessas e Retornos Fiscais**
Este projeto foi desenvolvido para automatizar e garantir a conformidade fiscal no processo de industrialização por encomenda. O foco principal é o controle de prazos e quantidades de mercadorias recebidas para manufatura, substituindo controles manuais em planilhas por uma solução robusta baseada em banco de dados e processamento de arquivos XML.

### 📋 **Contexto do Projeto**
Empresas que recebem matéria-prima para industrialização possuem benefícios fiscais (como a isenção de ICMS conforme o Decreto 31.825 do RN), desde que a mercadoria seja devolvida em sua totalidade em até 180 dias. A falha nesse controle pode resultar em multas severas e cobrança retroativa de impostos.

Este sistema gerencia o ciclo de vida dessas operações, desde a entrada da Nota Fiscal de Remessa (CFOP 6901) até o retorno total ou parcial (CFOP 6902).

### 🚀 **Funcionalidades Principais**
**Importação de XML**: Cadastro automatizado de Notas Fiscais de Remessa e Retorno a partir da leitura de arquivos XML.<br>
**Validação de CFOP**: Filtro rigoroso para garantir que apenas operações de remessa (6901) e retorno (6902) sejam processadas.<br>
**Rastreabilidade de Itens**: Vinculação direta entre os itens retornados e suas respectivas notas de origem.<br>
**Controle de Saldo**: Monitoramento de retornos parciais para garantir a baixa correta do estoque fiscal.<br>
**Gestão de Prazos**: Estrutura preparada para alertas sobre o vencimento do prazo de 180 dias para devolução.<br>

### 🏗️ **Estrutura do Projeto**
A documentação técnica do projeto está dividida nos seguintes artefatos (disponíveis na pasta /docs):<br>
**Levantamento de Requisitos**: Definição das regras de negócio e necessidades do cliente.<br>
**Diagrama de Caso de Uso**: Representação das interações dos usuários com o sistema.<br>
**Modelo Conceitual**: Representação de alto nível das entidades e seus relacionamentos.<br>
**Modelo Lógico**: Estruturação dos dados com chaves primárias, estrangeiras e tipos de dados.<br>
**Modelo Físico** (Script SQL): Scripts para criação das tabelas e integridade do banco de dados.<br>]

### 🛠️ **Tecnologias Utilizadas**
**Banco de Dados**: PostgreSQL.
**Modelagem**: Ferramentas de modelagem de dados (ER).
**Linguagem de Consulta**: SQL (DML/DDL).

### 📊 **Modelagem de Dados**
O banco de dados foi estruturado para suportar a complexidade de notas que possuem múltiplos itens e retornos que podem referenciar diferentes remessas.

**Entidades Principais**: Nota_Fiscal, Item_Nota, Cliente, Produto.<br>
**Regra de Integridade**: Um item de retorno deve obrigatoriamente referenciar um item de uma nota de remessa previamente cadastrada.<br>
