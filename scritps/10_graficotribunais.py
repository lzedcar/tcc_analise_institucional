import matplotlib.pyplot as plt
import pandas as pd
import os

# ---- Dados da tabela
df_tab = pd.DataFrame({
    "Tipo de órgão": ["1º Grau", "2º Grau", "Juizados Especiais", "Turmas Recursais", "Unidades mistas"],
    "Sigla": ["G1", "G2", "JE", "TR", "G1+JE"],
    "Descrição funcional": [
        "Varas judiciais com competência cível,\ncriminal ou especializada",
        "Câmaras e órgãos colegiados",
        "Unidades voltadas à tramitação\ncélere",
        "Instâncias recursais específicas",
        "Varas com competência simultânea\nou compartilhada entre\njustiça comum e justiça especial"
    ]
})

# ---- Figura (proporção parecida com A4 em paisagem, mas compacta)
fig, ax = plt.subplots(figsize=(7.2, 2.6), dpi=200)
ax.axis("off")

# Larguras relativas das colunas (ajuste fino aqui se quiser)
col_widths = [0.26, 0.15, 0.59]

# Cria a tabela e força ela a caber no canvas
tbl = ax.table(
    cellText=df_tab.values,
    colLabels=df_tab.columns,
    cellLoc="left",
    colLoc="center",
    colWidths=col_widths,
    bbox=[0.02, 0.02, 0.96, 0.96]  # [x, y, width, height] dentro do axes
)

# Fonte e escala (aqui é o que evita “vazar”)
tbl.auto_set_font_size(False)
tbl.set_fontsize(8.5)     # diminui um pouco sem ficar ilegível
tbl.scale(1, 1.35)        # aumenta altura das linhas

# Estilo: cabeçalho e alinhamentos
for (r, c), cell in tbl.get_celld().items():
    cell.set_linewidth(0.6)
    if r == 0:
        cell.set_text_props(weight="bold")
        cell.set_facecolor("#F2F2F2")  # cinza bem claro
        cell.set_height(cell.get_height() * 1.15)  # cabeçalho mais alto
    else:
        # garante que colunas 0 e 2 fiquem alinhadas à esquerda
        if c in (0, 2):
            cell._loc = "left"
        # aumenta especificamente a linha das "Unidades mistas" (última)
        if r == 5:
            cell.set_height(cell.get_height() * 1.35)

# Salvar
out_path = os.path.join("..", "graficos", "tabela_tipologia_tjsp.png")
plt.savefig(out_path, bbox_inches="tight", pad_inches=0.05)
plt.show()

print("Tabela salva em:", out_path)