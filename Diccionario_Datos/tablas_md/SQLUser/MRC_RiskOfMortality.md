# SQLUser.MRC_RiskOfMortality

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RSMORT_RowId | bigint | PK |  | NO | - |
| Q53Q1 | - |  |  | SI | Sin Dispositivo |
| Q53Q2 | - |  |  | SI | Dispositivo |
| Q53Q3 | - |  |  | SI | Otro Dispositivo |
| Q53Q4 | - |  |  | SI | Tamaño |
| Q53Q5 | - |  |  | SI | Ubicación |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RSMORT_Code | varchar |  |  | NO | Code |
| RSMORT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RSMORT_CreatedDate | date |  |  | SI | Created Date |
| RSMORT_CreatedTime | time |  |  | SI | Created Time |
| RSMORT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RSMORT_DateFrom | date |  |  | SI | Date From |
| RSMORT_DateTo | date |  |  | SI | Date To |
| RSMORT_Desc | varchar |  |  | NO | Description |
| RSMORT_Owner | varchar |  |  | SI | Owner |
| RSMORT_UpdatedDate | date |  |  | SI | Updated Date |
| RSMORT_UpdatedTime | time |  |  | SI | Updated Time |
| RSMORT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*