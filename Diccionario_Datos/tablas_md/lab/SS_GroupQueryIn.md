# lab.SS_GroupQueryIn

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSGRQ_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| SSGRQ_DisplaySequence | double |  |  | SI | Display Sequence |
| SSGRQ_Query_DR | varchar |  | FK | NO | Query DR |
| SSGRQ_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*