# Tools_DrugUpload_DURM.Queue

**Schema:** Tools_DrugUpload_DURM
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DRMQ_AcceptDate | date |  |  | SI | Accept Date / Time - if filled = Accepted |
| DRMQ_AcceptTime | time |  |  | SI | - |
| DRMQ_AcceptUser | varchar |  |  | SI | User (may contain "AUTO ACCEPT" not required real ... |
| DRMQ_Class | varchar |  |  | NO | - |
| DRMQ_ClassProp | varchar |  |  | NO | Property |
| DRMQ_Code | varchar |  |  | NO | Code reference |
| DRMQ_ConfigKey | varchar |  |  | NO | Key as per Config |
| DRMQ_CurrentValue | varchar |  |  | NO | - |
| DRMQ_NewValue | varchar |  |  | NO | - |
| DRMQ_ParentRef | varchar |  |  | SI | Parent reference (if needed, as Code) |
| DRMQ_ParentRow | varchar |  |  | SI | Parent reference (as RowID) |
| DRMQ_Row | varchar |  |  | NO | Row (loose) reference |
| DRMQ_RunRef | varchar |  |  | NO | - |
| DRMQ_UpdateDate | date |  |  | NO | last changed Date  |
| DRMQ_UpdateTime | time |  |  | NO | last changed Time  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*