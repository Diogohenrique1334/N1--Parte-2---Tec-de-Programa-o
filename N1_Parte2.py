listaNomes =[]

def cadastrarUsuário():
   
    usuarioTemp = {}

    usuarioTemp["nome"] = input("\nDigite o nome completo do usuário: ")

    usuarioTemp["email"] = input("Digite o e-mail do usuário: ")

    listaNomes.append(usuarioTemp["nome"])
    listaNomes.append(usuarioTemp["email"])
   
    print("\nUsuário Cadastrado!")

    main()

    return

def exibirCadastros():

   print("\n\n         Como gostaria de exibir os cadastros?"
   
   "\n\nEXIBIR EM ORDEM DE CADASTRO [1]  EXIBIR EM ORDEM ALFABÉTICA [2]"
   
   "\n\nBUSCAR USUÁRIO [3]               VOLTAR AO MENU PRINCIPAL [4]")

   respUsuario = int (input("\n\nDigite o número correspondente para selecionar uma opção: "))

   if(respUsuario == 1):

      print(listaNomes)

      exibirCadastros()
   
   elif(respUsuario == 2):

      listaNomes.sort()
      print(listaNomes)

      exibirCadastros()
   
   elif(respUsuario == 3):

      respUsuario = input("\n\nDigite o nome do usuário que você deseja encontrar: ")

      if(respUsuario in listaNomes):

         print("\nSim, {} está na lista de usuários".format(respUsuario))
      
      else:
         print("\nUsuário não encontrado")
         
      exibirCadastros()

   elif(respUsuario == 4):

      main()
   
   return

      


def main():
   
  print("\n\n                          MENU"
 
  "\n\nINSCREVER NOVO USUÁRIO [1]   EXIBIR CADASTROS [2]"  
 
  "\n\nREMOVER CADASTRO [3]         ALTERAR DADOS DE CADASTRO[4]")

  respostaUsuario = int (input("\n\n Digite o número correspondente para selecionar uma opção: "))

  if respostaUsuario == 1:

     cadastrarUsuário() 

  elif respostaUsuario == 2:

     exibirCadastros()
   
  elif respostaUsuario == 3:
    
     print("nada")

  elif respostaUsuario == 4:

     print("Conseguiu!!")
     

if(__name__ == "__main__"):
    
    main()