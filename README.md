# Visualizador de Imagens

Este projeto implementa um visualizador de imagens em Python, que permite ao usuário carregar uma imagem, aplicar múltiplos filtros e transformações de forma combinada, visualizar os resultados ao lado da imagem original e, finalmente, salvar a imagem modificada em um novo arquivo.

## Funcionalidades

- **Carregar Imagem**: Permite ao usuário carregar uma imagem para edição.
- **Aplicar Filtros Combinados**: O visualizador oferece vários filtros que podem ser ativados individualmente e aplicados em conjunto:
  - Escala de cinza
  - Inversão de cores
  - Aumento de contraste
  - Desfoque (blur)
  - Nitidez (sharpen)
  - Detecção de bordas
- **Aplicar Transformações**:
  - **Rotação**: Permite girar a imagem em qualquer ângulo (graus).
  - **Redimensionamento**: Permite definir manualmente a largura e a altura da imagem.
- **Exibição Lado a Lado**: A imagem original e a imagem modificada são exibidas lado a lado para facilitar a comparação.
- **Salvar Imagem**: O usuário pode salvar a imagem resultante das edições em um novo arquivo, sem alterar a imagem original.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal do projeto.
- **Tkinter**: Biblioteca nativa do Python utilizada para a criação da interface gráfica.
- **Pillow (PIL)**: Biblioteca usada para aplicar filtros, transformações e manipulação de imagens.

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
3. Caso queira, preencha os campos de **rotação** (em graus) e/ou **redimensionamento** (largura e altura em pixels).
4. Clique em **"Aplicar Filtros e Transformações"** para ver o resultado combinado.
5. A imagem original será exibida à esquerda e a imagem modificada à direita.
6. Para salvar a imagem editada, clique em **"Salvar Imagem"** e escolha o local e formato.

## Exemplo de Interface

A interface possui:

* Um **canvas** central com exibição lado a lado das imagens.
* Um grupo de **checkboxes** com os filtros disponíveis.
* Campos de entrada para aplicar **transformações manuais**.
* Botões de controle para carregar, aplicar e salvar imagens.

## Observações

* **Imagem Original Preservada**: A imagem original é mantida intacta. As alterações são feitas em uma cópia que pode ser salva separadamente.
* **Redimensionamento na Visualização**: As imagens são redimensionadas automaticamente para caber na interface, mantendo a proporção original, apenas para exibição.
* **Transformações Personalizadas**: A rotação e o redimensionamento podem ser usados em conjunto com os filtros para gerar resultados personalizados.
* **Filtros Reversíveis**: Pode aplicar diferentes combinações de filtros e transformações quantas vezes quiser sem reiniciar o aplicativo, apenas requer ajustar os campos e reaplicar.
