# SQLUser.CT_HospitalDRGFundGroup

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DFG_ParRef | bigint | PK |  | NO | CT_Hospital Parent Reference |
| ChildQ79DR | - |  |  | SI | Child Reference: Eyes closed, firm surface |
| DFG_Childsub | double |  |  | NO | Childsub |
| DFG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DFG_CreatedDate | date |  |  | SI | Created Date |
| DFG_CreatedTime | time |  |  | SI | Created Time |
| DFG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DFG_DateFrom | date |  |  | SI | Date From |
| DFG_DateTo | date |  |  | SI | Date To |
| DFG_HospDRGCateg_DR | bigint |  | FK | SI | Des Ref HospDRGCateg |
| DFG_RowId | varchar |  |  | NO | - |
| DFG_UpdatedDate | date |  |  | SI | Updated Date |
| DFG_UpdatedTime | time |  |  | SI | Updated Time |
| DFG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q78Q1 | - |  |  | SI | Time |
| Q78Q2 | - |  |  | SI | Strategy |
| Q78Q3 | - |  |  | SI | Sway |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*