# Condições da verificação do saldo:
# - Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
# - Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
# - Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:
# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo:


class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    def verificar_saldo(self):
        saldo = self.__saldo
        if saldo < 10:
            return (
                saldo,
                "Seu saldo está baixo. Recarregue e use os serviços do seu plano.",
            )
        elif saldo >= 50:
            return saldo, "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return (
                saldo,
                "Seu saldo está razoável. Aproveite o uso moderado do seu plano.",
            )

    def mensagem_personalizada(self):
        saldo, mensagem = self.verificar_saldo()
        return mensagem


# Classe UsuarioTelefone:
# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:


class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.__nome = nome
        self.__plano = plano

    def __str__(self):
        return f"Usuário {self.__nome}, plano: {self.__plano}."

    def verificar_saldo(self):
        return self.__plano.verificar_saldo()

    def mensagem_personalizada(self):
        return self.__plano.mensagem_personalizada()


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
