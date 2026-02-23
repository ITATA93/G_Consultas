# lab.CTBB_ProductGroupLocation

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBPGL_ParRef | varchar | PK |  | NO | CTBB_ProductGroups Parent Reference |
| BBPGL_BBLocation_DR | varchar |  | FK | SI | BB Location DR |
| BBPGL_RowID | varchar |  |  | NO | - |
| BBPGL_UserSite_DR | varchar |  | FK | NO | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*