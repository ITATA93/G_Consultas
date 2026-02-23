# Skill: diccionario-sync

## Descripcion
Sincroniza el Diccionario de Datos ALMA con el servidor IRIS.
IMPORTANTE: Esta skill SI consulta el servidor (una sola consulta eficiente).

**Trazabilidad automatica:**
- Registra fecha de sincronizacion
- Guarda historial en tabla `sync_log`
- Actualiza `fecha_actualizacion` en cada tabla modificada
- Actualiza metadata de version

## Uso
```
/diccionario-sync
```

## Instrucciones
1. Avisar al usuario que se consultara el servidor
2. Ejecutar:

```bash
cd "c:\_Consultas\Diccionario_Datos" && python sincronizar_todo.py
```

3. El script hace TODO automaticamente:
   - Importa schemas/tablas/columnas con descripciones
   - Actualiza fechas de mapeo y actualizacion
   - Exporta a CSV
   - Actualiza documentos MD
   - Registra sync en historial
   - Actualiza LOG

4. Mostrar las estadisticas finales al usuario

## Notas
- Solo hace UNA consulta grande al servidor (no satura)
- Actualiza LOG_AUDITORIA.md automaticamente
- Registra duracion y estadisticas de cada sync
- Si falla conexion, usa datos locales
