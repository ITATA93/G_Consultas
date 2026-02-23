# lab.CTBB_EmergencyIssue

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBEME_RowID | varchar | PK |  | NO | - |
| BBEME_BloodGroup_DR | varchar |  | FK | SI | Blood Group DR |
| BBEME_BloodProduct_DR | varchar |  | FK | SI | Blood Product DR |
| BBEME_Preference | numeric |  |  | SI | Preference |
| BBEME_ProductGroup_DR | varchar |  | FK | SI | Product Group |
| BBEME_Sequence | varchar |  |  | NO | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*