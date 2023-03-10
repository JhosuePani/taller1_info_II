class Sustancia:

    def __init__( self, diccionario ):
        self.sustancias = diccionario
        self.__identificador = ""
        self.__ubicacion = []
        self.__acceso = True or False
        self.__peligrosa = True or False 

    # METODO PARA OBTENER EL IDENTIFICADOR
    def sustanciaVerIdentificador( self ):
        return self.__identificador

    # METODOS PARA ASIGNAR
    def sustanciaAsignarIdentificador( self, identificador ):
        self.__identificador = identificador
        self.sustancias[ identificador ] = {}

    def sustanciaAsignarUbicacion( self, fila, columna ):
        self.__ubicacion = [ fila, columna ]
        self.sustancias[ self.__identificador ][ "Ubicacion" ] = self.__ubicacion

    def sustanciaAsignarAcceso( self, acceso ): # Acceso a estudiantes
        self.__acceso = acceso
        self.sustancias[ self.__identificador ][ "Acceso" ] =  self.__acceso

    def sustanciaAsignarPeligrosa( self, peligrosa ):
        self.__peligrosa = peligrosa
        self.sustancias[ self.__identificador ][ "Peligrosa" ] = self.__peligrosa
    

class AcidoBase( Sustancia ):
    def __init__(self, diccionario):
        super().__init__( diccionario )
        self.__concentracion = 0.0     
        self.__efectos = ""

    def acidoBaseAsignarConcentracion( self, concentracion ):
        self.__concentracion = concentracion
        self.sustancias[ Sustancia.sustanciaVerIdentificador(self) ][ "Concentracion" ] = self.__concentracion
 
    def acidoBaseAsignarEfectos( self, efectos ):
        self.__efectos = efectos     
        self.sustancias[ Sustancia.sustanciaVerIdentificador(self) ][ "Efectos" ] = self.__efectos   

class Alcohol( Sustancia ):
    def __init__( self, diccionario ):
        super().__init__( diccionario )
        self.__temperaturaEbullicion = 0.0
        self.__temperaturaArder = 0.0

    def alcoholAsignarTempEbullicion( self, temperaturaEbu ):
        self.__temperaturaEbullicion = temperaturaEbu
        self.sustancias[ Sustancia.sustanciaVerIdentificador(self) ][ "Temperatura de ebullicion" ] = self.__temperaturaEbullicion

    def alcoholAsignarTempArder( self, temperaturaArder ):
        self.__temperaturaArder = temperaturaArder
        self.sustancias[ Sustancia.sustanciaVerIdentificador(self) ][ "Temperatura Arder" ] = self.__temperaturaArder

class Solvente( Sustancia ):
    def __init__( self, diccionario ):
        super().__init__( diccionario )
        self.__naturaleza = ""
        self.__viscosidad = 0

    def solventeAsignarNaturaleza( self, naturaleza ):
        self.__naturaleza = naturaleza
        self.sustancias[ Sustancia.sustanciaVerIdentificador(self) ][ "Naturaleza" ] = self.__naturaleza

    def solventeAsignarViscosida( self, viscosidad ):
        self.__viscosidad = viscosidad
        self.sustancias[ Sustancia.sustanciaVerIdentificador(self) ][ "Viscosidad" ] = self.__viscosidad

class Otro( Sustancia ):
    def __init__( self, diccionario ):
        super().__init__( diccionario )
        self.__fecha = ""
        self.__motivo = ""
        self.__cantidad = ""

    def otrosAsignarFecha( self, fecha ):
        self.__fecha = fecha
        self.sustancias[ Sustancia.sustanciaVerIdentificador(self) ][ "Fecha Ingreso" ] = self.__fecha

    def otrosAsignarMotivo( self, motivo ):
        self.__motivo = motivo
        self.sustancias[ Sustancia.sustanciaVerIdentificador(self) ][ "Motivo" ] = self.__motivo

    def otrosAsignarCantidad( self, cantidad ):
        self.__cantidad = cantidad
        self.sustancias[ Sustancia.sustanciaVerIdentificador(self) ][ "Cantidad" ] = self.__cantidad


class Sistema( Sustancia ):
    
    def __init__( self, diccionario ):
        super().__init__( diccionario )   

    def sistemaVerificarSustancia( self, identificador ):
        if len( self.sustancias ) != 0:
            for id in self.sustancias.keys():
                if id == identificador:
                    return True
                else:
                    return False

    def sistemaVerSustancias( self ):
        return self.sustancias
    
    def sistemaBuscarSustancia( self, identificador ):
        if identificador in list( self.sustancias.keys() ):
            print( f"""
            Id: {identificador}
            
            """ )
            
################################ METODOS PARA VALIDAR ################################

def validarFloat( a ):
    try:
        a = float( a )
        return a 
    except:
        opcion  = input( "ingrese un nuero valido: " )
        validarFloat( opcion )

def validarInt( a ):
    try:
        a = int( a )
        return a
    except:
        opcion = input( "Ingrese una opcion valida: " )
        validarInt( opcion )

def validarBoolean( a ):
    if a == 'si':
        return True
    elif a == 'no':
        return False
    else:
        opcion = input( "Intentelo nuevamente: " )
        validarBoolean( opcion )

######################################################################################

def main():
    
    diccionario = {}

    while True:
        
        sustancia = Sistema( diccionario )

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

            if opcion1 == '1': # ACIDO BASE
                identificador = input( "Ingresa el identificador de la sustancia acido base: " ) + "AB"
                if sustancia.sistemaVerificarSustancia( identificador ) == True:
                    print( "El identificador ya esta ocupado con otra sustancia... " )
                    continue
                acidoBase = AcidoBase( diccionario )
                fila = validarInt( input( "Ingrese le numero de la fila: " ) )
                columna = validarInt( input( "Ingrese la columna del gabinete: " ) )
                peligrosa = validarBoolean( input( "La sustancia es peligrosa si/no: " ) )
                acceso = validarBoolean( input( "La sustancia tiene acceso para estudiantes si/no: " ) )
                concentracion = validarFloat( input( "Ingrese la concentracion: " ) )
                efectos = input( "Ingrese los efectos nocivos que produce esta sustancia: " )

                acidoBase.sustanciaAsignarIdentificador( identificador )
                acidoBase.sustanciaAsignarUbicacion( fila, columna )
                acidoBase.sustanciaAsignarPeligrosa( peligrosa )
                acidoBase.sustanciaAsignarAcceso( acceso )
                acidoBase.acidoBaseAsignarConcentracion( concentracion )
                acidoBase.acidoBaseAsignarEfectos( efectos )

            elif opcion1 == '2': # ALCOHOL
                identificador = input( "Ingresa el identificador de la sustancia acido base: " ) + "A"
                if sustancia.sistemaVerificarSustancia( identificador ) == True:
                    print( "El identificador ya esta ocupado con otra sustancia... " )
                    continue
                alcohol = Alcohol( diccionario )
                fila = validarInt( input( "Ingrese le numero de la fila: " ) )
                columna = validarInt( input( "Ingrese la columna del gabinete: " ) )
                peligrosa = validarBoolean( input( "La sustancia es peligrosa si/no: " ) )
                acceso = validarBoolean( input( "La sustancia tiene acceso para estudiantes si/no: " ) )
                tempEbullicion = validarFloat( input( "Ingrese la temperatura de ebullicion: " ) )
                tempArder = validarFloat( input( "Ingrese la temperatura a la que arde: " ) )

                alcohol.sustanciaAsignarIdentificador( identificador )
                alcohol.sustanciaAsignarUbicacion( fila, columna )
                alcohol.sustanciaAsignarPeligrosa( peligrosa )
                alcohol.sustanciaAsignarAcceso( acceso )
                alcohol.alcoholAsignarTempEbullicion( tempEbullicion )                
                alcohol.alcoholAsignarTempArder( tempArder )

            elif opcion1 == '3': # SOLVENTE
                identificador = input( "Ingresa el identificador de la sustancia acido base: " ) + "SOL"
                if sustancia.sistemaVerificarSustancia( identificador ) == True:
                    print( "El identificador ya esta ocupado con otra sustancia... " )
                    continue
                solvente = Solvente( diccionario )
                fila = validarInt( input( "Ingrese le numero de la fila: " ) )
                columna = validarInt( input( "Ingrese la columna del gabinete: " ) )
                peligrosa = validarBoolean( input( "La sustancia es peligrosa si/no: " ) )
                acceso = validarBoolean( input( "La sustancia tiene acceso para estudiantes si/no: " ) )
                naturaleza = input( "Polar o apolar: " )
                viscosidad = validarFloat( input( "Ingrese la viscosidad: " ) )

                solvente.sustanciaAsignarIdentificador( identificador )
                solvente.sustanciaAsignarUbicacion( fila, columna )
                solvente.sustanciaAsignarPeligrosa( peligrosa )
                solvente.sustanciaAsignarAcceso( acceso )
                solvente.solventeAsignarNaturaleza( naturaleza )
                solvente.solventeAsignarViscosida( viscosidad )

            elif opcion1 == '4': # OTROS
                identificador = input( "Ingresa el identificador de la sustancia acido base: " ) + "OTR"
                if sustancia.sistemaVerificarSustancia( identificador ) == True:
                    print( "El identificador ya esta ocupado con otra sustancia... " )
                    continue
                otros = Otro( diccionario )
                fila = validarInt( input( "Ingrese le numero de la fila: " ) )
                columna = validarInt( input( "Ingrese la columna del gabinete: " ) )
                peligrosa = validarBoolean( input( "La sustancia es peligrosa si/no: " ) )
                acceso = validarBoolean( input( "La sustancia tiene acceso para estudiantes si/no: " ) )
                fecha = input( "Ingrese la fecha de ingreso dd/mm/aaaa : " )
                motivo = input( "Ingrese el motivo por el cual ingresa la sustancia: " )
                cantidad = validarFloat( input( "Ingrese la cantidad: " ) )

                otros.sustanciaAsignarIdentificador( identificador )
                otros.sustanciaAsignarUbicacion( fila, columna )
                otros.sustanciaAsignarPeligrosa( peligrosa )
                otros.sustanciaAsignarAcceso( acceso )
                otros.otrosAsignarFecha( fecha )
                otros.otrosAsignarMotivo( motivo )
                otros.otrosAsignarCantidad( cantidad )

        elif opcion == '2': # BUSCAR SUSTANCIA
            id = input( """
            Ingrese el Id que desea buscar, tenga en cuenta, cuando ingrese el numero, posteriormente ingrese las 
            iniciales dependiendo del tipo de sustancia.
            Acido Base (AB)
            Alcohol (A)
            Solvente (SOL)
            Otros (OTR)
            > """ )
        elif opcion == '3': # ELIMINAR SUSTANCIA
            pass 
        elif opcion == '4': # CERRAR PROGRAMA
            print( "Programa cerrado..." )
            break

if __name__ == '__main__':
    main()
