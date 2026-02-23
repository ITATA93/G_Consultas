# Tools_Upload.TU_Group

**Schema:** Tools_Upload
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| TUG_Code | varchar |  |  | NO | - |
| TUG_CreateDate | date |  |  | SI | - |
| TUG_CreateTime | time |  |  | SI | - |
| TUG_Description | varchar |  |  | NO | - |
| TUG_FeatureGroup_DR | bigint |  | FK | SI | Grouping Option via FeatureGroup |
| TUG_FromDate | date |  |  | SI | - |
| TUG_GroupDetail_DR | bigint |  | FK | SI | Current RunTime Details |
| TUG_Status | varchar |  |  | SI | - |
| TUG_ToDate | date |  |  | SI | - |
| TUG_UpdDate | date |  |  | SI | - |
| TUG_UpdTime | time |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*