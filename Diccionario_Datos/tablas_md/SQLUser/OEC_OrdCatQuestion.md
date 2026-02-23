# SQLUser.OEC_OrdCatQuestion

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUES_ParRef | bigint | PK |  | NO | OEC_OrderCategory Parent Reference |
| Q05Q1 | - |  |  | SI | Activity |
| Q05Q2 | - |  |  | SI | Respiration |
| Q05Q3 | - |  |  | SI | Circulation |
| Q05Q4 | - |  |  | SI | Consciousness |
| Q05Q5 | - |  |  | SI | Pulse Oximetry on room air |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| QUES_Childsub | double |  |  | NO | Childsub |
| QUES_ClinicalDetails | varchar |  |  | SI | ClinicalDetails |
| QUES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QUES_CreatedDate | date |  |  | SI | Created Date |
| QUES_CreatedTime | time |  |  | SI | Created Time |
| QUES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QUES_DateFrom | date |  |  | SI | Date From |
| QUES_DateTo | date |  |  | SI | Date To |
| QUES_Mandatory | varchar |  |  | SI | Mandatory |
| QUES_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| QUES_Question_DR | bigint |  | FK | NO | Des Ref Question |
| QUES_RowId | varchar |  |  | NO | - |
| QUES_UpdatedDate | date |  |  | SI | Updated Date |
| QUES_UpdatedTime | time |  |  | SI | Updated Time |
| QUES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*