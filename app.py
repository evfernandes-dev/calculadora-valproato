# Interface da calculadora de Valproato com integração MySQL
import customtkinter as ctk
from tkinter import ttk
from calculadora import calcular_mensal
from database import inicializar_banco, buscar_paciente, salvar_ou_atualizar_paciente, obter_ultima_sobra, salvar_dispensacao

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

# Apenas para apresentação: cada caixa tem 50 comprimidos.
CP_POR_CAIXA_EXIBICAO = 50

# Conversão usada pelo preenchimento automático: comprimidos por dia -> por mês.
DIAS_POR_MES = 30

# Inicializa o banco de dados MySQL ao iniciar
db_ok = inicializar_banco()

janela = ctk.CTk()
janela.title("Calculadora Valproato (Depakene) - Com MySQL")
janela.geometry("960x860")
janela.minsize(840, 700)
janela.configure(fg_color=FUNDO)

# Título
titulo = ctk.CTkLabel(janela, text="Calculadora Valproato", font=FONTE_TITULO, text_color=TEXTO)
titulo.pack(pady=(18, 2))
sub_texto = "Caixa com 50 cp - sem fracionar caixa | Integrado ao MySQL" if db_ok else "Caixa com 50 cp - sem fracionar caixa (MySQL Offline)"
sub = ctk.CTkLabel(janela, text=sub_texto, font=FONTE_SUB, text_color="#81C784" if db_ok else "#E57373")
sub.pack(pady=(0, 10))

# ==========================================
# FRAME 1: IDENTIFICAÇÃO DO PACIENTE (NOVO)
# ==========================================
paciente_frame = ctk.CTkFrame(
    janela,
    fg_color=CARTAO,
    border_color=BORDA,
    border_width=1,
    corner_radius=12,
)
paciente_frame.pack(padx=24, pady=5, fill="x")
paciente_frame.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="pcol")

ctk.CTkLabel(paciente_frame, text="Identificação do Paciente (Nome, CPF ou SUS)", font=FONTE_LABEL, text_color="#E8E8E8").grid(row=0, column=0, columnspan=4, padx=14, pady=(14, 4), sticky="w")

entry_nome_paciente = ctk.CTkEntry(
    paciente_frame,
    placeholder_text="Nome do Paciente",
    height=40,
    corner_radius=8,
    font=FONTE_ENTRADA,
    fg_color=ENTRADA_FG,
    border_color=ENTRADA_BORDA,
    border_width=1,
    text_color="#FFFFFF",
    placeholder_text_color="#7A7A7A",
)
entry_nome_paciente.grid(row=1, column=0, columnspan=2, padx=14, pady=4, sticky="ew")

entry_doc_paciente = ctk.CTkEntry(
    paciente_frame,
    placeholder_text="CPF ou Cartão SUS",
    height=40,
    corner_radius=8,
    font=FONTE_ENTRADA,
    fg_color=ENTRADA_FG,
    border_color=ENTRADA_BORDA,
    border_width=1,
    text_color="#FFFFFF",
    placeholder_text_color="#7A7A7A",
    justify="center",
)
entry_doc_paciente.grid(row=1, column=2, padx=14, pady=4, sticky="ew")

btn_buscar = ctk.CTkButton(
    paciente_frame,
    text="Buscar / Carregar",
    height=40,
    corner_radius=8,
    font=FONTE_BOTAO,
    fg_color="#333333",
    hover_color="#444444",
    text_color="#FFFFFF",
)
btn_buscar.grid(row=1, column=3, padx=14, pady=4, sticky="ew")

lbl_status_paciente = ctk.CTkLabel(paciente_frame, text="Digite o nome ou documento e clique em Buscar para carregar sobras anteriores.", font=FONTE_ERRO, text_color="#A8A8A8")
lbl_status_paciente.grid(row=2, column=0, columnspan=4, padx=14, pady=(4, 12), sticky="w")

# Variável para armazenar o ID do paciente carregado/selecionado
paciente_atual_id = None

# ==========================================
# FRAME 2: CAMPOS DE DOSES E MESES
# ==========================================
campo_frame = ctk.CTkFrame(
    janela,
    fg_color=CARTAO,
    border_color=BORDA,
    border_width=1,
    corner_radius=12,
)
campo_frame.pack(padx=24, pady=5, fill="x")
campo_frame.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="col")

ctk.CTkLabel(campo_frame, text="Meses", font=FONTE_LABEL, text_color="#E8E8E8").grid(row=0, column=0, padx=14, pady=(16, 6), sticky="w")
ctk.CTkLabel(campo_frame, text="Comprimidos por dia", font=FONTE_LABEL, text_color="#E8E8E8").grid(row=0, column=1, padx=14, pady=(16, 6), sticky="w")
ctk.CTkLabel(campo_frame, text="Comprimidos por mês", font=FONTE_LABEL, text_color="#E8E8E8").grid(row=0, column=2, padx=14, pady=(16, 6), sticky="w")
ctk.CTkLabel(campo_frame, text="Sobra inicial", font=FONTE_LABEL, text_color="#E8E8E8").grid(row=0, column=3, padx=14, pady=(16, 6), sticky="w")

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

# Botões de Ação (Calcular e Salvar no Banco)
botoes_frame = ctk.CTkFrame(campo_frame, fg_color="transparent")
botoes_frame.grid(row=3, column=0, columnspan=4, padx=12, pady=(12, 16), sticky="ew")
botoes_frame.grid_columnconfigure((0, 1), weight=1, uniform="bcol")

botao_calcular = ctk.CTkButton(
    botoes_frame,
    text="Calcular",
    height=42,
    corner_radius=8,
    font=FONTE_BOTAO,
    fg_color="#E8E8E8",
    hover_color="#FFFFFF",
    text_color="#111111",
)
botao_calcular.grid(row=0, column=0, padx=(0, 6), sticky="ew")

botao_salvar = ctk.CTkButton(
    botoes_frame,
    text="Salvar Dispensação no Banco",
    height=42,
    corner_radius=8,
    font=FONTE_BOTAO,
    fg_color="#2E7D32",
    hover_color="#388E3C",
    text_color="#FFFFFF",
)
botao_salvar.grid(row=0, column=1, padx=(6, 0), sticky="ew")

# ==========================================
# FAIXA DE RESULTADO
# ==========================================
resultado_frame = ctk.CTkFrame(
    janela,
    fg_color=CARTAO,
    border_color=BORDA,
    border_width=1,
    corner_radius=10,
)
resultado_frame.pack(padx=24, pady=(6, 4), fill="x")

lbl_total = ctk.CTkLabel(
    resultado_frame,
    text="Preencha os dados e clique em Calcular.",
    font=FONTE_TOTAL,
    text_color="#FFFFFF",
)
lbl_total.pack(padx=14, pady=12)

# ==========================================
# TABELA DE RESULTADOS
# ==========================================
tabela_frame = ctk.CTkFrame(
    janela,
    fg_color=CARTAO,
    border_color=BORDA,
    border_width=1,
    corner_radius=12,
)
tabela_frame.pack(padx=24, pady=(6, 16), fill="both", expand=True)

tabela = ttk.Treeview(tabela_frame, columns=("Mes", "Caixas", "Qtd", "Sobra"), show="headings", height=8)
tabela.heading("Mes", text="Mês")
tabela.heading("Caixas", text="Caixas")
tabela.heading("Qtd", text="Comprimidos entregues")
tabela.heading("Sobra", text="Sobra para o próximo mês")
tabela.column("Mes", width=90, anchor="center")
tabela.column("Caixas", width=130, anchor="center")
tabela.column("Qtd", width=190, anchor="center")
tabela.column("Sobra", width=190, anchor="center")
tabela.pack(padx=12, pady=12, fill="both", expand=True)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Treeview",
    background="#1A1A1A",
    fieldbackground="#1A1A1A",
    foreground="#FFFFFF",
    rowheight=38,
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

tabela.tag_configure("par", background="#1E1E1E", foreground="#FFFFFF", font=FONTE_TABELA_FORTE)
tabela.tag_configure("impar", background="#2A2A2A", foreground="#FFFFFF", font=FONTE_TABELA_FORTE)


def buscar_paciente_acao():
    global paciente_atual_id
    if not db_ok:
        lbl_status_paciente.configure(text="MySQL está offline. Operando sem banco de dados.", text_color="#E57373")
        return

    termo = entry_nome_paciente.get().strip() or entry_doc_paciente.get().strip()
    if not termo:
        lbl_status_paciente.configure(text="Digite um nome ou documento para buscar.", text_color="#E57373")
        return

    resultados = buscar_paciente(termo)
    if not resultados:
        lbl_status_paciente.configure(text="Paciente não encontrado. Será cadastrado ao salvar a dispensação.", text_color="#FFB74D")
        paciente_atual_id = None
        return

    if len(resultados) == 1:
        p = resultados[0]
        paciente_atual_id = p['id']
        entry_nome_paciente.delete(0, "end")
        entry_nome_paciente.insert(0, p['nome'])
        entry_doc_paciente.delete(0, "end")
        if p['documento']:
            entry_doc_paciente.insert(0, p['documento'])
        elif p['sus']:
            entry_doc_paciente.insert(0, p['sus'])

        # Busca última sobra
        ultima_sobra = obter_ultima_sobra(paciente_atual_id)
        entry_sobra.delete(0, "end")
        entry_sobra.insert(0, str(ultima_sobra))
        lbl_status_paciente.configure(text=f"Paciente encontrado! Sobra anterior recuperada: {ultima_sobra} cps.", text_color="#81C784")
    else:
        # Se houver mais de um, pega o primeiro por simplicidade ou avisa
        p = resultados[0]
        paciente_atual_id = p['id']
        entry_nome_paciente.delete(0, "end")
        entry_nome_paciente.insert(0, p['nome'])
        ultima_sobra = obter_ultima_sobra(paciente_atual_id)
        entry_sobra.delete(0, "end")
        entry_sobra.insert(0, str(ultima_sobra))
        lbl_status_paciente.configure(text=f"Múltiplos pacientes encontrados. Carregado: {p['nome']} (Sobra: {ultima_sobra} cps).", text_color="#FFB74D")


btn_buscar.configure(command=buscar_paciente_acao)


def calcular():
    lbl_erro.configure(text="")
    preencher_por_mes()

    try:
        meses = int(entry_meses.get())
        cp = int(entry_cp.get())
        sobra = int(entry_sobra.get())
    except:
        lbl_erro.configure(text="Digite apenas números inteiros nos campos de cálculo.")
        return None

    try:
        r = calcular_mensal(meses, cp, sobra)
    except ValueError as e:
        lbl_erro.configure(text=str(e))
        return None

    for i in tabela.get_children():
        tabela.delete(i)

    for idx, linha in enumerate(r["linhas"]):
        tag = "par" if idx % 2 == 0 else "impar"
        caixas = linha["caixas"]
        qtd_cps = caixas * CP_POR_CAIXA_EXIBICAO
        caixas_txt = "%d caixa" % caixas if caixas == 1 else "%d caixas" % caixas
        qtd_txt = "%d cps" % qtd_cps
        sobra_txt = "%d cps" % linha["sobra_final"]
        tabela.insert("", "end", values=(linha["mes"], caixas_txt, qtd_txt, sobra_txt), tags=(tag,))

    lbl_total.configure(text="Total de caixas: %d   |   Sobra final: %d cp" % (r["total_caixas"], r["sobra_final"]))
    return r


botao_calcular.configure(command=calcular)


def salvar_dispensacao_banco():
    global paciente_atual_id
    if not db_ok:
        lbl_erro.configure(text="Erro: MySQL está offline. Não é possível salvar.")
        return

    nome = entry_nome_paciente.get().strip()
    doc = entry_doc_paciente.get().strip()

    if not nome:
        lbl_erro.configure(text="Informe o nome do paciente para salvar.")
        return

    # Executa o cálculo para garantir que temos os dados corretos
    res = calcular()
    if not res:
        return

    # Salva ou atualiza paciente
    # Verifica se doc parece CPF ou SUS
    documento = doc if doc else None
    sus = doc if doc else None

    # Salva paciente
    p_id = salvar_ou_atualizar_paciente(nome, documento=documento, sus=sus)
    if not p_id:
        lbl_erro.configure(text="Erro ao salvar paciente no MySQL.")
        return

    paciente_atual_id = p_id

    # Salva dispensação
    sucesso = salvar_dispensacao(
        paciente_id=p_id,
        meses=res["meses"],
        cp_por_dia=int(entry_cp.get()) // DIAS_POR_MES if entry_cp.get().isdigit() else 0,
        sobra_inicial=int(entry_sobra.get()) if entry_sobra.get().isdigit() else 0,
        total_caixas=res["total_caixas"],
        sobra_final=res["sobra_final"]
    )

    if sucesso:
        lbl_status_paciente.configure(text="Dispensação salva com sucesso no MySQL!", text_color="#81C784")
    else:
        lbl_erro.configure(text="Erro ao registrar dispensação no banco de dados.")


botao_salvar.configure(command=salvar_dispensacao_banco)

janela.mainloop()
