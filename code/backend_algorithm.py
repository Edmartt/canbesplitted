
class Splitter:

    def __init__(self):
        pass

    def canBeSplitted(self, array):
        aux = []
        if len(array) == 0:
            return 0

        for key, value in enumerate(array):
            aux.append(value)

            if sum(aux) == sum(array[key+1:]):
                #print(aux, '=', sum(aux), '|||', array[key+1:], '=', sum(array[key+1:]))
                return 1
        return -1

    def print_Result(self):
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
