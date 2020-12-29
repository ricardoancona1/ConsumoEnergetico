from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class MainFrame:
    import PySimpleGUI as sg
    import matplotlib.pyplot as plt
    from graficas import Graficas
    from preprocesamiento import Preprocessing
    from Heatmap import Heatmap
    from prediccion import Prediccion

    def draw_figure_w_toolbar(canvas, fig):
        if canvas.children:
            for child in canvas.winfo_children():
                child.destroy()
        figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
        figure_canvas_agg.draw()

        figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)
    
    centralesOptions = ['-Seleccione-', 'MDAP1', 'MDPP1',
                        'VLTP1', 'NCTP1', 'NCMP1', 'MDTP1', 'VADP1']
    years = ['2006', '2007', '2008', '2009', '2010',
             '2011', '2012', '2013', '2014', '2015']
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
              'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    sg.theme('Dark Blue 3')
    excel = sg.FileBrowse(key="filePath")
    centralesGUI1 =  sg.Combo(centralesOptions, enable_events=False, key='combo')
    centralesGUI2=sg.Combo(centralesOptions, enable_events=False, key='comboCentrales')
    tab2 = [

            [sg.Text('Seleccione fecha de inicio ', font=("Arial", 10)), sg.Input(key='dateStartField', size=(
                10, 1)), sg.CalendarButton('Fecha Inicio', target=(0, 1), key='dateStart', format='%Y-%m-%d')],

            [sg.Text('Ingrese No. de Predicciones', font=("Arial", 10)), sg.Input(key='numPredicciones', size=(
             10, 1))],
            [sg.Button('Predecir')],
            [sg.Text('Predicciones:', font=("Arial", 15))],
            [sg.Output(key='PrediccionesOut', size=(30, 10))],
            [sg.Button('Nueva Prediccion',key="nuevaPrediccion")]]
    tab1 = [[sg.In(), excel],
            [sg.Text('Seleccione Central Eléctrica:', font=("Arial", 15)),centralesGUI2],
            [sg.Button('Generar',key="Generar")], [sg.Text('Grafica:', font=("Arial", 15))],
            [sg.Canvas(key='fig_cv', size=(150 * 2, 150))]
        ,
        [sg.Text('Mapa de Calor:', font=("Arial", 15))],
        [sg.Canvas(key='fig_cv2', size=(150 * 2, 150))]

    ]

    layout = [[sg.TabGroup([[sg.Tab('Visualización Datos', tab1), sg.Tab('Predicción', tab2)]])]
              ]
    window = sg.Window('CONSUMO ENERGETICO', layout)
    while True:
        event, values = window.read()
        try:
            if event=="Generar":
                
                Preprocessing.cargarArchivo(values["filePath"])
                graficaX,graficaY=Graficas.plotConsumption(values["comboCentrales"])
            ####matplotlib#####
                plt.figure(1)
                plt.clf()
                fig = plt.gcf()
                DPI = fig.get_dpi()
            # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
                plt.rcParams['figure.figsize'] = (6, 3)
            # -------------------------------
                x = graficaX
                y = graficaY
                plt.plot(x, y)
                Graficas.plt.xlabel('Fecha') #etiqueta del eje X
                Graficas.plt.ylabel('Consumo en MW') #etiqueta del eje Y
                Graficas.plt.tight_layout()
                Graficas.plt.title('consumo de la central %s'%(values["comboCentrales"])) #etiqueta de titulo
                plt.grid()
                plt.figure(2)
                Heatmap.plt1.clf()
                fig2 = plt.gcf()
                DPI = fig2.get_dpi()
                draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig)
                heatmap_data=Heatmap.showHeatMap(values["comboCentrales"])
                Heatmap.sns.heatmap(heatmap_data)
                Heatmap.plt1.xlabel("dia del mes", size=14)
                Heatmap.plt1.ylabel("mes", size=14)
                Heatmap.plt1.title(" Capacidad promedio realizada 2009 promedio en MW", size=14)
                Heatmap.plt1.tight_layout()
                Heatmap.plt1.savefig('./heatmap_with_Seaborn_python.jpg',dpi=160, figsize=(9,6))
            ####/matplotlib####
            
                draw_figure_w_toolbar(window['fig_cv2'].TKCanvas, fig2)
            if event=="Predecir":
                numPredicciones=values["numPredicciones"]
                fechaInicio=values["dateStartField"]
                predicciones=Prediccion.predecir(fechaInicio,numPredicciones)
                for i in range(0,len(predicciones)):
                    print(predicciones[i])
                
                #values['PrediccionesOut']=predicciones
            if event=="nuevaPrediccion":
                window['PrediccionesOut'].update('')
                window['numPredicciones'].update('')
                window['dateStartField'].update('')
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
        except Exception as e:
            sg.Print(e)