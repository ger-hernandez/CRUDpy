#CRUD App - Pendient tasks
def create(tareas, identificador, tareaNueva):
    tareas[identificador] = tareaNueva
    return tareas

def read(tareas):
    for identificador in tareas.items():
        print(identificador, '-', end='')
        for nombre_atributo, atributo in tareas.items():
            print(atributo, '-', end='')
            print()

def estaElemento(tareas, identificador):
    conjunto = set(tareas.keys())
    return identificador in conjunto

tareas = {
    '01': {
        'descripcion': 'Ir a mercar',
        'estado': 'pendiente',
        'tiempo': 60
    },
    '02' : {
        'descripcion': 'Estudiar',
        'estado': 'pendiente',
        'tiempo': 180
    },
    '03': {
        'descripcion': 'Hacer ejercicio',
        'estado': 'pendiente',
        'tiempo': 50
    }
}


while(True):

    title = 'CRUD APP: To Do Tasks'.center(50, '-')
    print(title)
    options = ('adicionar tarea', 'consultar tarea', 
    'actualizar tarea', 'eliminar tarea', 'salir')

    for index, value in enumerate(options, start=1):
        print(f'{index}. {value.title()}')

    option = int(input('ingrese una opcion: '.capitalize()))
    #create
    if(option == 1):
        print()
        print('adicionando tarea'.title().center(50, '-'))
        identificador = input('ingrese identificador de la tarea: '.title())
        descripcion = input('ingrese descripcion de la tarea: '.title())
        estado = input('ingrese estado de la tarea: '.title())
        tiempo = int(input('ingrese el tiempo de realizacion. '.title()))

        tareaNueva = {
            'descripcion': descripcion,
            'estado': estado,
            'tiempo': tiempo
        }

        tareas = create(tareas, identificador, tareaNueva)
    elif(option == 2):
        print()
        print('listado de tareas'.title().center(50, '-'))
        print()
        read(tareas)
    elif(option == 3):
        print()
        print('actualizar tarea'.title().center(50, '-'))
        identificador = input('ingrese identificador  de la tarea a modificar'.title())
        if(estaElemento(tareas, identificador)):
            new_description = input('inserte nueva descripcion'.title())
            tareas[identificador]['descripcion'] = new_description
            new_status = input('inserte nuevo estado'.title())
            tareas[identificador]['estado'] = new_status
            new_time = int(input('ingrese nuevo tiempo'.title()))
            tareas[identificador]['tiempo'] = new_time
        else:
            print('Esa Tarea no Existe')
    elif(option == 4):
        pass
    elif option == 5:
        break
print(tareas)
