# Pydantic - Guía Básica para Consultas de Datos

## ¿Qué es Pydantic?

Pydantic es una librería de Python que te ayuda a validar datos de forma automática. Es muy útil para información de APIs, bases de datos o archivos y quieres asegurarte de que los datos están en el formato correcto.

La ventaja principal es que se define una vez cómo deben verse tus datos, y Pydantic se encarga de verificar que todo esté bien cada vez que se use.

## Instalación

```bash
pip install pydantic
```

## Ejemplo Básico - Crear un Modelo

Un modelo en Pydantic es como una plantilla que define qué datos esperas recibir:

```python
from pydantic import BaseModel

class Persona(BaseModel):
    nombre: str
    edad: int
    email: str
    activo: bool = True  # Valor por defecto
```

Esto significa que una Persona debe tener:
- Un nombre (texto)
- Una edad (número entero)
- Un email (texto)
- Un estado activo (verdadero/falso, por defecto True)

## Usar el Modelo

Una vez que tiene el modelo, se pueden crear personas y Pydantic validará automáticamente los datos:

```python
# Datos correctos - funciona bien
persona_datos = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "email": "juan@email.com"
}

persona = Persona(**persona_datos)
print(persona)
# Persona(nombre='Juan Pérez', edad=30, email='juan@email.com', activo=True)
```

Si los datos están mal, Pydantic avisa:

```python
# Datos incorrectos - edad como texto
datos_malos = {
    "nombre": "Ana",
    "edad": "treinta",  # Esto está mal!
    "email": "ana@email.com"
}

try:
    persona = Persona(**datos_malos)
except Exception as error:
    print("Error:", error)
    # Error: 1 validation error for Persona
    # edad: value is not a valid integer
```

## Ejemplo Práctico - Lista de Productos

Tienda online en la que se quieren manejar productos:

```python
from pydantic import BaseModel
from typing import List, Optional

class Producto(BaseModel):
    nombre: str
    precio: float
    categoria: str
    en_stock: bool = True
    descripcion: Optional[str] = None  # Opcional

# Crear algunos productos
productos_datos = [
    {"nombre": "Laptop", "precio": 1000.0, "categoria": "Electrónicos"},
    {"nombre": "Camiseta", "precio": 25.0, "categoria": "Ropa", "en_stock": False},
    {"nombre": "Mesa", "precio": 200.0, "categoria": "Muebles", "descripcion": "Mesa de madera"}
]

productos = [Producto(**datos) for datos in productos_datos]

for producto in productos:
    print(f"{producto.nombre} - ${producto.precio} - Stock: {producto.en_stock}")
```

## Hacer Consultas Simples

Ahora se pueden crear funciones para buscar productos:

```python
def buscar_por_categoria(productos: List[Producto], categoria: str) -> List[Producto]:
    """Busca productos por categoría"""
    return [p for p in productos if p.categoria.lower() == categoria.lower()]

def buscar_en_stock(productos: List[Producto]) -> List[Producto]:
    """Busca productos disponibles"""
    return [p for p in productos if p.en_stock]

def buscar_por_precio(productos: List[Producto], precio_max: float) -> List[Producto]:
    """Busca productos por debajo de un precio"""
    return [p for p in productos if p.precio <= precio_max]

# Usar las funciones
electronicos = buscar_por_categoria(productos, "Electrónicos")
disponibles = buscar_en_stock(productos)
baratos = buscar_por_precio(productos, 100)
```

## Validaciones Personalizadas

Se pueden agregar reglas propias de validación:

```python
from pydantic import validator

class Producto(BaseModel):
    nombre: str
    precio: float
    categoria: str
    
    @validator('precio')
    def precio_debe_ser_positivo(cls, valor):
        if valor <= 0:
            raise ValueError('El precio debe ser mayor a 0')
        return valor
    
    @validator('nombre')
    def nombre_no_vacio(cls, valor):
        if not valor.strip():
            raise ValueError('El nombre no puede estar vacío')
        return valor.strip().title()  # Capitaliza el nombre
```

## Convertir a Diccionario o JSON

Pydantic permite convertir fácilmente los datos a otros formatos:

```python
producto = Producto(nombre="laptop gaming", precio=1500.0, categoria="Electrónicos")

# Convertir a diccionario
print(producto.dict())
# {'nombre': 'Laptop Gaming', 'precio': 1500.0, 'categoria': 'Electrónicos'}

# Convertir a JSON
print(producto.json())
# {"nombre": "Laptop Gaming", "precio": 1500.0, "categoria": "Electrónicos"}
```

## Resumen

Pydantic ayuda a:

1. **Definir la estructura** de tus datos de forma clara
2. **Validar automáticamente** que los datos sean correctos
3. **Crear consultas seguras** usando modelos validados
4. **Convertir datos** entre diferentes formatos fácilmente
5. **Obtener errores claros** cuando algo está mal



## Referencias
- https://docs.pydantic.dev/latest/#who-is-using-pydantic
- https://dev.to/gfouz/introduccion-a-pydantic-para-principiantes-b6l
- https://realpython.com/python-pydantic/