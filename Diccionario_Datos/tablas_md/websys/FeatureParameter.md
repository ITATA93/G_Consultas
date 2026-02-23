# websys.FeatureParameter

> "Class to contains parameters defined for the feature.

**Schema:** websys
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Class to contains parameters defined for the feature.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| Name | varchar |  |  | NO | - |
| ServerOnly | varchar |  |  | SI | Indicates if a specific feature parameter should b... |
| TypeSpec | varchar |  |  | SI | - |
| Value | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*