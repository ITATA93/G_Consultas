# SQLUser.INC_ItmHospVenDiscount

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISC_ParRef | varchar | PK |  | NO | Des Ref to VEN |
| DISC_BonusStock | double |  |  | SI | Bonus Stock |
| DISC_ChildSub | numeric |  |  | NO | DISC Child Sub |
| DISC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DISC_CreatedDate | date |  |  | SI | Created Date |
| DISC_CreatedTime | time |  |  | SI | Created Time |
| DISC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISC_DateFrom | date |  |  | SI | Date From |
| DISC_DateTo | date |  |  | SI | Date To |
| DISC_Discount | double |  |  | SI | % Discount |
| DISC_QtyFrom | double |  |  | SI | Qty From |
| DISC_QtyTo | double |  |  | SI | Qty To |
| DISC_RowId | varchar |  |  | NO | - |
| DISC_UpdatedDate | date |  |  | SI | Updated Date |
| DISC_UpdatedTime | time |  |  | SI | Updated Time |
| DISC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q46Q1 | - |  |  | SI | Biopsy sample number |
| Q46Q2 | - |  |  | SI | Biopsy location |
| Q46Q3 | - |  |  | SI | Side |
| Q46Q4 | - |  |  | SI | Time of sample |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*