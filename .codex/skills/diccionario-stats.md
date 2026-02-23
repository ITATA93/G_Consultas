# Skill: diccionario-stats

## Descripcion
Muestra estadisticas actuales del Diccionario de Datos ALMA.
NO consulta el servidor - solo lee la base de datos local.

**Incluye trazabilidad:**
- Version del diccionario
- Fecha de ultima sincronizacion con servidor
- Fecha de ultima exportacion
- Historial de sincronizaciones

## Uso
```
/diccionario-stats
```

## Instrucciones
Ejecuta el siguiente comando y muestra los resultados al usuario:

```bash
cd "c:\_Consultas\Diccionario_Datos" && python sincronizar_todo.py --stats
```

El comando muestra:
- **Version** del diccionario
- **Ultima sync** con servidor
- Total de schemas
- Total de tablas
- Total de columnas
- Columnas con descripcion (%)
- Relaciones FK
- Datos de la ultima sincronizacion
