# SQLUser.ARC_SurchSpecialist

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPEC_ParRef | bigint | PK |  | NO | ARC_SurchargeCode Parent Reference |
| ChildQ08DR | - |  |  | SI | Child Reference: Motivo de consulta según adolesce... |
| Q09Q1 | - |  |  | SI | Código |
| Q09Q2 | - |  |  | SI | Descripción |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SPEC_Childsub | double |  |  | NO | Childsub |
| SPEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SPEC_CreatedDate | date |  |  | SI | Created Date |
| SPEC_CreatedTime | time |  |  | SI | Created Time |
| SPEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SPEC_DateFrom | date |  |  | SI | Date From |
| SPEC_DateTo | date |  |  | SI | Date To |
| SPEC_FixedAmt | double |  |  | SI | Fixed Amt |
| SPEC_Name | varchar |  |  | SI | Description |
| SPEC_Perc | double |  |  | SI | % Charge |
| SPEC_RowId | varchar |  |  | NO | - |
| SPEC_UpdatedDate | date |  |  | SI | Updated Date |
| SPEC_UpdatedTime | time |  |  | SI | Updated Time |
| SPEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SPEC_VisitType | varchar |  |  | SI | Visit Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*