# SQLUser.PAC_EscortSource

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ESCS_RowId | bigint | PK |  | NO | - |
| ESCS_Code | varchar |  |  | NO | Code |
| ESCS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ESCS_CreatedDate | date |  |  | SI | Created Date |
| ESCS_CreatedTime | time |  |  | SI | Created Time |
| ESCS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ESCS_DateFrom | date |  |  | SI | Date From |
| ESCS_DateTo | date |  |  | SI | Date To |
| ESCS_Desc | varchar |  |  | NO | Description |
| ESCS_Owner | varchar |  |  | SI | Owner |
| ESCS_UpdatedDate | date |  |  | SI | Updated Date |
| ESCS_UpdatedTime | time |  |  | SI | Updated Time |
| ESCS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q04Q1 | - |  |  | SI | Day |
| Q04Q10 | - |  |  | SI | Assessment time |
| Q04Q2 | - |  |  | SI | The antibiotic is prescribed in accordance with ho... |
| Q04Q3 | - |  |  | SI | Culture and sensitivity result is reviewed. |
| Q04Q4 | - |  |  | SI | Contact precaution is implemented and proper used ... |
| Q04Q5 | - |  |  | SI | Environmental cleaning using hospital approved dis... |
| Q04Q6 | - |  |  | SI | Hand hygiene |
| Q04Q7 | - |  |  | SI | Decolonization |
| Q04Q8 | - |  |  | SI | Assessing care provider |
| Q04Q9 | - |  |  | SI | Assessment date |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*