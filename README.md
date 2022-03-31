# fasecolda-dataset
En este repositorio se aloja un pequeño proyecto de extracción de datos el cual consiste en construir un dataseet con datos históricos de la guía de valores de automóviles y motocicletas de la Federación de Aseguradores Colombianos -FASECOLDA-.

El objetivo del proyecto es disponibilizar los datos en crudo para que sean utilizado en ejercicios de aprendizaje de analítica de datos.

## Datos del Repositorio
La extracción de los datos se realizó a través de un script de python el cual realiza consultas requests a las diferentes APIs que alojan la información.

La información se encuentra disponible para su consulta a través del siguiente [LINK](https://fasecolda.com/guia-de-valores/) a través de listas desplegables donde se puede hacer una busqueda básica y filtrar la información por **categoria, estado, modelo, marca y referencia.**

A través de las herramientas de desarrollador del navegador web, identificamos las direcciones de las APIs e identificamos los Request Headers necesarios para hacer las consultas a las APIs. En concreto, identificamos un **authorization bearer** que copiamos y pegamos al script para garantizar respuestas 200 en las diferentes consultas.

Los datos extraídos fueron exportados en formato **CSV -separados por ;-, y .XLSX** 

Inicialmente se planteó la posiblidad de disponibilizar los datos en formato JSON sin embargo su tamaño excedía los límites dispuestos por Github por tanto se omitió el cargue de este archivo, aunque en el script se encuentra codigicada la exportación en formato JSON.


## 💻 Requisitos para ejecutar el script
Si su intención es ejecutar el script en su máquina local es importante tener en cuenta lo siguiente:

* Actualizar el **authorization bearer**, el cual puede consultar ingresando a este [LINK](https://fasecolda.com/guia-de-valores/), clic derecho en inspeccionar, clic en Network, realizar un primer filtro en los filtros de la página y finalmente inspeccionar el último requests que aparece en la consola, allí ir al apartado de Headers/Request Headers.

* En términos de librerías, el script utiliza requests, pandas y tqdm las cuales debe instalarser previamente para garantizar su correcto funcionamiento.

* Finalmente, es importanet indicar que el script realiza una gran cantidad de consultas a las API por lo que su tiempo de ejecución dependerá de las interacciones por segundos que pueda procesar su máquina. Para que tengan una referencia, mi máquina tomó al rededor de 3 horas en terminar la ejecución del script.

## 🚀 Siguientes pasos
El objetivo como tal del repositorio esta cumplido al disponibilizar los datos en crudo de fasecolda. Sin embargo, con el ánimo de seguirle dando vida y valor a este dataset, a continuación se proponen objetivos adicionales que espero en un futuro desarrollar y que a la vez insito a cualquiera que se tome con este repositorio que los pueda desarrollar a modo de ejercicio práctico:

* Actualizar el script de python agregando manejo de errores y desarrollando funciones que logren optimizar el código.
* separar el dataset en dos: uno para autmóviles y otro para motocicletas.
* Limpiar el dataset utilizando la librería PANDAS o utilizando el lenguaje R.
* Realizar un análisis de datos a través de estadística descriptiva del dataset.
* Otros objetivos que quieras plantear.

## 📝 Licencia
[MIT](https://choosealicense.com/licenses/mit/)
