# SQLUser.PAC_VacDoseOrderItem

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACVDOI_RowID | bigint | PK |  | NO | - |
| PACVDOI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACVDOI_CreatedDate | date |  |  | SI | Created Date |
| PACVDOI_CreatedTime | time |  |  | SI | Created Time |
| PACVDOI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACVDOI_DateFrom | date |  |  | SI | Date From |
| PACVDOI_DateTo | date |  |  | SI | Date To |
| PACVDOI_ItmMast_DR | varchar |  | FK | SI | Order Item |
| PACVDOI_Owner | varchar |  |  | SI | Owner |
| PACVDOI_UpdatedDate | date |  |  | SI | Updated Date |
| PACVDOI_UpdatedTime | time |  |  | SI | Updated Time |
| PACVDOI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PACVDOI_VacDose_DR | bigint |  | FK | SI | Parent PACVacDose object |
| Q40Q1 | - |  |  | SI | Date |
| Q40Q2 | - |  |  | SI | Time |
| Q40Q3 | - |  |  | SI | Condition of site |
| Q40Q4 | - |  |  | SI | Cannula left in situ |
| Q40Q5 | - |  |  | SI | Condition of cannula |
| Q40Q6 | - |  |  | SI | Site check notes |
| Q40Q7 | - |  |  | SI | Checked by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*