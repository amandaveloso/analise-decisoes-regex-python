{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOSm+XkY15AW5KixlWDuscJ"
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
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LX2XS4p8fwoi"
      },
      "outputs": [],
      "source": [
        "import re\n",
        "import pandas as pd\n",
        "from pathlib import Path\n",
        "import pandas as pd\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def extract_values(text):\n",
        "  regex = r\"(?<!\\d)(R\\$)(\\d{1,3}(\\.\\d{3})*|\\d{1,3}(,\\d{3})*(\\.\\d{2})?)(?!\\d)\"\n",
        "  matches = re.findall(regex, text, re.IGNORECASE)\n",
        "  return matches\n",
        "\n"
      ],
      "metadata": {
        "id": "ls3y7CkbfylA"
      },
      "execution_count": 45,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def encontrar_ultimo_valor_financeiro(texto):\n",
        "    # Padrão para encontrar valores financeiros como \"R$ 50.000,00\" ou \"R$ 50.000\"\n",
        "    padrao = r'R\\$ \\d{1,3}(?:\\.\\d{3})*(?:,\\d{2})?'\n",
        "    # Encontrar todos os valores que correspondem ao padrão\n",
        "    valores = re.findall(padrao, texto)\n",
        "    # Verificar se encontrou algum valor\n",
        "    if valores:\n",
        "        # Pegar o último valor encontrado, remover o \"R$ \", substituir \".\" por nada e \",\" por \".\"\n",
        "        valor_formatado = valores[-1].replace('R$ ', '').replace('.', '').replace(',', '.')\n",
        "        # Converter o valor formatado para float\n",
        "        return float(valor_formatado)\n",
        "    else:\n",
        "        return None\n"
      ],
      "metadata": {
        "id": "GmkFOe9w8tAx"
      },
      "execution_count": 56,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "texto_teste = \"\"\"\n",
        "Danos Morais: R$ 20.000,00\n",
        "Honorários advocatícios: R$ 4.000,00\n",
        "Custas processuais: R$ 1.000,00\n",
        "\"\"\"\n",
        "\n",
        "ultimo_valor = encontrar_ultimo_valor_financeiro(texto_teste)\n",
        "print(ultimo_valor)  # Deve imprimir 1000.00 como float\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uoVCi2hx8-O0",
        "outputId": "1b629a4b-6d63-4955-b573-d7a1bfcbce8b"
      },
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1000.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_excel(\"julgados.xlsx\", engine= \"openpyxl\")\n",
        "df[\"Valores Extraídos\"] = df[\"julgado\"].apply(encontrar_ultimo_valor_financeiro)\n",
        "df.to_excel(\"teste2.xlsx\")"
      ],
      "metadata": {
        "id": "rFEWujkbf0av",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "66897682-fd29-45e4-95e6-155c40907bb0"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Exception ignored in: <function ZipFile.__del__ at 0x7b9c6e4b6320>\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/lib/python3.10/zipfile.py\", line 1821, in __del__\n",
            "    self.close()\n",
            "  File \"/usr/lib/python3.10/zipfile.py\", line 1838, in close\n",
            "    self.fp.seek(self.start_dir)\n",
            "ValueError: seek of closed file\n"
          ]
        }
      ]
    }
  ]
}