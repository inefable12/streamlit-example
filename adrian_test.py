import streamlit as st

def inicio():
    st.title("Página de Inicio")
    st.write("¡Bienvenido a nuestra página de inicio sobre tecnología!")
    # Puedes agregar contenido adicional aquí

def contenido():
    st.title("Numpy")
    st.write("Aquí encontrarás contenido relacionado con la tecnología.")
    # Puedes agregar contenido adicional aquí

def redes_sociales():
    st.title("Pandas")
    st.write("Síguenos en nuestras redes sociales para mantenerte actualizado.")
    # Puedes agregar contenido adicional aquí

def redes_sociales():
    st.title("Matplotlib")
    st.write("Síguenos en nuestras redes sociales para mantenerte actualizado.")
    # Puedes agregar contenido adicional aquí

def main():
    st.sidebar.title("Navegación")
    selection = st.sidebar.radio("Ir a:", ["Inicio", "Numpy", "Pandas", "Matplotlib])
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/9/9c/Alan_Turing_in_watercolour.png",
                 caption="Acuarela de Alan Turing, generada mediante inteligencia artificial, considerado el padre de la misma")

    if selection == "Inicio":
        inicio()
    elif selection == "Contenido":
        contenido()
    elif selection == "Redes Sociales":
        redes_sociales()

if __name__ == "__main__":
    main()
