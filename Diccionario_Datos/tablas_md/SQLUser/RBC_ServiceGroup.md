# SQLUser.RBC_ServiceGroup

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SG_RowId | bigint | PK |  | NO | - |
| SG_AllowBookAfterDischarge | varchar |  |  | SI | Allow Booking After Discharge Date |
| SG_BypassDateCheck | varchar |  |  | SI | Bypass Date Check |
| SG_Code | varchar |  |  | NO | Code |
| SG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SG_CreatedDate | date |  |  | SI | Created Date |
| SG_CreatedTime | time |  |  | SI | Created Time |
| SG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SG_DateFrom | date |  |  | SI | Date From |
| SG_DateTo | date |  |  | SI | Date To |
| SG_DaysForOPDOffer | double |  |  | SI | DaysForOPDOffer |
| SG_DaysForOPLetterResponse | double |  |  | SI | DaysForOPLetterResponse |
| SG_DaysOfferOutcomeChange | double |  |  | SI | DaysOfferOutcomeChange |
| SG_Desc | varchar |  |  | NO | Description |
| SG_OffersBeforeIP_OPWaitReset | double |  |  | SI | OffersBeforeIP OPWaitReset |
| SG_Owner | varchar |  |  | SI | Owner |
| SG_PreadmissionCheck | varchar |  |  | SI | Preadmission Check |
| SG_TelehealthAppointment | varchar |  |  | SI | Flag for Telehealth Appointments. Flag will not dr... |
| SG_UpdatedDate | date |  |  | SI | Updated Date |
| SG_UpdatedTime | time |  |  | SI | Updated Time |
| SG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SG_WeeksSuspensionReview | double |  |  | SI | WeeksSuspensionReview |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*