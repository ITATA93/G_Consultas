# Skill: diccionario-export

## Descripcion
Exporta el Diccionario de Datos a CSV y actualiza documentos MD.
NO consulta el servidor - solo usa datos locales.

## Uso
```
/diccionario-export
```

## Instrucciones
Ejecutar:

```bash
cd "c:\_Consultas\Diccionario_Datos" && python sincronizar_todo.py --solo-local
```

Esto actualiza:
- diccionario_tablas.csv
- diccionario_columnas.csv
- diccionario_relaciones.csv
- diccionario_resumen.csv
- _LISTADO_TABLAS.md
- _INDICE.md
- LOG_AUDITORIA.md

## Archivos generados
Los CSV se pueden abrir en Excel para analisis.
