# SQLUser.AR_HICClaimElement

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CE_ParRef | bigint | PK |  | NO | - |
| CE_DisplayOrder | varchar |  |  | SI | Segment Display Order |
| CE_ElementName | varchar |  |  | NO | Name of the element |
| CE_ElementValue | varchar |  |  | SI | Value of the element |
| CE_OEORI_DR | varchar |  | FK | SI | Order for the Service |
| CE_PatientBill_DR | bigint |  | FK | SI | Patient bill for the voucher |
| CE_RowID | varchar |  |  | NO | - |
| CE_SegmentID | varchar |  |  | NO | Segment identifier |
| CE_SegmentNumber | varchar |  |  | SI | Segment number
Only used if a segment can be repe... |
| CE_SubsegmentID | varchar |  |  | SI | Subsegement identifier |
| CE_SubsegmentNumber | varchar |  |  | SI | Subsegment number
Only used if a subsegment can b... |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*