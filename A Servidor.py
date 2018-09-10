from socket import socket, error

def main():
    print("## SERVIDOR ##")
    s = socket()
    # Escuchar peticiones en el puerto 10000.
    s.bind(("", 10000))
    s.listen(1)
    
    conn, addr = s.accept()

    while True:
        f = open("archivos/data.txt", "rb")
        #f = open("archivos/prueba.mp3", "rb")
        content = f.read(1)
        
        while content:
            # Enviar contenido.
            conn.send(content)
            print(content)
            content = f.read(1)
        
        break
    
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        conn.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        conn.send(bytes(chr(1), "utf-8"))
    
    # Cerrar conexión y archivo.
    s.close()
    f.close()
    print("El archivo ha sido enviado correctamente.")

if __name__ == "__main__":
    main()