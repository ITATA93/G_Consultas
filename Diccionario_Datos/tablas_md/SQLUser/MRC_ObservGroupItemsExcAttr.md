# SQLUser.MRC_ObservGroupItemsExcAttr

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXCA_ParRef | varchar | PK |  | NO | - |
| ChildQ08DR | - |  |  | SI | Child Reference: Factores de Riesgo y Protectores |
| EXCA_Childsub | double |  |  | NO | Childsub |
| EXCA_CreatedDate | date |  |  | SI | Created Date |
| EXCA_CreatedTime | time |  |  | SI | Created Time |
| EXCA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EXCA_ObsItemAttrDR | varchar |  | FK | SI | Des Ref Observation Item Attribute |
| EXCA_RowId | varchar |  |  | NO | - |
| EXCA_UpdatedDate | date |  |  | SI | Updated Date |
| EXCA_UpdatedTime | time |  |  | SI | Updated Time |
| EXCA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q09Q1 | - |  |  | SI | Acuerdos |
| Q09Q2 | - |  |  | SI | Responsables |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*