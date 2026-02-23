# websys.DSSRule

**Schema:** websys
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Code | varchar |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| FieldId | varchar |  |  | SI | - |
| FldId | varchar |  |  | NO | - |
| FldValue | varchar |  |  | NO | - |
| FldValueType | varchar |  |  | SI | - |
| LastRun | varchar |  |  | SI | - |
| LstRange | varchar |  |  | SI | Comma separated list of ranges
E.g 0-10,11-20,21-... |
| RulType | varchar |  |  | NO | - |
| Status | varchar |  |  | SI | - |
| TblIndexName | varchar |  |  | SI | - |
| TblName | varchar |  |  | NO | - |
| TriggerClass | varchar |  |  | SI | - |
| TriggerSQL | varchar |  |  | SI | - |
| Triggerpath | varchar |  |  | SI | - |
| ValLength | integer |  |  | SI | - |
| ValMatch | varchar |  |  | SI | - |
| ValType | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*