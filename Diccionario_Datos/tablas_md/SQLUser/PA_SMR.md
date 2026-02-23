# SQLUser.PA_SMR

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SMR_RowId | bigint | PK |  | NO | - |
| SMR_AdmCoding_DR | varchar |  | FK | SI | Des Ref AdmCoding |
| SMR_Appointment_DR | varchar |  | FK | SI | Des Ref Appointment |
| SMR_ApptSMR00_DR | varchar |  | FK | SI | Des Ref ApptSMR00 |
| SMR_Batch_DR | bigint |  | FK | SI | Des Ref SMR Batch |
| SMR_ExtractBuild_DR | bigint |  | FK | SI | Des Ref ExtractBuild |
| SMR_Extract_DR | bigint |  | FK | SI | Des Ref Extract |
| SMR_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| SMR_Status_DR | bigint |  | FK | SI | Status |
| SMR_ValidationStatus | varchar |  |  | SI | Validation Status |
| SMR_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |
| SMR_isdref | varchar |  |  | SI | isdref |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*