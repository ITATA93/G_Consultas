# SQLUser.PAC_RefStageTemplate

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RFSTMP_RowId | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: Compliance |
| Q10Q1 | - |  |  | SI | Date |
| Q10Q2 | - |  |  | SI | Peritonitis incidence number |
| Q10Q3 | - |  |  | SI | Organism |
| Q10Q4 | - |  |  | SI | Antibiotic therapy |
| Q10Q5 | - |  |  | SI | Outcome |
| Q10Q6 | - |  |  | SI | Comment |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RFSTMP_Code | varchar |  |  | NO | Code |
| RFSTMP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RFSTMP_CreatedDate | date |  |  | SI | Created Date |
| RFSTMP_CreatedTime | time |  |  | SI | Created Time |
| RFSTMP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RFSTMP_DateFrom | date |  |  | SI | Date From |
| RFSTMP_DateTo | date |  |  | SI | Date To |
| RFSTMP_Desc | varchar |  |  | NO | Description |
| RFSTMP_Duration | double |  |  | SI | Duration |
| RFSTMP_MaxExtension | double |  |  | SI | Maximum Extention days to the stage duration RFSTM... |
| RFSTMP_MaxReduction | double |  |  | SI | Maximum Reduction days to the stage duration RFSTM... |
| RFSTMP_Owner | varchar |  |  | SI | Owner |
| RFSTMP_Type_DR | bigint |  | FK | SI | Des Ref Type |
| RFSTMP_UpdatedDate | date |  |  | SI | Updated Date |
| RFSTMP_UpdatedTime | time |  |  | SI | Updated Time |
| RFSTMP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*