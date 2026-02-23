# SQLUser.OE_AdmixNurseResItem

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEANRI_ParRef | varchar | PK |  | NO | OE_OrdExec Parent Reference |
| ChildQ62DR | - |  |  | SI | Child Reference: Medical Review |
| OEANRI_AdmixItemID | varchar |  |  | SI | Admixture Item ID |
| OEANRI_Childsub | double |  |  | NO | Childsub |
| OEANRI_RowId | varchar |  |  | NO | - |
| OEANRI_StockItem_DR | varchar |  | FK | SI | Stock Item |
| OEANRI_StockLocation_DR | bigint |  | FK | SI | Stock Location |
| Q08Q1 | - |  |  | SI | Date |
| Q08Q2 | - |  |  | SI | Time |
| Q08Q3 | - |  |  | SI | Type of pain |
| Q08Q4 | - |  |  | SI | Pain scale |
| Q08Q4NEW | - |  |  | SI | Pain scale |
| Q08Q5 | - |  |  | SI | Note |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*