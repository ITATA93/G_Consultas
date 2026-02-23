# SQLUser.RB_ResEffDateSessLocation

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParRef | varchar | PK |  | NO | RB_ResEffDateSession Parent Reference |
| LOC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_DOW_DR | double |  | FK | SI | Des Ref DOW |
| LOC_RowId | varchar |  |  | NO | - |
| LOC_StartTime | time |  |  | SI | Start Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*