# lab.EP_VisitBillingItems

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISBI_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISBI_Amount | double |  |  | SI | Amount |
| VISBI_BaseAmount | double |  |  | SI | Base Amount |
| VISBI_Desc | varchar |  |  | SI | Description |
| VISBI_GST | varchar |  |  | SI | GST item |
| VISBI_Item_DR | varchar |  | FK | NO | Des Ref Billing Item |
| VISBI_RowId | varchar |  |  | NO | - |
| VISBI_Rule3_Exempt | varchar |  |  | SI | Rule 3 Exempt |
| VISBI_Rule4_Exempt | varchar |  |  | SI | Rule4 Exempt |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*