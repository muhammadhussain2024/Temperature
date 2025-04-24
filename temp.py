import streamlit as st

st.title("Fahrenheit to Celsius Converter")

f = st.number_input("Enter temperature in Fahrenheit:", value=32.0, step=0.1)

if st.button("Convert"):
    c = (f - 32) * 5/9
    st.write(f"{f}°F = {c:.1f}°C")
    
    if c < -20:
        st.write("That's Antarctic-level cold! ❄️")
    elif c < 0:
        st.write("Below freezing! 🥶")
    elif c < 10:
        st.write("Chilly! 🧣")
    elif c < 20:
        st.write("Cool and comfortable 😎")
    elif c < 30:
        st.write("Warm and nice! ☀️")
    else:
        st.write("Scorching hot! 🔥")