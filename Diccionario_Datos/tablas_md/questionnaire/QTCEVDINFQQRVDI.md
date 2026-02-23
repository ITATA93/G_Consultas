# questionnaire.QTCEVDINFQQRVDI

> Visita Domiciliaria Integral : Resumen Visita Diaria Integral

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Visita Domiciliaria Integral : Resumen Visita Diaria Integral

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| QRVDIQ1 | date |  |  | SI | Fecha |
| QRVDIQ2 | varchar |  |  | SI | Responsable |
| QRVDIQ3 | numeric |  |  | SI | N° de Visita |
| QRVDIQ4 | varchar |  |  | SI | Motivo de la visita |
| QRVDIQ5 | varchar |  |  | SI | Intervenciones o acciones realizadas y temas trata... |
| QRVDIQ6 | varchar |  |  | SI | Acuerdos tomados |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*