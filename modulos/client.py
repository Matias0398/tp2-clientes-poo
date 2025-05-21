class Client:
    def __init__(self, name: str, mail: str, address: str, phone: int):
        self.name = name
        self.mail = mail
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"Cliente: {self.name}"
    
    """muestra los datos del cliente"""
    def show_client(self):
        print(f"cliente: {self.name}\ncorreo: {self.mail}\ndireccion: {self.address}\ntelefono: {self.phone}")
    
    """actualiza la direccion del cliente"""
    def update_address(self, new_address: str)-> None:
        self.address=new_address
        print(f"direccion actualizada a: {self.address}")
