# IMPORTS
from tkinter import *
from tkinter import Toplevel as NovaJanela

# Variáveis Globais
janela = Tk()
fontes = ("Times New Roman",)
cores = ("MediumPurple4", "white", "purple4", "navy",
         "blue4", "midnight blue", "gray12", "green",
         "darkorange1")


# CLASSE DE TELA
class TelaInicial:
    def telaInicio(self):
        # Iniciando variável--------------------------------------------------------------------------------------------
        self.janela = janela
        # Imagem de tela------------------------------------------------------------------------------------------------
        self.fundoJanela = PhotoImage(file="rise-of-firstborn-ios-android-update-cover.gif")
        Label(self.janela, image=self.fundoJanela).pack()
        # Configurando tela---------------------------------------------------------------------------------------------
        self.janela.title("Rise of Firstborn - Simulador")
        self.janela.geometry("305x305")
        self.janela.resizable(False, False)  # se permite o redimensionar, horizontal e vertical
        # Criando botões------------------------------------------------------------------------------------------------
        # Botão Defesa--------------------------------------------------------------------------------------------------
        self.guarda = Button(self.janela, text="DEFESAS", bd=4, bg=cores[4], fg=cores[1],
                             font=(fontes[0], 8, "bold"), command=lambda: self.telaDefesa())
        self.guarda.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.1)
        # INICIAR TELA--------------------------------------------------------------------------------------------------
        self.janela.mainloop()

    def telaDefesa(self):
        # INICIANDO TELA================================================================================================
        self.telaH = NovaJanela()
        self.frameDeTela(fechar=True)
        # IMAGEM DE TELA================================================================================================
        self.fundoJanelaTelaH = PhotoImage(file="guarda.gif")
        self.imagem = Label(self.telaH, image=self.fundoJanelaTelaH)
        self.imagem.place(x=0, y=0, width=269, height=516)
        # CONFIGURANDO TELA=============================================================================================
        self.telaH.title("DEFESAS")
        self.telaH.geometry("989x516")
        self.telaH.resizable(False, False)
        # CRIANDO BOTÕES================================================================================================
        # BOTÃO DE HERÓI================================================================================================
        self.guarda = Button(self.telaH, text="GUARDA", bd=4, bg=cores[4], fg=cores[1],
                             font=(fontes[0], 8, "bold"), command=lambda: self.CHAMADA(1))
        self.guarda.place(relx=0.0350, rely=0.1, relwidth=0.2, relheight=0.0550)
        # BOTÃO DE CASTELO==============================================================================================
        self.castelo = Button(self.telaH, text="CASTELO", bd=4, bg=cores[4], fg=cores[1],
                              font=(fontes[0], 8, "bold"), command=lambda: self.CHAMADA(2))
        self.castelo.place(relx=0.0350, rely=0.2, relwidth=0.2, relheight=0.0550)

    def frameDeTela(self, fechar=False):
        # FRAME DE TELA=================================================================================================
        self.frameDefesa = Frame(self.telaH, bg="gray12", highlightbackground="gray10", highlightthickness=3)
        self.frameDefesa.place(rely=0, relx=0.269, relheight=1, relwidth=1)
        self.frameDefesa.bind("<Button-1>", self.rastreiar)
        self.rise = PhotoImage(file="riseOfFis.gif")
        self.imagem2 = Label(self.frameDefesa, image=self.rise)
        self.imagem2.place(rely=0, relx=0.612, relwidth=0.1, relheight=1)
        if fechar:
            # FECHAR====================================================================================================
            self.btVoltar = Button(self.frameDefesa, text="FECHAR", bd=4, bg=cores[4], fg=cores[1],
                                   font=(fontes[0], 8, "bold"), command=lambda: self.telaH.destroy())
            self.btVoltar.place(relx=0.26, rely=0.9, relheight=0.0550, relwidth=0.1)

    def CHAMADA(self, função):
        """ID DE FUNÇÕES: /1 - Guarda/ 2 - Castelo/ 3 - Titã/ 4 - Tropas"""
        self.frameDefesa.destroy()
        self.frameDeTela()
        if função == 1:
            self.label_entryGUARDA()
        elif função == 2:
            self.label_entryCASTELO()

    def fechar_Salvar_Voltar(self, func, btSalvar=True, btVoltar=True):
        """Para o botão de voltar deve ser especificado para qual função voltar.
        0 - volta para tela inicial de configuração de defesa
        2 - volta para tela de escolha de categoria de tropa da opção CASTELO
        4 - volta para tela de escolha de categoria de tropa da opção TROPAS"""

        # FUNÇÕES=======================================================================================================
        def VOLTAR():
            self.frameDefesa.destroy()
            self.frameDeTela()
            if func == 0:
                return self.frameDeTela(fechar=True)
            elif func == 2:
                return self.label_entryCASTELO()

        def SALVAR():
            self.frameDefesa.destroy()
            self.frameDeTela()
            # ------FRAME DE SALVO------- #
            # ------LABEL DE SALVO------- #
            self.lbSalvo = Label(self.frameDefesa, text="SALVO COM SUCESSO!", fg=cores[7], bg=cores[6])
            # ------BOTÕES------- #
            self.btSalvo = Button(self.frameDefesa, text="OK", bd=4, bg=cores[4], fg=cores[1],
                                  font=(fontes[0], 8, "bold"), command=lambda: self.frameDeTela(fechar=True))
            self.btfechatTela = Button(self.frameDefesa, text="FECHAR", bd=4, bg=cores[4], fg=cores[1],
                                       font=(fontes[0], 8, "bold"), command=lambda: self.telaH.destroy())
            # ------POSIÇÕES------- #
            self.btSalvo.place(relx=0.260, rely=0.42, relheight=0.0550, relwidth=0.1)
            self.btfechatTela.place(relx=0.260, rely=0.48, relheight=0.0550, relwidth=0.1)
            self.lbSalvo.place(relx=0.21, rely=0.35, relheight=0.0550, relwidth=0.2)

        if btVoltar:
            # VOLTAR====================================================================================================
            self.btVoltar = Button(self.frameDefesa, text="VOLTAR", bd=4, bg=cores[4], fg=cores[1],
                                   font=(fontes[0], 8, "bold"), command=lambda: VOLTAR())
            self.btVoltar.place(relx=0.021, rely=0.9, relheight=0.0550, relwidth=0.1)
        if btSalvar:
            # SALVAR====================================================================================================
            self.btSalvar = Button(self.frameDefesa, text="SALVAR", bd=4, bg=cores[4], fg=cores[1],
                                   font=(fontes[0], 8, "bold"), command=lambda: SALVAR())
            self.btSalvar.place(relx=0.497, rely=0.9, relheight=0.0550, relwidth=0.1)

    def rastreiar(self, retorno):
        print(retorno)

    def label_entryGUARDA(self):
        # SALVAR========================================================================================================
        self.fechar_Salvar_Voltar(0)
        # LABELS========================================================================================================
        # ATRIBUTOS POSITIVOS===========================================================================================
        # ATK-/DEF-/PV-
        self.lbAtributos = Label(self.frameDefesa, text="Ataque de Infantaria:"
                                                        "\nDefesa de Infantaria:"
                                                        "\nPv de Infantaria:\n"
                                                        "\nAtaque de Arqueiro:"
                                                        "\nDefesa de Arqueiro:"
                                                        "\nPv de Arqueiro:\n"
                                                        "\nAtaque de Tropas:"
                                                        "\nDefesa de Tropas:"
                                                        "\nPv de Tropas:", fg=cores[1], bg=cores[6])
        self.lbAtributos.place(relx=0)
        self.lbAUX = Label(self.frameDefesa, text="%\n%\n%\n"
                                                  "\n%\n%\n%\n"
                                                  "\n%\n%\n%", fg=cores[1], bg=cores[6])
        self.lbAUX.place(relx=0.240, rely=0.001)
        # HERO =========================================================================================================
        self.lbHero = Label(self.frameDefesa, text="HERÓI\n=========================",
                            fg=cores[1], bg=cores[6])
        self.lbHeroAtrib = Label(self.frameDefesa, text="Ataque Básico:"
                                                        "\nDefesa Básica:"
                                                        "\nPv Básico:", fg=cores[1], bg=cores[6])
        self.lbHero.place(relx=0.212, rely=0.35)
        self.lbHeroAtrib.place(relx=0.212, rely=0.412)
        # EXCLUSIVOS A DEFESA ==========================================================================================
        self.lbExclusivo = Label(self.frameDefesa, text="EXCLUSIVO À DEFESA DO CASTELO\n"
                                                        "======================================",
                                 fg=cores[1], bg=cores[6])
        self.lbExclusivo.place(relx=0.146, rely=0.55)
        self.lbExclusivoAtrb = Label(self.frameDefesa, text="Ataque de Tropa:"
                                                            "\nDefesa de Tropa:"
                                                            "\nPV de Tropa:"
                                                            "\nP. de Ataque de tropa inimiga:"
                                                            "\nP. de Defesa de tropa inimiga:"
                                                            "\nP. de PV de tropa inimiga:", fg=cores[1], bg=cores[6])
        self.lbExclusivoAtrb.place(relx=0.146, rely=0.65)
        self.lbAUX3 = Label(self.frameDefesa, text="%\n%\n%\n%\n%\n%", fg=cores[1], bg=cores[6])
        self.lbAUX3.place(relx=0.436, rely=0.653)
        # PENALIDADES/ ATRIBUTOS NEGATIVOS==============================================================================

        self.lbAtributosPe = Label(self.frameDefesa, text="P. Ataque de Infantaria inimiga:"
                                                          "\nP. Defesa de Infantaria inimiga:"
                                                          "\nP. de Pv de Infantaria inimiga:\n"
                                                          "\nP. de Ataque de Arqueiro inimigo:"
                                                          "\nP. de Defesa de Arqueiro inimigo:"
                                                          "\nP. de Pv de Arqueiro inimigo:\n"
                                                          "\nP. de Ataque de Tropas inimiga:"
                                                          "\np. de Defesa de Tropas inimigas:"
                                                          "\nP. de Pv de tropas inimigas:", fg=cores[1], bg=cores[6])
        self.lbAtributosPe.place(relx=0.272)
        self.lbAUX2 = Label(self.frameDefesa, text="%\n%\n%\n"
                                                   "\n%\n%\n%\n"
                                                   "\n%\n%\n%", fg=cores[1], bg=cores[6])
        self.lbAUX2.place(relx=0.574, rely=0.001)
        # ENTRY=========================================================================================================
        # ATRIBUTOS POSITIVOS===========================================================================================

        self.varAux = 0.011
        self.entryDados = []
        for i in range(5):
            self.listaAux = []
            for j in range(3):
                self.listaAux.append(Entry(self.frameDefesa, bg="gray13", fg=cores[1]))
                if i < 3:
                    self.listaAux[j].place(relx=0.122, rely=self.varAux, relheight=0.025, relwidth=0.12)
                elif i == 3:
                    self.listaAux[j].place(relx=0.297, rely=self.varAux, relheight=0.025, relwidth=0.12)
                elif i == 4:
                    self.listaAux[j].place(relx=0.317, rely=self.varAux, relheight=0.025, relwidth=0.12)
                self.varAux += 0.030
            if i < 2:
                self.varAux += 0.027
            elif i == 2:
                self.varAux += 0.087
            elif i == 3:
                self.varAux += 0.147
            self.entryDados.append(self.listaAux)
        # PENALIDADES/ ATRIBUTOS NEGATIVOS==============================================================================

        self.varAux2 = 0.011
        self.entryDadosNegativos = []
        for i in range(4):
            self.listaAux = []
            for j in range(3):
                self.listaAux.append(Entry(self.frameDefesa, bg="gray13", fg=cores[1]))
                if i < 3:
                    self.listaAux[j].place(relx=0.457, rely=self.varAux2, relheight=0.025, relwidth=0.12)
                elif i == 3:
                    self.listaAux[j].place(relx=0.317, rely=self.varAux2, relheight=0.025, relwidth=0.12)
                self.varAux2 += 0.030
            if i < 2:
                self.varAux2 += 0.027
            elif i == 2:
                self.varAux2 += 0.414
            self.entryDadosNegativos.append(self.listaAux)

    def label_entryCASTELO(self):

        # FUNÇÕES DE BOTÕES=============================================================================================
        # INFANTARIA====================================================================================================

        def INFANTARIA():
            # --- INICIA TELA --- #
            self.btInfant.destroy()
            self.btArqueiro.destroy()
            self.fechar_Salvar_Voltar(2)
            # --- CONFG DE TELA --- #
            self.lbCategoria = Label(self.frameDefesa, text="INFANTARIA", fg=cores[8], bg=cores[6])
            self.lbAtributos = Label(self.frameDefesa, text="Ataque"
                                                            "\nDefesa"
                                                            "\nPV"
                                                            "\nAtaque aumenta ao defender"
                                                            "\nDefesa aumenta ao defender"
                                                            "\nPV aumenta ao defender"
                                                            "\nAumento de dano em vantagem\n"
                                                            "\nAtaque básico categoria I"
                                                            "\nAtaque básico categoria II"
                                                            "\nAtaque básico categoria III"
                                                            "\nAtaque básico categoria IV"
                                                            "\nAtaque básico categoria V"
                                                            "\nAtaque básico categoria VI"
                                                            "\nAtaque básico categoria VII"
                                                            "\nAtaque básico categoria VIII\n"
                                                            "\nDefesa básico categoria I"
                                                            "\nDefesa básico categoria II"
                                                            "\nDefesa básico categoria III"
                                                            "\nDefesa básico categoria IV"
                                                            "\nDefesa básico categoria V"
                                                            "\nDefesa básico categoria VI"
                                                            "\nDefesa básico categoria VII"
                                                            "\nDefesa básico categoria VIII", fg=cores[1], bg=cores[6])
            self.lbAtributos2 = Label(self.frameDefesa, text="\nPV básico categoria I"
                                                             "\nPV básico categoria II"
                                                             "\nPV básico categoria III"
                                                             "\nPV básico categoria IV"
                                                             "\nPV básico categoria V"
                                                             "\nPV básico categoria VI"
                                                             "\nPV básico categoria VII"
                                                             "\nPV básico categoria VIII", fg=cores[1], bg=cores[6])
            self.lbAUX = Label(self.frameDefesa, text="%\n%\n%\n"
                                                      "\n%\n%\n%\n"
                                                      "\n%\n%\n%", fg=cores[1], bg=cores[6])
            # --- PLACE --- #
            self.lbAUX.place(relx=0.240, rely=0.051)
            self.lbAtributos.place(relx=0, rely=0.05)
            self.lbAtributos2.place(relx=0.350, rely=0.0159)
            self.lbCategoria.place(relx=0.26)

        def ARQUEIRO():
            # --- INICIA TELA --- #
            self.btInfant.destroy()
            self.btArqueiro.destroy()
            self.fechar_Salvar_Voltar(2)
            # --- CONFG DE TELA --- #
            self.lbCategoria = Label(self.frameDefesa, text="ARQUEIRO", fg=cores[8], bg=cores[6])
            self.lbAtributos = Label(self.frameDefesa, text="Ataque"
                                                            "\nDefesa"
                                                            "\nPV"
                                                            "\nAtaque aumenta ao defender"
                                                            "\nDefesa aumenta ao defender"
                                                            "\nPV aumenta ao defender"
                                                            "\nAumento de dano em vantagem\n"
                                                            "\nAtaque básico categoria I"
                                                            "\nAtaque básico categoria II"
                                                            "\nAtaque básico categoria III"
                                                            "\nAtaque básico categoria IV"
                                                            "\nAtaque básico categoria V"
                                                            "\nAtaque básico categoria VI"
                                                            "\nAtaque básico categoria VII"
                                                            "\nAtaque básico categoria VIII\n"
                                                            "\nDefesa básico categoria I"
                                                            "\nDefesa básico categoria II"
                                                            "\nDefesa básico categoria III"
                                                            "\nDefesa básico categoria IV"
                                                            "\nDefesa básico categoria V"
                                                            "\nDefesa básico categoria VI"
                                                            "\nDefesa básico categoria VII"
                                                            "\nDefesa básico categoria VIII", fg=cores[1], bg=cores[6])
            self.lbAtributos2 = Label(self.frameDefesa, text="\nPV básico categoria I"
                                                             "\nPV básico categoria II"
                                                             "\nPV básico categoria III"
                                                             "\nPV básico categoria IV"
                                                             "\nPV básico categoria V"
                                                             "\nPV básico categoria VI"
                                                             "\nPV básico categoria VII"
                                                             "\nPV básico categoria VIII", fg=cores[1], bg=cores[6])
            self.lbAUX = Label(self.frameDefesa, text="%\n%\n%\n"
                                                      "\n%\n%\n%\n"
                                                      "\n%\n%\n%", fg=cores[1], bg=cores[6])
            # --- PLACE --- #
            self.lbAUX.place(relx=0.240, rely=0.051)
            self.lbAtributos.place(relx=0, rely=0.05)
            self.lbAtributos2.place(relx=0.350, rely=0.0159)
            self.lbCategoria.place(relx=0.26)

        def CAVALARIA():
            pass

        # BOTÕES========================================================================================================
        # --- INFANTARIA --- #
        self.btInfant = Button(self.frameDefesa, text="INFANTARIA", bd=4, bg=cores[4], fg=cores[1],
                               font=(fontes[0], 8, "bold"), command=lambda: INFANTARIA())
        self.btInfant.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.0550)
        # --- ARQUEIRO --- #
        self.btArqueiro = Button(self.frameDefesa, text="ARQUEIRO", bd=4, bg=cores[4], fg=cores[1],
                                 font=(fontes[0], 8, "bold"), command=lambda: ARQUEIRO())
        self.btArqueiro.place(relx=0.2, rely=0.38, relwidth=0.2, relheight=0.0550)
        # --- CAVALARIA --- #
        self.btCavalaria = Button(self.frameDefesa, text="CAVALARIA", bd=4, bg=cores[4], fg=cores[1],
                                  font=(fontes[0], 8, "bold"), command=lambda: CAVALARIA())
        self.btCavalaria.place(relx=0.2, rely=0.46, relwidth=0.2, relheight=0.0550)


if __name__ == '__main__':
    iniciar = TelaInicial()
    iniciar.telaInicio()
