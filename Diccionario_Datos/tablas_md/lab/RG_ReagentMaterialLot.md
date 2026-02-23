# lab.RG_ReagentMaterialLot

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RGML_ParRef | varchar | PK |  | NO | RG_ReagentMaterial Parent Reference |
| RGML_Comments | varchar |  |  | SI | Comments |
| RGML_DateClosed | date |  |  | SI | Date Closed |
| RGML_DateExpiry | date |  |  | SI | Date Expiry |
| RGML_DateOpen | date |  |  | SI | Date Open |
| RGML_LotNumber | varchar |  |  | SI | Lot Number |
| RGML_NumberOfUnits | double |  |  | SI | Number of Units |
| RGML_Quarantine | varchar |  |  | SI | Quarantine |
| RGML_RowID | varchar |  |  | NO | - |
| RGML_Sequence | varchar |  |  | NO | Sequence |
| RGML_UnitsInStock | double |  |  | SI | Units In Stock |
| RGML_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*