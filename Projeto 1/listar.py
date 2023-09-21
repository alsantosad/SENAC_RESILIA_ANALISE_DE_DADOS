def listar( arg:tuple|list ):
    "informe uma lista ou tupla contendo apenas strings e a função exibirá os elementos enumerados"
    for index in range(len(arg)):
        print('%2d-%s'%(index+1,arg[index]))