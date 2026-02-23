# questionnaire.QTCEVDINFQQRR

> Visita Domiciliaria Integral : Motivo / Diagnóstico / Plan de Intervención

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Visita Domiciliaria Integral : Motivo / Diagnóstico / Plan de Intervención

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| QRRQ1 | varchar |  |  | SI | Problemas Detectados |
| QRRQ2 | varchar |  |  | SI | Caso Índice / Familiar |
| QRRQ3 | varchar |  |  | SI | Plan de acción y acuerdos |
| QRRQ4 | varchar |  |  | SI | Responsable |
| QRRQ5 | varchar |  |  | SI | Tiempo de ejecución |
| QRRQ6 | varchar |  |  | SI | Evaluación |
| QRRQ7 | varchar |  |  | SI | Observación |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*