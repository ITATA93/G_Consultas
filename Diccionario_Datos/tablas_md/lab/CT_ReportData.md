# lab.CT_ReportData

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTRPD_ParRef | varchar | PK |  | NO | CT_Report Parent Reference |
| CTRPD_ExcludeForInclusions | varchar |  |  | SI | Exclude For Inclusions |
| CTRPD_RowID | varchar |  |  | NO | - |
| CTRPD_Sequence | double |  |  | NO | Sequence |
| CTRPD_TextExclude | varchar |  |  | SI | Text Exclude |
| CTRPD_TextInclude | varchar |  |  | SI | Text Include |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*