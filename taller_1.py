class Sustancia:

    def __init__( self ):
        self.__sustancias = dict()
        self.__identificador = ""
        self.__ubicacion = []
        self.__acceso = True or False
        self.__peligrosa = True or False 

    # METODOS PARA ASIGNAR
    def sustanciaAsignarIdentificador( self, identificador ):
        self.__identificador = identificador
        self.__sustancias[ identificador ] = {}

    def sustanciaAsignarUbicacion( self, fila, columna ):
        self.__ubicacion = list( fila, columna )
        self.__sustancias[ self.__identificador ][ "Ubicacion" ] = self.__ubicacion

    def sustanciaAsignarAcceso( self, acceso ): # Acceso a estudiantes
        self.__acceso = acceso
        self.__sustancias[ self.__identificador ][ "Acceso" ] =  self.__acceso

    def sustanciaAsignarPeligrosa( self, peligrosa ):
        self.__peligrosa = peligrosa
        self.__sustancias[ self.__identificador ][ "Peligrosa" ] = self.__peligrosa
    

class AcidoBase( Sustancia ):
    def __init__(self):
        super().__init__()
        self.__concentracion = 0.0     
        self.__efectos = ""

    def acidoBaseAsignarConcentracion( self, concentracion ):
        self.__concentracion = concentracion
        self.__sustancias[ self.__identificador ][ "Concentracion" ] = self.__concentracion
 
    def acidoBaseAsignarEfectos( self, efectos ):
        self.__efectos = efectos     
        self.__sustancias[ self.__identificador ][ "Efectos" ] = self.__efectos   

class Alcohol( Sustancia ):
    def __init__( self ):
        super().__init__()
        self.__temperaturaEbullicion = 0.0
        self.__temperaturaArder = 0.0

    def alcoholAsignarTempEbullicion( self, temperaturaEbu ):
        self.__temperaturaEbullicion = temperaturaEbu
        self.__sustancias[ self.__identificador ][ "Temperatura de ebullicion" ] = self.__temperaturaEbullicion

    def alcoholAsignarTempArder( self, temperaturaArder ):
        self.__temperaturaArder = temperaturaArder
        self.__sustancias[ self.__identificador ][ "Temperatura Arder" ] = self.__temperaturaArder

class Solvente( Sustancia ):
    def __init__( self ):
        super().__init__()
        self.__naturaleza = ""
        self.__viscosidad = 0

    def solventeAsignarNaturaleza( self, naturaleza ):
        self.__naturaleza = naturaleza
        self.__sustancias[ self.__identificador ][ "Naturaleza" ] = self.__naturaleza

    def solventeAsignarViscosida( self, viscosidad ):
        self.__viscosidad = viscosidad
        self.__sustancias[ self.__identificador ][ "Viscosidad" ] = self.__viscosidad

class Otro( Sustancia ):
    def __init__( self ):
        super().__init__()
        self.__fecha = ""
        self.__motivo = ""
        self.__cantidad = ""

    def otrosAsignarFecha( self, fecha ):
        self.__fecha = fecha
        self.__sustancias[ self.__identificador ][ "Fecha Ingreso" ] = self.__fecha

    def otrosAsignarMotivo( self, motivo ):
        self.__motivo = motivo
        self.__sustancias[ self.__identificador ][ "Motivo" ] = self.__motivo

    def otrosAsignarCantidad( self, cantidad ):
        self.__cantidad = cantidad
        self.__sustancias[ self.__identificador ][ "Cantidad" ] = self.__cantidad


class Sistema( Sustancia ):
    
    def __init__( self ):
        super().__init__()   

    
    def sistemaVerificarSustancia( self, identificador ):
        for id in self.__sustancias.keys():
            if id == identificador:
                return True
            else:
                return False
    
            
################################ METODOS PARA VALIDAR ################################

def validarFloat( a ):
    try:
        a = float( a )
        return a 
    except:
        opcion  = input( "ingrese un nuero valido: " )
        validarFloat( opcion )

######################################################################################

def main():
    
    while True:
        
        sustancia = Sistema()

        opcion = input( """
        (1) Ingresar sustancia
        (2) Buscar sustancia
        (3) Eliminar sustancia
        (4) Cerrar programa
        """ )
        
        if opcion == '1': # INGRESAR SUSTANCIA

            opcion1 = input( """
            (1) Acido Base 
            (2) Alcohol
            (3) Solvente
            (4) Otros        
            > """ )

            if opcion == '1':
                identificador = input( "Ingresa el identificador de la sustancia acido base: " ) + "AB"
                verificar = sustancia.sistemaVerificarSustancia( identificador ) if True else False
                if verificar == False:
                    continue
                acidoBase = AcidoBase()
                fila = validarFloat( input( "Ingrese le numero de la fila: " ) )
                columna = validarFloat( input( "Ingrese la columna del gabinete: " ) )
                
                acidoBase.sustanciaAsignarIdentificador( identificador )
                acidoBase.sustanciaAsignarUbicacion( fila, columna )
                acidoBase.sustanciaAsignarPeligrosa()
                acidoBase.sustanciaAsignarAcceso()
                acidoBase.acidoBaseAsignarConcentracion()
                acidoBase.acidoBaseAsignarEfectos()

            elif opcion == '2':
                pass
            elif opcion == '3':
                pass
            elif opcion == '4':
                pass

        elif opcion == '2': # BUSCAR SUSTANCIA
            pass
        elif opcion == '3': # ELIMINAR SUSTANCIA
            pass 
        elif opcion == '4': # CERRAR PROGRAMA
            break

if __name__ == '__main__':
    main()
