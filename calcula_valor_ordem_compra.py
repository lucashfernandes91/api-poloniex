import json, requests

moeda_par = "" # Criptomoeda que deve ser consultada
porcentagem_de_lucro = float() # lucro em '%' que deseja

def response(moeda_par):
    response = requests.get("https://poloniex.com/public?command=returnOrderBook&currencyPair=BTC_" + moeda_par + "&depth=1")
    fechamentos = json.loads(response.content)
    return fechamentos

def primeira_ordem_compra(response):
    valor = response(moeda_par)['bids'][0][0] #-*-retorna quantidade que está a compra ['asks'][0][1] -*-
    return float(valor)

def primeira_ordem_venda(response):
    valor = response(moeda_par)['asks'][0][0] #-*- retorna quantidade que está a venda ['asks'][0][1] -*-
    return float(valor)

def valor_ordem_compra(porcentagem_de_lucro, primeira_ordem_compra):
    porcentagem = porcentagem_de_lucro / 100
    margem_lucro = porcentagem * primeira_ordem_compra(response)
    total = float(primeira_ordem_compra(response)) - margem_lucro
    return total #Retorna o valor que deve ser a ordem de COMPRA

def valor_autal_mais_porcentagem(primeira_ordem_compra, porcentagem_de_lucro):
    porcentagem = porcentagem_de_lucro / 100
    margem_lucro = porcentagem * primeira_ordem_compra(response)
    total = margem_lucro + primeira_ordem_compra(response)
    return total

print("Moeda consultada: {:s}".format(moeda_par))
print("Primeira ordem de Compra: {:10.8f}".format(primeira_ordem_compra(response)))
print("Primeira ordem de Venda:  {:10.8f}\n".format(primeira_ordem_venda(response)))
print("Lucro solicitado: {:4.2f}%".format(porcentagem_de_lucro))
print("Valor de Compra: {:10.8f}\n".format(valor_ordem_compra(porcentagem_de_lucro, primeira_ordem_compra)))
print("Ordem atual + lucro solitado: {:10.8f}".format(valor_autal_mais_porcentagem(primeira_ordem_compra, porcentagem_de_lucro)))
