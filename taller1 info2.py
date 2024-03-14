from datetime import datetime

class ImplanteMedico:
    def __init__(self, tipo, material, tamaño):
        self.__tipo = tipo
        self.__material = material
        self.__tamaño = tamaño
        self.__fecha_implantacion = None
        self.__medico_responsable = None
        self.__estado = None

    def __str__(self):
        return f"Tipo: {self.__tipo}\nMaterial: {self.__material}\nTamaño: {self.__tamaño}\nFecha de Implante: {self.__fecha_implantacion}\nMédico Responsable: {self.__medico_responsable}\nEstado: {self.__estado}"

    def get_tipo(self):
        return self.__tipo

    def get_material(self):
        return self.__material

    def get_tamaño(self):
        return self.__tamaño

    def get_fecha_implantacion(self):
        return self.__fecha_implantacion

    def set_fecha_implantacion(self, fecha):
        self.__fecha_implantacion = fecha

    def get_medico_responsable(self):
        return self.__medico_responsable

    def set_medico_responsable(self, medico):
        self.__medico_responsable = medico

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado