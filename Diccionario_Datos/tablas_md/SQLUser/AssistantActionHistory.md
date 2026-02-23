# SQLUser.AssistantActionHistory

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AAH_History | varchar |  |  | SI | A $listbuild() of history items, each of which den... |
| AAH_HistoryType | varchar |  |  | SI | The type of the history being recorded, e.g. for t... |
| AAH_UserID | varchar |  |  | SI | The ID of user that is accessing the Assistant |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*