# lab.SS_GroupVBExecFunction

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSGVF_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| SSGVF_ReadOnly | varchar |  |  | SI | Read Only |
| SSGVF_RowId | varchar |  |  | NO | - |
| SSGVF_SSVBF_DR | bigint |  | FK | NO | Des Ref to SSVBF |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*