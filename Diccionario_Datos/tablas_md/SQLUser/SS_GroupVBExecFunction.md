# SQLUser.SS_GroupVBExecFunction

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VBEX_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| VBEX_Display | varchar |  |  | SI | Display Icon for executable |
| VBEX_ReadOnly | varchar |  |  | SI | Read Only |
| VBEX_RowId | varchar |  |  | NO | - |
| VBEX_SSVBF_DR | bigint |  | FK | NO | Des Ref to SSVBF |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*