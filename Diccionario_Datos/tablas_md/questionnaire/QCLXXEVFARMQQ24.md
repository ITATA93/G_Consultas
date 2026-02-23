# questionnaire.QCLXXEVFARMQQ24

> Estudio Evaluación e Intervención  : Intervención con Usuario

**Schema:** questionnaire
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Estudio Evaluación e Intervención  : Intervención con Usuario

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q24Q1 | varchar |  |  | SI | ¿Acepta? |
| Q24Q2 | varchar |  |  | SI | Motivo Rechazo |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*