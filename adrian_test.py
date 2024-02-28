import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def inicio():
    #st.title("Herramientas computacionales básicas")
    st.markdown("<h1 style='text-align: center;'>Herramientas computacionales básicas</h1>", unsafe_allow_html=True)
    st.write("Descubre cómo extraer información de páginas web, evaluar el rendimiento de futbolistas u obtener imágenes mediante código simple, como por ejemplo:")
    st.code("st.code(url de la imagen)")
    st.image("https://cdn1.epicgames.com/offer/24b9b5e323bc40eea252a10cdd3b2f10/EGS_LeagueofLegends_RiotGames_S1_2560x1440-80471666c140f790f28dff68d72c384b")

def numpy():
    st.title("Numpy")
    st.write("**¿Cuál es la diferencia entre np.array y np.arange en NumPy?**")
    st.write("Respuesta: np.array se utiliza para crear un array NumPy a partir de una secuencia de elementos, mientras que np.arange genera un array NumPy con valores espaciados uniformemente dentro de un rango especificado.")
    st.write("**¿Cómo se puede realizar la multiplicación de matrices en NumPy?** Proporcione un ejemplo.")
    st.write("Respuesta: La multiplicación de matrices en NumPy se realiza utilizando la función np.dot o el operador @. Por ejemplo:")
    st.code("import numpy as np", language='python')
    st.code("A = np.array([[1, 2], [3, 4]])", language='python')
    st.code("B = np.array([[5, 6], [7, 8]])", language='python')
    st.code("C = np.dot(A, B)", language='python')
    st.code("# También se puede usar C = A @ B", language='python')
    st.code("print(C)", language='python')

def pandas():
    st.title("Pandas")
    st.write("**¿Cuál es la diferencia entre DataFrame y Series en Pandas?**")
    st.write("Respuesta: DataFrame es una estructura de datos bidimensional que puede contener múltiples columnas, mientras que Series es una estructura de datos unidimensional que representa una columna en un DataFrame.")
    st.write("**¿Cómo se pueden eliminar filas duplicadas en un DataFrame de Pandas?**")
    st.write("Respuesta: Se puede utilizar el método drop_duplicates() para eliminar filas duplicadas en un DataFrame. Por ejemplo:")
    st.code("""
    import pandas as pd 
    
    df = pd.DataFrame({'A': [1, 2, 2, 3], 'B': ['a', 'b', 'b', 'c']})
    df_sin_duplicados = df.drop_duplicates()
    print(df_sin_duplicados)
    """)

def matplotlib():
    st.title("Matplotlib")
    st.write("**¿Cuál es la diferencia entre plt.plot() y plt.scatter() en Matplotlib?**")
    st.write("Respuesta: plt.plot() se utiliza para trazar líneas o curvas conectando los puntos de datos, mientras que plt.scatter() se utiliza para trazar puntos de datos individuales sin conectarlos con líneas.")
    st.write("**¿Cómo se puede agregar un título y etiquetas de ejes en un gráfico de Matplotlib?**")
    st.write("Respuesta: Se puede agregar un título utilizando plt.title('Título') y etiquetas de ejes con plt.xlabel('Etiqueta X') y plt.ylabel('Etiqueta Y'). Por ejemplo:")
    st.code("""
    import matplotlib.pyplot as plt
    
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    
    plt.plot(x, y)
    plt.title('Gráfico de ejemplo')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()

    """)
    st.write("Esto da como resultado:")

def evaluacion():
    st.title('Evaluación')

    # Inserta el código HTML del formulario de Google
    st.components.v1.html(
        """
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSc3N9Lanr3N0tkoHmHM8ClTgbM3B-Tpwk7m7XwveeuylYskkA/viewform?usp=sf_link" 
                width="640" height="480" frameborder="0" marginheight="0" marginwidth="0">Cargando...</iframe>
        """,
        height=600,
    )

def main():
    st.sidebar.title("Verano 2024")
    selection = st.sidebar.radio("Contenido:", ["Inicio", "Numpy", "Pandas", "Matplotlib", "Evaluacion"])
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/9/9c/Alan_Turing_in_watercolour.png",
                 caption="Acuarela de Alan Turing, generada mediante inteligencia artificial, considerado el padre de la misma")

    if selection == "Inicio":
        inicio()
    elif selection == "Numpy":
        numpy()
    elif selection == "Pandas":
        pandas()
    elif selection == "Matplotlib":
        matplotlib()
    elif selection == "Evaluacion":
        evaluacion()

if __name__ == "__main__":
    main()
