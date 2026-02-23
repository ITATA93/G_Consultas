# SQLUser.PA_WaitingListGuarDate

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GD_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| GD_ApptReasonForCancel_DR | bigint |  | FK | SI | Des Ref Reason For Cancel |
| GD_ApptReasonForTransfer_DR | bigint |  | FK | SI | Des Ref Reason For Transfer |
| GD_ApptReasonNotShow_DR | bigint |  | FK | SI | Des Ref Reason Not Show |
| GD_ChangeDate | date |  |  | SI | ChangeDate |
| GD_ChangeReason | varchar |  |  | SI | ChangeReason |
| GD_ChangeTime | time |  |  | SI | ChangeTime |
| GD_Childsub | double |  |  | NO | Childsub |
| GD_EffDate | date |  |  | SI | EffDate |
| GD_GuaranteedDate | date |  |  | SI | Guaranteed Date |
| GD_ReasonGroup_DR | bigint |  | FK | SI | Des Ref ReasonGroup |
| GD_RowId | varchar |  |  | NO | - |
| GD_TTGGuaranteedDate | date |  |  | SI | Guaranteed Date |
| GD_User_DR | bigint |  | FK | SI | Des Ref User |
| GD_WLReasonNotAvail_DR | bigint |  | FK | SI | Des Ref Reason Not Avail |
| GD_WaitTime | double |  |  | SI | WaitTime |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*