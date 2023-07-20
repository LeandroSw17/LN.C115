import os

def move_file(source_path, destination_path):
    try:
        os.rename(source_path, destination_path)
        print("Arquivo movido com sucesso!")
    except Exception as e:
        print(f"Erro ao mover o arquivo: {e}")

if __name__ == "__main__":
    source_file_path = "C:/Users/Leandro Oliveira/Desktop/Projeto115/newmain.txt"

    destination_file_path = "C:/Users/Leandro Oliveira/Desktop/Projeto115/main.txt"

    move_file(source_file_path, destination_file_path)
