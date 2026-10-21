# Interface da calculadora de Valproato
import customtkinter as ctk
from tkinter import ttk
from calculadora import calcular_mensal

ctk.set_appearance_mode("dark")

# Paleta simples em tons de cinza / preto / branco
FUNDO = "#121212"
CARTAO = "#1E1E1E"
BORDA = "#2F2F2F"
ENTRADA_FG = "#242424"
ENTRADA_BORDA = "#3A3A3A"
TEXTO = "#F2F2F2"
TEXTO_SEC = "#A8A8A8"
TEXTO_LABEL = "#BDBDBD"

FONTE_TITULO = ("Segoe UI", 22, "bold")
FONTE_SUB = ("Segoe UI", 13)
FONTE_LABEL = ("Segoe UI", 13, "bold")
FONTE_ENTRADA = ("Segoe UI", 15, "bold")
FONTE_BOTAO = ("Segoe UI", 15, "bold")
FONTE_TOTAL = ("Segoe UI", 16, "bold")
FONTE_ERRO = ("Segoe UI", 12)
FONTE_TABELA = ("Segoe UI", 14)
FONTE_TABELA_FORTE = ("Segoe UI", 14, "bold")
FONTE_CABECALHO = ("Segoe UI", 14, "bold")

# Apenas para apresentacao: cada caixa tem 50 comprimidos.
# Nao altera o calculo, so converte o valor de caixas ja calculado.
CP_POR_CAIXA_EXIBICAO = 50

# Conversao usada pelo preenchimento automatico: comprimidos por dia -> por mes.
DIAS_POR_MES = 30

janela = ctk.CTk()
janela.title("Calculadora Valproato (Depakene)")
janela.geometry("920x740")
janela.minsize(800, 640)
janela.configure(fg_color=FUNDO)

# titulo (mesma estrutura atual)
titulo = ctk.CTkLabel(janela, text="Calculadora Valproato", font=FONTE_TITULO, text_color=TEXTO)
titulo.pack(pady=(22, 2))
sub = ctk.CTkLabel(janela, text="Caixa com 50 cp - sem fracionar caixa", font=FONTE_SUB, text_color=TEXTO_SEC)
sub.pack(pady=(0, 14))

# campos
campo_frame = ctk.CTkFrame(
    janela,
    fg_color=CARTAO,
    border_color=BORDA,
    border_width=1,
    corner_radius=12,
)
campo_frame.pack(padx=24, pady=5, fill="x")

# colunas iguais para alinhamento consistente
campo_frame.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="col")

ctk.CTkLabel(campo_frame, text="Meses", font=FONTE_LABEL, text_color="#E8E8E8").grid(row=0, column=0, padx=14, pady=(18, 6), sticky="w")
ctk.CTkLabel(campo_frame, text="Comprimidos por dia", font=FONTE_LABEL, text_color="#E8E8E8").grid(row=0, column=1, padx=14, pady=(18, 6), sticky="w")
ctk.CTkLabel(campo_frame, text="Comprimidos por mes", font=FONTE_LABEL, text_color="#E8E8E8").grid(row=0, column=2, padx=14, pady=(18, 6), sticky="w")
ctk.CTkLabel(campo_frame, text="Sobra inicial", font=FONTE_LABEL, text_color="#E8E8E8").grid(row=0, column=3, padx=14, pady=(18, 6), sticky="w")

entry_meses = ctk.CTkEntry(
    campo_frame,
    placeholder_text="ex: 6",
    height=44,
    corner_radius=8,
    font=FONTE_ENTRADA,
    fg_color=ENTRADA_FG,
    border_color=ENTRADA_BORDA,
    border_width=1,
    text_color="#FFFFFF",
    placeholder_text_color="#7A7A7A",
    justify="center",
)
entry_meses.grid(row=1, column=0, padx=14, pady=4, sticky="ew")

entry_dia = ctk.CTkEntry(
    campo_frame,
    placeholder_text="ex: 2",
    height=44,
    corner_radius=8,
    font=FONTE_ENTRADA,
    fg_color=ENTRADA_FG,
    border_color=ENTRADA_BORDA,
    border_width=1,
    text_color="#FFFFFF",
    placeholder_text_color="#7A7A7A",
    justify="center",
)
entry_dia.grid(row=1, column=1, padx=14, pady=4, sticky="ew")

entry_cp = ctk.CTkEntry(
    campo_frame,
    placeholder_text="ex: 60",
    height=44,
    corner_radius=8,
    font=FONTE_ENTRADA,
    fg_color=ENTRADA_FG,
    border_color=ENTRADA_BORDA,
    border_width=1,
    text_color="#FFFFFF",
    placeholder_text_color="#7A7A7A",
    justify="center",
)
entry_cp.grid(row=1, column=2, padx=14, pady=4, sticky="ew")

entry_sobra = ctk.CTkEntry(
    campo_frame,
    height=44,
    corner_radius=8,
    font=FONTE_ENTRADA,
    fg_color=ENTRADA_FG,
    border_color=ENTRADA_BORDA,
    border_width=1,
    text_color="#FFFFFF",
    justify="center",
)
entry_sobra.insert(0, "0")
entry_sobra.grid(row=1, column=3, padx=14, pady=4, sticky="ew")


def preencher_por_mes(_evento=None):
    # "Comprimidos por mes" e preenchido automaticamente a partir de "Comprimidos por dia".
    texto = entry_dia.get().strip()
    try:
        por_dia = int(texto)
    except ValueError:
        return
    if por_dia <= 0:
        return
    entry_cp.delete(0, "end")
    entry_cp.insert(0, str(por_dia * DIAS_POR_MES))


entry_dia.bind("<KeyRelease>", preencher_por_mes)
entry_dia.bind("<FocusOut>", preencher_por_mes)

lbl_erro = ctk.CTkLabel(campo_frame, text="", font=FONTE_ERRO, text_color="#E57373")
lbl_erro.grid(row=2, column=0, columnspan=4, padx=12, pady=(4, 0))

botao = ctk.CTkButton(
    campo_frame,
    text="Calcular",
    height=42,
    corner_radius=8,
    font=FONTE_BOTAO,
    fg_color="#E8E8E8",
    hover_color="#FFFFFF",
    text_color="#111111",
    border_width=0,
)
botao.grid(row=3, column=0, columnspan=4, padx=12, pady=(12, 16), sticky="ew")

# faixa de resultado
resultado_frame = ctk.CTkFrame(
    janela,
    fg_color=CARTAO,
    border_color=BORDA,
    border_width=1,
    corner_radius=10,
)
resultado_frame.pack(padx=24, pady=(10, 4), fill="x")

lbl_total = ctk.CTkLabel(
    resultado_frame,
    text="Preencha os dados e clique em Calcular.",
    font=FONTE_TOTAL,
    text_color="#FFFFFF",
)
lbl_total.pack(padx=14, pady=14)

# tabela
tabela_frame = ctk.CTkFrame(
    janela,
    fg_color=CARTAO,
    border_color=BORDA,
    border_width=1,
    corner_radius=12,
)
tabela_frame.pack(padx=24, pady=(8, 16), fill="both", expand=True)

tabela = ttk.Treeview(tabela_frame, columns=("Mes", "Caixas", "Qtd", "Sobra"), show="headings", height=10)
tabela.heading("Mes", text="Mês")
tabela.heading("Caixas", text="Caixas")
tabela.heading("Qtd", text="Comprimidos entregues")
tabela.heading("Sobra", text="Sobra para o próximo mês")
tabela.column("Mes", width=100, anchor="center")
tabela.column("Caixas", width=140, anchor="center")
tabela.column("Qtd", width=200, anchor="center")
tabela.column("Sobra", width=200, anchor="center")
tabela.pack(padx=12, pady=12, fill="both", expand=True)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Treeview",
    background="#1A1A1A",
    fieldbackground="#1A1A1A",
    foreground="#FFFFFF",
    rowheight=44,
    borderwidth=0,
    font=FONTE_TABELA,
)
style.configure(
    "Treeview.Heading",
    background="#333333",
    foreground="#FFFFFF",
    borderwidth=1,
    relief="flat",
    font=FONTE_CABECALHO,
)
style.map(
    "Treeview",
    background=[("selected", "#3D3D3D")],
    foreground=[("selected", "#FFFFFF")],
)
style.map(
    "Treeview.Heading",
    background=[("active", "#333333")],
)

# listras suaves para leitura (cinza escuro alternado)
# fonte maior/negrito so na apresentacao: mes e caixas mais visiveis,
# sobra facil de ler, tudo em branco puro para melhor contraste.
tabela.tag_configure("par", background="#1E1E1E", foreground="#FFFFFF", font=FONTE_TABELA_FORTE)
tabela.tag_configure("impar", background="#2A2A2A", foreground="#FFFFFF", font=FONTE_TABELA_FORTE)


def calcular():
    lbl_erro.configure(text="")
    preencher_por_mes()

    try:
        meses = int(entry_meses.get())
        cp = int(entry_cp.get())
        sobra = int(entry_sobra.get())
    except:
        lbl_erro.configure(text="Digite apenas numeros inteiros.")
        return

    try:
        r = calcular_mensal(meses, cp, sobra)
    except ValueError as e:
        lbl_erro.configure(text=str(e))
        return

    for i in tabela.get_children():
        tabela.delete(i)

    for idx, linha in enumerate(r["linhas"]):
        tag = "par" if idx % 2 == 0 else "impar"
        caixas = linha["caixas"]
        # Apenas apresentacao: caixas * 50, sem alterar o calculo original.
        qtd_cps = caixas * CP_POR_CAIXA_EXIBICAO
        caixas_txt = "%d caixa" % caixas if caixas == 1 else "%d caixas" % caixas
        qtd_txt = "%d cps" % qtd_cps
        sobra_txt = "%d cps" % linha["sobra_final"]
        tabela.insert("", "end", values=(linha["mes"], caixas_txt, qtd_txt, sobra_txt), tags=(tag,))

    lbl_total.configure(text="Total de caixas: %d   |   Sobra final: %d cp" % (r["total_caixas"], r["sobra_final"]))


botao.configure(command=calcular)

janela.mainloop()
