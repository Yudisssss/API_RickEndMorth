import os
from character_id import get_character_by_id
from character_name import get_character_by_name
from location_id import get_locale_id
from location_name import get_locale_name
from ep_id import get_episode_id     
from ep_name import get_episode_name

fe=""
while fe not in ("y", "yes"):
    print("=============| ESCOLHA DA API |=============")
    print("[1]- Personagem")
    print("[2]- Localização")
    print("[3]- Episódio")
    print("============================================")
    choice = input()

    match choice:
        case "1":
            print("\n" * os.get_terminal_size().lines)
            print("===========| Ecolha de Personagem |============")
            select_type = ""
            while select_type not in ("1", "2"): 
                print("[1]- Nome")
                print("[2]- ID")
                select_type = input()
                if select_type == "1":
                    print("\n" * os.get_terminal_size().lines)
                    per_name = input("Informe o nome do Personagem: ")
                    get_character_by_name(per_name) 
                if select_type == "2":
                    print("\n" * os.get_terminal_size().lines)
                    per_id = input("Informe o ID do Personagem: ")  
                    get_character_by_id(per_id)
                    fe =  input("Pressione 'y' ou 'yes' para continuar ou qualquer tecla para sair: ")          
        case "2":
            print("\n" * os.get_terminal_size().lines)
            print("===========| Ecolha a Localização |============")
            select_type = ""
            while select_type not in ("1", "2"): 
                print("[1]- Nome")
                print("[2]- ID")
                select_type = input()
                if select_type == "1":
                    print("\n" * os.get_terminal_size().lines)
                    loc_name = input("Informe o nome da Localização: ")
                    get_locale_name(loc_name)
                if select_type == "2":
                    print("\n" * os.get_terminal_size().lines)
                    loc_id = input("Informe o ID da Localização: ")  
                    get_locale_id(loc_id)
                    fe =  input("Pressione 'y' ou 'yes' para continuar ou qualquer tecla para sair: ")   
        case "3":
            print("\n" * os.get_terminal_size().lines)
            print("===========| Ecolha o Episodio |============")
            select_type = ""
            while select_type not in ("1", "2", "3"): 
                print("[1]- Nome")
                print("[2]- ID")
                print("[3]- Número do Episódio")
                select_type = input()
                if select_type == "1":
                    print("\n" * os.get_terminal_size().lines)
                    ep_name = input("Informe o nome do Episódio: ")
                    get_episode_name(ep_name)
                if select_type == "2":
                    print("\n" * os.get_terminal_size().lines)
                    ep_id = input("Informe o ID do Episódio: ")  
                    get_episode_id(ep_id)
                if select_type == "3":
                    pass  
                    fe =  input("Pressione 'y' ou 'yes' para continuar ou qualquer tecla para sair: ")  
        case _:
            print("\n" * os.get_terminal_size().lines)
            print("Opção inválida. Tente novamente.")
             
                   
