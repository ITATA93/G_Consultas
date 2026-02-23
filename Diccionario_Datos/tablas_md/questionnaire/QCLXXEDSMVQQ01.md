# questionnaire.QCLXXEDSMVQQ01

> Ejes Diagnósticos DSM-V : Hipótesis Diagnóstica (Ejes)

**Schema:** questionnaire
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ejes Diagnósticos DSM-V : Hipótesis Diagnóstica (Ejes)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | varchar |  |  | SI | Eje Diagnóstico |
| Q01Q2 | varchar |  |  | SI | Diagnóstico |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*