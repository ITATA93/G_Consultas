# questionnaire.QCLXXEFPEDQQ14

> Examen Físico Pediátrico : Desarrollo Psicomotor

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico Pediátrico : Desarrollo Psicomotor

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q14Q1 | varchar |  |  | SI | Área |
| Q14Q2 | varchar |  |  | SI | Resultados |
| Q14Q3 | varchar |  |  | SI | Observaciones |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*