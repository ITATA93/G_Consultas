# questionnaire.QGXXXIVAQQ55

> Intravascular Access : Daily shift assessment

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intravascular Access : Daily shift assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q55Q1 | varchar |  |  | SI | IV check |
| Q55Q2 | varchar |  |  | SI | IV access heparin locked and labeled |
| Q55Q3 | varchar |  |  | SI | Flush bag pressure checked |
| Q55Q4 | date |  |  | SI | Date |
| Q55Q5 | time |  |  | SI | Time |
| Q55Q6 | varchar |  |  | SI | Note |
| Q55Q7 | varchar |  |  | SI | Actions |
| Q55Q8 | varchar |  |  | SI | Dressing status |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*