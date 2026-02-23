# epr.CTTextTranslation

**Schema:** epr
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| TRNCode | varchar |  |  | NO | - |
| TRNCodeTableTags | varchar |  |  | SI | - |
| TRNDesc | varchar |  |  | SI | - |
| TRNDesc2 | varchar |  |  | SI | - |
| TRN_Owner | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*