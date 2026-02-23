# lab.CTBB_BloodGroupNeonatalXM

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBBGN_ParRef | varchar | PK |  | NO | CTBB_BloodGroup Parent Reference |
| BBBGN_AvailableBloodGroup_DR | varchar |  | FK | SI | Available Blood Group DR |
| BBBGN_BloodProduct_DR | varchar |  | FK | SI | Blood Product DR |
| BBBGN_Genotype_DR | varchar |  | FK | SI | Genotype DR |
| BBBGN_MotherBloodGroup_Calc | varchar |  |  | SI | Mother Blood Group calculated |
| BBBGN_MotherBloodGroup_DR | varchar |  | FK | SI | Mother Blood Group DR |
| BBBGN_Order | numeric |  |  | NO | Order |
| BBBGN_Preference | numeric |  |  | SI | Preference |
| BBBGN_ProductGroup_DR | varchar |  | FK | SI | Blood Product Group DR |
| BBBGN_RowID | varchar |  |  | NO | - |
| BBBGN_Sequence | numeric |  |  | NO | Display Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*