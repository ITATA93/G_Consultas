# SQLUser.PA_Vaccination

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| PAVAC_Date | date |  |  | SI | Date |
| PAVAC_Dose_DR | bigint |  | FK | SI | Dose |
| PAVAC_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| PAVAC_ErrorReason_DR | bigint |  | FK | SI | Des Ref - Error Reason |
| PAVAC_IsApproximateDate | bit |  |  | SI | Is Approximate Date |
| PAVAC_LotNumber | varchar |  |  | SI | Lot Number |
| PAVAC_OrderItemFreeText | varchar |  |  | SI | Order Item Free Text |
| PAVAC_OrderItem_DR | varchar |  | FK | SI | Order Item |
| PAVAC_PatMas_DR | bigint |  | FK | SI | Ref PAPatMas |
| PAVAC_PathwayItem_DR | varchar |  | FK | SI | Pathway Item |
| PAVAC_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref - Reason For Correction |
| PAVAC_Route_DR | bigint |  | FK | SI | Route |
| PAVAC_Site_DR | bigint |  | FK | SI | Site |
| PAVAC_VaccinationNotes | varchar |  |  | SI | Vaccination Notes |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*