# SQLUser.SS_GroupEventRestrictions

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EVTREST_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| EVTREST_Childsub | double |  |  | NO | Childsub |
| EVTREST_EventSubType_DR | varchar |  | FK | SI | Des Ref RBCEventSubType |
| EVTREST_EventType_DR | bigint |  | FK | SI | Des Ref RBCEventType |
| EVTREST_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*