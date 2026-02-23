# lab.CT_LabelPrint

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLB_RowId | varchar | PK |  | NO | - |
| CTLB_Aliquot | varchar |  |  | SI | Aliquot |
| CTLB_Code | varchar |  |  | NO | Code |
| CTLB_DefaultSpecimen_DR | varchar |  | FK | SI | Default Specimen DR |
| CTLB_Description | varchar |  |  | SI | Description |
| CTLB_ExtraLabels | double |  |  | SI | Extra Labels |
| CTLB_MaxNumberOfTests | double |  |  | SI | Max Number Of Tests |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*