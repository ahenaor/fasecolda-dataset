import requests
from requests.structures import CaseInsensitiveDict
import pandas as pd
from tqdm import tqdm

headers = CaseInsensitiveDict()
headers['Accept'] = 'application/json'
headers['Authorization'] = 'bearer 44EcIjfeZUNZR4Y6DWKIzJkorjHrDipbbACmb3vbnZTSFi9qgNXBKQvzEfC4hgLmKDUSNLDdVED0yIcV1LQJoNE84nRgHgI0noTHvARc57x24cDa6IAXnJo49eJ5nlixozcfk-TEoAOpN0Zy8Ub0sy13_vNHBOkgNa8HawdyUiSXEhZO_NE0f5c2AlF_6ii5obhKvHTjLplrNG_XFLaTt84gLSF-OuyEfGcCMgMzUyVgDaQSCTxLreLg3TD2qO7-1Rn_AiqMimjaAyBfmBHboA'


URL = 'https://guiadevalores.fasecolda.com/apifasecolda/api/'

apiCategoria  = 'categoria'
apiEstado     = 'estadovehiculo/getestadovehiculo/'  # adicionamos el id de la categoria -- /2
apiModelo     = 'modelo/getmodelo/'                  # adicionamos el id de la categoria y estado -- /1/0
apiMarca      = 'marca/getmarca/'                    # adicionamos el id de la categoria, estado y modelo -- /2/0/41006
apiReferencia = 'referenciauno/getgeferenciauno/'    # adicionamos el id de la categoria, estado, modelo y marca -- /2/0/41006/361
apiDetalle    = 'listacodigos/getbuscabasica/'       # adicionamos el id de la categoria, estado, modelo, marca y referencia, al final agregamos un 1 -- /2/0/41006/361/5007-13/1

#-------------- 
rCategoria = requests.get(URL + apiCategoria) # - Consultamos las categorias
dfCategoria = pd.DataFrame(rCategoria.json()) # - Guardamos en dataframe el resultado
dfCategoria = dfCategoria.sort_values('id') # - Ordenamos por id

#--------------
dfEstado = pd.DataFrame(columns=['id','idCategoria', 'nombreCategoria', 'idEstado', 'nombreEstado'])
for i in dfCategoria.index:
    rEstado = requests.get(URL + apiEstado + str(dfCategoria['id'][i]), headers = headers)
    df = pd.DataFrame(rEstado.json())
    df['idCategoria'] =dfCategoria['id'][i] # Agregamos una nueva columna con el id de la categoria como constante
    df['nombreCategoria'] = dfCategoria['nombre'][i] # Agregamos una nueva columna con el nombre de la categoria como constante
    df.rename(columns = {'id':'idEstado', 'nombre':'nombreEstado'}, inplace = True) # Renombramos las columnas
    df['id'] = df['idCategoria'].map(str) + '/' + df['idEstado'].map(str)
    df = df[['id','idCategoria','nombreCategoria','idEstado','nombreEstado']] # Ordenamos las columnas
    dfEstado = pd.concat([dfEstado, df])
dfEstado.index = range(dfEstado.shape[0])

#--------------
dfModelo = pd.DataFrame(columns=['id','idCategoria', 'nombreCategoria', 'idEstado', 'nombreEstado', 'idModelo', 'anioModelo'])
for i in dfEstado.index:
    rModelo = requests.get(URL + apiModelo + str(dfEstado['id'][i]), headers = headers)
    df = pd.DataFrame(rModelo.json())
    df.rename(columns = {'id':'idModelo', 'nombre':'anioModelo'}, inplace = True) # Renombramos las columnas
    df['idCategoria'] = dfEstado['idCategoria'][i]
    df['nombreCategoria'] = dfEstado['nombreCategoria'][i]
    df['idEstado'] = dfEstado['idEstado'][i]
    df['nombreEstado'] = dfEstado['nombreEstado'][i]
    df['id'] = dfEstado['id'][i] + '/' + df['idModelo'].map(str)
    df = df[['id','idCategoria','nombreCategoria','idEstado','nombreEstado', 'idModelo', 'anioModelo']] # Ordenamos las columnas
    dfModelo = pd.concat([dfModelo, df])
dfModelo.index = range(dfModelo.shape[0])

#--------------
dfMarca = pd.DataFrame(columns=['id','idCategoria', 'nombreCategoria', 'idEstado', 'nombreEstado', 'idModelo', 'anioModelo', 'idMarca', 'nombreMarca'])
for i in dfModelo.index:
    rMarca = requests.get(URL + apiMarca + str(dfModelo['id'][i]), headers = headers)
    df = pd.DataFrame(rMarca.json())
    df.rename(columns = {'id':'idMarca', 'nombre':'nombreMarca'}, inplace = True) # Renombramos las columnas
    df['idCategoria'] = dfModelo['idCategoria'][i]
    df['nombreCategoria'] = dfModelo['nombreCategoria'][i]
    df['idEstado'] = dfModelo['idEstado'][i]
    df['nombreEstado'] = dfModelo['nombreEstado'][i]
    df['idModelo'] = dfModelo['idModelo'][i]
    df['anioModelo'] = dfModelo['anioModelo'][i]
    df['id'] = dfModelo['id'][i] + '/' + df['idMarca'].map(str)
    df = df[['id','idCategoria','nombreCategoria','idEstado','nombreEstado', 'idModelo', 'anioModelo', 'idMarca', 'nombreMarca']] # Ordenamos las columnas
    dfMarca = pd.concat([dfMarca, df])
dfMarca.index = range(dfMarca.shape[0])

#--------------
dfReferencia = pd.DataFrame(columns=['id','idCategoria', 'nombreCategoria', 'idEstado', 'nombreEstado', 'idModelo', 'anioModelo', 'idMarca', 'nombreMarca', 'idReferencia', 'nombreReferencia'])
for i in tqdm(dfMarca.index):
    rReferencia = requests.get(URL + apiReferencia + str(dfMarca['id'][i]), headers = headers)
    df = pd.DataFrame(rReferencia.json())
    df.rename(columns = {'id':'idReferencia', 'nombre':'nombreReferencia'}, inplace = True) # Renombramos las columnas
    df['idCategoria'] = dfMarca['idCategoria'][i]
    df['nombreCategoria'] = dfMarca['nombreCategoria'][i]
    df['idEstado'] = dfMarca['idEstado'][i]
    df['nombreEstado'] = dfMarca['nombreEstado'][i]
    df['idModelo'] = dfMarca['idModelo'][i]
    df['anioModelo'] = dfMarca['anioModelo'][i]
    df['idMarca'] = dfMarca['idMarca'][i]
    df['nombreMarca'] = dfMarca['nombreMarca'][i]
    df['id'] = dfMarca['id'][i] + '/' + df['idReferencia'].map(str)
    df = df[['id','idCategoria','nombreCategoria','idEstado','nombreEstado', 'idModelo', 'anioModelo', 'idMarca', 'nombreMarca', 'idReferencia', 'nombreReferencia']] # Ordenamos las columnas
    dfReferencia = pd.concat([dfReferencia, df])
dfReferencia.index = range(dfReferencia.shape[0])

#---------------
dfDetalle = pd.DataFrame(columns=['id','idCategoria', 'nombreCategoria', 'idEstado', 'nombreEstado', 'idModelo', 'anioModelo', 'idMarca', 'nombreMarca', 'idReferencia', 'nombreReferencia'
                                , 'idDetalle', 'consecutivo', 'codigo', 'cilindraje', 'importadoMostrar', 'peso', 'pesoCategoria', 'potencia', 'capacidadPasajeros', 'capacidadCarga','puertas'
                                , 'aireAcondicionadoMostrar', 'tipoAireAcondicionado', 'ejes','novedad', 'observacion', 'bcpp', 'camaraReversaMostrar', 'exploradorasMostrar', 'sensoresMostrar'
                                , 'sistemaAlimentacion', 'sunroofMostrar', 'suspensiontrasera', 'tacometro', 'tipoDireccion', 'tipoFaros', 'traccion', 'absMostrar', 'sillasElectricas'
                                , 'vidriosElectricos', 'airbags', 'espejosElectricos', 'tapiceriaCueroMostrar', 'largo', 'segmentoTamaño', 'segmentoCilindraje', 'grupoActualizacion'
                                , 'homoloCodigo', 'um', 'marca', 'clase', 'referenciaUno', 'referenciaDos', 'referenciaTres', 'nacionalidad', 'servicio', 'combustible', 'tipoCaja'
                                , 'transmision', 'frenos', 'categoria', 'tipologia', 'valor', 'modelo', 'modeloId', 'estadoVehiculo', 'codigoFoto'])

for i in tqdm(dfReferencia.index):
    rDetalle = requests.get(URL + apiDetalle + str(dfReferencia['id'][i]) + '/1', headers = headers)
    df = pd.DataFrame(rDetalle.json())
    df.rename(columns = {'id':'idDetalle'}, inplace = True) # Renombramos las columnas
    df['idCategoria'] = dfReferencia['idCategoria'][i]
    df['nombreCategoria'] = dfReferencia['nombreCategoria'][i]
    df['idEstado'] = dfReferencia['idEstado'][i]
    df['nombreEstado'] = dfReferencia['nombreEstado'][i]
    df['idModelo'] = dfReferencia['idModelo'][i]
    df['anioModelo'] = dfReferencia['anioModelo'][i]
    df['idMarca'] = dfReferencia['idMarca'][i]
    df['nombreMarca'] = dfReferencia['nombreMarca'][i]
    df['idReferencia'] = dfReferencia['idReferencia'][i]
    df['nombreReferencia'] = dfReferencia['nombreReferencia'][i]
    df['id'] = dfReferencia['id'][i] + '/1'
    df = df[['id','idCategoria', 'nombreCategoria', 'idEstado', 'nombreEstado', 'idModelo', 'anioModelo', 'idMarca', 'nombreMarca', 'idReferencia', 'nombreReferencia', 'idDetalle', 'consecutivo', 'codigo', 'cilindraje', 'importadoMostrar', 'peso', 'pesoCategoria', 'potencia', 'capacidadPasajeros', 'capacidadCarga','puertas', 'aireAcondicionadoMostrar', 'tipoAireAcondicionado', 'ejes','novedad', 'observacion', 'bcpp', 'camaraReversaMostrar', 'exploradorasMostrar', 'sensoresMostrar', 'sistemaAlimentacion', 'sunroofMostrar', 'suspensiontrasera', 'tacometro', 'tipoDireccion', 'tipoFaros', 'traccion', 'absMostrar', 'sillasElectricas', 'vidriosElectricos', 'airbags', 'espejosElectricos', 'tapiceriaCueroMostrar', 'largo', 'segmentoTamaño', 'segmentoCilindraje', 'grupoActualizacion', 'homoloCodigo', 'um', 'marca', 'clase', 'referenciaUno', 'referenciaDos', 'referenciaTres', 'nacionalidad', 'servicio', 'combustible', 'tipoCaja', 'transmision', 'frenos', 'categoria', 'tipologia', 'valor', 'modelo', 'modeloId', 'estadoVehiculo', 'codigoFoto']] # Ordenamos las columnas
    dfDetalle = pd.concat([dfDetalle, df])
dfDetalle.index = range(dfDetalle.shape[0])

#---------------Exportar data cruda en csv, json y xlsx
dfDetalle.to_csv('raw-data/output-raw-fasecolda.csv', sep=';')
dfDetalle.to_json('raw-data/output-raw-fasecolda.json')
dfDetalle.to_excel("raw-data/output-raw-fasecolda.xlsx",sheet_name='raw-data')