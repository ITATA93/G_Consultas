# SQLUser.ARC_InsTypePostOffice

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYPO_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| ChildQ84DR | - |  |  | SI | Child Reference: Funciones Cognitivas |
| PAYPO_Childsub | double |  |  | NO | Childsub |
| PAYPO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAYPO_CreatedDate | date |  |  | SI | Created Date |
| PAYPO_CreatedTime | time |  |  | SI | Created Time |
| PAYPO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAYPO_DateFrom | date |  |  | SI | Date From |
| PAYPO_DateTo | date |  |  | SI | Date To |
| PAYPO_PostOffice_DR | bigint |  | FK | NO | Post Office |
| PAYPO_RowId | varchar |  |  | NO | - |
| PAYPO_UpdatedDate | date |  |  | SI | Updated Date |
| PAYPO_UpdatedTime | time |  |  | SI | Updated Time |
| PAYPO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q78Q1 | - |  |  | SI | Características |
| Q78Q2 | - |  |  | SI | Evaluación |
| Q78Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*