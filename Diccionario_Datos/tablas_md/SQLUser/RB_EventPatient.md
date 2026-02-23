# SQLUser.RB_EventPatient

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAT_ParRef | bigint | PK |  | NO | RB_Event Parent Reference |
| PAT_Arrived | varchar |  |  | SI | Arrived |
| PAT_Childsub | double |  |  | NO | Childsub |
| PAT_EndDate | date |  |  | SI | EndDate |
| PAT_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| PAT_PatMas_DR | bigint |  | FK | SI | Des Ref PatMas |
| PAT_RSVP | varchar |  |  | SI | RSVP |
| PAT_ReasonForNotShow_DR | bigint |  | FK | SI | Des Ref RBCReasonForNotShow |
| PAT_RowId | varchar |  |  | NO | - |
| PAT_SelectedForBooking | varchar |  |  | SI | Selected for Appointments |
| PAT_WaiverFee | varchar |  |  | SI | Waiver Fee |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*