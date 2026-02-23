# Region_CLXX_Misc.FichasNoDevueltas

**Schema:** Region_CLXX_Misc
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Personalización Regional Chile**. Adaptaciones y extensiones locales del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Data | date |  |  | SI | - |
| Hora | time |  |  | SI | - |
| HospitalDR | bigint |  | FK | SI | - |
| LocalDR | bigint |  | FK | SI | - |
| MotivoDR | bigint |  | FK | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*