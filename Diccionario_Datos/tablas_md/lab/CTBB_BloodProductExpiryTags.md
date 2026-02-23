# lab.CTBB_BloodProductExpiryTags

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBBPEX_ParRef | varchar | PK |  | NO | CTBB_BloodProduct Parent Reference |
| BBBPEX_BloodTags_DR | varchar |  | FK | NO | Blood Tag DR |
| BBBPEX_Default | varchar |  |  | SI | Default |
| BBBPEX_IgnoreTag | varchar |  |  | SI | Ignore Tag |
| BBBPEX_Lifespan | double |  |  | SI | Life span |
| BBBPEX_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*