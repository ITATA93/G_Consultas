# TC_hmf_Process_TrakOutbound.Context__ResponseHandlers

**Schema:** TC_hmf_Process_TrakOutbound
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Contexto**. Datos de contexto de sesión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| Context | bigint | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| _ResponseHandlers | varchar |  |  | SI | _ResponseHandlers |
| element_key | varchar |  |  | NO | %ResponseHandlers array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*