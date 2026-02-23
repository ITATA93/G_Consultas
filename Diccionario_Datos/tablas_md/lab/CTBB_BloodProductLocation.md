# lab.CTBB_BloodProductLocation

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBBPL_ParRef | varchar | PK |  | NO | CTBB_BloodProduct Parent Reference |
| BBBPL_BBLocation_DR | varchar |  | FK | SI | BB Location DR |
| BBBPL_RowID | varchar |  |  | NO | - |
| BBBPL_UserSite_DR | varchar |  | FK | NO | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*