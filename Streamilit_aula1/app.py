import pandas as pd
import streamlit as st

nome = "Matheus"
idade = 17

st.title("Meu primeiro dash")
st.subheader(nome)
st.write("Olá, mundo")
st.write(f"Meu nome é {nome} e tenho {idade} anos.")

st.divider()
df = pd.DataFrame({
    "Disciplina": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [5, 9, 7, 10],
})
# O Streamlit exibe o dataframe quando escrevemos df em uma linha sozinha.
df

st.divider()
st.subheader("Compras de supermercado")
st.caption("Preços de exemplo para a atividade.")

precos = {
    "Arroz (1 kg)": 8.00,
    "Feijão (1 kg)": 9.50,
    "Leite (1 litro)": 5.00,
    "Macarrão (500 g)": 4.50,
    "Café (250 g)": 12.00,
}


def calcular_preco_compra(preco_unitario, quantidade):
    return round(preco_unitario * quantidade, 2)


produto = st.selectbox("Escolha um produto", list(precos))
quantidade = st.number_input("Quantidade", min_value=1, value=1, step=1)
preco_unitario = precos[produto]
total = calcular_preco_compra(preco_unitario, quantidade)

st.write(f"Preço por unidade: R$ {preco_unitario:.2f}".replace(".", ","))
st.metric("Preço total da compra", f"R$ {total:.2f}".replace(".", ","))
