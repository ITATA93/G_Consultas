# lab.CTBB_TransfEventProducts

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBTEP_ParRef | varchar | PK |  | NO | CTBB_TransfusionEvent Parent Reference |
| BBTEP_NumberOfUnits | double |  |  | SI | Number Of Units |
| BBTEP_Order | double |  |  | NO | Order |
| BBTEP_ProductGroup_DR | varchar |  | FK | SI | Product Group DR |
| BBTEP_Product_DR | varchar |  | FK | SI | BB Product DR |
| BBTEP_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*