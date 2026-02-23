# Tools_Upload.TU_HeaderDetail

**Schema:** Tools_Upload
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TUHD_ParRef | bigint | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| TUHD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TUHD_CustomProperty | varchar |  |  | SI | Custom Properties - as many as required 
Property... |
| TUHD_CustomValue | varchar |  |  | SI | - |
| TUHD_Description | varchar |  |  | SI | Detailed description  |
| TUHD_FromDate | date |  |  | SI | - |
| TUHD_Owner | varchar |  |  | SI | Owner - DEPRECATED - Code Table Overrides |
| TUHD_ToDate | date |  |  | SI | - |
| TUHD_UpdDate | date |  |  | SI | - |
| TUHD_UpdTime | time |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*