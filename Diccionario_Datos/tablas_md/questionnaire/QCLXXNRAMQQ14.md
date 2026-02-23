# questionnaire.QCLXXNRAMQQ14

> Notificación de Sospecha de Reacción Adversa a Medicamentos : Tabla Fármaco

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Notificación de Sospecha de Reacción Adversa a Medicamentos : Tabla Fármaco

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q14Q1 | varchar |  |  | SI | Tipo de Fármaco |
| Q14Q10 | varchar |  |  | SI | Motivo de la Prescripción |
| Q14Q2 | varchar |  |  | SI | Fármaco (s) |
| Q14Q3 | varchar |  |  | SI | Marca ® |
| Q14Q4 | varchar |  |  | SI | Lote |
| Q14Q5 | varchar |  |  | SI | Dosis |
| Q14Q6 | varchar |  |  | SI | Frecuencia |
| Q14Q7 | varchar |  |  | SI | Vía de Administración |
| Q14Q8 | date |  |  | SI | Fecha Inicio |
| Q14Q9 | date |  |  | SI | Fecha Término |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*