# questionnaire.QCLXXNRAMQQ42

> Notificación de Sospecha de Reacción Adversa a Medicamentos : Tabla reacción Adversa

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Notificación de Sospecha de Reacción Adversa a Medicamentos : Tabla reacción Adversa

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q42Q1 | varchar |  |  | SI | Reacción Adversa |
| Q42Q2 | date |  |  | SI | Fecha Inicio RAM* |
| Q42Q3 | numeric |  |  | SI | Duración de la RAM (Cantidad) |
| Q42Q4 | varchar |  |  | SI | Unidad de Tiempo |
| Q42Q5 | varchar |  |  | SI | Reacción Adversa |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*