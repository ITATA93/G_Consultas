# lab.CTBB_BloodGroupSupplier

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBBGS_ParRef | varchar | PK |  | NO | CTBB_BloodGroup Parent Reference |
| BBBGS_BarCode | varchar |  |  | SI | BarCode |
| BBBGS_RowID | varchar |  |  | NO | - |
| BBBGS_Supplier_DR | varchar |  | FK | NO | Supplier DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*