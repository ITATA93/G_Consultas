# SQLUser.SS_GroupAlertCategory

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALC_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| ALC_AlertCateg_DR | bigint |  | FK | SI | Des Ref AlertCateg |
| ALC_Childsub | double |  |  | NO | Childsub |
| ALC_ReadOnly | varchar |  |  | SI | Read Only |
| ALC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*