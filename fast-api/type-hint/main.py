# Without type hints
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("leonardo", "teramatsu"))

# With type hints - Quando vc quer verificar os metodos disponiveis utilizando o ponto vc conseguira ver todas elas
# Utilizar o type hints seria uma das maneiras de o editor conseguir te dar suporte nos momentos em que vc queira filtrar os metodos disponiveis
# visto que ja se sabe qual o tipo de dado que esta sendo esperado.
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("leonardo", "teramatsu"))
