# questionnaire.QTCETIVAQQ17

> Anestesia Intravenosa Total (TIVA) : Agente anestésico

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Anestesia Intravenosa Total (TIVA) : Agente anestésico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q17Q1 | varchar |  |  | SI | Agente anestésico |
| Q17Q2 | varchar |  |  | SI | Otro (Texto Libre) |
| Q17Q3 | varchar |  |  | SI | Dosis |
| Q17Q4 | varchar |  |  | SI | Unidad de medida |
| Q17Q5 | numeric |  |  | SI | Dilución (ml) |
| Q17Q6 | varchar |  |  | SI | Modelo |
| Q17Q7 | varchar |  |  | SI | Comentario / Observaciones |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*