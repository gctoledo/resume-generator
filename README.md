# Gerador de Relatórios de Vendas

Este é um projeto em Python que transforma uma planilha Excel de vendas em um relatório mensal resumido e formatado.  
O resultado final é um arquivo Excel com colunas estilizadas, totais agrupados por cliente e mês, e uma apresentação visual limpa.

-- Projeto simples criado para otimizar tempo na empresa em que trabalho --

---

## 📦 Requisitos

- Python 3.10 ou superior
- Ambiente virtual (recomendado)

### 📚 Instalação das dependências

Para instalar as bibliotecas necessárias, execute:

```bash
pip install -r requirements.txt
```

Conteúdo de `requirements.txt`:

```
pandas
openpyxl
xlrd
```

---

## 🚀 Como executar

1. Execute o script principal:

```bash
python run.py
```

2. Uma janela será aberta para você selecionar o arquivo Excel de entrada (`.xls` ou `.xlsx`).

3. O relatório será gerado na pasta `relatorios/` e aberto automaticamente.

---

## 📁 Estrutura do projeto

```
project_root/
├── data/               # Pasta opcional para arquivos de entrada
├── relatorios/            # Onde os relatórios gerados são salvos
├── src/
│   ├── main.py         # Ponto de entrada principal
│   ├── loader.py       # Lógica de seleção e leitura do arquivo
│   ├── transformer.py  # Tratamento, agregação e pivotamento dos dados
│   ├── exporter.py     # Salva o Excel final e aplica a formatação
│   └── styles.py       # Estilos e formatação visual do Excel
├── requirements.txt
└── README.md
```

---

## 📝 Observações

- O arquivo de entrada deve conter, no mínimo, as seguintes colunas:
  - `Data`
  - `Valor da Venda`
  - `Cliente`
  - `Cód Cliente`

- O relatório gerado inclui:
  - Colunas mensais com totais por cliente
  - Formatação condicional (verde para valores, vermelho para células vazias)
  - Largura de colunas ajustada e cabeçalhos fixos
