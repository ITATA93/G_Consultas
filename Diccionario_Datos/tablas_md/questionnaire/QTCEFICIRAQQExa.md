# questionnaire.QTCEFICIRAQQExa

> Ficha IRA : Exámenes

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha IRA : Exámenes

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| QExaQ1 | varchar |  |  | SI | Examenes |
| QExaQ2 | date |  |  | SI | Fecha |
| QExaQ3 | varchar |  |  | SI | Resultado |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*