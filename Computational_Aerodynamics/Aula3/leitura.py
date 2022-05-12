import numpy as npy

# rotina de leitura dos dados
def colunas(name,columns,skip):

  # abre arquivo e conta o numero de linhas
  num_lines = sum(1 for line in open(name))

  #inicializando um array para salvar os dados da leitura
  var  = npy.zeros((num_lines-skip,columns))

  # abre o arquivo novamente e pula 
  # as linhas do cabecario
  file1 = open(name,"r")
  for j in range(skip):
     dummy = file1.readline()

  # loop de leitura das linhas restantes
  for i in range(num_lines-skip):

    # leitura da linha completa como texto
    dummy = file1.readline()

    # separa as  colunas
    pair = dummy.split()

    # converte para float e separa cada coluna
    for j in range(columns):
       var[i,j] =float(pair[j])

  # fecha o arquivo
  file1.close()
  return var



# rotina de leitura dos dados
def linhas(name,skip):

  # abre arquivo e conta o numero de linhas
  num_lines = sum(1 for line in open(name))

  #inicializando um array para salvar os dados da leitura
  var  = npy.zeros((num_lines-skip))

  # abre o arquivo novamente e pula 
  # as linhas do cabecario
  file1 = open(name,"r")
  for j in range(skip):
     dummy = file1.readline()

  # loop de leitura das linhas restantes
  for i in range(num_lines-skip):
    var[i] = float(file1.readline())

  # fecha o arquivo
  file1.close()
  return var

# Cria um vetor com um indice a mais onde o ultimo indice eh igual ao indice 0
def periodic(var):
    n = var.shape[0]
    new = npy.zeros((n+1))
    new[0:n] = var
    new[n] = var[0]
    return new
