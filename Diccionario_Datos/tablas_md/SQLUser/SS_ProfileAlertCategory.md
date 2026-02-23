# SQLUser.SS_ProfileAlertCategory

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALC_ParRef | bigint | PK |  | NO | Parent table |
| ALC_AlertCateg_DR | bigint |  | FK | SI | Alert Category |
| ALC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALC_ReadOnly | varchar |  |  | SI | Read Only |
| ALC_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*