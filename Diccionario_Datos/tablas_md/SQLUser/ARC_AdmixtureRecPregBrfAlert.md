# SQLUser.ARC_AdmixtureRecPregBrfAlert

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBA_ParRef | bigint | PK |  | NO | ARC_AdmixtureRecipe Parent Reference |
| ChildQ32DR | - |  |  | SI | Child Reference: Audífonos |
| PBA_Childsub | double |  |  | NO | Childsub |
| PBA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PBA_CreatedDate | date |  |  | SI | Created Date |
| PBA_CreatedTime | time |  |  | SI | Created Time |
| PBA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PBA_DateFrom | date |  |  | SI | DateFrom |
| PBA_DateTo | date |  |  | SI | DateTo |
| PBA_Message | varchar |  |  | SI | Message |
| PBA_Options | varchar |  |  | SI | Options |
| PBA_PregnCateg_DR | bigint |  | FK | SI | Des Ref PACPregnancyCategory |
| PBA_RowId | varchar |  |  | NO | - |
| PBA_UpdatedDate | date |  |  | SI | Updated Date |
| PBA_UpdatedTime | time |  |  | SI | Updated Time |
| PBA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q31Q1 | - |  |  | SI | Sin Lentes |
| Q31Q2 | - |  |  | SI | Tipo de Lentes |
| Q31Q3 | - |  |  | SI | Estado |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*