# SQLUser.RB_ResEffDateSessServAgeSexRest

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AGESEX_ParRef | varchar | PK |  | NO | RB_ResEffDateSessServices Parent Reference |
| AGESEX_AgeMonthsFrom | double |  |  | SI | AgeMonthsFrom |
| AGESEX_AgeMonthsTo | double |  |  | SI | AgeMonthsTo |
| AGESEX_AgeYearsFrom | double |  |  | SI | AgeYearsFrom |
| AGESEX_AgeYearsTo | double |  |  | SI | AgeYearsTo |
| AGESEX_Childsub | double |  |  | NO | Childsub |
| AGESEX_RowId | varchar |  |  | NO | - |
| AGESEX_Sex_DR | bigint |  | FK | SI | Des Ref CTSex |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*