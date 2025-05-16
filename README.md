# Visualizador de Imagens

Este projeto implementa um visualizador de imagens em Python, que permite ao usuário carregar uma imagem, aplicar múltiplos filtros de forma combinada, visualizar os resultados ao lado da imagem original e, finalmente, salvar a imagem modificada em um novo arquivo.

## Funcionalidades

- **Carregar Imagem**: Permite ao usuário carregar uma imagem para edição.
- **Aplicar Filtros Combinados**: O visualizador oferece vários filtros que podem ser ativados individualmente e aplicados em conjunto:
  - Escala de cinza
  - Inversão de cores
  - Aumento de contraste
  - Desfoque (blur)
  - Nitidez (sharpen)
  - Detecção de bordas
- **Exibição Lado a Lado**: A imagem original e a imagem modificada são exibidas lado a lado para facilitar a comparação.
- **Salvar Imagem**: O usuário pode salvar a imagem resultante dos filtros em um novo arquivo, sem alterar a imagem original.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal do projeto.
- **Tkinter**: Biblioteca nativa do Python utilizada para a criação da interface gráfica.
- **Pillow (PIL)**: Biblioteca usada para aplicar filtros, redimensionamento e manipulação de imagens.

## Como Usar

### Passo 1: Instalar Dependências

Certifique-se de ter o Python 3.x instalado. Em seguida, instale a biblioteca Pillow com:

```bash
pip install pillow
````

### Passo 2: Executar o Script

Execute o arquivo principal para abrir o visualizador:

```bash
python app.py
```

### Passo 3: Utilizar o Visualizador

1. Clique em **"Carregar Imagem"** para selecionar uma imagem do seu computador.
2. Marque os filtros desejados usando os checkboxes.
3. Clique em **"Aplicar Filtros Selecionados"** para ver o resultado combinado.
4. A imagem original será exibida à esquerda e a imagem modificada à direita.
5. Para salvar a imagem editada, clique em **"Salvar Imagem"** e escolha o local e formato.

## Exemplo de Interface

A interface possui:

* Um **canvas** central com exibição lado a lado das imagens.
* Um grupo de **checkboxes** com os filtros disponíveis.
* Botões de controle para carregar, aplicar e salvar imagens.

## Observações

* **Imagem Original Preservada**: A imagem original é mantida intacta. As alterações são feitas em uma cópia que pode ser salva separadamente.
* **Redimensionamento**: As imagens são redimensionadas automaticamente para caber na visualização, mantendo sua proporção original.
* **Filtros Reversíveis**: Pode aplicar diferentes combinações de filtros quantas vezes quiser sem reiniciar o aplicativo, basta alterar os checkboxes e reaplicar.