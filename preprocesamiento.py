class Preprocessing:
    import pandas as pd
    from graficas import Graficas
    suma=""
    def cargarArchivo(filePath,centrales):
        read_file = Preprocessing.pd.read_excel('%s' % (filePath))
        read_file.to_csv('./archivo.csv', index=None, header=True)
        Preprocessing.extraerCentrales(centrales)

    def extraerCentrales(centrales):
        df = Preprocessing.pd.read_csv('./archivo.csv')
        capacidadRealizada = df[[
            'Día', 'Central', 'Capacidad promedio realizada MW', 'Capacidad promedio prevista MW']]
        capacidadYucatan = capacidadRealizada.loc[(capacidadRealizada['Central'] == 'MDAP1 ') | (capacidadRealizada['Central'] == 'MDPP1 ') | (capacidadRealizada['Central'] == 'MDTP1 ') | (capacidadRealizada['Central'] == 'NCMP1 ') | (capacidadRealizada['Central'] == 'NCMP1 ') | (capacidadRealizada['Central'] == 'NCTP1 ') | (capacidadRealizada['Central'] == 'VADP1 ') | (
            capacidadRealizada['Central'] == 'VLTP1 ') | (capacidadRealizada['Central'] == 'MDAP1') | (capacidadRealizada['Central'] == 'MDPP1') | (capacidadRealizada['Central'] == 'MDTP1') | (capacidadRealizada['Central'] == 'NCMP1') | (capacidadRealizada['Central'] == 'NCMP1') | (capacidadRealizada['Central'] == 'NCTP1') | (capacidadRealizada['Central'] == 'VADP1') | (capacidadRealizada['Central'] == 'VLTP1')]
        capacidadSinCentral = capacidadYucatan[[
            'Día', 'Capacidad promedio realizada MW', 'Central', 'Capacidad promedio prevista MW']]
        capacidadSinCentral.to_csv(
            './soloCentral.csv', index=False)
        Preprocessing.sumarCentrales(centrales)

    def sumarCentrales(centrales):
        soloCentral = Preprocessing.pd.read_csv('./soloCentral.csv')
        Preprocessing.suma = soloCentral.groupby('Día').sum().reset_index()
        Preprocessing.suma = Preprocessing.suma.sort_values(by="Día")
        Preprocessing.suma.to_csv('./sumadas.csv', index=False)
        Preprocessing.setCentralsAsColumns(centrales)

    def setCentralsAsColumns(centrales):
        ## este codigo se encarga de encontrar las centrales y agregarlas en un dataset nuevo como columnas##
        ##se adapto para utilizarse en consumo real y previsto##
        anios = Preprocessing.pd.read_csv('./soloCentral.csv')
        aniosDf = Preprocessing.pd.DataFrame(anios)
        centralMDAP1 = aniosDf[(aniosDf.Central == 'MDAP1')
                               | (aniosDf.Central == 'MDAP1 ')]
        centralVLTP1 = aniosDf.loc[(aniosDf.Central == 'VLTP1') | (
            aniosDf.Central == 'VLTP1 ')]
        centralNCTP1 = aniosDf.loc[(aniosDf.Central == 'NCTP1') | (
            aniosDf.Central == 'NCTP1 ')]
        centralNCMP1 = aniosDf.loc[(aniosDf.Central == 'NCMP1') | (
            aniosDf.Central == 'NCMP1 ')]
        centralMDTP1 = aniosDf.loc[(aniosDf.Central == 'MDTP1') | (
            aniosDf.Central == 'MDTP1 ')]
        centralVADP1 = aniosDf.loc[(aniosDf.Central == 'VADP1') | (
            aniosDf.Central == 'VADP1 ')]
        centralMDAP1.to_csv('./borrameMDAP1.csv', index=False)
        tempMDAP1 = Preprocessing.pd.read_csv('./borrameMDAP1.csv')

        centralMDTP1.to_csv('./borrameMDTP1.csv', index=False)
        tempMDTP1 = Preprocessing.pd.read_csv('./borrameMDTP1.csv')
        
        centralVLTP1.to_csv('./borrameVLTP1.csv', index=False)
        tempVLTP1 = Preprocessing.pd.read_csv('./borrameVLTP1.csv')

        centralNCTP1.to_csv('./borrameNCTP1.csv', index=False)
        tempNCTP1 = Preprocessing.pd.read_csv('./borrameNCTP1.csv')
        
        centralNCMP1.to_csv('./borrameNCMP1.csv', index=False)
        tempNCMP1 = Preprocessing.pd.read_csv('./borrameNCMP1.csv')

        centralVADP1.to_csv('./borrameVADP1.csv', index=False)
        tempVADP1 = Preprocessing.pd.read_csv('./borrameVADP1.csv')

        tempMDAP1 = Preprocessing.pd.read_csv('./borrameMDAP1.csv')
        tempMDTP1 = Preprocessing.pd.read_csv('./borrameMDTP1.csv')
        tempVLTP1 = Preprocessing.pd.read_csv('./borrameVLTP1.csv')
        tempNCTP1 = Preprocessing.pd.read_csv('./borrameNCTP1.csv')
        tempNCMP1 = Preprocessing.pd.read_csv('./borrameNCMP1.csv')
        tempVADP1 = Preprocessing.pd.read_csv('./borrameVADP1.csv')
        nuevoDataFrmeFinal=Preprocessing.pd.DataFrame()
        nuevoDataFrmeFinal.insert(
            0, "Fecha", Preprocessing.suma["Día"])
        nuevoDataFrmeFinal.insert(
            1, "MDAP1", tempMDAP1["Capacidad promedio realizada MW"])
        nuevoDataFrmeFinal.insert(
            2, "MDTP1", tempMDTP1["Capacidad promedio realizada MW"])
        nuevoDataFrmeFinal.insert(
            3, "VLTP1", tempVLTP1["Capacidad promedio realizada MW"])
        nuevoDataFrmeFinal.insert(
            4, "NCTP1", tempNCTP1["Capacidad promedio realizada MW"])
        nuevoDataFrmeFinal.insert(
            5, "NCMP1", tempNCMP1["Capacidad promedio realizada MW"])
        nuevoDataFrmeFinal.insert(
            6, "VADP1", tempVADP1["Capacidad promedio realizada MW"])
        nuevoDataFrmeFinal.to_csv('./final.csv', index=False)
        Preprocessing.Graficas.plotConsumption(2009,[1],centrales)

