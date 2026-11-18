# ¿Incide el turismo en el precio de la vivienda?

![Header_EDA](src/Images/Header_EDA.jpg)

**Proyecto 2 · Análisis exploratorio de datos (EDA). 

## Objetivo

Explorar, con datos públicos y con Python, si existe asociación entre el **crecimiento del turismo receptivo**, la **inflación**, el **crecimiento del PIB per cápita** y la **evolución del precio de la vivienda** a nivel mundial (2016-2024).

El **turismo receptivo** (*inbound tourism*) es el de los no residentes que llegan a un país desde el extranjero y pernoctan al menos una noche.

> Este trabajo habla de **asociación, no de causalidad**: comprueba si las variables se mueven juntas, no si una provoca la otra.

## Hipótesis

| | Pregunta |
|---|---|
| **H1** (principal) | ¿Los países donde más crece el turismo internacional son también los países donde más sube el precio de la vivienda? |
| **H2** (secundaria) | ¿La línea de la inflación acompaña a la línea de la subida de los precios de la vivienda? |
| **H3** (contexto) | ¿Acompaña el crecimiento del PIB per cápita al crecimiento del precio de la vivienda? |

## Datos

| Variable | Fuente |
|---|---|
| Turistas internacionales que pernoctan | [UN Tourism (OMT)](https://www.untourism.int/es/la-omt-recopila-sistematicamente-estadisticas-turisticas) |
| Precio de la vivienda (variación interanual, trimestral) | [BIS](https://data.bis.org/topics/RPP), a través de [Datahub](https://datahub.io/core/house-prices-global) |
| Inflación (precios al consumidor) | [Banco Mundial](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG) |
| PIB per cápita (US$ corrientes) | [Banco Mundial](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD) |

Los cuatro datasets se limpian por separado, se homogenizan con un código de país común (`iso3`) y se unen por país y año. Resultado: **54 países** con datos completos en algún tramo (408 observaciones) y un **panel de 25 países** con la serie completa 2016-2024.

## Qué se ha hecho

1. Limpieza de cada dataset (un notebook por fuente).
2. Unión de los cuatro datasets (*merge*) y selección de muestra.
3. Medianas por año (más robustas que la media ante los extremos de la pandemia).
4. Crecimiento real de la vivienda (precio menos inflación).
5. Seis visualizaciones y una comprobación de robustez de las correlaciones.

## Conclusiones (resumen)

- **H1:** no hay indicios de que turismo y precio de la vivienda se muevan juntos en estos datos (correlación -0,02).
- **H2:** hay indicios de asociación positiva con la inflación, pero poco estable (0,73 con todos los datos).
- **H3:** asociación positiva débil con el PIB per cápita (0,17).
- La mediana del precio de la vivienda crece alrededor de un 6 % anual, por encima de la inflación mediana (2,4 %).

El detalle y la discusión están en la [memoria](MEMORIA_EDA.ipynb).

## Estructura del repositorio

```
├── MEMORIA_EDA.ipynb      # Memoria: libro de instrucciones del proyecto
├── README.md
└── src/
    ├── data/
    │   ├── Brutos/        # Datos originales de las fuentes
    │   ├── Depurados/     # Un CSV limpio por dataset
    │   └── Mergeados/     # Datasets unidos y medianas
    ├── notebooks/         # Limpieza de cada dataset y merge final
    ├── Visualizaciones/   # Un notebook y una imagen por gráfico
    ├── utils/             # archivos.py: funciones para cargar y guardar
    └── images/            # Imágenes de la memoria y del README
```

## Cómo reproducirlo

1. Clonar el repositorio e instalar las librerías: `pip install pandas numpy matplotlib seaborn jupyter`
2. Ejecutar los notebooks de [`src/notebooks`](src/notebooks) (los cuatro de limpieza y después el del *merge*).
3. Ejecutar los notebooks de [`src/Visualizaciones`](src/Visualizaciones), del 01 al 06.

Cada notebook se ejecuta con *Restart + Run All*.

## Tecnologías

Python · Pandas · NumPy · Matplotlib · Seaborn · Jupyter Notebook · Visual Studio Code · Git y GitHub

## Limitaciones

- **Cobertura:** el BIS solo cubre 57 países, sobre todo economías avanzadas.
- **Turismo:** faltan datos de 2023 y 2024 en muchos países, y 2020-2022 son años atípicos por la pandemia (efecto de base).
- **Pocos años:** la serie mundial tiene 9 puntos.
- **PIB en dólares corrientes:** mezcla crecimiento económico y tipo de cambio.
- **Vivienda en términos nominales:** el crecimiento real es una aproximación (precio menos inflación).

## Uso de IA

Se ha utilizado Claude como apoyo en la revisión del código, en dudas, en la organización de partes del proyecto como la memoria, y elaboración de las funciones que permiten la automatización de algunos procesos.

## Autoría

[GitHub](https://github.com/iboulandier)
