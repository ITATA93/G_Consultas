# web_Msg_OEOrdItem_PharmacyReview.Item

**Schema:** web_Msg_OEOrdItem_PharmacyReview
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| MedicationSourceDR | bigint |  | FK | SI | Des Ref PHCMedicationSource  |
| OEOrdItemDR | varchar |  | FK | SI | Des Ref OEOrdItem |
| OrderStatusDR | bigint |  | FK | SI | Des Ref OECOrderStatus |
| PharmRevStatDR | bigint |  | FK | SI | Des Ref OECPharmacyReviewStatus |
| PharmRevwNotApprDR | bigint |  | FK | SI | Des Ref PHCReasonPharmRevwNotApproved |
| PharmRevwNotes | varchar |  |  | SI | PharmRevwNotes |
| PharmacyStatus | varchar |  |  | SI | PharmacyStatus |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*