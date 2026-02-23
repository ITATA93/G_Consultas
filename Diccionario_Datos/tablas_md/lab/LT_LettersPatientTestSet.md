# lab.LT_LettersPatientTestSet

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LTPTT_ParRef | varchar | PK |  | NO | LT_LettersPatient Parent Reference |
| LTPTT_RowID | varchar |  |  | NO | - |
| LTPTT_TestSetCounter | numeric |  |  | NO | Test Set Counter |
| LTPTT_TestSet_DR | varchar |  | FK | NO | TestSet_DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*