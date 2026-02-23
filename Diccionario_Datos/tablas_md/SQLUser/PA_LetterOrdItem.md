# SQLUser.PA_LetterOrdItem

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LETORD_ParRef | bigint | PK |  | NO | PA_Letter Parent Reference |
| LETORD_Childsub | double |  |  | NO | Childsub |
| LETORD_OEORI_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| LETORD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*