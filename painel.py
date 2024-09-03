import streamlit as st
from PIL import Image
import os

st.title("Verificação de Montagem")

st.write("Selecione a região da máquina para ver a montagem ideal.")

# Lista de regiões com base nas pastas fornecidas
regioes = [
    "Bloco do jib", 
    "Bloco do principal", 
    "Calha LE do secundario", 
    "Entrada da esteira do secundario", 
    "entrada da esteira porta cabos primario", 
    "entrada da esteira porta cabos primario do secundario", 
    "entrada do secundario", 
    "jib", 
    "mangueira da direção direita", 
    "Magueiras Cilindro de direcao", 
    "mangueiras da bomba de driver", 
    "mangueiras da valvula cam superior", 
    "mangueiras direcao dianteiro esquerdo", 
    "mangueiras do cilindro de oscilacao", 
    "mangueiras do jib", 
    "pads", 
    "Saida do secundario para valvula cam", 
    "saida superior da esteira do secundario"
]

regiao_selecionada = st.selectbox("Escolha a região da máquina:", regioes)

st.write("**Em breve:** Função para tirar foto e verificar montagem.")

# Caminhos relativos para as pastas de imagens
mapeamento_diretorios = {
    "Bloco do jib": "imagens/Bloco do jib",
    "Bloco do principal": "imagens/Bloco do principal",
    "Calha LE do secundario": "imagens/Calha LE do secundario",
    "Entrada da esteira do secundario": "imagens/Entrada da esteira do secundario",
    "entrada da esteira porta cabos primario": "imagens/entrada da esteira porta cabos primario",
    "entrada da esteira porta cabos primario do secundario": "imagens/entrada da esteira porta cabos primario do secundario",
    "entrada do secundario": "imagens/entrada do secundario",
    "jib": "imagens/jib",
    "mangueira da direção direita": "imagens/mangueira da direção direita",
    "Magueiras Cilindro de direcao": "imagens/Magueiras Cilindro de direcao",
    "mangueiras da bomba de driver": "imagens/mangueiras da bomba de driver",
    "mangueiras da valvula cam superior": "imagens/mangueiras da valvula cam superior",
    "mangueiras direcao dianteiro esquerdo": "imagens/mangueiras direcao dianteiro esquerdo",
    "mangueiras do cilindro de oscilacao": "imagens/mangueiras do cilindro de oscilacao",
    "mangueiras do jib": "imagens/mangueiras do jib",
    "pads": "imagens/pads",
    "Saida do secundario para valvula cam": "imagens/Saida do secundario para valvula cam",
    "saida superior da esteira do secundario": "imagens/saida superior da esteira do secundario"
}

# Obtendo o caminho absoluto de forma dinâmica
base_dir = os.path.dirname(os.path.abspath(__file__))
subdiretorio_path = os.path.join(base_dir, mapeamento_diretorios[regiao_selecionada])

# Verifica se o caminho da pasta existe
if os.path.exists(subdiretorio_path) and os.path.isdir(subdiretorio_path):
    # Listando arquivos na pasta e pegando o primeiro encontrado
    arquivos = os.listdir(subdiretorio_path)
    image_file = None

    for arquivo in arquivos:
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_file = arquivo
            break

    if image_file:
        image_path = os.path.join(subdiretorio_path, image_file)
        try:
            imagem = Image.open(image_path)
            # Exibe a imagem com uma largura fixa para mantê-la proporcional
            st.image(imagem, caption=f"Montagem ideal para {regiao_selecionada}.", use_column_width=False, width=400)
        except Exception as e:
            st.error(f"Erro ao abrir a imagem: {e}")
    else:
        st.error("Nenhuma imagem encontrada na pasta para a região selecionada.")
else:
    st.error("Opção de região inválida ou pasta não encontrada.")

