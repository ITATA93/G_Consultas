# SQLUser.LBC_WorksheetGroup

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCWSG_RowID | bigint | PK |  | NO | - |
| LBCWSG_Code | varchar |  |  | NO | Worksheet Group Code |
| LBCWSG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCWSG_CreatedDate | date |  |  | SI | Created Date |
| LBCWSG_CreatedTime | time |  |  | SI | Created Time |
| LBCWSG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCWSG_DateFrom | date |  |  | SI | Date From |
| LBCWSG_DateTo | date |  |  | SI | Date To |
| LBCWSG_Desc | varchar |  |  | NO | Worksheet Group Description |
| LBCWSG_Owner | varchar |  |  | SI | Owner |
| LBCWSG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCWSG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCWSG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q50Q1 | - |  |  | SI | Método |
| Q50Q2 | - |  |  | SI | Virus |
| Q50Q3 | - |  |  | SI | Establecimiento |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*