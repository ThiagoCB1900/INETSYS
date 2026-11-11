
import tkinter as tk
from tkinter import ttk, messagebox


class MimicIV:

    def __init__(self, root):

        self.root = root

        self.root.title("Mimic IV")
        self.root.geometry("850x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#F5F7FA")

        self.azul = "#3776AB"
        self.amarelo = "#FFD43B"
        self.fundo = "#F5F7FA"

        self.features = [
            "fc", "pas", "pad", "pam", "fr", "spo", "tem",
            "cre", "lac", "leu", "pla", "ph", "uri",
            "hem", "pes", "ida", "alt",
            "sofa", "qsofa", "mews"
        ]

        self.campos = {}

        self.configurar_estilos()
        self.criar_interface()


    def configurar_estilos(self):

        estilo = ttk.Style()

        estilo.theme_use("clam")

        estilo.configure(
            "TEntry",
            padding=5,
            fieldbackground="white",
            bordercolor="#D0D7DE"
        )

        estilo.configure(
            "Azul.TButton",
            font=("Arial", 10, "bold"),
            background=self.azul,
            foreground="white",
            padding=10
        )

        estilo.map(
            "Azul.TButton",
            background=[("active", "#285A87")]
        )

        estilo.configure(
            "Amarelo.TButton",
            font=("Arial", 10, "bold"),
            background=self.amarelo,
            foreground="#202020",
            padding=10
        )

        estilo.map(
            "Amarelo.TButton",
            background=[("active", "#E8BC30")]
        )


    def criar_interface(self):

        # ===== CABEÇALHO =====

        cabecalho = tk.Frame(
            self.root,
            bg=self.azul,
            height=100
        )

        cabecalho.pack(fill="x")
        cabecalho.pack_propagate(False)

        tk.Label(
            cabecalho,
            text="Mimic IV",
            font=("Arial", 25, "bold"),
            fg="white",
            bg=self.azul
        ).pack(pady=(17, 2))

        tk.Label(
            cabecalho,
            text="Entrada de dados clínicos",
            font=("Arial", 10),
            fg="#E5EDF5",
            bg=self.azul
        ).pack()


        # ===== CONTEÚDO =====

        conteudo = tk.Frame(
            self.root,
            bg=self.fundo,
            padx=35,
            pady=20
        )

        conteudo.pack(fill="both", expand=True)

        tk.Label(
            conteudo,
            text="Características do paciente",
            font=("Arial", 15, "bold"),
            fg="#263238",
            bg=self.fundo
        ).pack(anchor="w")

        tk.Label(
            conteudo,
            text="Informe os valores das 20 features abaixo.",
            font=("Arial", 10),
            fg="#687782",
            bg=self.fundo
        ).pack(anchor="w", pady=(3, 15))


        # ===== CAMPOS =====

        formulario = tk.Frame(
            conteudo,
            bg=self.fundo
        )

        formulario.pack(fill="both", expand=True)

        for i, feature in enumerate(self.features):

            coluna = i // 10
            linha = i % 10

            campo = tk.Frame(
                formulario,
                bg=self.fundo
            )

            campo.grid(
                row=linha,
                column=coluna,
                sticky="ew",
                padx=(0, 20) if coluna == 0 else (20, 0),
                pady=2
            )

            tk.Label(
                campo,
                text=feature.upper(),
                font=("Arial", 10, "bold"),
                fg=self.azul,
                bg=self.fundo,
                width=8,
                anchor="w"
            ).pack(side="left")

            entrada = ttk.Entry(
                campo,
                font=("Arial", 10),
                width=22
            )

            entrada.pack(
                side="right",
                fill="x",
                expand=True
            )

            self.campos[feature] = entrada

        formulario.columnconfigure(0, weight=1)
        formulario.columnconfigure(1, weight=1)


        # ===== RODAPÉ =====

        rodape = tk.Frame(
            conteudo,
            bg=self.fundo
        )

        rodape.pack(fill="x", pady=(8, 0))

        ttk.Button(
            rodape,
            text="Limpar",
            style="Amarelo.TButton",
            command=self.limpar
        ).pack(side="left")

        ttk.Button(
            rodape,
            text="Confirmar",
            style="Azul.TButton",
            command=self.confirmar
        ).pack(side="right")


    def limpar(self):

        for entrada in self.campos.values():
            entrada.delete(0, tk.END)


    def confirmar(self):

        dados = {}

        try:

            for feature, entrada in self.campos.items():

                valor = entrada.get().strip().replace(",", ".")

                if not valor:
                    raise ValueError(
                        f"O campo {feature.upper()} está vazio."
                    )

                dados[feature] = float(valor)

        except ValueError as erro:

            messagebox.showerror(
                "Erro de entrada",
                str(erro)
            )

            return

        messagebox.showinfo(
            "Mimic IV",
            "Dados preenchidos com sucesso!"
        )

        print(dados)


# ===== EXECUÇÃO =====

if __name__ == "__main__":

    root = tk.Tk()

    app = MimicIV(root)

    root.mainloop()
