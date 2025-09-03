# INVESTIGACIÓN: libreria de python PYDANTIC

## Contenido
- [Conceptos básicos y fundamentos](#conceptos-básicos-y-fundamentos)
  - [Qué es Pydantic](#qué-es-pydantic)
  - [Propósito y casos de uso](#propósito-y-casos-de-uso)
  - [Instalación y configuración inicial](#instalación-y-configuración-inicial)
  - [Relación con Python type hints y typing module](#relación-con-python-type-hints-y-typing-module)

- [Modelos y validación de datos](#modelos-y-validación-de-datos)
  - [BaseModel](#-basemodel)
  - [Definición de campos](#-definición-de-campos-en-pydantic)
  - [Campos opcionales](#-campos-opcionales)
  - [Valores por defecto](#-valores-por-defecto)
  - [Tipos de datos comunes](#-tipos-de-datos-comunes)
  - [Conversión automática de tipos](#conversión-automática-de-tipos)

- [Validadores y manejo de errores](#validadores-y-manejo-de-errores-en-pydantic)
  - [Validadores personalizados](#validadores-personalizados)

- [Tipos de datos y campos en Pydantic](#-tipos-de-datos-y-campos-en-pydantic)
  - [Tipos especiales de Pydantic](#tipos-especiales-de-pydantic)
  - [Instalación de dependencias para tipos especiales](#-instalación-de-dependencias-para-tipos-especiales)
  - [Uso de Field()](#-field)
  - [Parámetros comunes de Field()](#parámetros-comunes-de-field)
  - [Campos opcionales](#-campos-opcionales-1)
  - [Valores por defecto](#-valores-por-defecto-1)

- [Validación estricta vs flexible](#validación-estricta-vs-flexible)

- [Ejemplo práctico](#ejemplo-práctico)

- [Referencias](#referencias)

---

## Conceptos básicos y fundamentos
### ¿Qué es Pydantic?
Es una librería de Python que permite definir modelos de datos utilizando anotaciones de tipo, y automáticamente valida y transforma los datos según estas anotaciones. Permite asegurarse de que los datos tienen el formato correcto antes de usarlos en la aplicación.

### Propósito y casos de uso
Pydantic existe principalmente para asegurar que los datos cumplan exactamente con las especificaciones definidas mediante *type hints(anotaciones de tipo)*, validando y transformando datos para prevenir errores antes de que causen problemas en la aplicación. Es una biblioteca diseñada para mejorar la robustez y confiabilidad del código Python

**¿Cuándo usar Pydantic?:**
- *APIs y servicios web:* se usa comúnmente con frameworks web como FastAPI, donde simplifica el manejo, para asegurar que las entradas tengan el tipo y formato que la aplicación espera, como verificar que un email tenga formato RFC 
- *Análisis y procesamiento de datos:* puede validar y limpiar datos de diversas fuentes como archivos CSV, bases de datos o web scraping, proporcionando métodos útiles como model_dump(), schema(), fields, etc.

**Ventajas clave:**
- *Validación automática:* Detecta errores de tipo antes de la ejecución
- *Transformación de datos:* Convierte automáticamente tipos compatibles
- *Documentación integrada:* Genera schemas y documentación automáticamente
- *Ecosistema amplio:* Alrededor de 8,000 paquetes en PyPI usan Pydantic, incluyendo bibliotecas populares como FastAPI, Hugging Face, Django Ninja, SQLModel y LangChain
- *Personalización:* Permite validadores y serializadores personalizados para alterar cómo se procesan los datos

*¿Cuándo NO usar Pydantic?:*: Para scripts simples sin validación compleja. Cuando el rendimiento es crítico y la validación no es necesaria.En casos donde los tipos de datos son estáticos y conocidos

### Instalación y configuración inicial
**🖥️ En Windows**
Desde el Command Prompt (CMD)
- Presiona Win + R
- Escribe cmd y presiona Enter
- Ejecutar los comandos: `pip install pydantic`

**🔍 Verificar que funciona:**
Después de instalar, crea un archivo test.py
```python
# test.py
import pydantic
print(f"✅ Pydantic instalado correctamente: {pydantic.__version__}")

from pydantic import BaseModel

class Persona(BaseModel):
    nombre: str
    edad: int

# Crear una instancia para probar
persona = Persona(nombre="Juan", edad=25)
print(f"✅ Modelo creado: {persona}")
print(f"✅ Nombre: {persona.nombre}")
print(f"✅ Edad: {persona.edad}")

# Probar validación de errores
try:
    persona_invalida = Persona(nombre="Ana", edad="texto")
except Exception as e:
    print(f"✅ Validación funciona: {e}")

print("¡Todo funciona correctamente!")
```
- **Resultado esperado**
```python
✅ Pydantic instalado correctamente: 2.5.0
✅ Modelo creado: nombre='Juan' edad=25
✅ Nombre: Juan
✅ Edad: 25
✅ Validación funciona: 1 validation error for Persona
edad
  ¡Todo funciona correctamente!
```
### Relación con Python type hints y typing module
El módulo typing de Python proporciona herramientas para hacer anotaciones de tipo más avanzadas. Viene incluido con Python.
Para qué sirve:
```python
# Sin typing - solo tipos básicos
nombre: str
edad: int

# Con typing - tipos más complejos
from typing import List, Dict, Optional, Union

hobbies: List[str]           # Lista que contiene solo strings
configuracion: Dict[str, int] # Diccionario con keys string y valores enteros
email: Optional[str]         # Puede ser string o None
id: Union[str, int]          # Puede ser string O entero
```
Tipos más comunes de typing:

```python
pythonfrom typing import List, Dict, Optional, Union, Any, Tuple

class Ejemplo(BaseModel):
    # Listas
    numeros: List[int]           # [1, 2, 3, 4]
    
    # Diccionarios  
    configuracion: Dict[str, Any]  # {"nombre": "Juan", "edad": 25}
    
    # Opcionales (puede ser None)
    telefono: Optional[str] = None
    
    # Uniones (uno u otro)
    identificador: Union[str, int]  # "12345" o 12345
    
    # Tuplas
    coordenadas: Tuple[float, float]  # (10.5, 20.3)
```

## Modelos y validación de datos

### **- BaseModel**
Es la clase padre fundamental de Pydantic que convierte una clase Python común en un modelo validado. Cómo heredar de BaseModel elimina la necesidad de escribir constructores manuales y proporciona validación automática de tipos.

### **- Definición de campos en Pydantic**

En Pydantic, los campos se definen usando **type hints** (anotaciones de tipo) de Python. Es para decirle al modelo: "este campo debe ser de este tipo específico".

### **- Sintaxis básica**
```python
from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str          # Campo obligatorio de tipo string
    edad: int           # Campo obligatorio de tipo entero
    activo: bool        # Campo obligatorio de tipo booleano
```

### **- Campos opcionales**
```python
from typing import Optional

class Usuario(BaseModel):
    nombre: str
    edad: int
    email: Optional[str] = None  # Campo opcional con valor por defecto
```

### **- Valores por defecto**
```python
class Usuario(BaseModel):
    nombre: str
    edad: int
    activo: bool = True          # Si no se proporciona, será True
    rol: str = "usuario"         # Valor por defecto como string
```

### **- Tipos de datos comunes**

```python
from typing import List, Dict
from datetime import datetime

class Perfil(BaseModel):
    # Tipos básicos
    nombre: str
    edad: int
    precio: float
    activo: bool
    
    # Colecciones
    tags: List[str]              # Lista de strings
    configuracion: Dict[str, int] # Diccionario con keys string y valores entero
    
    # Fechas
    fecha_creacion: datetime
```

### Conversión automática de tipos

Pydantic es inteligente con las conversiones:
- `"25"` → `25` (string a int) ✅
- `"25.5"` → `25` (float a int) ✅
- `"abc"` → Error ❌

```python
# Esto funciona
usuario = Usuario(nombre="Juan", edad="25")  # "25" se convierte a 25

# Esto falla
usuario = Usuario(nombre="Juan", edad="abc")  # No se puede convertir "abc" a int
```

## Validadores y Manejo de Errores en Pydantic

### **Validadores personalizados**

Son funciones que creas para validar datos más allá de solo el tipo. Te permiten implementar reglas de negocio específicas:

```python
from pydantic import BaseModel, validator
import re

class Usuario(BaseModel):
    nombre: str
    edad: int
    email: str
    
    @validator('edad')
    def validar_edad(cls, v):
        if v < 0 or v > 120:
            raise ValueError('La edad debe estar entre 0 y 120 años')
        return v
```

### **- Tipos de datos y campos en Pydantic**

Pydantic proporciona tipos específicos con validaciones integradas:

```python
from pydantic import BaseModel, EmailStr, HttpUrl, UUID4, validator
from datetime import datetime
from decimal import Decimal

class UsuarioCompleto(BaseModel):
    # Validación de email automática
    email: EmailStr                       # "usuario@ejemplo.com"
    
    # URLs válidas
    sitio_web: HttpUrl                    # "https://ejemplo.com"
    
    # UUIDs
    id_unico: UUID4                       # "123e4567-e89b-12d3-a456-426614174000"
    
    # Fechas y tiempo
    fecha_nacimiento: datetime            # "2023-12-25T15:30:00"
    
    # Decimales precisos (para dinero)
    salario: Decimal                      # 1234.56 (sin errores de punto flotante)
    
    # Rutas de archivos
    from pydantic import FilePath, DirectoryPath
    archivo: FilePath                     # Debe existir el archivo
    carpeta: DirectoryPath                # Debe existir el directorio
```

### **- Instalación de dependencias para tipos especiales**
```bash
# Para EmailStr
pip install pydantic[email]

# Para HttpUrl (incluido por defecto en versiones recientes)
```
---

### **- Field()**

`Field()` permite agregar metadatos, validaciones y configuraciones adicionales a los campos:

```python
from pydantic import BaseModel, Field

class Producto(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    precio: float = Field(..., gt=0, description="Precio en USD")
    descuento: int = Field(0, ge=0, le=100, description="Porcentaje de descuento")
    codigo: str = Field(..., regex=r'^[A-Z]{2}\d{4}$')
    
    class Config:
        schema_extra = {
            "example": {
                "nombre": "Laptop Gaming",
                "precio": 999.99,
                "descuento": 15,
                "codigo": "LP1234"
            }
        }
```

### Parámetros comunes de Field():
- `...` = Campo obligatorio (equivale a `Required`)
- `default=valor` = Valor por defecto
- `min_length`, `max_length` = Longitud mínima y máxima para strings
- `gt`, `ge`, `lt`, `le` = Mayor que, mayor igual, menor que, menor igual
- `regex` = Patrón de expresión regular
- `description` = Descripción para documentación
- `example` = Ejemplo para la documentación

---

### **- Campos opcionales**
```python
from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str                           # Obligatorio
    edad: int                             # Obligatorio
    email: Optional[str] = None           # Opcional, puede ser None
    telefono: str | None = None           # Sintaxis Python 3.10+
```

### **- Valores por defecto**
```python
from datetime import datetime
from pydantic import BaseModel, Field

class Articulo(BaseModel):
    titulo: str                           # Obligatorio
    contenido: str                        # Obligatorio
    
    # Valores por defecto simples
    publicado: bool = False
    categoria: str = "general"
    
    # Valores por defecto con funciones
    fecha_creacion: datetime = Field(default_factory=datetime.now)
    id: str = Field(default_factory=lambda: f"art_{hash(datetime.now())}")
    
```


## Validación estricta vs flexible

Pydantic puede ser estricto o flexible con las conversiones de tipos:

```python
from pydantic import BaseModel, StrictStr, StrictInt, ValidationError

class ModeloFlexible(BaseModel):
    nombre: str
    edad: int

class ModeloEstricto(BaseModel):
    nombre: StrictStr    # Solo acepta strings, no convierte
    edad: StrictInt      # Solo acepta enteros, no convierte

# Modelo flexible - convierte tipos
flexible = ModeloFlexible(nombre="Juan", edad="25")  #  "25" → 25

# Modelo estricto - no convierte
try:
    estricto = ModeloEstricto(nombre="Juan", edad="25")
except ValidationError as e:
    print("Error: edad debe ser exactamente un entero")

```

## Ejemplo práctico

```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class PerfilUsuario(BaseModel):
    # Campos obligatorios
    nombre: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    
    # Campos opcionales
    telefono: Optional[str] = None
    bio: Optional[str] = Field(None, max_length=500)
    
    # Valores por defecto
    activo: bool = True
    rol: str = "usuario"
    fecha_registro: datetime = Field(default_factory=datetime.now)
    
    # Listas con valores por defecto, se usa default_factory para que cada objeto tenga su lista
    intereses: List[str] = Field(default_factory=list) 
    seguidores: List[str] = Field(default_factory=list)
```

## Referencias
- https://docs.pydantic.dev/latest/#who-is-using-pydantic
- https://dev.to/gfouz/introduccion-a-pydantic-para-principiantes-b6l
- https://realpython.com/python-pydantic/