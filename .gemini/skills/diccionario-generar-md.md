# Skill: diccionario-generar-md

## Descripcion
Genera archivos MD individuales para cada tabla del diccionario.
Cada MD contiene todas las columnas con tipos, PK/FK, y descripciones.
NO consulta el servidor - solo usa datos locales de SQLite.

**Organizacion de archivos:**
- Archiva MD existentes con `--archivar` (guarda en `_archivo/fecha/`)
- Limpia archivos huerfanos (tablas eliminadas) con `--limpiar`
- Actualiza LOG_AUDITORIA.md automaticamente
- Mantiene estructura de directorios por schema

## Uso
```
/diccionario-generar-md                    # Todas las tablas
/diccionario-generar-md --schema SQLUser   # Solo un schema
/diccionario-generar-md --tabla PA_Adm     # Solo tablas que coincidan
/diccionario-generar-md --limpiar          # Limpiar huerfanos primero
/diccionario-generar-md --archivar         # Archivar MD antes de regenerar
```

## Instrucciones
Ejecutar:

```bash
cd "c:\_Consultas\Diccionario_Datos" && python generar_md_tablas.py [opciones]
```

Opciones:
- `--schema NOMBRE` - Solo generar para ese schema
- `--tabla PATRON` - Solo tablas que contengan ese patron
- `--limite N` - Limitar a N tablas
- `--limpiar` - Eliminar archivos MD huerfanos antes de generar
- `--archivar` - Mover MD existentes a `_archivo/YYYY-MM-DD_HHMM/` antes de regenerar
- `--no-log` - No actualizar LOG_AUDITORIA.md

## Salida
Los archivos MD se generan en:
```
c:\_Consultas\Diccionario_Datos\tablas_md/
├── _INDICE.md           # Indice general
├── SQLUser/             # Un directorio por schema
│   ├── PA_Adm.md
│   ├── PA_Person.md
│   └── ...
├── lab/
├── questionnaire/
└── ...
```

## Ejemplo de MD generado
Cada archivo incluye:
- Nombre completo (schema.tabla)
- Cantidad de columnas
- Tabla con: Columna, Tipo, PK, FK, Nullable, Descripcion

## Actualizacion automatica
El script actualiza automaticamente:
- LOG_AUDITORIA.md (fecha y conteo de archivos)
- _INDICE.md (indice de todas las tablas)
