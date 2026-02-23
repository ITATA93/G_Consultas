# lab.CT_StandardLetterTestSet

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSLT_ParRef | varchar | PK |  | NO | CT_StandardLetter Parent Reference |
| CTSLT_RowId | varchar |  |  | NO | - |
| CTSLT_TestSet_DR | varchar |  | FK | NO | Des Ref TestSet |
| CTSLT_xxx1 | varchar |  |  | SI | Des Ref TestCode |
| CTSLT_xxx2 | varchar |  |  | SI | Standard Comment |
| CTSLT_xxx3 | varchar |  |  | SI | Exclude Tests |
| CTSLT_xxx4 | varchar |  |  | SI | Result Grade |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*