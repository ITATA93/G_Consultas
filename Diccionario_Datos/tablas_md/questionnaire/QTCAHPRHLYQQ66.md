# questionnaire.QTCAHPRHLYQQ66

> Lymphoedema Assessment : Bioimpedance and volumeter

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Lymphoedema Assessment : Bioimpedance and volumeter

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q66Q1 | date |  |  | SI | Date |
| Q66Q2 | numeric |  |  | SI | Weight |
| Q66Q3 | numeric |  |  | SI | Volume right |
| Q66Q4 | numeric |  |  | SI | Volume Left |
| Q66Q5 | numeric |  |  | SI | Difference |
| Q66Q6 | varchar |  |  | SI | Bioimpedance L-Dex score |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*