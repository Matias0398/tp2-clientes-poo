from modulos import Client  # Importa la clase Client desde el paquete client

def main():
    client1 = Client("matias", "matiasllanos@example.com","Mendoza",4458796)
    
    print("Cliente creado:")
    client1.show_client() # Muestra la informacion del cliente recién creado

    # Cambia la dirección del cliente a una nueva
    client1.update_address("Belgrano 1200")

    print("Información actualizada:")
    client1.show_client()  # Muestra la informacion actualizada del cliente

if __name__ == "__main__":
    main()