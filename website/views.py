import re
from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

def analizar_productos(entrada):
    productos = []
    lineas = entrada.split("\n")

    for linea in lineas:
        linea = linea.strip()  # Eliminar espacios en blanco al principio y al final
        if linea:
            partes = linea.split()  # Dividir la línea en palabras separadas por espacios en blanco
            if len(partes) == 2:
                nombre_producto = partes[0]
                precio_texto = partes[1]

                try:
                    precio_decimal = float(precio_texto)
                    iva = precio_decimal * 1.16  # Calcular el IVA (16%)
                    total = precio_decimal + iva
                    producto = {
                        "nombre": nombre_producto,
                        "precio": precio_decimal,
                        "iva": iva,
                        "total": total
                    }
                    productos.append(producto)
                except ValueError:
                    # El precio no es un número válido, ignorar esta línea
                    pass

    return productos

@views.route('/', methods=['GET', 'POST'])
def index():
    productos = []

    if request.method == 'POST':
        entrada = request.form['entrada']
        productos = analizar_productos(entrada)

    return render_template('home.html', productos=productos)