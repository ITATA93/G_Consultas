# Tools_Recorder.ObjectRecorder

**Schema:** Tools_Recorder
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AuditEndRow | integer |  |  | SI | - |
| AuditStartRow | integer |  |  | SI | - |
| CreatedBy | bigint |  |  | SI | - |
| DateCreated | date |  |  | SI | - |
| ItemsTouched | varchar |  |  | SI | This Parameter is updated by Perforce |
| LastUpdated | date |  |  | SI | - |
| LastUpdatedBy | bigint |  |  | SI | - |
| TestDescription | varchar |  |  | SI | - |
| TestName | varchar |  |  | NO | - |
| TestStatus | varchar |  |  | SI | - |
| TextOutput | longvarchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*