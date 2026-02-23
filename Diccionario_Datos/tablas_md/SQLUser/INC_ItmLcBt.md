# SQLUser.INC_ItmLcBt

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCLB_INCIL_ParRef | varchar | PK |  | NO | INCIL Par Ref |
| ChildQ70DR | - |  |  | SI | Child Reference: Test Movement Describe Effect on ... |
| INCLB_ChildSub | numeric |  |  | NO | INCLB ChildSub (NewKey) |
| INCLB_CreatedDate | date |  |  | SI | Created Date |
| INCLB_CreatedTime | time |  |  | SI | Created Time |
| INCLB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCLB_DirtyQty | double |  |  | SI | Dirty Qty |
| INCLB_INCIB_DR | varchar |  | FK | NO | Des Ref to INCIB |
| INCLB_OrigManufBatch_DR | varchar |  | FK | SI | Des Ref to Original Manufactured INCItmLcBt |
| INCLB_PhyQty | double |  |  | NO | Physical Quantity  |
| INCLB_RowId | varchar |  |  | NO | - |
| INCLB_UpdatedDate | date |  |  | SI | Updated Date |
| INCLB_UpdatedTime | time |  |  | SI | Updated Time |
| INCLB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q67Q1 | - |  |  | SI | Location |
| Q67Q2 | - |  |  | SI | Sensation |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*