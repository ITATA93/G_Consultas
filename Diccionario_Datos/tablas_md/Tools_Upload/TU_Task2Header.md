# Tools_Upload.TU_Task2Header

**Schema:** Tools_Upload
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| TUT2H_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TUT2H_CreateDate | date |  |  | SI | - |
| TUT2H_CreateTime | time |  |  | SI | - |
| TUT2H_FreezeDate | date |  |  | SI | used to compare if a new freeze is required  |
| TUT2H_FreezeForCode | varchar |  |  | SI | Reference to the original Header (just Code)  |
| TUT2H_FreezeTime | time |  |  | SI | used to compare if a new freeze is required  |
| TUT2H_FreezeVersion | integer |  |  | SI | To keep freezed copies this flag indicates a "used... |
| TUT2H_FromDate | date |  |  | SI | - |
| TUT2H_Header_DR | bigint |  | FK | NO | - |
| TUT2H_Owner | varchar |  |  | SI | Owner |
| TUT2H_Sequence | integer |  |  | SI | - |
| TUT2H_Task_DR | bigint |  | FK | NO | - |
| TUT2H_ToDate | date |  |  | SI | - |
| TUT2H_UpdDate | date |  |  | SI | - |
| TUT2H_UpdTime | time |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*