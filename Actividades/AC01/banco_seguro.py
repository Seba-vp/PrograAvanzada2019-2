from entidades_banco import Cliente, BancoDCC
from os import path
'''
Deberas completar las clases ClienteSeguro, BancoSeguroDCC y  sus metodos
'''


class ClienteSeguro(Cliente):
    def __init__(self, id_cliente, nombre, contrasena):
        # completar
        self.tiene_fraude = False
        super().__init__(id_cliente, nombre, contrasena)

    @property
    def saldo_actual(self):
        return  self.saldo
        

    @saldo_actual.setter
    def saldo_actual(self, nuevo_saldo):
        self.saldo = nuevo_saldo
        if self.saldo <0:
            self.tiene_fraude = True

    def deposito_seguro(self, dinero):
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        
        self.depositar(dinero)
        self.saldo_actual = self.saldo

        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            transaccion = str(self.id_cliente)+', deposito, '+ str(dinero)
            archivo.writelines(transaccion)
            archivo.close()
    

    def retiro_seguro(self, dinero):
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''
        self.retirar(dinero)
        self.saldo_actual = self.saldo
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')

        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            transaccion = str(self.id_cliente)+', retiro, '+ str(dinero)
            archivo.writelines(transaccion)
            archivo.close()
    



class BancoSeguroDCC(BancoDCC):
    def __init__(self):
        super().__init__(clientes)
        

    def cargar_clientes(self, ruta):
        # completar
        #self.cargar_clientes(ruta)


        with open(ruta, "r", encoding="UTF-8") as file:
            for line in file:
                id_cliente, nombre, saldo, contrasena = line.strip().split(",")
                # Notar que dejamos el id como string, no hay problema
                # mientras se sea consistente
                instancia_cliente = ClienteSeguro(id_cliente, nombre, contrasena)
                instancia_cliente.saldo_actual = saldo
                self.clientes.append(instancia_cliente)

    def realizar_transaccion(self, id_cliente, dinero, accion):
        #buscar cliente busca en la lista Clientes, esta lista ya contiene objetos clientes seguros
        cliente = self.buscar_cliente(id_cliente)
        if accion == "depositar":
            cliente.deposito_seguro(dinero)
        elif accion == "retirar":
            cliente.retiro_seguro(dinero)



    def verificar_historial_transacciones(self, historial):
        print('Validando transacciones')
        # completar
        for transaccion in historial:
            id_cliente, accion, monto = transaccion.strip().split(",")
            self.realizar_transaccion(id_cliente, monto, accion)

    def validar_monto_clientes(self, ruta):
        print('Validando monto de los clientes')
        with open(ruta, "r", encoding="UTF-8") as file:
            for line in file:
                id_cliente, nombre, saldo, contrasena = line.strip().split(",")
                # Notar que dejamos el id como string, no hay problema
                # mientras se sea consistente
                cliente = self.buscar_cliente(id_cliente)

            
                if cliente.saldo_actual != saldo:
                    cliente.tiene_fraude() = True 



