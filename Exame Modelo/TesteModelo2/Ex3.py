import AlterarInfo
import Calculos
import LerFicheiro
import Listagens

result = LerFicheiro.ler("alunos.txt")
notasAlunos = result[0]
nomeAlunos = result[1]

Calculos.media(notasAlunos)

# print(Calculos.media(notasAlunos))
# print(Listagens.listagem(notasAlunos, nomeAlunos))
AlterarInfo.adicionaDados("alunos.txt")
