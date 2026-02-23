# questionnaire.QTCEEVMOV4QQ01

> Evaluación de Movilidad Miembro Inferior : Evaluación de Movilidad

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación de Movilidad Miembro Inferior : Evaluación de Movilidad

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | varchar |  |  | SI | Movimiento |
| Q01Q2 | varchar |  |  | SI | Tipo |
| Q01Q3 | varchar |  |  | SI | Segmento |
| Q01Q4 | varchar |  |  | SI | Lateralidad |
| Q01Q5 | numeric |  |  | SI | ROM |
| Q01Q6 | varchar |  |  | SI | Fuerza |
| Q01Q7 | numeric |  |  | SI | EVA |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*