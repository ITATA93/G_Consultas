# SQLUser.ARC_ServTax

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCST_RowId | bigint | PK |  | NO | - |
| ARCST_AccruedAccount_DR | bigint |  | FK | SI | Des Ref AccruedAccount |
| ARCST_Code | varchar |  |  | NO | Service Tax Code |
| ARCST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCST_Cosmetic | varchar |  |  | SI | Cosmetic Flag |
| ARCST_CreatedDate | date |  |  | SI | Created Date |
| ARCST_CreatedTime | time |  |  | SI | Created Time |
| ARCST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCST_Desc | varchar |  |  | NO | Description |
| ARCST_ExcludeFromStampDuty | varchar |  |  | SI |  Exclude from Stamp Duty Calculation |
| ARCST_IpRate | double |  |  | SI | Inpatient Rate |
| ARCST_OpRate | double |  |  | SI | Outpatient Rate |
| ARCST_Owner | varchar |  |  | SI | Owner |
| ARCST_RcFlag | varchar |  |  | SI | Archived Flag |
| ARCST_UpdatedDate | date |  |  | SI | Updated Date |
| ARCST_UpdatedTime | time |  |  | SI | Updated Time |
| ARCST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ19DR | - |  |  | SI | Child Reference: Motivo de consulta según acompaña... |
| Q18Q1 | - |  |  | SI | Motivo |
| Q18Q2 | - |  |  | SI | Código |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*