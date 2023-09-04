# Firestore common python library

Firestore common python library es una libreria para uso general, la cual contiene logica relacionado a firestore. Agregar, eliminar, etc.

## Authors

- [@Serialk89](https://github.com/Serialk89)


## Installation

Install the library with pip

```bash
  cd my-project
  pip install firestore-common-jimmykvick
```

```python
from tu_libreria import firestore_instance, add_document
```

### Inicializar Firestore

La función `firestore_instance()` se utiliza para inicializar una instancia de Firestore. No es necesario llamarla explícitamente ya que `add_document` la utiliza internamente.

```python
db = firestore_instance()
```

### Añadir un nuevo documento

Para añadir un nuevo documento a una colección, puedes utilizar la función `add_document`. 

```python
collection = "tu_coleccion"
body = {
  "clave": "valor",
  "otra_clave": "otro_valor"
}

doc_id = add_document(collection, body)
```

#### Parámetros:

- `col` : El nombre de la colección a la que se añadirá el nuevo documento.
- `body` : Un diccionario con los campos y valores del nuevo documento.

#### Valor de retorno:

La función devuelve el ID del documento recién creado.

## Errores

Las funciones lanzarán una excepción `ValueError` si se pasan argumentos inválidos.


## Build
python3 -m build

