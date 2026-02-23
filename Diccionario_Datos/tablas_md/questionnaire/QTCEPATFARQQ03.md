# questionnaire.QTCEPATFARQQ03

> Registro de Oportunidad de Entrega : Tabular

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro de Oportunidad de Entrega : Tabular

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q03Q1 | date |  |  | SI | Fecha de Presentacion 1 |
| Q03Q2 | varchar |  |  | SI | Motivo de Rechazo |
| Q03Q3 | varchar |  |  | SI | Medicamento |
| Q03Q4 | varchar |  |  | SI | N° de Repetición |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*