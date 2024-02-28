import streamlit as st

def inicio():
    st.title("Página de Inicio")
    st.write("¡Bienvenido a nuestra página de inicio sobre tecnología!")
    # Puedes agregar contenido adicional aquí

def contenido():
    st.title("Contenido")
    st.write("Aquí encontrarás contenido relacionado con la tecnología.")
    # Puedes agregar contenido adicional aquí

def redes_sociales():
    st.title("Redes Sociales")
    st.write("Síguenos en nuestras redes sociales para mantenerte actualizado.")
    # Puedes agregar contenido adicional aquí

def main():
    st.sidebar.title("Navegación")
    selection = st.sidebar.radio("Ir a:", ["Inicio", "Contenido", "Redes Sociales"])

    if selection == "Inicio":
        inicio()
    elif selection == "Contenido":
        contenido()
    elif selection == "Redes Sociales":
        redes_sociales()

if __name__ == "__main__":
    main()
