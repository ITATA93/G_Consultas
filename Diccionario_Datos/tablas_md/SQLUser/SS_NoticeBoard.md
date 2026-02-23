# SQLUser.SS_NoticeBoard

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NB_RowId | bigint | PK |  | NO | - |
| NB_Date | date |  |  | SI | Date |
| NB_Message | varchar |  |  | SI | Message |
| NB_Time | time |  |  | SI | Time |
| NB_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*