# web_Msg.OE_OrdQuestion_QA_AnswerMultiline

**Schema:** web_Msg
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OE_OrdQuestion | varchar | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| QA_AnswerMultiline | varchar |  |  | SI | QA_AnswerMultiline |
| element_key | varchar |  |  | NO | QAAnswerMultiline array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*