# SQLUser.RB_EventCPFacilitator

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPF_ParRef | bigint | PK |  | NO | RB_Event Parent Reference |
| CPF_Arrived | varchar |  |  | SI | Arrived |
| CPF_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| CPF_Childsub | double |  |  | NO | Childsub |
| CPF_EndDate | date |  |  | SI | EndDate |
| CPF_RSVP | varchar |  |  | SI | RSVP |
| CPF_ReasonForNotShow_DR | bigint |  | FK | SI | Des Ref RBCReasonForNotShow |
| CPF_RestrictedBooking | varchar |  |  | SI | Restricted Booking |
| CPF_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*