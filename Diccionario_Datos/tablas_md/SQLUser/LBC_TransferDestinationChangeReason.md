# SQLUser.LBC_TransferDestinationChangeReason

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTDCR_RowID | bigint | PK |  | NO | - |
| LBCTDCR_Code | varchar |  |  | NO | Code |
| LBCTDCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTDCR_CreatedDate | date |  |  | SI | Created Date |
| LBCTDCR_CreatedTime | time |  |  | SI | Created Time |
| LBCTDCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTDCR_DateFrom | date |  |  | NO | Date From |
| LBCTDCR_DateTo | date |  |  | SI | Date To |
| LBCTDCR_Desc | varchar |  |  | NO | Description |
| LBCTDCR_Owner | varchar |  |  | SI | Owner |
| LBCTDCR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTDCR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTDCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q21Q1 | - |  |  | SI | Ojo |
| Q21Q2 | - |  |  | SI | Cuadrante |
| Q21Q3 | - |  |  | SI | Comentarios |
| Q21Q4 | - |  |  | SI | Hemorragia Subconjuntival |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*