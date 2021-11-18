import json

veiculos = {}
imoveis = {}

with open("dados2.txt") as file:
    for line in file:
        line = line.strip().split(";")
        if not line[0] in veiculos.keys():
            veiculos[line[0]] = {line[2]: float(line[3])}
        else:
            veiculos[line[0]][line[2]] = float(line[3])

        if line[4] and line[5] and line[6]:
            imiPago = float(line[5]) * float(line[6]) / 100
            if not line[0] in imoveis.keys():
                imoveis[line[0]] = {line[4]: imiPago}
            else:
                imoveis[line[0]][line[4]] = imiPago


resultNif = 0
highestImiPaid = 0

# B)
for nif, value in imoveis.items():
    for imiPago in value.values():
        #print("NIF:", nif, "\t", "Imi:", imiPago)
        if imiPago > highestImiPaid:
            resultNif = nif
            highestImiPaid = imiPago

#print("NIF:", resultNif, "\t", "Imi Pago:", highestImiPaid)


# C)

print(json.dumps(imoveis, indent=2))

pagamentosIMI = {}

for nif, value in imoveis.items():
    imiPaid = 0.00
    for imi in value.values():
        imiPaid = imiPaid + float(imi)
    pagamentosIMI[nif] = imiPaid

print(json.dumps(pagamentosIMI, indent=2))
