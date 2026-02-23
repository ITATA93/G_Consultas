# questionnaire.QTCRAICQQ88

> Regional Anaesthesia Insertion and Care : Test doses

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Regional Anaesthesia Insertion and Care : Test doses

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q88Q1 | numeric |  |  | SI | Test dose volume (mLs) |
| Q88Q2 | time |  |  | SI | Time |
| Q88Q3 | varchar |  |  | SI | Test dose anaesthetic |
| Q88Q4 | varchar |  |  | SI | Other (please specify) |
| Q88Q5 | numeric |  |  | SI | Concentration (%) |
| Q88Q6 | varchar |  |  | SI | Vasoconstrictor added |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*