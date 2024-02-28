import streamlit as st

def inicio():
    st.title("Página de Inicio")
    st.write("¡Bienvenido a nuestra página de inicio sobre tecnología!")
    # Puedes agregar contenido adicional aquí

def contenido():
    st.title("Numpy")
    st.write("Aquí encontrarás contenido relacionado con la tecnología.")
    # Puedes agregar contenido adicional aquí

def pandas():
    st.title("Pandas")
    st.write("Síguenos en nuestras redes sociales para mantenerte actualizado.")
    # Puedes agregar contenido adicional aquí

def matplotlib():
    st.title("Matplotlib")
    st.write("Síguenos en nuestras redes sociales para mantenerte actualizado.")
    # Puedes agregar contenido adicional aquí

def evaluacion():
    st.title('Formulario de Google')

    # Inserta el código HTML del formulario de Google
    st.components.v1.html(
        """
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSc3N9Lanr3N0tkoHmHM8ClTgbM3B-Tpwk7m7XwveeuylYskkA/viewform?usp=sf_link" 
                width="640" height="480" frameborder="0" marginheight="0" marginwidth="0">Cargando...</iframe>
        """,
        height=600,
    )

#https://docs.google.com/forms/d/e/1FAIpQLSc3N9Lanr3N0tkoHmHM8ClTgbM3B-Tpwk7m7XwveeuylYskkA/viewform?usp=sf_link

def main():
    st.sidebar.title("Verano 2024")
    selection = st.sidebar.radio("Ir a:", ["Inicio", "Numpy", "Pandas", "Matplotlib", "Evaluacion"])
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/9/9c/Alan_Turing_in_watercolour.png",
                 caption="Acuarela de Alan Turing, generada mediante inteligencia artificial, considerado el padre de la misma")

    if selection == "Inicio":
        inicio()
    elif selection == "Numpy":
        numpy()
    elif selection == "Matplotlib":
        matplotlib()
    elif selection == "Evaluacion":
        evaluacion()

if __name__ == "__main__":
    main()
