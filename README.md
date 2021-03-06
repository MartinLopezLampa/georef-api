# georef-api

[![Build Status](https://travis-ci.org/datosgobar/georef-api.svg?branch=master)](https://travis-ci.org/datosgobar/georef-api)

API del servicio de normalización y geocodificación de direcciones para organismos de la Administración Pública Nacional.

*Importante: este proyecto está en etapa de desarrollo y usa una muestra con datos de prueba.*

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

## Indice

- [Uso de georef-api](#uso-de-georef-api)
  - [Direcciones `/api/v1.0/direcciones`](#direcciones-apiv10direcciones)
  - [Ejemplos](#ejemplos)
  - [Calles `/api/v1.0/calles`](#calles-apiv10calles)
  - [Provincias `/api/v1.0/provincias`](#provincias-apiv10provincias)
  - [Departamentos `/api/v1.0/departamentos`](#departamentos-apiv10departamentos)
  - [Municipios `/api/v1.0/municipios`](#municipios-apiv10municipios)
  - [Localidades `/api/v1.0/localidades`](#localidades-apiv10localidades)
- [Contacto](#contacto)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Uso de georef-api

### Direcciones `/api/v1.0/direcciones`

Entrada:
- **direccion**: la dirección que se quiere normalizar (campo obligatorio).
- localidad: para filtrar por *nombre* de localidad censal.
- departamento: para filtrar por *nombre* de departamento.
- provincia: para filtrar por *nombre* de provincia.
- campos: qué campos devolver.
- max: cantidad máxima esperada de sugerencias.

Salida: JSON con el siguiente formato.
```json
{
  "direcciones": [
    {
      "nomenclatura": "Avenida Presidente Roque Sáenz Peña 250, Ciudad ...",
      "tipo": "Avenida",
      "nombre": "Presidente Roque Sáenz Peña",
      "altura": 250,
      "localidad": "Ciudad Autónoma de Buenos Aires",
      "partido": "Ciudad Autónoma de Buenos Aires",
      "provincia": "Capital Federal",
      "observaciones": {
        "fuente": "Fuente del resultado.",
        "info": "Información adicional sobre el resultado."
        }
    },
    {
      "..."
    },
  ]
}
```

### Ejemplos

Un cliente quiere saber a qué localidad corresponde una dirección dada.
En este caso, consumiría la API de búsqueda pasando los parámetros `dirección` y `provincia`.
Si la dirección existe, debería recibir uno o más resultados.

**GET** `/api/v1.0/direcciones?direccion=Echeverria+4497&provincia=Buenos+Aires`
```json
{
  "direcciones": [
    {
      "nomenclatura": "Esteban Echeverría 4497, Gregorio Laferrere, Buenos Aires",
      "tipo": "Calle",
      "nombre": "Esteban Echeverría",
      "altura": 4497,
      "localidad": "Gregorio Laferrere",
      "partido": "La Matanza",
      "provincia": "Buenos Aires",
      "observaciones": {
        "fuente": "INDEC",
        "info": "Se procesó correctamente la dirección buscada."
        }
    },
    {
      "nomenclatura": "Esteban Echeverría 4497, Villa Sarmiento, Buenos Aires",
      "tipo": "Calle",
      "nombre": "Esteban Echeverría",
      "altura": 4497,
      "localidad": "Villa Sarmiento",
      "partido": "Morón",
      "provincia": "Buenos Aires",
      "observaciones": {
        "fuente": "INDEC",
        "info": "Se procesó correctamente la dirección buscada."
        }
    },
    {
      "..."
    },
  ],
}
```

**Errores**

Cuando se produce un error durante el procesamiento de una consulta,
la respuesta de la API incluye el campo "error" con información detallada.
```json
{
  "codigo": 400, 
  "error": {
    "codigo_interno": null,
    "info": "https://github.com/datosgobar/georef-api",
    "mensaje": "El Request tiene parámetros inválidos o está incompleto.",
  },
}
```


**Normalizar lote de direcciones**

**POST** `/api/v1.0/direcciones`

Entrada:
- campos: qué campos devolver.
- **body**: JSON con lote de direcciones para normalizar.
```json
{
  "direcciones": [
    "Roque Sáenz Peña 788, Buenos Aires",
    "Calle Principal 123, 1425 CABA",
    "Esmeralda 1000, Capital Federal",
    "..."
  ]
}
```

Salida: JSON con el siguiente formato.
```json
{
  "direcciones": [
    {
      "original": "Roque Sáenz Peña 788, Buenos Aires",
      "normalizadas": [
        {
          "nomenclatura": "Av. Presidente Roque Sáenz Peña 788, Ciudad Autónoma ...",
          "tipo": "Avenida",
          "nombre": "Presidente Roque Sáenz Peña",
          "altura": 788,
          "localidad": "Ciudad Autónoma de Buenos Aires",
          "partido": "Ciudad Autónoma de Buenos Aires",
          "provincia": "Capital Federal",
          "observaciones": {
            "fuente": "INDEC",
            "info": "Se procesó correctamente la dirección buscada."
            }
        },
      ]
    },
    {
      "..."
    },
  ]
}
```

### Calles `/api/v1.0/calles`
Retorna calles (normalizadas) de una localidad o provincia.

Entrada:
- localidad: para filtrar por *nombre* de localidad censal.
- departamento: para filtrar por *nombre* de departamento.
- provincia: para filtrar por *nombre* de provincia.
- tipo: para filtrar por tipo de camino.
- campos: qué campos devolver.
- max: cantidad máxima esperada de sugerencias.

Ejemplo: obtener todas las calles de Bariloche, mostrando *nomenclatura* y *tipo*.

**GET** `/api/v1.0/calles?localidad=Bariloche&campos=nomenclatura,tipo`

Salida: JSON con el siguiente formato.
```json
{
  "calles": [
    {
      "nomenclatura": "Avenida 12 de Octubre, 8400 San Carlos de Bariloche, Río Negro",
      "tipo": "Avenida"
    },
    {
      "nomenclatura": "Diagonal 1, 8400 San Carlos de Bariloche, Río Negro",
      "tipo": "Calle"
    },
    {
      "..."
    },
  ],
}
```

### Provincias `/api/v1.0/provincias`
Retorna un listado de provincias.

Entrada:
- id: para filtrar por id.
- nombre: para filtrar por nombre.
- campos: qué campos devolver.
- orden: *id* o *nombre*.
- max: cantidad máxima esperada de sugerencias.

**GET** `/api/v1.0/provincias`
```json
{
  "provincias": [
    {
      "id": "14", 
      "nombre": "Córdoba"
    }, 
    {
      "id": "22", 
      "nombre": "Chaco"
    }, 
    {
      "id": "26", 
      "nombre": "Chubut"
    }, 
    {
      "id": "06", 
      "nombre": "Buenos Aires"
    }, 
    {
      "id": "10", 
      "nombre": "Catamarca"
    },
    "..."
  ]
}
```

### Departamentos `/api/v1.0/departamentos`
Retorna un listado de departamentos.

Entrada:
- id: para filtrar por id.
- nombre: para filtrar por nombre.
- provincia: para filtrar por *ID* o *nombre* de provincia.
- campos: qué campos devolver.
- orden: *id* o *nombre*.
- aplanar: si está presente, muestra el resultado con una estructura plana.
- max: cantidad máxima esperada de sugerencias.

**GET** `/api/v1.0/departamentos?nombre=capital`
```json
{
  "departamentos": [
    {
      "id": "50007", 
      "nombre": "Capital", 
      "provincia": {
        "id": "50",
        "nombre": "Mendoza"
      }
    }, 
    {
      "id": "54028", 
      "nombre": "Capital", 
      "provincia": {
        "id": "54",
        "nombre": "Misiones"
      }
    }, 
    {
      "id": "86049", 
      "nombre": "Capital", 
      "provincia": {
        "id": "86",
        "nombre": "Santiago del Estero"
      }
    },
    "..."
  ]
}
```

**GET** `/api/v1.0/departamentos?nombre=capital&aplanar`. Resultado con estructura plana.
```json
{
  "departamentos": [
    {
      "id": "50007", 
      "nombre": "Capital", 
      "provincia_id": "50",
      "provincia_nombre": "Mendoza"
    }, 
    {
      "id": "54028", 
      "nombre": "Capital", 
      "provincia_id": "54",
      "provincia_nombre": "Misiones"
    }, 
    {
      "id": "86049", 
      "nombre": "Capital", 
      "provincia_id": "86",
      "provincia_nombre": "Santiago del Estero"
    },
    "..."
  ]
}
```

### Municipios `/api/v1.0/municipios`
Retorna un listado de municipios.

Entrada:
- id: para filtrar por id.
- nombre: para filtrar por nombre.
- provincia: para filtrar por *ID* o *nombre* de provincia.
- campos: qué campos devolver.
- orden: *id* o *nombre*.
- aplanar: si está presente, muestra el resultado con una estructura plana.
- max: cantidad máxima esperada de sugerencias.

**GET** `/api/v1.0/municipios?provincia=54`
```json
{
  "municipios": [
    {
      "id": "24089",
      "nombre": "MONTECARLO",
      "provincia": {
        "id": "54",
        "nombre": "Misiones"
      },
      "ubicacion": {
        "lat": -26.6388110114284,
        "lon": -54.561398302505
      }
    },
    {
      "id": "24138",
      "nombre": "CAMPO VIERA",
      "provincia": {
        "id": "54",
        "nombre": "Misiones"
      },
      "ubicacion": {
        "lat": -27.2794449755344,
        "lon": -55.0708317700693
      }
    },
    {
      "id": "24147",
      "nombre": "ARISTOBULO DEL VALLE",
      "provincia": {
        "id": "54",
        "nombre": "Misiones"
      },
      "ubicacion": {
        "lat": -27.1206229393642,
        "lon": -54.8280097328346
      }
    },
    "..."
  ]
}
```

**GET** `/api/v1.0/municipios?provincia=54&aplanar` Resultado con estructura plana.
```json
{
  "municipios": [
    {
      "id": "24089",
      "nombre": "MONTECARLO",
      "provincia_id": "54",
      "provincia_nombre": "Misiones",
      "ubicacion": {
        "lat": -26.6388110114284,
        "lon": -54.561398302505
      }
    },
    {
      "id": "24138",
      "nombre": "CAMPO VIERA",
      "provincia_id": "54",
      "provincia_nombre": "Misiones",
      "ubicacion": {
        "lat": -27.2794449755344,
        "lon": -55.0708317700693
      }
    },
    {
      "id": "24147",
      "nombre": "ARISTOBULO DEL VALLE",
      "provincia_id": "54",
      "provincia_nombre": "Misiones",
      "ubicacion": {
        "lat": -27.1206229393642,
        "lon": -54.8280097328346
      }
    },
    "..."
  ]
}
```

### Localidades `/api/v1.0/localidades`
Retorna un listado de localidades y entidades de BAHRA.

Entrada:
- id: para filtrar por id.
- nombre: para filtrar por nombre.
- departamento: para filtrar por *ID* o *nombre* de departamento.
- provincia: para filtrar por *ID* o *nombre* de provincia.
- campos: qué campos devolver.
- orden: *id* o *nombre*.
- aplanar: si está presente, muestra el resultado con una estructura plana.
- max: cantidad máxima esperada de sugerencias.

**GET** `/api/v1.0/localidades?departamento=la+matanza`
```json
{
  "localidades": [
    {
      "departamento": {
        "id": "06427",
        "nombre": "La Matanza"
      },
      "id": "06427010004",
      "nombre": "GREGORIO DE LAFERRERE",
      "provincia": {
        "id": "06",
        "nombre": "Buenos Aires"
      },
      "tipo": "Entidad (E)",
      "ubicacion": {
        "lat": -34.7468379962,
        "lon": -58.5925328858
      }
    },
    {
      "departamento": {
        "id": "06427", 
        "nombre": "La Matanza"
      },
      "id": "06427010006",
      "nombre": "LA TABLADA",
      "provincia": {
        "id": "06",
        "nombre": "Buenos Aires"
      },
      "tipo": "Entidad (E)",
      "ubicacion": {
        "lat": -34.687053669,
        "lon": -58.5256123986
      }
    },
    "..."
  ]
}
```

**GET** `/api/v1.0/localidades?departamento=la+matanza&aplanar`. Resultado con estructura plana.
```json
{
  "localidades": [
    {
      "departamento_id": "06427",
      "departamento_nombre": "La Matanza",
      "id": "06427010004",
      "nombre": "GREGORIO DE LAFERRERE",
      "provincia_id": "06",
      "provincia_nombre": "Buenos Aires",
      "tipo": "Entidad (E)",
      "ubicacion_lat": -34.7468379962,
      "ubicacion_lon": -58.5925328858
    },
    {
      "departamento_id": "06427",
      "departamento_nombre": "La Matanza",
      "id": "06427010006",
      "nombre": "LA TABLADA",
      "provincia_id": "06",
      "provincia_nombre": "Buenos Aires",
      "tipo": "Entidad (E)",
      "ubicacion_lat": -34.687053669,
      "ubicacion_lon": -58.5256123986
    },
    "..."
  ]
}
```

## Contacto
Te invitamos a [crearnos un issue](https://github.com/datosgobar/georef-api/issues/new?title=Encontre-un-bug-en-georef-api) en caso de que encuentres algún bug o tengas comentarios     de alguna parte de `georef-api`. Para todo lo demás, podés mandarnos tu sugerencia o consulta a [datos@modernizacion.gob.ar](mailto:datos@modernizacion.gob.ar).
