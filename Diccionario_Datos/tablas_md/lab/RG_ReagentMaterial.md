# lab.RG_ReagentMaterial

**Schema:** lab
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RGM_RowID | varchar | PK |  | NO | - |
| RGM_ActiveFlag | varchar |  |  | SI | Active Flag |
| RGM_Barcodes | varchar |  |  | SI | Barcodes |
| RGM_Classification_DR | varchar |  | FK | SI | Classification DR |
| RGM_Code | varchar |  |  | NO | Code |
| RGM_Comments | varchar |  |  | SI | Comments |
| RGM_DefaultBatchSize | double |  |  | SI | Default batch size |
| RGM_Description | varchar |  |  | SI | Description |
| RGM_ExternalLink | varchar |  |  | SI | External Link |
| RGM_MaterialBaseUnit_DR | varchar |  | FK | SI | Material Base Unit DR |
| RGM_MaxLevelWarning | double |  |  | SI | MAX Stock level Warning |
| RGM_MinLevelWarning | double |  |  | SI | MIN Stock level Warning |
| RGM_OrderBy | double |  |  | SI | Order By |
| RGM_Supplier_DR | varchar |  | FK | SI | Supplier DR |
| RGM_UnitsInStock | double |  |  | SI | Units In Stock |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*