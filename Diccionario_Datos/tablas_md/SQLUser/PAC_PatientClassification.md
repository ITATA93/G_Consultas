# SQLUser.PAC_PatientClassification

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PCLASS_RowId | bigint | PK |  | NO | - |
| PCLASS_Code | varchar |  |  | NO | Code |
| PCLASS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PCLASS_CreatedDate | date |  |  | SI | Created Date |
| PCLASS_CreatedTime | time |  |  | SI | Created Time |
| PCLASS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PCLASS_DateFrom | date |  |  | SI | Date From |
| PCLASS_DateTo | date |  |  | SI | Date To |
| PCLASS_Desc | varchar |  |  | NO | Description |
| PCLASS_Owner | varchar |  |  | SI | Owner |
| PCLASS_UpdatedDate | date |  |  | SI | Updated Date |
| PCLASS_UpdatedTime | time |  |  | SI | Updated Time |
| PCLASS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q30Q1 | - |  |  | SI | Bone mineral density |
| Q30Q10 | - |  |  | SI | % changes |
| Q30Q2 | - |  |  | SI | Latest result date |
| Q30Q3 | - |  |  | SI | Latest T score |
| Q30Q4 | - |  |  | SI | Latest Z score |
| Q30Q5 | - |  |  | SI | Latest Bone Mineral Content (BMC) |
| Q30Q6 | - |  |  | SI | Previous result date |
| Q30Q7 | - |  |  | SI | Previous T score |
| Q30Q8 | - |  |  | SI | Previous Z score |
| Q30Q9 | - |  |  | SI | Previous BMC |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*