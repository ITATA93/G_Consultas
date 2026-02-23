# lab.CT_StandardLetterTSResult

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSLR_ParRef | varchar | PK |  | NO | CT_StandardLetterTestSet Parent Reference |
| CTSLR_ExcludeTests | varchar |  |  | SI | Exclude Tests |
| CTSLR_ResultGrade | varchar |  |  | SI | Result Grade |
| CTSLR_RowID | varchar |  |  | NO | - |
| CTSLR_StandardComment | varchar |  |  | NO | Standard Comment |
| CTSLR_TestCode_DR | varchar |  | FK | NO | Test Code_DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*