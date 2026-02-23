# lab.CTBB_BloodGroupXMatch

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBBGX_ParRef | varchar | PK |  | NO | CTBB_BloodGroups Parent Reference |
| BBBGX_BloodGroup_DR | varchar |  | FK | SI | Blood Group DR |
| BBBGX_BloodProduct_DR | varchar |  | FK | SI | Blood Product DR |
| BBBGX_Genotype_DR | varchar |  | FK | SI | Genotype DR |
| BBBGX_Order | varchar |  |  | NO | Order |
| BBBGX_Preference | numeric |  |  | SI | Preference |
| BBBGX_ProductGroup_DR | varchar |  | FK | SI | Product Group DR |
| BBBGX_RowID | varchar |  |  | NO | - |
| BBBGX_Sequence | numeric |  |  | NO | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*