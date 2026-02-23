# lab.CTBB_BloodGroupReaction

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBBGR_ParRef | varchar | PK |  | NO | CTBB_BloodGroups Parent Reference |
| BBBGR_Result | varchar |  |  | SI | Result |
| BBBGR_RowID | varchar |  |  | NO | - |
| BBBGR_TestItem_DR | varchar |  | FK | NO | Test Item DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*