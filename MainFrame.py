import PySimpleGUI as sg
centralesOptions = ['TODAS', 'MDAP1', 'MDPP1',
                    'VLTP1', 'NCTP1', 'NCMP1', 'MDTP1', 'VADP1']
years=['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
months=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
sg.theme('Dark Blue 3')

tab2 = [[sg.Text('      Seleccione Central Eléctrica:', font=("Arial", 15))],
        [sg.Text('Central Eléctrica', font=("Arial", 10)), sg.Combo(
            centralesOptions, enable_events=True, key='combo', size=(10, 1))],
        [sg.Text('   Basar Predicciones en el Periodo:', font=("Arial", 15))],
        [sg.Text('Seleccione fecha de inicio ', font=("Arial", 10)), sg.Input(key='dateStart', size=(
            10, 1)), sg.CalendarButton('Fecha Inicio', target=(3, 1), key='dateStart')],
        [sg.Text('Seleccione fecha de fin    ', font=("Arial", 10)), sg.Input(key='dateEnd', size=(
            10, 1)), sg.CalendarButton(' Fecha Fin  ', target=(4, 1), key='dateEnd')],
        [sg.Text('Ingrese No. de Predicciones', font=("Arial", 10)), sg.Input(key='dateStart', size=(
            10, 1))],
        [sg.Text('Predecir consumo energético para:', font=("Arial", 15))],
        [sg.Output(key='-IN-', size=(30, 15))],
        [sg.Button('Predecir')],
        [sg.Text('Predicciones:', font=("Arial", 15))],
        [sg.Output(key='-IN-', size=(30, 10))],
        [sg.Button('Nueva Prediccion')]]
tab1 = [[sg.T('Visualización de los datos', font=("Arial", 15))],
        [sg.Text('Marque las centrales :', font=("Arial", 10))],
        [sg.Checkbox('MDAP1'), sg.Checkbox('MDPP1'), sg.Checkbox('VLTP1'), sg.Checkbox(
            'NCTP1'), sg.Checkbox('NCMP1'), sg.Checkbox('MDTP1'), sg.Checkbox('VADP1')],
        [sg.Text('Periodo:', font=("Arial", 10))],
        [sg.Text('De', font=("Arial", 10)), sg.Combo(
            years, enable_events=True, key='combo', size=(10, 1)),sg.Text('', font=("Arial", 10)), sg.Combo(
            months, enable_events=True, key='combo', size=(10, 1)),
            sg.Text('Al', font=("Arial", 10)), sg.Combo(
            years, enable_events=True, key='combo', size=(10, 1)),sg.Text('', font=("Arial", 10)), sg.Combo(
            months, enable_events=True, key='combo', size=(10, 1)),sg.Button('Generar')
            

        ] ,[sg.Text('Grafica:', font=("Arial", 15))],[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],[sg.Text('')],
         [sg.Text('Mapa de Calor:', font=("Arial", 15))]
       
            ]

layout = [[sg.TabGroup([[sg.Tab('Visualización Datos', tab1), sg.Tab('Predicción', tab2)]])]
          ]
window = sg.Window('CONSUMO ENERGETICO', layout)
while True:
    event, values = window.read()
    print(event)

window.close()
