#Este apartado lo entiendo, pero junto al de funciones, me cuesta mucho desarrollarlo por mi cuenta y lo he hecho con ayuda íntegra de la IA, si bien luego lo entiendo. 

import matplotlib.pyplot as plt

from utils.archivos import cargar_dataset, guardar_dataset, guardar_grafico


def main():
    # 1. Cargar un dataset
    dataset_mediana_mundial = cargar_dataset("merge_mediana_mundial.csv")
    print("dataset_mediana_mundial:", dataset_mediana_mundial.shape)

    # 2. Probar guardar_dataset
    guardar_dataset(dataset_mediana_mundial, "prueba_dataset.csv")

    # 3. Probar guardar_grafico (un gráfico sencillo de prueba)
    plt.figure()
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title("Gráfico de prueba")
    guardar_grafico("prueba_grafico.png")
    plt.close()


if __name__ == "__main__":
    main()