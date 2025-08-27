class Cliente: #clase para crear la persona, con nombre y documento
    def __init__(self, nombre:str, documento:str):
        self.nombre =  nombre
        self.documento = documento

    def __str__(self) -> str:
        return f"{self.nombre}, se creo esta persona con el documento {self.documento}"# Terminen el codigo