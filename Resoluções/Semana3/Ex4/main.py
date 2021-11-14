import json


def getNifBiggestIMIPaid(imoveis: dict):
    biggestIMIPaid = 0
    targetNif = 0
    for nif, nifValues in imoveis.items():
        tmpIMI = 0
        for imiPago in nifValues.values():
            tmpIMI += imiPago

        if tmpIMI > biggestIMIPaid:
            targetNif = nif
            biggestIMIPaid = tmpIMI
    return targetNif


def getNIFTaxes(veiculo: dict, imoveis: dict):
    table = {}
    for nif, nifValue in veiculo.items():
        table[nif] = 0
        for iuc in dict(nifValue).values():
            table[nif] += iuc

    for nif, nifValue in imoveis.items():
        if not nif in table.keys():
            table[nif] = 0

        for valorIMI in dict(nifValue).values():
            table[nif] += valorIMI

    return table


veiculos = {}
imoveis = {}
with open("dados.txt") as file:
    for line in file.readlines():
        info = line.strip().split(";")
        nif = int(info[0])
        ano = int(info[1])
        matricula = info[2]
        valorIUC = float(info[3])
        artigoMatricial = info[4]
        valor = info[5]
        taxaImi = info[6]

        ## Info do veiculo
        if not nif in veiculos.keys():
            veiculos[nif] = {matricula: valorIUC}
        else:
            veiculos[nif][matricula] = valorIUC

        # Info do imovel
        if artigoMatricial and taxaImi and valor:
            taxaImi = float(taxaImi)
            valor = float(valor)
            imiPago = valor * taxaImi / 100
            if not nif in imoveis.keys():
                imoveis[nif] = {artigoMatricial: imiPago}
            else:
                imoveis[nif][artigoMatricial] = imiPago

print(json.dumps(veiculos, indent=2))
print("-------------------------------")
print(json.dumps(imoveis, indent=2))

print(getNIFTaxes(veiculos, imoveis))
