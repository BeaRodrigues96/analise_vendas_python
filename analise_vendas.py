import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler o arquivo CSV
df = pd.read_csv("vendas.csv", parse_dates=["data"])

# 2. Calcular o faturamento de cada venda
df["faturamento"] = df["quantidade"] * df["preco"]

# 3. Estatísticas simples
print("📊 Total de vendas:", df["quantidade"].sum())
print("💰 Faturamento total: R$", df["faturamento"].sum())

# Produto mais vendido
produto_mais_vendido = df.groupby("produto")["quantidade"].sum().idxmax()
print("🏆 Produto mais vendido:", produto_mais_vendido)

# 4. Faturamento por mês
df["mes"] = df["data"].dt.to_period("M")
faturamento_mes = df.groupby("mes")["faturamento"].sum()

print("\n📅 Faturamento por mês:")
print(faturamento_mes)

# 5. Gráfico
faturamento_mes.plot(kind="bar", title="Faturamento por Mês")
plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.show()
