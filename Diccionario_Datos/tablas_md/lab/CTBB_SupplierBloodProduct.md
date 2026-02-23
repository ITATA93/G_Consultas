# lab.CTBB_SupplierBloodProduct

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBSPP_ParRef | varchar | PK |  | NO | CTBB_Supplier Parent Reference |
| BBSPP_BarCode | varchar |  |  | SI | Bar Code |
| BBSPP_BloodProduct_DR | varchar |  | FK | NO | Blood Product DR |
| BBSPP_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*