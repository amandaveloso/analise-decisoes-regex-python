{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOPuchytV/2ZbNIUpB/wBN8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/amandaveloso/analise-decisoes-regex-python/blob/main/TPV.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import re\n",
        "df = pd.read_excel(\"teste_excel.xlsx\")\n",
        "for index, row in df.iterrows():\n",
        "  ementa = row['Ementa']"
      ],
      "metadata": {
        "id": "8iduRDD_hmfC"
      },
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Definido a função para analisar a prova necessária mencionada na ementa do julgamento\n"
      ],
      "metadata": {
        "id": "2Tdb6vJHR35k"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def analisar_prova_necessaria(prova_necessaria):\n",
        "    if any(palavra in prova_necessaria.lower() for palavra in [\"nota fiscal\", \"ordem de serviço\", \"guia\"]):\n",
        "        return \"Nota fiscal ou Ordem de serviço\"\n",
        "    elif any(palavra in prova_necessaria.lower() for palavra in [\"laudo\", \"prova documental\", \"laudo técnico\", \"laudo tecnico\", \"documento\", \"protocolo\", \"testemunhal\", \"e-mail\"]):\n",
        "        return \"Laudo ou prova documental - análise do produto\"\n",
        "    elif \"não especificada\" in prova_necessaria.lower():\n",
        "        return \"Em branco\"\n",
        "    else:\n",
        "        return prova_necessaria\n"
      ],
      "metadata": {
        "id": "ze3mB2sTR1vU"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Função para analisar a prova necessária mencionada na ementa do julgamento"
      ],
      "metadata": {
        "id": "qCcdOG6LSFkT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def analisar_prova_necessaria(prova_necessaria):\n",
        "    if any(palavra in prova_necessaria.lower() for palavra in [\"nota fiscal\", \"ordem de serviço\", \"guia\"]):\n",
        "        return \"Nota fiscal ou Ordem de serviço\"\n",
        "    elif any(palavra in prova_necessaria.lower() for palavra in [\"laudo\", \"prova documental\", \"laudo técnico\", \"laudo tecnico\", \"documento\", \"protocolo\", \"testemunhal\", \"e-mail\"]):\n",
        "        return \"Laudo ou prova documental - análise do produto\"\n",
        "    elif \"não especificada\" in prova_necessaria.lower():\n",
        "        return \"Em branco\"\n",
        "    else:\n",
        "        return prova_necessaria  # Retorna o valor original se nenhuma condição for atendida\n",
        "\n",
        "def analisar_ementa(ementa):\n",
        "    # Decisão do Julgamento\n",
        "    resultado_julgamento = re.search(r\"\\b(julgou os pedidos improcedentes|julgou improcedentes os pedidos|julgou improcedente o pedido|indeferiu o pedido de danos|julgo totalmente improcedente|julgo totalmente improcedentes| julgo improcedente|julgou improcedentes|improcedente o pedido| improcedentes os pedidos|procedente|julgou procedente|julgou parcialmente procedente|improcedente|)\\b\", ementa, re.I)\n",
        "    decisao = \"Não determinada\"\n",
        "    if resultado_julgamento:\n",
        "        if resultado_julgamento.group().lower() in [\"procedente\", \"dar provimento\", \"provido\", \"apelo provido\"]:\n",
        "            decisao = \"Procedente (desfavorável à fornecedora)\"\n",
        "        else:\n",
        "            decisao = \"Improcedente (favorável à fornecedora)\"\n",
        "\n",
        "    # Prova Necessária\n",
        "    prova = re.search(r\"\\b(documentação|documento|documentos|nota fiscal|notas fiscais|ordem de serviço|laudo|anexo|anexado|anexos)\\b\", ementa, re.I)\n",
        "    prova_necessaria = prova.group() + ' ' + ementa.split(prova.group(), 1)[1].split('.')[0] if prova else \"Não especificada\"\n",
        "\n",
        "    # Valor da Condenação\n",
        "    valor_condenacao = re.search(r\"(?<=R\\$)\\s*\\d{1,3}(?:\\.\\d{3})*(?:,\\d{2})?\", ementa)\n",
        "    valor_condenacao = valor_condenacao.group() if valor_condenacao else \"Não aplicável\"\n",
        "\n",
        "    # Dano Moral\n",
        "    dano_moral = \"Sim\" if re.search(r\"\\b(dano moral|danos morais)\\b\", ementa, re.I) and re.search(r\"\\b(condenar|condeno|indenizar|pagamento)\\b\", ementa, re.I) else \"Não\"\n",
        "\n",
        "    return {\"Decisão\": decisao, \"Prova Necessária\": prova_necessaria, \"Valor da Condenação\": valor_condenacao, \"Existência de Dano Moral\": dano_moral}\n"
      ],
      "metadata": {
        "id": "ZYfZllHBb8DS"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Criando um novo Dataset com essas informações"
      ],
      "metadata": {
        "id": "rqApZcDCSabh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Abrindo o meu arquivo\n",
        "df = pd.read_excel('teste_excel.xlsx')  # Especifique a codificação correta se necessário\n",
        "\n",
        "# Aplicando a análise em cada ementa\n",
        "for index, row in df.iterrows():\n",
        "    resultados = analisar_ementa(row['Ementa'])\n",
        "    for key, value in resultados.items():\n",
        "        df.at[index, key] = value\n",
        "\n",
        "# Aplicando a análise adicional na coluna \"Prova Necessária\"\n",
        "df['Análise Prova Necessária'] = df['Prova Necessária'].apply(analisar_prova_necessaria)\n",
        "\n",
        "# Salvando os resultados\n",
        "df.to_excel('ementas_analisadas.xlsx', index=False)\n"
      ],
      "metadata": {
        "id": "JxMFFU4ottbl"
      },
      "execution_count": 37,
      "outputs": []
    }
  ]
}