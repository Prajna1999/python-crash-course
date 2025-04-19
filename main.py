def create_dictionary():
    spanish=dict()
    spanish["hello"]="hola"
    spanish['hello'] = 'hola'
    spanish['yes'] = 'si'
    spanish['one'] = 'uno'
    spanish['two'] = 'dos'
    spanish['three'] = 'tres'
    spanish['red'] = 'rojo'
    spanish['black'] = 'negro'
    spanish['green'] = 'verde'
    spanish['blue'] = 'azul'
    
    return spanish
  
  
def main():
    # x = 20
    # y = 30
    # sum = x + y
    # prod = x * y
    # formatStr = '{x} + {y} = {sum}; {x} * {y} = {prod}.'
    # # takes all the local variables and makes them into dictionary with key:value 
    # equations = formatStr.format(**locals())
    # print(locals())
    def listOnOneLine(items):
        for item in items:
            print(item, end=' ')
        # print()

    listOnOneLine(['apple', 'banana', 'pear'])
    print('This may not be what you expected!', end=' ')
    print('This is the third line')


if __name__ == "__main__":
    main()
    
