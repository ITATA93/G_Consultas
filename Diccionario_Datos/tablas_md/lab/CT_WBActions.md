# lab.CT_WBActions

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTWBA_RowID | numeric | PK |  | NO | - |
| CTWBA_ActionType | varchar |  |  | SI | Action Type |
| CTWBA_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTWBA_EventTime | varchar |  |  | SI | Event Time |
| CTWBA_EventType | varchar |  |  | SI | Event Type |
| CTWBA_Group | varchar |  |  | SI | Group |
| CTWBA_Message | varchar |  |  | SI | Message |
| CTWBA_Order | numeric |  |  | NO | Order Number |
| CTWBA_UsersList | varchar |  |  | SI | Users List |
| CTWBA_ValidatedFlag | varchar |  |  | SI | Validated Flag |
| CTWBA_Value | varchar |  |  | SI | Value |
| CTWBA_xxx1 | varchar |  |  | SI | xxx1 Staff Notes in TS Actions |
| CTWBA_xxx2 | varchar |  |  | SI | xxx2 Report in TS Actions |
| CTWBA_xxx3 | varchar |  |  | SI | xxx3 Field To Set in TS Actions |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*