# SQLUser.INC_ItmHospVenCommItems

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COMM_ParRef | varchar | PK |  | NO | Des Ref to VEN |
| COMM_ChildSub | numeric |  |  | NO | COMM Child Sub |
| COMM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COMM_CommItem_DR | bigint |  | FK | SI | Des REf CommItem |
| COMM_CreatedDate | date |  |  | SI | Created Date |
| COMM_CreatedTime | time |  |  | SI | Created Time |
| COMM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COMM_DateFrom | date |  |  | SI | DateFrom |
| COMM_DateTo | date |  |  | SI | DateTo |
| COMM_Preffered | varchar |  |  | SI | Preffered |
| COMM_Price | double |  |  | SI | Price |
| COMM_RowId | varchar |  |  | NO | - |
| COMM_UOM_DR | bigint |  | FK | SI | Des REf UOM |
| COMM_UpdatedDate | date |  |  | SI | Updated Date |
| COMM_UpdatedTime | time |  |  | SI | Updated Time |
| COMM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ46DR | - |  |  | SI | Child Reference: Biopsy details |
| Q31Q1 | - |  |  | SI | Lesion number |
| Q31Q2 | - |  |  | SI | Clock position |
| Q31Q3 | - |  |  | SI | At the SCJ |
| Q31Q4 | - |  |  | SI | Lesion visualized |
| Q31Q5 | - |  |  | SI | Satellite lesion |
| Q31Q6 | - |  |  | SI | Lesion size (mm) |
| Q31Q7 | - |  |  | SI | Size of the lesion |
| Q31Q8 | - |  |  | SI | No. Quadrants the lesion involves |
| Q31Q9 | - |  |  | SI | Percentage of affected area (%) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*