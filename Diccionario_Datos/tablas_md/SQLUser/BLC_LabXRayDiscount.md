# SQLUser.BLC_LabXRayDiscount

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LABX_RowId | bigint | PK |  | NO | - |
| ChildQ06DR | - |  |  | SI | Child Reference: LABORAL COMUNITARIO |
| LABX_BillSubGrp_DR | varchar |  | FK | SI | Des Ref BillSubGrp_DR |
| LABX_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LABX_CreatedDate | date |  |  | SI | Created Date |
| LABX_CreatedTime | time |  |  | SI | Created Time |
| LABX_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LABX_DateFrom | date |  |  | NO | Date From |
| LABX_DateTo | date |  |  | SI | Date To |
| LABX_EpisodeType | varchar |  |  | SI | EpisodeType |
| LABX_FromXtest | double |  |  | SI | From X test |
| LABX_HospClass_DR | bigint |  | FK | SI | Des Ref HospClass |
| LABX_InsType_DR | bigint |  | FK | SI | Des Ref InsType_DR |
| LABX_Owner | varchar |  |  | SI | Owner |
| LABX_Perc | double |  |  | SI | % Discount |
| LABX_ToXtest | double |  |  | SI | To X test |
| LABX_UpdatedDate | date |  |  | SI | Updated Date |
| LABX_UpdatedTime | time |  |  | SI | Updated Time |
| LABX_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q05Q1 | - |  |  | SI | Objetivos |
| Q05Q2 | - |  |  | SI | Estrategias o Actividades |
| Q05Q3 | - |  |  | SI | Responsables |
| Q05Q4 | - |  |  | SI | Plazo |
| Q05Q5 | - |  |  | SI | Indicador de Logro |
| Q05Q6 | - |  |  | SI | Cumplimiento |
| Q05Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*