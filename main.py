from inscricoes import Inscricao
from provas import Notas

NomeAprovados = []
NotaAprovados = []
Inscritos = []
InscritosNotas = []


while True:
    controle = input('Fazer mais uma inscrição? (s/n) ')
    if controle == 'n':
        break
    elif controle == 's':
        nome = input('Informe o nome do candidato: ')
        endereco = input('Cidade: ')
        exp = int(input('Anos de experiência: '))
        descr = input('Descrição: ')
        candidato = Inscricao(nome, endereco, exp, descr)
        Inscritos.append(candidato)
    else:
        print('Comando inválido!')
        continue

while True:
    controle = input('Deseja informar nota? (s/n) ')
    if controle == 'n':
        break
    elif controle == 's':
        nome = input('Informe o nome do candidado que vai informar a nota: ')
        nota = float(input('Nota: '))
        for candidato in Inscritos:
            if nome == candidato.nome:
                cand = Notas(candidato,nota)
                InscritosNotas.append(cand)
    else:
        print('Comando inválido!')
        continue

for finalistas in InscritosNotas:
    if finalistas.nota >= 8:
        NomeAprovados.append(finalistas.inscricao.nome)
        NotaAprovados.append(finalistas.nota)

for i in range(0,len(NomeAprovados)):
    print(f'\n{NomeAprovados[i]}   -   APROVADO   -   {NotaAprovados[i]}')
