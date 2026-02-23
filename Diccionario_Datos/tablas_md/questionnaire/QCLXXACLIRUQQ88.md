# questionnaire.QCLXXACLIRUQQ88

> REGISTRO ANTECEDENTES RUI : Amputación de extremidad Especificación

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* REGISTRO ANTECEDENTES RUI : Amputación de extremidad Especificación

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q88Q1 | varchar |  |  | SI | Lateralidad |
| Q88Q2 | varchar |  |  | SI | Extremidad |
| Q88Q3 | varchar |  |  | SI | Especificación |
| Q88Q4 | date |  |  | SI | Fecha  |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*