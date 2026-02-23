# SQLUser.SS_GroupWaitListPriority

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLP_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| WLP_Childsub | double |  |  | NO | Childsub |
| WLP_RowId | varchar |  |  | NO | - |
| WLP_WaitListPriority_DR | bigint |  | FK | SI | Des Ref WaitListPriority |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*