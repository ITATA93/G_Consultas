# SQLUser.LB_InstrumentTestImageFile

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBITIF_ParRef | bigint | PK |  | NO | Parent TestSet DR |
| ChildQ74DR | - |  |  | SI | Child Reference: Pulsos |
| LBITIF_Desc | varchar |  |  | SI | File description |
| LBITIF_FileType | varchar |  |  | SI | Type of the image file JPG, BMP, SVG, etc... |
| LBITIF_Image_DR | bigint |  | FK | SI | websys.document that stores the image data |
| LBITIF_RawData | longvarchar |  |  | SI | If the image is a SVG this property stores the raw... |
| LBITIF_RowID | varchar |  |  | NO | - |
| Q71Q1 | - |  |  | SI | Hallazgos |
| Q71Q2 | - |  |  | SI | Extremidad superior |
| Q71Q3 | - |  |  | SI | Extremidad inferior |
| Q71Q4 | - |  |  | SI | Ubicación |
| Q71Q5 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*