ano = int(input("digite o ano que nasceu: "))
ano_atual = int(input("digite o ano atual: "))
if ano >= ano_atual:
    print("invalid year")
    exit()
idade = (ano_atual - ano)
print("você tem", idade, "anos")