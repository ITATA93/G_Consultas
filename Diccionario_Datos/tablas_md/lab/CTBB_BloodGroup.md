# lab.CTBB_BloodGroup

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBBG_RowID | varchar | PK |  | NO | - |
| BBBG_128_IntendedUse | varchar |  |  | SI | 128 Intended Use |
| BBBG_ABO | varchar |  |  | SI | ABO |
| BBBG_BarCode | varchar |  |  | SI | Bar Code |
| BBBG_Code | varchar |  |  | NO | Code |
| BBBG_Description | varchar |  |  | SI | Description |
| BBBG_DisplaySequence | numeric |  |  | SI | Display Sequence |
| BBBG_ProductOnly | varchar |  |  | SI | Product Only |
| BBBG_Rh | varchar |  |  | SI | Rh |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*