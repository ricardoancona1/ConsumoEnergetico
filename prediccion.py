from numpy import loadtxt
from keras.models import load_model
from random import randrange
import pandas
import numpy
from sklearn.preprocessing import MinMaxScaler 
import matplotlib.pyplot as plt
class Prediccion:
    def predecir(fechaInicio,numPredicciones):
        
        # load model
        model = load_model('./modelo_entrenado')
        # summarize model
        
        dataframe = pandas.read_csv('./nuevoDF6.csv',  parse_dates=[0], header=None,index_col=0, squeeze=True,usecols=[0,16],names=['fecha','unidades'])#lee la columna 2 del dataset
        ultimosDias = dataframe['2015-12-02':'2015-12-31']
        ultimosDias=ultimosDias.values.astype('float64')
        
        fecha1=pandas.datetime.strptime("2015-12-31", "%Y-%m-%d").date()
        fecha2=pandas.datetime.strptime(fechaInicio, "%Y-%m-%d").date()
        fecha3=fecha2-fecha1
        numeroPredicciones=int(fecha3.days)+int(numPredicciones)
        
        #numeroPredicciones=365
        nuevasPredicciones=[]
        ultimosDias=numpy.reshape(ultimosDias, (1, 1, ultimosDias.shape[0]))
        for i in range(0,numeroPredicciones):
            paraPredecir=[[[]]]
            for i in range(0,30):
                paraPredecir[0][0].append(ultimosDias[0][0][randrange(len(ultimosDias[0][0]))])
  
            prediccion=model.predict(paraPredecir)
            numpy.append(ultimosDias,prediccion[0][0])
            nuevasPredicciones.append(prediccion[0][0])
            scaler = MinMaxScaler(feature_range=(0, 1))
            dataset=dataframe
            dataset = dataset[1:].astype('float64') #solo toma los valores  remueve las etiquetas  y castea a  float64
            dataset=pandas.DataFrame(dataset)
            dataset=dataset.dropna()
            dataset = dataset[1:].astype('float64') 
            dataset = scaler.fit_transform(dataset)
        nuevasPredicciones = scaler.inverse_transform([nuevasPredicciones])


        return nuevasPredicciones[0][numeroPredicciones-int(numPredicciones):]