import random
import uuid


class ImpulsivoEstrategia:
    def vai_comprar(self, saldo, propriedade):
        return True


class ExigenteEstrategia:
    def __init__(self, valor_minimo_aluguel=50) -> None:
        self.valor_minimo_aluguel = valor_minimo_aluguel

    def vai_comprar(self, saldo, propriedade):
        if propriedade.valor_aluguel > self.valor_minimo_aluguel:
            return True
        return False


class CautelosoEstrategia:
    def __init__(self, reserva_apos_compra=80) -> None:
        self.reserva_apos_compra = reserva_apos_compra

    def vai_comprar(self, saldo, propriedade):
        if saldo - propriedade.custo_compra > self.reserva_apos_compra:
            return True
        return False


class AleatorioEstrategia:
    def vai_comprar(self, saldo, propriedade):
        return random.choice([True, False])


class Jogador:
    def __init__(self, estrategia, saldo=300) -> None:
        self.saldo = saldo
        self.estrategia = estrategia
        self.id = uuid.uuid4()

    def jogar_dados(self):
        return random.choice([1, 2, 3, 4, 5, 6])

    def comprar(self, propriedade):
        if self.saldo > propriedade.custo_compra and self.estrategia.vai_comprar(
            self.saldo, propriedade
        ):
            return True
        return False

    def retirar_saldo(self, valor):
        self.saldo -= valor

    def adicionar_saldo(self, valor):
        self.saldo += valor

    def falido(self):
        return self.saldo <= 0

    def __hash__(self):
        return self.id.__hash__()

    def __eq__(self, other):
        return self.id.__eq__(other)

    def __repr__(self) -> str:
        return f"jogador {self.id} com estratégia {type(self.estrategia)}"


class Propriedade:
    def __init__(
        self,
        custo_compra,
        valor_aluguel,
    ) -> None:
        self.custo_compra = custo_compra
        self.valor_aluguel = valor_aluguel
        self.proprietario = None

    def tem_proprietario(self):
        return self.proprietario != None

    def comprar(self, jogador):
        jogador.retirar_saldo(self.custo_compra)
        self.proprietario = jogador

    def pagar_aluguel(self, jogador):
        return jogador.retirar_saldo(self.valor_aluguel)


class Tabuleiro:

    PRIMEIRA_POSICAO = 0

    def __init__(
        self,
        propriedades=None,
        quantidade_propriedades=20,
        valor_volta_completa=100,
        fator_propriedade=500,
        fator_aluguel=100,
    ) -> None:
        self.quantidade_propriedades = quantidade_propriedades
        self.propriedades = propriedades
        if not propriedades:
            self.propriedades = [
                Propriedade(
                    random.random() * fator_propriedade, random.random() * fator_aluguel
                )
                for i in range(quantidade_propriedades)
            ]
        self.posicao_jogadores = {}
        self.valor_volta_completa = valor_volta_completa

    def adicionar_jogadores(self, jogadores):
        for jogador in jogadores:
            self.adicionar_jogador(jogador)

    def adicionar_jogador(self, jogador):
        self.posicao_jogadores[jogador] = self.PRIMEIRA_POSICAO

    def mover_jogador(self, jogador: Jogador, passos) -> Propriedade:
        posicao = self.posicao_jogadores[jogador]
        posicao += passos
        if posicao >= self.quantidade_propriedades:
            posicao %= self.quantidade_propriedades
            jogador.adicionar_saldo(self.valor_volta_completa)
        self.posicao_jogadores[jogador] = posicao
        return self.propriedades[posicao]


class Partida:
    def __init__(self, jogadores=None, tabuleiro=None, max_rodadas=1000) -> None:
        self.jogadores = jogadores
        if not jogadores:
            self.jogadores = [
                Jogador(ImpulsivoEstrategia()),
                Jogador(ExigenteEstrategia()),
                Jogador(CautelosoEstrategia()),
                Jogador(AleatorioEstrategia()),
            ]

        if not tabuleiro:
            self.tabuleiro = Tabuleiro()
        self.tabuleiro.adicionar_jogadores(self.jogadores)

        self.vencedor = None
        self.quantidade_turnos = 0
        self.max_rodadas = max_rodadas

    def jogar(self):
        jogadores_ativos = self.jogadores
        for i in range(1, self.max_rodadas + 1):
            if len(jogadores_ativos) == 1:
                self.vencedor = jogadores_ativos[0]
                self.quantidade_turnos = i
                break
            for jogador in jogadores_ativos:
                valor_dado = jogador.jogar_dados()
                propriedade = self.tabuleiro.mover_jogador(jogador, valor_dado)
                if propriedade.tem_proprietario():
                    propriedade.pagar_aluguel(jogador)
                elif jogador.comprar(propriedade):
                    propriedade.comprar(jogador)

                if jogador.falido():
                    jogadores_ativos.remove(jogador)


class Simulacao:
    def __init__(self):
        pass
