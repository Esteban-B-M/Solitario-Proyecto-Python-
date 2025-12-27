from core.Clase_Carta import Cartas
from core.Baraja_Inglesa import Inglesa
from core.Clase_Mano import Mano

class Solitario:

    #Tendre que eliminar y recuperar nombres varias veces asi que un diccionario como el de inglesa sera util
    Nombres_decartas = {
        1:"As",
        11:"Jota",
        12:"Reina",
        13:"Rey",
    }


    def  Inicializar_Columnas(self, baraja):
        """Metodo que busca llenar las columnas con la baraja, cada columna recibe tantas cartas como su numero de columna
        Ademas, devuelve una lista llamada columnas para self._columnas

        Cada Columna es a su vez una especie de Mano
        """

        columnas = []

        for n in range(1,8):
            
            columnas.append(Mano(baraja,n))

        return columnas
    def __init__(self):
        #Baraja y Mano del usuario
        self._stock = Inglesa()
        self._stock.Barajar()
        self._Mano_Usuario=Mano(self._stock,0)

        # Pila de descarte, una baraja nueva inicialmente vacía
        self._descarte = Inglesa(True)

        #Fundaciones
        self._fundaciones = {
            "Corazones": Inglesa(True),
            "Diamantes": Inglesa(True),
            "Tréboles": Inglesa(True),
            "Picas": Inglesa(True)
        }

        #Columnas o en verdad manos del juego con tantas cartas como su numero de columna, guardadas en una lista
        self._columnas=self.Inicializar_Columnas(self._stock)

    def visibilidad_inicial(self,Columna:Mano):
        """Define las condiciones inciales de las columnas al tapar todas las cartas menos la de encima, la ultima
        
        recibe:
        Columna(Mano): La columna que deseamos tapar
        """
        if len(Columna) == 0:
            return
        for n in range(len(Columna)-1):
            Columna._mano[n].cambiar_nombre("Tapada")
    
    def actualizar_visibilidad(self,Columna:Mano):
        """Revisa si la carta que deberia ser visible de la columna lo esta, si no lo esta. recostruye su nombre
        apartir de su valor para que vuelva a ser visible
        
        recibe:
        Columna(Mano): La columna que deseamos revisar
        """

        if len(Columna) == 0:
            return
        destapada=Columna._mano[-1]
        if destapada.ver_nombre()=="Tapada":
            valor = destapada.ver_valor()
            nombre = self.Nombres_decartas.get(valor,str(valor))
            destapada.cambiar_nombre(nombre)

    def diferente_color(self,carta1:Cartas,carta2:Cartas):
        """Metodo que verifica si dos cartas son de diferente color osea, si una pertence a diamantes o corazones
        y la otra a treboles y picas, este metodo esta pensado para la baraja inglesa
        
        recibe 2 cartas de tipo carta
        
        devuelve un booleano True/False
        """
        rojas = ["Corazones", "Diamantes"]
        negras = ["Tréboles", "Picas"]

        return ( 
            (carta1.ver_palo() in rojas and carta2.ver_palo() in negras) or
            (carta1.ver_palo() in negras and carta2.ver_palo() in rojas)
        )
    
    def movimiento_validoUna(self,Carta:Cartas,Columna_receptora:int):
        """Detecta si una carta puede cambiarse de la mano del jugador o una columna a otra columna

        Argumentos:
        Columna_receptora(int): Valor entre 1 y 7 que señaliza la columna hacia la que va la carta
        Carta(Carta): Es la carta o cartas que viajan entre columnas

        Devuelve:
        Validez(Booleano):Valor True o False que permite a otros metodos usar este para permitir cambios
           """
        Columna_receptora -= 1
        if not Columna_receptora in range (0,7):
            raise ValueError("Columna_receptora debe estar entre 1 y 7")
        
        receptora=self._columnas[Columna_receptora]
        tamaño=len(receptora)
       
        #Columna vacia, solo entra el rey
        if not receptora._mano:
            return Carta.ver_valor()==13
        
        carta_superior=receptora[tamaño-1]

        if Carta.ver_valor() == carta_superior.ver_valor() - 1 and self.diferente_color(Carta,carta_superior):
            return True
        else:
            return False
    
    def movimiento_validoVarias(self,Lista:list[Cartas],Columna_receptora:int):
            """Detecta si una carta o varias pueden cambiarse de la mano del jugador (o una columna) a otra columna

        Argumentos:
        Columna_receptora(int): Valor entre 1 y 7 que señaliza la columna hacia la que va la carta
        Carta(Carta): Es la carta o cartas que viajan entre columnas

        Devuelve:
        Validez(Booleano):Valor True o False que permite a otros metodos usar este para permitir cambios
           """
            return self.movimiento_validoUna(Lista[0],Columna_receptora)

    def cambiar_columna(self,Columna_actual:int,Lista:list[Cartas],Columna_receptora:int):
        """Metodo que traspasa una carta de una columna a otra
        Argumentos:
            Columna_actual(int): Valor entre 1 y 7 que señaliza la columna actual en la que se encuentra la carta
            Columna_receptora(int): Valor entre 1 y 7 que señaliza la columna hacia la que va la carta
            Carta(Carta): Es la carta que viaja entre columnas
           """
        
        Columna_receptora -= 1
        Columna_actual -= 1
        if not Columna_receptora in range (0,7) or not Columna_actual in range(0,7):
            raise ValueError("Las columnas deben estar entre 1 y 7")
        
        Actual = self._columnas[Columna_actual]
        Receptora = self._columnas[Columna_receptora]
        if self.movimiento_validoVarias(Lista,Columna_receptora+1):
            Actual.dar(Lista,Receptora)
            return True
        else:
            return False
        
    def mover_a_columna(self,Lista:list[Cartas],Columna_receptora:int):
        """Metodo que traspasa una carta de la mano del usuario a una columna
        Argumentos:
            Columna_receptora(int): Valor entre 1 y 7 que señaliza la columna hacia la que va la carta
            Carta(Carta): Es la carta que viaja entre columnas
           """
        
        Columna_receptora -= 1
        if not Columna_receptora in range (0,7):
            raise ValueError("La columna deben estar entre 1 y 7")
        
        Receptora = self._columnas[Columna_receptora]
        if self.movimiento_validoVarias(Lista,Columna_receptora+1):
            self._Mano_Usuario.dar(Lista,Receptora)
            return True
        else:
            return False
    
    def Reponer_stock(self):
        """Metodo que saca las cartas de la pila de descartes y vuelve a ponerlas en la pila de stock"""
        self._descarte.dar(self._descarte[::-1],self._stock)
    
    def Recuperar_descarte(self):
        """Metodo para recuperar el ultimo descarte agregado a la baraja de descartes"""
        if len(self._descarte) > 0:
            self._Mano_Usuario.pedir_y_ubicar(self._descarte,1)

    def pedir_stock(self):
        """Metodo para pedirle una carta al stock
        
        si el metodo retorna False es porque el stock no tiene cartas y debe rellenarse con los descartes
        retornara True en una operacion exitosa"""

        if len(self._stock) > 0:
            self._Mano_Usuario.pedir(self._stock,1)
            return True
        else:
            return False
    def Valido_Fundacion(self,carta:Cartas):
        """Verifica si la carta puede ser colocada en su fundación correspondiente.
        devuelve un booleano, True o False"""
        palo = carta.ver_palo()
        fundacion = self._fundaciones[palo]

        if len(fundacion) == 0:
            return carta.ver_valor() == 1  # Solo vale el As
        else:
            carta_tope = fundacion[-1]
            return carta.ver_valor() == carta_tope.ver_valor() + 1
        
    def hacia_fundacion(self, carta:Cartas,Origen:Mano):
        """Metodo que comprueba si una carta es valida para una fundacion
        devuelve False en caso de que no se cumplan las condiciones y True en caso contrario"""
        
        if self.Valido_Fundacion(carta):
            palo = carta.ver_palo()
            self._fundaciones[palo].agregarCarta(carta)
            Origen.eliminarCarta(carta)
            return True
        else:
            return False
        
    def Victoria(self):
        """Revisa que las fundiciones esten llenas cada una con sus respectivas 13 cartas, en ese caso
        devuelve True
        """
        Contador=4
        for fundacion in self._fundaciones.values():
            if len(fundacion) == 13:
                Contador-=1
        
        if Contador==0:
            return True
        else:
            return False
  
    def ver_estado(self):
        print("\n--------estado actual del juego--------")
        print(f"stock: {len(self._stock)} cartas.")
        print(f"descartes: {len(self._descarte)} cartas.")
        print(f"Mano del usuario {[str(carta) for carta in self._Mano_Usuario]}.")


        print(f"\nColumnas")
        for i, col in enumerate(self._columnas):
            
            cartas = [
                str(carta) if carta.ver_nombre() != "Tapada" else "Tapada"
                for carta in col ]
            print(f"Columna {i+1}: {cartas}")


        print(f"\nFundaciones")
        for palo, fund in self._fundaciones.items():
            print(f"{palo}: {fund[-1] if len(fund) > 0 else 'Vacía'}")


        
    def jugar(self):
        """Bucle donde se ejecuta el juego Solitario"""
        self.visibilidad_inicial(self._columnas[0])
        self.visibilidad_inicial(self._columnas[1])
        self.visibilidad_inicial(self._columnas[2])
        self.visibilidad_inicial(self._columnas[3])
        self.visibilidad_inicial(self._columnas[4])
        self.visibilidad_inicial(self._columnas[5])
        self.visibilidad_inicial(self._columnas[6])
        while not self.Victoria():
            self.ver_estado()
            print("\nOpciones:")
            print("1. Pedir carta del stock")
            print("2. Mover carta(s) entre columnas")
            print("3. Mover carta a fundación")
            print("4. Mover carta desde mano a columna")
            print("5. Salir del juego")

            opcion = input("Elija una opción: ")

            if opcion == "1":
                if len(self._Mano_Usuario)==3:
                    if self.pedir_stock():
                        descartada= self._Mano_Usuario.eliminarCarta(self._Mano_Usuario[0])
                        self._descarte.agregarCarta(descartada)
                        print("Se ha añadido una nueva carta y descartado la mas vieja")
                    else:
                        self.Reponer_stock()
                        print("se ha repuesto el stock, apartir de los descartes")
                else:
                    if self.pedir_stock():
                        print("Se ha añadido una nueva carta")
                    else:
                        self.Reponer_stock()
                        print("se ha repuesto el stock, apartir de los descartes")
            
            elif opcion == "2":
                try:
                    col_origen = int(input("Columna origen (1-7): "))
                    col_destino = int(input("Columna destino (1-7): "))
                    cantidad = int(input("Cuántas cartas desea mover: "))

                    if col_origen not in range(1, 8) or col_destino not in range(1, 8):
                        print("Las columnas deben estar entre 1 y 7.")
                        continue

                    mano = self._columnas[col_origen - 1]

                    if cantidad > len(mano):
                        print("Cantidad demasiado alta.")
                        continue

                    # Suponiendo que ver_nombre es método
                    if mano[-cantidad].ver_nombre() == "Tapada":
                        print("No puedes mover cartas tapadas.")
                        continue

                    cartas_a_mover = mano[-cantidad:]

                    if self.cambiar_columna(col_origen, cartas_a_mover, col_destino):
                        self.actualizar_visibilidad(mano)
                    else:
                        print("Movimiento no válido.")
                except ValueError:
                    print("Por favor ingresa números válidos.")
                except Exception as fallo:
                    print(f"Error inesperado: {fallo}")

            elif opcion == "3":
                try:
                    zona = input("¿Desde qué zona? (mano/columna): ").lower()
                    if zona == "mano":
                        if len(self._Mano_Usuario) == 0:
                            print("No hay cartas en la mano.")
                            continue
                        carta = self._Mano_Usuario[-1]
                        exito = self.hacia_fundacion(carta, self._Mano_Usuario)
                        if exito:
                            print("Carta movida a fundación.")
                            if len(self._descarte) != 0:
                                self.Recuperar_descarte()
                                print("Se ha recuperado el descarte mas reciente")
                        else:
                            print("No se puede mover a fundación.")

                    elif zona == "columna":
                        col = int(input("Número de columna (1-7): "))
                        if not col in range(1,8):
                            print("Número de columna inválido.")
                            continue
                        columna = self._columnas[col - 1]
                        if len(columna) == 0:
                            print("Columna vacía.")
                            continue
                        carta = columna[-1]
                        if self.hacia_fundacion(carta, columna):
                            self.actualizar_visibilidad(columna)
                            print("Carta movida a fundación.")
                        else:
                            print("No se puede mover a fundación.")

                    else:
                        print("Zona no válida.")
                        continue
                except Exception as fallo:
                    print(f"Error: {fallo}")

            elif opcion == "4":
                try:
                    if len(self._Mano_Usuario) == 0:
                        print("No hay cartas en la mano para mover.")
                        continue
                    
                    col_destino = int(input("Columna destino (1-7): "))
                    if col_destino not in range(1, 8):
                        print("Número de columna inválido.")
                        continue

                    carta = self._Mano_Usuario[-1]  
                    cartas_a_mover = [carta]

                    if self.mover_a_columna(cartas_a_mover, col_destino):
                        self.actualizar_visibilidad(self._columnas[col_destino - 1])
                        print(f"Carta {carta} movida a la columna {col_destino}.")

                        if len(self._descarte) != 0:
                            self.Recuperar_descarte()
                            print("Se ha recuperado el descarte mas reciente")
                    else:
                        print("Movimiento no válido.")
                except ValueError:
                    print("Por favor ingresa un número válido para la columna.")
                except Exception as fallo:
                    print(f"Error inesperado: {fallo}")
            elif opcion == "5":
                print("Juego terminado por el usuario.")
                break
            else:
                print("Opción no válida.")

        if self.Victoria():

            print("¡Felicidades! Has ganado el Solitario.")
