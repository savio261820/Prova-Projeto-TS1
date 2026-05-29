import tkinter as tk
from tkinter import ttk, messagebox
import database.schema
from database.connection import conectar

BG_DARK      = "#0f1117"
BG_PANEL     = "#1a1d27"
BG_CARD      = "#21253a"
BG_INPUT     = "#161926"
ACCENT       = "#4f8ef7"
ACCENT_HOVER = "#3a72d4"
ACCENT_SOFT  = "#1e2d4d"
SUCCESS      = "#2ecc71"
DANGER       = "#e74c3c"
WARNING      = "#f39c12"
TEXT_PRIMARY = "#e8ecf4"
TEXT_MUTED   = "#6b7592"
TEXT_LABEL   = "#a0aac0"
BORDER       = "#2a2f45"
SCROLLBAR    = "#2a2f45"

FONT_TITLE   = ("Segoe UI", 20, "bold")
FONT_HEADING = ("Segoe UI", 13, "bold")
FONT_BODY    = ("Segoe UI", 11)
FONT_SMALL   = ("Segoe UI", 9)
FONT_MONO    = ("Consolas", 10)
FONT_BTN     = ("Segoe UI", 10, "bold")

def apply_entry_style(widget):
	widget.config(
		bg=BG_INPUT, fg=TEXT_PRIMARY,
		insertbackground=ACCENT,
		relief="flat", bd=0,
		font=FONT_BODY,
		highlightthickness=1,
		highlightbackground=BORDER,
		highlightcolor=ACCENT,
	)

def apply_button_style(btn, color=ACCENT, hover=ACCENT_HOVER, fg=TEXT_PRIMARY):
	btn.config(
		bg=color, fg=fg,
		relief="flat", bd=0,
		font=FONT_BTN,
		cursor="hand2",
		activebackground=hover,
		activeforeground=fg,
		padx=16, pady=8,
	)
	btn.bind("<Enter>", lambda e: btn.config(bg=hover))
	btn.bind("<Leave>", lambda e: btn.config(bg=color))

def apply_danger_button(btn):
	apply_button_style(btn, color=DANGER, hover="#c0392b")

def apply_success_button(btn):
	apply_button_style(btn, color=SUCCESS, hover="#27ae60")

def card_frame(parent, **kwargs):
	f = tk.Frame(parent, bg=BG_CARD, **kwargs)
	return f

def section_label(parent, text):
	lbl = tk.Label(
		parent, text=text,
		bg=BG_PANEL, fg=ACCENT,
		font=FONT_HEADING,
	)
	return lbl

def field_label(parent, text):
	return tk.Label(
		parent, text=text,
		bg=BG_CARD, fg=TEXT_LABEL,
		font=FONT_SMALL, anchor="w",
	)

def separator(parent):
	return tk.Frame(parent, bg=BORDER, height=1)

class LabeledEntry(tk.Frame):
	def __init__(self, parent, label, show=None, **kwargs):
		super().__init__(parent, bg=BG_CARD, **kwargs)
		tk.Label(self, text=label, bg=BG_CARD, fg=TEXT_LABEL,
				 font=FONT_SMALL, anchor="w").pack(fill="x")
		self.entry = tk.Entry(self, show=show)
		apply_entry_style(self.entry)
		self.entry.pack(fill="x", ipady=6)

	def get(self):
		return self.entry.get().strip()

	def set(self, value):
		self.entry.delete(0, tk.END)
		self.entry.insert(0, value)

	def clear(self):
		self.entry.delete(0, tk.END)

class LabeledCombo(tk.Frame):
	def __init__(self, parent, label, values, **kwargs):
		super().__init__(parent, bg=BG_CARD, **kwargs)
		tk.Label(self, text=label, bg=BG_CARD, fg=TEXT_LABEL,
				 font=FONT_SMALL, anchor="w").pack(fill="x")
		style = ttk.Style()
		style.theme_use("clam")
		style.configure("Dark.TCombobox",
			fieldbackground=BG_INPUT,
			background=BG_INPUT,
			foreground=TEXT_PRIMARY,
			selectbackground=ACCENT_SOFT,
			selectforeground=TEXT_PRIMARY,
			bordercolor=BORDER,
			arrowcolor=ACCENT,
		)
		self.var = tk.StringVar()
		self.combo = ttk.Combobox(
			self, textvariable=self.var,
			values=values, state="readonly",
			style="Dark.TCombobox", font=FONT_BODY,
		)
		self.combo.pack(fill="x", ipady=4)

	def get(self):
		return self.var.get()

	def set(self, value):
		self.var.set(value)

	def current(self, idx=None):
		if idx is not None:
			self.combo.current(idx)
		else:
			return self.combo.current()


class StyledTable(tk.Frame):
	def __init__(self, parent, columns, **kwargs):
		super().__init__(parent, bg=BG_PANEL, **kwargs)
		style = ttk.Style()
		style.configure("Dark.Treeview",
			background=BG_CARD,
			foreground=TEXT_PRIMARY,
			fieldbackground=BG_CARD,
			bordercolor=BORDER,
			rowheight=32,
			font=FONT_BODY,
		)
		style.configure("Dark.Treeview.Heading",
			background=BG_PANEL,
			foreground=ACCENT,
			font=("Segoe UI", 10, "bold"),
			bordercolor=BORDER,
			relief="flat",
		)
		style.map("Dark.Treeview",
			background=[("selected", ACCENT_SOFT)],
			foreground=[("selected", TEXT_PRIMARY)],
		)

		self.tree = ttk.Treeview(
			self, columns=columns, show="headings",
			style="Dark.Treeview", selectmode="browse",
		)
		for col in columns:
			self.tree.heading(col, text=col)
			self.tree.column(col, anchor="center", minwidth=80)

		scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
		self.tree.configure(yscrollcommand=scroll_y.set)
		scroll_x = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
		self.tree.configure(xscrollcommand=scroll_x.set)

		self.tree.grid(row=0, column=0, sticky="nsew")
		scroll_y.grid(row=0, column=1, sticky="ns")
		scroll_x.grid(row=1, column=0, sticky="ew")
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

	def clear(self):
		for row in self.tree.get_children():
			self.tree.delete(row)

	def insert(self, values, tag=None):
		kw = {"values": values}
		if tag:
			kw["tags"] = (tag,)
		self.tree.insert("", "end", **kw)

	def selected_values(self):
		sel = self.tree.selection()
		if sel:
			return self.tree.item(sel[0])["values"]
		return None

class Toast:
	def __init__(self, root):
		self.root = root
		self._label = None

	def show(self, msg, kind="success"):
		color = SUCCESS if kind == "success" else DANGER if kind == "error" else WARNING
		if self._label:
			self._label.destroy()
		self._label = tk.Label(
			self.root, text=f"  {msg}  ",
			bg=color, fg="#ffffff",
			font=("Segoe UI", 10, "bold"),
			padx=12, pady=6,
			relief="flat",
		)
		self._label.place(relx=0.5, rely=0.97, anchor="s")
		self.root.after(3000, self._hide)

	def _hide(self):
		if self._label:
			self._label.destroy()
			self._label = None


class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("CRUD TRABALHO UFU")
		self.geometry("1100x700")
		self.minsize(900, 600)
		self.configure(bg=BG_DARK)
		self.resizable(True, True)
		self.toast = Toast(self)
		self._build_layout()
		self._show_frame("listar")

	def _build_layout(self):
		self.sidebar = tk.Frame(self, bg=BG_PANEL, width=210)
		self.sidebar.pack(side="left", fill="y")
		self.sidebar.pack_propagate(False)

		logo_frame = tk.Frame(self.sidebar, bg=BG_PANEL, pady=24)
		logo_frame.pack(fill="x")
		tk.Label(
			logo_frame, text="🛡", bg=BG_PANEL, fg=ACCENT,
			font=("Segoe UI", 28),
		).pack()
		tk.Label(
			logo_frame, text="Asset Manager",
			bg=BG_PANEL, fg=TEXT_PRIMARY,
			font=("Segoe UI", 12, "bold"),
		).pack()
		tk.Label(
			logo_frame, text="Security Suite",
			bg=BG_PANEL, fg=TEXT_MUTED,
			font=FONT_SMALL,
		).pack()

		separator(self.sidebar).pack(fill="x", padx=16, pady=8)

		nav_items = [
			("📋  Listar Ativos",           "listar"),
			("➕  Cadastrar Ativo",          "cadastrar"),
			("✏️   Editar Ativo",             "editar"),
			("🗑️   Deletar Ativo",            "deletar"),
			("🔍  Buscar Ativo",             "buscar"),
			("🐛  Vulnerabilidades",         "vuln_menu"),
		]
		self._nav_buttons = {}
		for label, key in nav_items:
			btn = tk.Button(
				self.sidebar, text=label, anchor="w",
				bg=BG_PANEL, fg=TEXT_LABEL,
				font=("Segoe UI", 10),
				relief="flat", bd=0,
				padx=20, pady=10,
				cursor="hand2",
				activebackground=ACCENT_SOFT,
				activeforeground=TEXT_PRIMARY,
			)
			btn.config(command=lambda k=key, b=btn: self._nav_click(k, b))
			btn.pack(fill="x")
			self._nav_buttons[key] = btn

		self.main = tk.Frame(self, bg=BG_DARK)
		self.main.pack(side="left", fill="both", expand=True, padx=0, pady=0)

		self.frames = {}
		for FrameClass, key in [
			(TelaListar,           "listar"),
			(TelaCadastrar,        "cadastrar"),
			(TelaEditar,           "editar"),
			(TelaDeletar,          "deletar"),
			(TelaBuscar,           "buscar"),
			(TelaVulnMenu,         "vuln_menu"),
			(TelaCadastrarVuln,    "cadastrar_vuln"),
			(TelaListarVuln,       "listar_vuln"),
		]:
			frame = FrameClass(self.main, self)
			frame.place(relx=0, rely=0, relwidth=1, relheight=1)
			self.frames[key] = frame

	def _nav_click(self, key, btn):
		for b in self._nav_buttons.values():
			b.config(bg=BG_PANEL, fg=TEXT_LABEL)
		btn.config(bg=ACCENT_SOFT, fg=TEXT_PRIMARY)
		self._show_frame(key)

	def _show_frame(self, key):
		frame = self.frames[key]
		frame.tkraise()
		if hasattr(frame, "on_show"):
			frame.on_show()

	def navigate(self, key):
		self._show_frame(key)
		if key in self._nav_buttons:
			for b in self._nav_buttons.values():
				b.config(bg=BG_PANEL, fg=TEXT_LABEL)
			self._nav_buttons[key].config(bg=ACCENT_SOFT, fg=TEXT_PRIMARY)


class BasePage(tk.Frame):
	def __init__(self, parent, app):
		super().__init__(parent, bg=BG_DARK)
		self.app = app

	def page_header(self, icon, title, subtitle=""):
		hdr = tk.Frame(self, bg=BG_DARK, pady=20, padx=30)
		hdr.pack(fill="x")
		top = tk.Frame(hdr, bg=BG_DARK)
		top.pack(fill="x")
		tk.Label(top, text=icon, bg=BG_DARK, fg=ACCENT, font=("Segoe UI", 22)).pack(side="left")
		txt = tk.Frame(top, bg=BG_DARK)
		txt.pack(side="left", padx=10)
		tk.Label(txt, text=title, bg=BG_DARK, fg=TEXT_PRIMARY, font=FONT_TITLE).pack(anchor="w")
		if subtitle:
			tk.Label(txt, text=subtitle, bg=BG_DARK, fg=TEXT_MUTED, font=FONT_SMALL).pack(anchor="w")
		separator(self).pack(fill="x", padx=30)

	def content(self):
		c = tk.Frame(self, bg=BG_DARK, padx=30, pady=20)
		c.pack(fill="both", expand=True)
		return c

class TelaListar(BasePage):
	def __init__(self, parent, app):
		super().__init__(parent, app)
		self.page_header("📋", "Listar Ativos", "Todos os ativos cadastrados no sistema")
		c = self.content()

		btn_frame = tk.Frame(c, bg=BG_DARK)
		btn_frame.pack(fill="x", pady=(0, 12))
		self.btn_refresh = tk.Button(btn_frame, text="↺  Atualizar", command=self.carregar)
		apply_button_style(self.btn_refresh)
		self.btn_refresh.pack(side="left")

		self.table = StyledTable(c, ["ID", "Nome", "Tipo", "Local", "Último Usuário"])
		self.table.pack(fill="both", expand=True)

		self.count_lbl = tk.Label(c, text="", bg=BG_DARK, fg=TEXT_MUTED, font=FONT_SMALL)
		self.count_lbl.pack(anchor="e", pady=4)

	def on_show(self):
		self.carregar()

	def carregar(self):
		self.table.clear()
		conn = conectar()
		rows = conn.execute("SELECT id, nome, tipo, local, ultimo_usuario FROM ativos").fetchall()
		conn.close()
		for row in rows:
			self.table.insert(row)
		self.count_lbl.config(text=f"{len(rows)} ativo(s) encontrado(s)")


TIPOS = ["Servidores", "Workstations", "Aparelhos", "Impressoras"]

class TelaCadastrar(BasePage):
	def __init__(self, parent, app):
		super().__init__(parent, app)
		self.page_header("➕", "Cadastrar Ativo", "Adicione um novo ativo ao sistema")
		c = self.content()

		form = card_frame(c, padx=24, pady=24)
		form.pack(fill="x", ipadx=0)

		self.f_usuario = LabeledEntry(form, "Seu nome (usuário)")
		self.f_usuario.pack(fill="x", pady=6)

		self.f_nome = LabeledEntry(form, "Nome do ativo")
		self.f_nome.pack(fill="x", pady=6)

		self.f_tipo = LabeledCombo(form, "Tipo", TIPOS)
		self.f_tipo.pack(fill="x", pady=6)
		self.f_tipo.current(0)

		self.f_local = LabeledEntry(form, "Local")
		self.f_local.pack(fill="x", pady=6)

		btn_row = tk.Frame(form, bg=BG_CARD)
		btn_row.pack(fill="x", pady=(16, 0))

		btn_salvar = tk.Button(btn_row, text="✔  Salvar Ativo", command=self.salvar)
		apply_success_button(btn_salvar)
		btn_salvar.pack(side="left")

		btn_limpar = tk.Button(btn_row, text="✖  Limpar", command=self.limpar)
		apply_button_style(btn_limpar, color="#2a2f45", hover="#353a55")
		btn_limpar.pack(side="left", padx=8)

	def salvar(self):
		usuario = self.f_usuario.get()
		nome    = self.f_nome.get()
		tipo    = self.f_tipo.get()
		local   = self.f_local.get()
		if not all([usuario, nome, tipo, local]):
			self.app.toast.show("Preencha todos os campos!", "error")
			return
		conn = conectar()
		conn.execute(
			"INSERT INTO ativos (nome, tipo, local, ultimo_usuario) VALUES (?, ?, ?, ?)",
			(nome, tipo, local, usuario)
		)
		conn.commit()
		conn.close()
		self.app.toast.show(f"Ativo '{nome}' cadastrado com sucesso!")
		self.limpar()

	def limpar(self):
		self.f_usuario.clear()
		self.f_nome.clear()
		self.f_local.clear()
		self.f_tipo.current(0)


class TelaEditar(BasePage):
	def __init__(self, parent, app):
		super().__init__(parent, app)
		self.page_header("✏️", "Editar Ativo", "Modifique os dados de um ativo existente")
		c = self.content()

		# Seleção
		sel_frame = card_frame(c, padx=24, pady=16)
		sel_frame.pack(fill="x")
		field_label(sel_frame, "Selecione o ativo:").pack(anchor="w")
		row = tk.Frame(sel_frame, bg=BG_CARD)
		row.pack(fill="x", pady=4)
		self.combo_ativo = ttk.Combobox(row, state="readonly", font=FONT_BODY)
		self.combo_ativo.pack(side="left", fill="x", expand=True, ipady=4)
		btn_sel = tk.Button(row, text="  Carregar  ", command=self.carregar_ativo)
		apply_button_style(btn_sel)
		btn_sel.pack(side="left", padx=(8, 0))

		separator(c).pack(fill="x", pady=12)

		# Formulário
		self.form = card_frame(c, padx=24, pady=24)
		self.form.pack(fill="x")

		self.f_nome  = LabeledEntry(self.form, "Nome do ativo")
		self.f_nome.pack(fill="x", pady=6)

		self.f_tipo  = LabeledCombo(self.form, "Tipo", TIPOS)
		self.f_tipo.pack(fill="x", pady=6)

		self.f_local = LabeledEntry(self.form, "Local")
		self.f_local.pack(fill="x", pady=6)

		self.f_usuario = LabeledEntry(self.form, "Quem realizou esta alteração?")
		self.f_usuario.pack(fill="x", pady=6)

		btn_row = tk.Frame(self.form, bg=BG_CARD)
		btn_row.pack(fill="x", pady=(16, 0))
		btn_save = tk.Button(btn_row, text="✔  Salvar Alterações", command=self.salvar)
		apply_success_button(btn_save)
		btn_save.pack(side="left")

		self._ativo_id = None
		self._ativos = []

	def on_show(self):
		self._carregar_lista()

	def _carregar_lista(self):
		conn = conectar()
		self._ativos = conn.execute("SELECT id, nome FROM ativos ORDER BY id").fetchall()
		conn.close()
		self.combo_ativo["values"] = [f"{a[0]} - {a[1]}" for a in self._ativos]
		if self._ativos:
			self.combo_ativo.current(0)

	def carregar_ativo(self):
		idx = self.combo_ativo.current()
		if idx < 0:
			self.app.toast.show("Selecione um ativo!", "error")
			return
		ativo_id = self._ativos[idx][0]
		conn = conectar()
		row = conn.execute(
			"SELECT id, nome, tipo, local, ultimo_usuario FROM ativos WHERE id = ?", (ativo_id,)
		).fetchone()
		conn.close()
		if not row:
			self.app.toast.show("Ativo não encontrado!", "error")
			return
		self._ativo_id = row[0]
		self.f_nome.set(row[1])
		self.f_tipo.set(row[2])
		self.f_local.set(row[3])
		self.f_usuario.clear()

	def salvar(self):
		if not self._ativo_id:
			self.app.toast.show("Carregue um ativo primeiro!", "error")
			return
		nome    = self.f_nome.get()    or None
		tipo    = self.f_tipo.get()    or None
		local   = self.f_local.get()   or None
		usuario = self.f_usuario.get()
		if not usuario:
			self.app.toast.show("Informe quem realizou a alteração!", "error")
			return
		conn = conectar()
		old = conn.execute(
			"SELECT nome, tipo, local FROM ativos WHERE id = ?", (self._ativo_id,)
		).fetchone()
		conn.execute(
			"UPDATE ativos SET nome=?, tipo=?, local=?, ultimo_usuario=? WHERE id=?",
			(nome or old[0], tipo or old[1], local or old[2], usuario, self._ativo_id)
		)
		conn.commit()
		conn.close()
		self.app.toast.show("Ativo atualizado com sucesso!")
		self._carregar_lista()


class TelaDeletar(BasePage):
	def __init__(self, parent, app):
		super().__init__(parent, app)
		self.page_header("🗑️", "Deletar Ativo", "Remova permanentemente um ativo do sistema")
		c = self.content()

		sel_frame = card_frame(c, padx=24, pady=16)
		sel_frame.pack(fill="x")
		field_label(sel_frame, "Selecione o ativo para deletar:").pack(anchor="w")
		self.combo_ativo = ttk.Combobox(sel_frame, state="readonly", font=FONT_BODY)
		self.combo_ativo.pack(fill="x", ipady=4, pady=4)

		# Prévia
		self.preview = card_frame(c, padx=24, pady=16)
		self.preview.pack(fill="x", pady=12)
		self.preview_lbl = tk.Label(
			self.preview, text="Selecione um ativo para ver detalhes",
			bg=BG_CARD, fg=TEXT_MUTED, font=FONT_BODY, justify="left",
		)
		self.preview_lbl.pack(anchor="w")

		btn_del = tk.Button(c, text="🗑️  Deletar Ativo Selecionado", command=self.deletar)
		apply_danger_button(btn_del)
		btn_del.pack(anchor="w")

		self.combo_ativo.bind("<<ComboboxSelected>>", self._preview)
		self._ativos = []

	def on_show(self):
		conn = conectar()
		self._ativos = conn.execute("SELECT id, nome, tipo, local FROM ativos ORDER BY id").fetchall()
		conn.close()
		self.combo_ativo["values"] = [f"{a[0]} - {a[1]}" for a in self._ativos]
		self.preview_lbl.config(text="Selecione um ativo para ver detalhes")
		if self._ativos:
			self.combo_ativo.current(0)
			self._preview()

	def _preview(self, event=None):
		idx = self.combo_ativo.current()
		if idx < 0:
			return
		a = self._ativos[idx]
		self.preview_lbl.config(
			text=f"ID: {a[0]}   •   Nome: {a[1]}\nTipo: {a[2]}   •   Local: {a[3]}",
			fg=TEXT_PRIMARY,
		)

	def deletar(self):
		idx = self.combo_ativo.current()
		if idx < 0:
			self.app.toast.show("Selecione um ativo!", "error")
			return
		a = self._ativos[idx]
		confirm = messagebox.askyesno(
			"Confirmar exclusão",
			f'Deseja deletar o ativo:\n\n"{a[1]}" (ID {a[0]})\n\nTodas as vulnerabilidades associadas também serão removidas.',
			icon="warning",
		)
		if not confirm:
			return
		conn = conectar()
		conn.execute("PRAGMA foreign_keys = ON")
		conn.execute("DELETE FROM ativos WHERE id = ?", (a[0],))
		conn.commit()
		conn.close()
		self.app.toast.show(f"Ativo '{a[1]}' deletado com sucesso!")
		self.on_show()


class TelaBuscar(BasePage):
	def __init__(self, parent, app):
		super().__init__(parent, app)
		self.page_header("🔍", "Buscar Ativos", "Pesquise por ID, nome, usuário ou local")
		c = self.content()

		search_card = card_frame(c, padx=24, pady=16)
		search_card.pack(fill="x")

		row = tk.Frame(search_card, bg=BG_CARD)
		row.pack(fill="x", pady=4)

		self.f_search = tk.Entry(row)
		apply_entry_style(self.f_search)
		self.f_search.pack(side="left", fill="x", expand=True, ipady=7)
		self.f_search.bind("<Return>", lambda e: self.buscar())

		self.combo_tipo = ttk.Combobox(
			row, values=["ID", "Nome", "Usuário", "Local"],
			state="readonly", font=FONT_BODY, width=10,
		)
		self.combo_tipo.current(0)
		self.combo_tipo.pack(side="left", padx=8, ipady=4)

		btn_buscar = tk.Button(row, text="  Buscar  ", command=self.buscar)
		apply_button_style(btn_buscar)
		btn_buscar.pack(side="left")

		self.table = StyledTable(c, ["ID", "Nome", "Tipo", "Local", "Último Usuário"])
		self.table.pack(fill="both", expand=True, pady=12)

		self.count_lbl = tk.Label(c, text="", bg=BG_DARK, fg=TEXT_MUTED, font=FONT_SMALL)
		self.count_lbl.pack(anchor="e")

	def buscar(self):
		termo = self.f_search.get().strip()
		campo = self.combo_tipo.get()
		if not termo:
			self.app.toast.show("Digite algo para buscar!", "error")
			return

		col_map = {"ID": "id", "Nome": "nome", "Usuário": "ultimo_usuario", "Local": "local"}
		col = col_map.get(campo, "nome")

		conn = conectar()
		if campo == "ID":
			if not termo.isdigit():
				self.app.toast.show("ID deve ser numérico!", "error")
				conn.close()
				return
			rows = conn.execute(
				f"SELECT id, nome, tipo, local, ultimo_usuario FROM ativos WHERE id = ?", (int(termo),)
			).fetchall()
		else:
			rows = conn.execute(
				f"SELECT id, nome, tipo, local, ultimo_usuario FROM ativos WHERE LOWER({col}) LIKE LOWER(?)",
				(f"%{termo}%",)
			).fetchall()
		conn.close()

		self.table.clear()
		for row in rows:
			self.table.insert(row)
		self.count_lbl.config(text=f"{len(rows)} resultado(s)")
		if not rows:
			self.app.toast.show("Nenhum ativo encontrado.", "warning")


class TelaVulnMenu(BasePage):
	def __init__(self, parent, app):
		super().__init__(parent, app)
		self.page_header("🐛", "Vulnerabilidades", "Gerencie vulnerabilidades dos ativos")
		c = self.content()

		inner = tk.Frame(c, bg=BG_DARK)
		inner.pack(expand=True, fill="both")

		for icon, label, key in [
			("➕", "Cadastrar Vulnerabilidade", "cadastrar_vuln"),
			("📋", "Listar Vulnerabilidades",   "listar_vuln"),
		]:
			card = card_frame(inner, padx=32, pady=32)
			card.pack(fill="x", pady=10)
			row = tk.Frame(card, bg=BG_CARD)
			row.pack(fill="x")
			tk.Label(row, text=icon, bg=BG_CARD, fg=ACCENT, font=("Segoe UI", 28)).pack(side="left")
			txt = tk.Frame(row, bg=BG_CARD)
			txt.pack(side="left", padx=16)
			tk.Label(txt, text=label, bg=BG_CARD, fg=TEXT_PRIMARY, font=FONT_HEADING).pack(anchor="w")
			btn = tk.Button(card, text=f"  Acessar →  ", command=lambda k=key: app.navigate(k))
			apply_button_style(btn)
			btn.pack(anchor="w", pady=(12, 0))


SEVERIDADES = ["Baixa", "Média", "Alta", "Crítica"]
STATUS_LISTA = ["Aberta", "Em tratamento", "Corrigida", "Aceita como risco"]


class TelaCadastrarVuln(BasePage):
	def __init__(self, parent, app):
		super().__init__(parent, app)
		self.page_header("➕", "Cadastrar Vulnerabilidade", "Registre uma vulnerabilidade em um ativo")
		c = self.content()

		form = card_frame(c, padx=24, pady=24)
		form.pack(fill="x")

		field_label(form, "Selecione o ativo:").pack(anchor="w")
		self.combo_ativo = ttk.Combobox(form, state="readonly", font=FONT_BODY)
		self.combo_ativo.pack(fill="x", ipady=4, pady=4)

		self.f_desc = LabeledEntry(form, "Descrição da vulnerabilidade")
		self.f_desc.pack(fill="x", pady=6)

		self.f_cat = LabeledEntry(form, "Categoria / Tipo")
		self.f_cat.pack(fill="x", pady=6)

		col2 = tk.Frame(form, bg=BG_CARD)
		col2.pack(fill="x", pady=6)
		self.f_sev = LabeledCombo(col2, "Severidade", SEVERIDADES)
		self.f_sev.pack(side="left", fill="x", expand=True, padx=(0, 8))
		self.f_sev.current(0)
		self.f_status = LabeledCombo(col2, "Status", STATUS_LISTA)
		self.f_status.pack(side="left", fill="x", expand=True)
		self.f_status.current(0)

		self.f_usuario = LabeledEntry(form, "Seu nome")
		self.f_usuario.pack(fill="x", pady=6)

		btn_row = tk.Frame(form, bg=BG_CARD)
		btn_row.pack(fill="x", pady=(16, 0))
		btn_save = tk.Button(btn_row, text="✔  Salvar Vulnerabilidade", command=self.salvar)
		apply_success_button(btn_save)
		btn_save.pack(side="left")

		self._ativos = []

	def on_show(self):
		conn = conectar()
		self._ativos = conn.execute("SELECT id, nome FROM ativos ORDER BY id").fetchall()
		conn.close()
		self.combo_ativo["values"] = [f"{a[0]} - {a[1]}" for a in self._ativos]
		if self._ativos:
			self.combo_ativo.current(0)

	def salvar(self):
		idx = self.combo_ativo.current()
		if idx < 0 or not self._ativos:
			self.app.toast.show("Selecione um ativo!", "error")
			return
		ativo_id = self._ativos[idx][0]
		desc     = self.f_desc.get()
		cat      = self.f_cat.get()
		sev      = self.f_sev.get()
		status   = self.f_status.get()
		usuario  = self.f_usuario.get()
		if not all([desc, cat, sev, status, usuario]):
			self.app.toast.show("Preencha todos os campos!", "error")
			return
		conn = conectar()
		conn.execute(
			"INSERT INTO vulnerabilidades (ativo_id, descricao, categoria, severidade, status, usuario) VALUES (?, ?, ?, ?, ?, ?)",
			(ativo_id, desc, cat, sev, status, usuario)
		)
		conn.commit()
		conn.close()
		self.app.toast.show("Vulnerabilidade cadastrada com sucesso!")
		self.f_desc.clear()
		self.f_cat.clear()
		self.f_usuario.clear()
		self.f_sev.current(0)
		self.f_status.current(0)

class TelaListarVuln(BasePage):
	def __init__(self, parent, app):
		super().__init__(parent, app)
		self.page_header("📋", "Listar Vulnerabilidades", "Consulte as vulnerabilidades de um ativo")
		c = self.content()

		sel_frame = card_frame(c, padx=24, pady=16)
		sel_frame.pack(fill="x")
		field_label(sel_frame, "Selecione o ativo:").pack(anchor="w")
		row = tk.Frame(sel_frame, bg=BG_CARD)
		row.pack(fill="x", pady=4)
		self.combo_ativo = ttk.Combobox(row, state="readonly", font=FONT_BODY)
		self.combo_ativo.pack(side="left", fill="x", expand=True, ipady=4)
		btn_ver = tk.Button(row, text="  Ver  ", command=self.carregar)
		apply_button_style(btn_ver)
		btn_ver.pack(side="left", padx=(8, 0))

		self.table = StyledTable(c, ["Descrição", "Categoria", "Severidade", "Status", "Usuário"])
		self.table.pack(fill="both", expand=True, pady=12)

		# Tag de cores por severidade
		self.table.tree.tag_configure("Baixa",    foreground="#2ecc71")
		self.table.tree.tag_configure("Média",    foreground="#f39c12")
		self.table.tree.tag_configure("Alta",     foreground="#e67e22")
		self.table.tree.tag_configure("Crítica",  foreground="#e74c3c")

		self.count_lbl = tk.Label(c, text="", bg=BG_DARK, fg=TEXT_MUTED, font=FONT_SMALL)
		self.count_lbl.pack(anchor="e")

		self._ativos = []

	def on_show(self):
		conn = conectar()
		self._ativos = conn.execute("SELECT id, nome FROM ativos ORDER BY id").fetchall()
		conn.close()
		self.combo_ativo["values"] = [f"{a[0]} - {a[1]}" for a in self._ativos]
		if self._ativos:
			self.combo_ativo.current(0)

	def carregar(self):
		idx = self.combo_ativo.current()
		if idx < 0:
			self.app.toast.show("Selecione um ativo!", "error")
			return
		ativo_id = self._ativos[idx][0]
		conn = conectar()
		rows = conn.execute(
			"SELECT descricao, categoria, severidade, status, usuario FROM vulnerabilidades WHERE ativo_id = ?",
			(ativo_id,)
		).fetchall()
		conn.close()
		self.table.clear()
		for row in rows:
			sev_tag = row[2]
			self.table.insert(row, tag=sev_tag)
		self.count_lbl.config(text=f"{len(rows)} vulnerabilidade(s)")
		if not rows:
			self.app.toast.show("Nenhuma vulnerabilidade encontrada.", "warning")


def main():
	app = App()
	app.mainloop()


if __name__ == "__main__":
	main()