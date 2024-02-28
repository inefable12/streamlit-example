import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def inicio():
    st.title("Página de Inicio")
    st.write("¡Bienvenido a nuestra página de inicio sobre tecnología!")
    # Puedes agregar contenido adicional aquí

def numpy():
    st.title("Numpy")
    st.write("¿Cuál es la diferencia entre np.array y np.arange en NumPy?")
    st.write("Respuesta: np.array se utiliza para crear un array NumPy a partir de una secuencia de elementos, mientras que np.arange genera un array NumPy con valores espaciados uniformemente dentro de un rango especificado.")
    st.write("¿Cómo se puede realizar la multiplicación de matrices en NumPy? Proporcione un ejemplo.")
    st.write("Respuesta: La multiplicación de matrices en NumPy se realiza utilizando la función np.dot o el operador @. Por ejemplo:")
    st.code("import numpy as np", language='python')
    st.code("A = np.array([[1, 2], [3, 4]])", language='python')
    st.code("B = np.array([[5, 6], [7, 8]])", language='python')
    st.code("C = np.dot(A, B)", language='python')
    st.code("# También se puede usar C = A @ B", language='python')
    st.code("print(C)", language='python')

def pandas():
    st.title("Pandas")
    st.write("Síguenos en nuestras redes sociales para mantenerte actualizado.")
    # Puedes agregar contenido adicional aquí

def matplotlib():
    st.title("Matplotlib")
    st.write("Síguenos en nuestras redes sociales para mantenerte actualizado.")
    # Puedes agregar contenido adicional aquí

def evaluacion():
    st.title('Evaluaciòn')

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
