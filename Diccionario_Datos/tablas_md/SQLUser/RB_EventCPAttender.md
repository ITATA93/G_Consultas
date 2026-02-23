# SQLUser.RB_EventCPAttender

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPAT_ParRef | bigint | PK |  | NO | RB_Event Parent Reference |
| CPAT_Arrived | varchar |  |  | SI | Arrived |
| CPAT_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| CPAT_Childsub | double |  |  | NO | Childsub |
| CPAT_RSVP | varchar |  |  | SI | RSVP |
| CPAT_RestrictedBooking | varchar |  |  | SI | Restricted Booking |
| CPAT_RowId | varchar |  |  | NO | - |
| CPAT_SelectedForBooking | varchar |  |  | SI | Selected For Appt |
| CP_EndDate | date |  |  | SI | EndDate |
| CP_ReasonForNotShow_DR | bigint |  | FK | SI | Des Ref RBCReasonForNotShow |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*