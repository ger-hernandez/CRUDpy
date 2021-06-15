#CRUD App - Pendient tasks
def create(tareas, identificador, tareaNueva):
        tareas[identificador] = tareaNueva
        return tareas

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
    if option == 5:
        break

print(tareas)