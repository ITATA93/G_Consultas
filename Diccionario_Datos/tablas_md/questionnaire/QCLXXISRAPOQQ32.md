# questionnaire.QCLXXISRAPOQQ32

> Informe Social y de Redes de Apoyo : Identificación con quienes cohabita el paciente

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe Social y de Redes de Apoyo : Identificación con quienes cohabita el paciente

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q32Q1 | varchar |  |  | SI | Nombre y apellidos |
| Q32Q2 | numeric |  |  | SI | Edad |
| Q32Q3 | varchar |  |  | SI | Relación de parentesco |
| Q32Q4 | varchar |  |  | SI | Actividad principal |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*