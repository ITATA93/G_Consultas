# websys.MonitorGlobals

> "Capture, Store and report global size.<br/>

**Schema:** websys
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Capture, Store and report global size.<br/>

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DataBasePath | varchar |  |  | SI | Database path |
| GlobalName | varchar |  |  | SI | Global name |
| RunDate | date |  |  | SI | Date this run was started
RunDate and RunTime uni... |
| RunTime | time |  |  | SI | Time this run was started
RunDate and RunTime uni... |
| SizeAllocated | integer |  |  | SI | Size of allocated space in MB |
| SizeUsed | integer |  |  | SI | Size of used space in MB |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*