# SQLUser.LBC_PathogenGroup

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPAG_RowID | bigint | PK |  | NO | - |
| LBCPAG_Code | varchar |  |  | SI | Code |
| LBCPAG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPAG_CreatedDate | date |  |  | SI | Created Date |
| LBCPAG_CreatedTime | time |  |  | SI | Created Time |
| LBCPAG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPAG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPAG_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPAG_Desc | varchar |  |  | SI | Description |
| LBCPAG_Owner | varchar |  |  | SI | Owner |
| LBCPAG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPAG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPAG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01Q1 | - |  |  | SI | ETAPA |
| Q01Q2 | - |  |  | SI | HORA DE ATENCIÓN |
| Q01Q3 | - |  |  | SI | SCORE DE TAL MODIFICADO (SBO) |
| Q01Q4 | - |  |  | SI | SATURACIÓN DE OXÍGENO |
| Q01Q5 | - |  |  | SI | INHALOTERAPIA |
| Q01Q6 | - |  |  | SI | APLICACIÓN DE OXÍGENO |
| Q01Q7 | - |  |  | SI | KINESIOTERAPIA RESPIRATORIA |
| Q01Q8 | - |  |  | SI | OBSERVACIONES |
| Q01Q9 | - |  |  | SI | DERIVACIÓN |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*