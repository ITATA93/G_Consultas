# websys.SSCRule

> "Allows configuration of rules that define whether a second signature is required on Administration.

**Schema:** websys
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Allows configuration of rules that define whether a second signature is required on Administration.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| SSCRAgeFrom | double |  |  | SI | AgeFrom |
| SSCRAgeTo | double |  |  | SI | AgeTo |
| SSCRAgeType | varchar |  |  | SI | Age Type |
| SSCRDateFrom | date |  |  | SI | - |
| SSCRDateTo | date |  |  | SI | - |
| SSCRSchedDrugClassDR | bigint |  | FK | SI | Scheduled Drug Classification |
| SSCRSchemaGroup | varchar |  |  | SI | Schema Groups |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*