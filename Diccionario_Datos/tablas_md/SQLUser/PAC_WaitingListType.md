# SQLUser.PAC_WaitingListType

**Schema:** SQLUser
**Columnas:** 44
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLT_RowId | bigint | PK |  | NO | - |
| Q06Q1 | - |  |  | SI | Date |
| Q06Q2 | - |  |  | SI | Time |
| Q06Q3 | - |  |  | SI | Confirm volume remaining in syringe (mL) |
| Q06Q4 | - |  |  | SI | Site checked |
| Q06Q5 | - |  |  | SI | Site changed |
| Q06Q6 | - |  |  | SI | Light checked |
| Q06Q7 | - |  |  | SI | Check performed by |
| Q06Q8 | - |  |  | SI | Confirm volume remaining in syringe (mL) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| WLT_AllowLinkToDoneWithCurrent | varchar |  |  | SI | Allow to link to Done wait list with current episo... |
| WLT_AllowToRemoveApptNoOutcome | varchar |  |  | SI | Allowed to Remove Appointments with no Outcome for... |
| WLT_AppointmentRequired | varchar |  |  | SI | Appointement Required |
| WLT_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| WLT_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| WLT_Code | varchar |  |  | NO | Code |
| WLT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLT_CreatedDate | date |  |  | SI | Created Date |
| WLT_CreatedTime | time |  |  | SI | Created Time |
| WLT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLT_DateFrom | date |  |  | SI | Date From |
| WLT_DateTo | date |  |  | SI | Date To |
| WLT_DaysAlertAmber | double |  |  | SI | Days Alert Amber |
| WLT_DaysAlertGreen | double |  |  | SI | Days Alert Green |
| WLT_DaysAlertRed | double |  |  | SI | Days Alert Red |
| WLT_Desc | varchar |  |  | NO | Description |
| WLT_DontClearEpisodeSubType | varchar |  |  | SI | Do not clear episode subtype field when changing w... |
| WLT_EpisodeSubType_DR | bigint |  | FK | SI | Des Ref PACEpisodeSubType |
| WLT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| WLT_MainMRRequired | varchar |  |  | SI | Main MR Required |
| WLT_NationalCode | varchar |  |  | SI | National Code |
| WLT_NoInitialOnDeferred | varchar |  |  | SI | Do not set to INITIAL on dereffered treatment disc... |
| WLT_NumOfAllowedNonAttApp | double |  |  | SI | Number of Allowed Non Attended Appointments |
| WLT_OffListCriteria | varchar |  |  | SI | Off List Criteria |
| WLT_OperBookRequired | varchar |  |  | SI | Operation Booking Required |
| WLT_Owner | varchar |  |  | SI | Owner |
| WLT_PayorAppRequired | varchar |  |  | SI | Payor Approval Required |
| WLT_PreadmRequired | varchar |  |  | SI | Preadm Required |
| WLT_SetWLDoneWhenOPisDone | varchar |  |  | SI | Set Waiting List to Done when Operation Details is... |
| WLT_Type | varchar |  |  | SI | Type |
| WLT_UpdatedDate | date |  |  | SI | Updated Date |
| WLT_UpdatedTime | time |  |  | SI | Updated Time |
| WLT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WLT_WaitMinutes | varchar |  |  | SI | Wait Minutes |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*