from socket import socket
import time

def main():
    print("## CLIENTE ##")
    inicio = time.strftime("%I:%M:%S")
    s = socket()
    s.connect(("mariohernandezvzla.ddns.net", 10000))
    
    f = open("archivos/recibido.txt", "wb")
    #f = open("archivos/recibido.mp3", "wb")
    
    while True:
        try:
            # Recibir datos del cliente.
            input_data = s.recv(1)
            print(input_data)
        except error:
            print("Error de lectura.")
            break
        else:
            if input_data:
                # Compatibilidad con Python 3.
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1
                else:
                    end = input_data == chr(1)
                if not end:
                    # Almacenar datos.
                    f.write(input_data)
                else:
                    break
    
    print("El archivo se ha recibido correctamente.")
    f.close()
    fin = time.strftime("%I:%M:%S")
    print(inicio)
    print(fin)

if __name__ == "__main__":
    main()
