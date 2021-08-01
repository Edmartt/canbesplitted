
class Splitter:

    def canBeSplitted(self, array):
        """
        Este metodo toma un array y lo separa en dos partes.

        Suma los valores existentes en cada una de las partes
        y verifica si la sumatoria de los valores
        es la misma en las dos partes.

        Ejemplo: lista = [1,3,3,8,4,3,2,3,3]

        Al sumar desde el 1 hasta el 8 da 15, esa seria la primera separacion,
        ya que al sumar desde el 4 en adelante tambien da como resultado 15

        [1,3,3,8]=15 [4,3,2,3,3]=15

        :param: array: El array o lista que se debe pasar al método
        :type array: Debe ser un array con valores enteros o puede estar vacio

        :returns: 1 si se puede hacer la separacion, 0 si el array esta vacio
        y -1 si no se puede separar.
        """
        aux = []

        if len(array) == 0:
            return 0

        for key, value in enumerate(array):
            aux.append(value)

            if sum(aux) == sum(array[key+1:]):
                #print(aux, '=', sum(aux), '|||', array[key+1:], '=', sum(array[key+1:]))
                return 1
        return -1

    def print_result(self):
        """
        Imprime en pantalla el resultado de canBeSplitted.

        Pide al usuario ingresar el tamaño del array
        y verifica que sea un dato numerico.
        Luego de la comprobacion pide se ingrese la cantidad de valores
        indicados por el tamaño ingresado e imprime en pantalla el resultado
        obtenido por el metodo canBeSplitted.
        """
        values = []
        size = input('Type the size of the array: ')
        if size.isdigit():
            for initial in range(int(size)):
                number = int(input('Type the value {} of the array: '.format(initial+1)))
                values.append(number)
        else:
            print('The size must be an integer')

        print('Result: ', self.canBeSplitted(values))


#splitter = Splitter()
#splitter.print_Result()
