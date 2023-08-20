{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMTzCwTReU143hmnO+b/s//"
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
      "source": [
        "def calculadora(num1, num2, operacao):\n",
        "  num1 = int (input(\"Insira o primeiro número:\"))\n",
        "  num2 = int (input(\"Insira o segundo número:\"))\n",
        "  operacao = int (input(\"Insira a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): \"))\n",
        "\n",
        "  if operacao == 1:\n",
        "    return num1 + num2\n",
        "\n",
        "  elif operacao == 2:\n",
        "    return num1 - num2\n",
        "\n",
        "  elif operacao == 3:\n",
        "    return num1 * num2\n",
        "\n",
        "  elif operacao == 4:\n",
        "      if num2 != 0:\n",
        "          return num1 / num2\n",
        "      else:\n",
        "          return \"Erro: não há divisão por zero\"\n",
        "  else:\n",
        "      return 0\n",
        "\n",
        "resultado = calculadora (numero1, numero2, operacao)\n",
        "print(resultado)"
      ],
      "metadata": {
        "id": "fLeC-fLlcgVk"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}