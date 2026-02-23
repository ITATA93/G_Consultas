# lab.CT_TestSetActions

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSK_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSK_ActionType | varchar |  |  | SI | Action Type |
| CTTSK_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTTSK_EventTime | varchar |  |  | SI | Event Time |
| CTTSK_EventType | varchar |  |  | SI | Event Type |
| CTTSK_FieldToSet | varchar |  |  | SI | Field To Set |
| CTTSK_Group | varchar |  |  | SI | Group |
| CTTSK_Message | varchar |  |  | SI | Message |
| CTTSK_Order | numeric |  |  | NO | Order Number |
| CTTSK_PINRequired | varchar |  |  | SI | PIN Required |
| CTTSK_Report | varchar |  |  | SI | Report |
| CTTSK_RowID | varchar |  |  | NO | - |
| CTTSK_StaffNotes | varchar |  |  | SI | Staff Notes |
| CTTSK_UsersList | varchar |  |  | SI | Users List |
| CTTSK_ValidatedFlag | varchar |  |  | SI | Validated Flag |
| CTTSK_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*