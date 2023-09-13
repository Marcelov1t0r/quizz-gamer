from time import sleep
questao1={
    'Valor_questao':"5",
    'Gabarito':'c',
    'Enunciado':'Qual o chefe mais difícil de Dark Souls 2?',
    'Opcao1':'Nameless King',
    'Opcao2':'Sir Alonne',
    'Opcao3':'Fume Knight',
    'Opcao4':'King Vendrick'
}
questao2={'Valor_questao':"3",
    'Gabarito':'a',
    'Enunciado':'Qual identidade do Noob Saibot?',
    'Opcao1':'Bi-Han',
    'Opcao2':'Artorias',
    'Opcao3':'Hanzo Hasashi',
    'Opcao4':'Shao'
} 
questao3={'Valor_questao':"5",
    'Gabarito':'b',
    'Enunciado':'Quem carrega a runa da morte em Elden Ring?',
    'Opcao1':'Godrick',
    'Opcao2':'Maliketh',
    'Opcao3':'Nobre da Pele Divina',
    'Opcao4':'Radagon'
}
questao4={'Valor_questao':"3",
    'Gabarito':'d',
    'Enunciado':'Qual o líder dos cavaleiros de Gwyn?',
    'Opcao1':'Nameless King',
    'Opcao2':'Artorias',
    'Opcao3':'Smough',
    'Opcao4':'Ornstein'
}

prova=[]
gabarito_5=['c','','b','']
gabarito_3=['','a','','d']
respostas=[]

prova.append(questao1)
prova.append(questao2)
prova.append(questao3)
prova.append(questao4)

for num,questao in enumerate(prova):
    print(num+1,"-",questao["Enunciado"])
    print("a)",questao["Opcao1"])
    print("b)",questao["Opcao2"])
    print("c)",questao["Opcao3"])
    print("d)",questao["Opcao4"])
    print("\n")
    respostas.append(input("Digite a opção correta:"))

pontuacao = 0

for i in range(0,4):
    if respostas[i]==gabarito_5[i]:
        print("Questao",i+1,"certa")
        pontuacao=pontuacao + 5
    elif respostas[i]==gabarito_3[i]:
        print("Questao",i+1,"certa")
        pontuacao=pontuacao + 3
    else:
        print("Questão",i+1,"errada")
    
print("Sua pontuação foi de:",pontuacao,"pontos.")
