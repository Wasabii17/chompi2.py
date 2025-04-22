# pages/4_Ecuacion_Combinada.py
import streamlit as st
st.set_page_config(page_title="Ecuación Combinada de Gases", page_icon="🔁")
st.title("🔁 Ecuación Combinada de los Gases")
st.markdown(r"""La ecuación combinada de los gases es:
\[
\frac{P_i \cdot V_i}{T_i} = \frac{P_f \cdot V_f}{T_f}
\]

Completa los valores conocidos y elige qué variable quieres calcular.
""")

variables = {
    "Presión Inicial (Pᵢ)": "Pi",
    "Volumen Inicial (Vᵢ)": "Vi",
    "Temperatura Inicial (Tᵢ)": "Ti",
    "Presión Final (P𝒇)": "Pf",
    "Volumen Final (V𝒇)": "Vf",
    "Temperatura Final (T𝒇)": "Tf"
}

opcion = st.selectbox("¿Qué variable deseas calcular?", list(variables.keys()))

# Crear campos numéricos con valores iniciales
campos = {}

for nombre, codigo in variables.items():
    if nombre != opcion:
        campos[codigo] = st.number_input(f"{nombre}", min_value=0.01)

# Calcular la variable deseada
if st.button("Calcular"):
    Pi = campos.get("Pi", None)
    Vi = campos.get("Vi", None)
    Ti = campos.get("Ti", None)
    Pf = campos.get("Pf", None)
    Vf = campos.get("Vf", None)
    Tf = campos.get("Tf", None)
    
    resultado = None
    unidad = ""
 st.image("image1.png")
    try:
        if opcion == "Presión Inicial (Pᵢ)":
            resultado = (Pf * Vf * Ti) / (Tf * Vi)
            unidad = "atm"
        elif opcion == "Volumen Inicial (Vᵢ)":
            resultado = (Pf * Vf * Ti) / (Tf * Pi)
            unidad = "L"
        elif opcion == "Temperatura Inicial (Tᵢ)":
            resultado = (Pi * Vi * Tf) / (Pf * Vf)
            unidad = "K"
        elif opcion == "Presión Final (P𝒇)":
            resultado = (Pi * Vi * Tf) / (Ti * Vf)
            unidad = "atm"
        elif opcion == "Volumen Final (V𝒇)":
            resultado = (Pi * Vi * Tf) / (Ti * Pf)
            unidad = "L"
        elif opcion == "Temperatura Final (T𝒇)":
            resultado = (Pf * Vf * Ti) / (Pi * Vi)
            unidad = "K"
           

        st.success(f"{opcion} = {resultado:.3f} {unidad}")

    except Exception as e:
        st.error("Verifica que todos los valores estén completos y sean mayores que cero.")
