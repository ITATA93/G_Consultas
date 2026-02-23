# lab.CT_ICD10

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTICD_RowID | varchar | PK |  | NO | - |
| CTICD_ClinicalUse | varchar |  |  | SI | Clinical Use |
| CTICD_Code | varchar |  |  | NO | Code |
| CTICD_Description | varchar |  |  | SI | Description |
| CTICD_FullDescription | varchar |  |  | SI | Full Description |
| CTICD_ICD10Group_DR | varchar |  | FK | SI | ICD10 Group DR |
| CTICD_Primary | varchar |  |  | SI | Primary |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*