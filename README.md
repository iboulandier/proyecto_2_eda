# proyecto_2_eda
EDA: ¿Incide el turismo en el precio de la vivienda?

## Objetivo
En este EDA se explorar, con data sets de referencia, si existe alguna correlación entre el **crecimiento del turismo receptivo** y la **evolución del precio de la vivienda** a nivel mundial. El análisis exploratorio de datos (EDA) lo he filtrado y depurado con Python y diversas librerías (Numpy, Pandas, Seaborn, Matplotlib...)

En este caso, el **turismo receptivo** (*inbound tourism*) es el de los visitantes no residentes que llegan a un país desde el extranjero, y pernoctan al menos una noche.

## Hipótesis principal

> **¿Los países donde más crece el turismo receptivo son también los países donde más sube el precio de la vivienda?**

La lógica es que más turistas aumentan la demanda de alojamiento, no solo a nivel hotelero, sino también extrahotelero (con el impulso de vivienda vacacional, alquileres de temporada, colivings, segunda residencia, multipropiedad, home sharing...). Este aumento de la demanda, podría presionar los precios al alza. 

Este trabajo no pretende demostrar que el turismo cause la subida de la vivienda. Pretende comprobar si ambas variables **se mueven juntas**: en caso de ser así, merecería la pena poner la lupa y analizar todo de manera más detallada.


## Fuentes de datos

### BIS Data Portal: precios de vivienda

El **BIS** (*Bank for International Settlements*, Banco de Pagos Internacionales) es una organización con sede en Basilea (Suiza) que agrupa a bancos centrales de todo el mundo y publica estadísticas económicas y financieras. Su **Data Portal** (`data.bis.org`) reúne esas series.

- **Dataset:** *Selected residential property prices* (`WS_SPP`).
- **Contenido:** índice de precios de vivienda residencial, **real** (descontada la inflación) y **nominal**, base 2010 = 100.
- **Cobertura:** 57 países (más 4 agregados regionales, que se excluyen), con datos trimestrales.

### OMT / UN Tourism: turismo receptivo

La **OMT** (Organización Mundial del Turismo), que desde 2024 se denomina **UN Tourism**, es el organismo de las Naciones Unidas dedicado a promover el turismo y a recopilar sus estadísticas. Su sede está en Madrid.

## Limitaciones

**Cobertura limitada de países:** el mercado de la vivienda es local y nacional, y cada país mide los precios a su manera. El BIS, que reúne los datos de los bancos centrales, es la mejor fuente abierta que he encontrado, pero solo cubre 57 países.
- **Huecos en el turismo:** la base de la OMT es amplia, pero en 2023 y 2024 hay pocos países con datos, por lo que el periodo más sólido es anterior.
- **2020 y 2021** son años atípicos por la pandemia.
- El indicador cuenta **viajes**, no personas, noches ni gasto, y no distingue el tipo de alojamiento.
