class VendaVeiculo:
    def __init__(self, 
                 idVenda:int=None
                 ):
        ### SETTERS ###
        def set_idVenda(self, idVenda:int):
            self.idVenda = idVenda
        
        ### GETTERS ###

    def get_idVenda(self) -> int:
        return self.codigo

    def to_string(self) -> str:
        return f"Codigo: {self.get_codigo()} | Descrição: {self.get_idVenda()}"
    ### DUVIDA ###