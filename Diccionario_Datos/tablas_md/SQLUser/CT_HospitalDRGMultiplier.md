# SQLUser.CT_HospitalDRGMultiplier

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGML_ParRef | bigint | PK |  | NO | CT_Hospital Parent Reference |
| ChildQ80DR | - |  |  | SI | Child Reference: Eyes open, foam surface |
| DRGML_Childsub | double |  |  | NO | Childsub |
| DRGML_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGML_CreatedDate | date |  |  | SI | Created Date |
| DRGML_CreatedTime | time |  |  | SI | Created Time |
| DRGML_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGML_DRGMultiplier | double |  |  | SI | DRG Multiplier |
| DRGML_DateFrom | date |  |  | SI | Date From |
| DRGML_DateTo | date |  |  | SI | Date To |
| DRGML_Rowid | varchar |  |  | NO | - |
| DRGML_UpdatedDate | date |  |  | SI | Updated Date |
| DRGML_UpdatedTime | time |  |  | SI | Updated Time |
| DRGML_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q79Q1 | - |  |  | SI | Time |
| Q79Q2 | - |  |  | SI | Strategy |
| Q79Q3 | - |  |  | SI | Sway |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*