class Graficas:
    import pandas as pd
    import seaborn as sb
    import matplotlib.pyplot as plt
    newDataFrame=""
    newDataFrame=pd.read_csv('./final.csv')
    newDataFrame['Fecha'] = pd.to_datetime(newDataFrame.Fecha, format='%d/%m/%Y')

    plt.rcParams['figure.figsize'] = (6, 2)
    sb.set()
    def plotConsumption(central):
        meses=[Graficas.newDataFrame.Fecha.dt.month[0]]
        conditionYear =  (Graficas.newDataFrame.Fecha.dt.year == Graficas.newDataFrame.Fecha.dt.year[0])
        dia=Graficas.newDataFrame[conditionYear]
        if meses[0] >0:
            for i in range(0,len(meses)):            
                meses[i]=dia[dia.Fecha.dt.month == meses[i]]

                if i>0:
                    meses[i]=Graficas.pd.concat([meses[i],meses[i-1]],axis=0,  sort=False ).fillna(0)
                    #dia = df1.merge(df2, how='outer').fillna(0)

            
        if central=="Todas":
            Graficas.plt.plot(meses[-1]["Fecha"],meses[-1]["Capacidad promedio realizada MW"],alpha=1) #histograma eje X:numero de clusters, eje Y:scores inertia obtenidos 
        else:
            datosParaGraficarX=meses[-1]["Fecha"]
            datosParaGraficarY=meses[-1][central]
            #Graficas.plt.plot(datosParaGraficarX,datosParaGraficarY,alpha=1)
    
        #Graficas.plt.xlabel('Fecha') #etiqueta del eje X
        #Graficas.plt.ylabel('Consumo en MW') #etiqueta del eje Y
        #Graficas.plt.title('consumo del %s en la central: %s'%(Graficas.newDataFrame.Fecha.dt.year[0],central)) #etiqueta de titulo
        #Graficas.plt.show() #muestra el histograma 
        return datosParaGraficarX,datosParaGraficarY
