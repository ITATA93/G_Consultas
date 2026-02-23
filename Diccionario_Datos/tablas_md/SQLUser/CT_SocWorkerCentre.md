# SQLUser.CT_SocWorkerCentre

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SWC_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Patient mobility	 |
| Q02 | - |  |  | SI | Patient mental state 	 |
| Q03 | - |  |  | SI | Bed type in use	 |
| Q04 | - |  |  | SI | Are bed rails required?	 |
| Q05 | - |  |  | SI | Rationale	 |
| Q06 | - |  |  | SI | Review date	 |
| Q07 | - |  |  | SI | Ensure that the appropriate use of bed rails is as... |
| Q08 | - |  |  | SI | Bumpers used	 |
| Q09 | - |  |  | SI | Has the use of bed rails been discussed 	 |
| Q10 | - |  |  | SI | Do bed rails click into place and are secure	 |
| Q11 | - |  |  | SI | Have you ensured both bed rails in use (even if ag... |
| Q12 | - |  |  | SI | Confirm that an overlay mattress is NOT in use	 |
| Q13 | - |  |  | SI | Call bell explained and in reach	 |
| Q14 | - |  |  | SI | Is an alternative call method required	 |
| Q15 | - |  |  | SI | State the alternative used	 |
| Q16 | - |  |  | SI | Is there sufficient space surrounding the bed to u... |
| Q17 | - |  |  | SI | Has the patient been assessed for care rounding	 |
| Q18 | - |  |  | SI | Does the patient require reasonable adjustments to... |
| Q19 | - |  |  | SI | Is the appropriate care plan in place	 |
| Q20 | - |  |  | SI | Ensure patient information leaflet is given	 |
| Q21 | - |  |  | SI | Ensure the need for the use of bedrails is communi... |
| Q22 | - |  |  | SI | Date of bed rail discontinuation	 |
| Q23 | - |  |  | SI | Please state the reason why the use of bedrails is... |
| Q24 | - |  |  | SI | Ensure that the appropriate use of bed rails is as... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| SWC_Code | varchar |  |  | NO | Code |
| SWC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SWC_CreatedDate | date |  |  | SI | Created Date |
| SWC_CreatedTime | time |  |  | SI | Created Time |
| SWC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SWC_DateFrom | date |  |  | SI | Date From |
| SWC_DateTo | date |  |  | SI | Date To |
| SWC_Desc | varchar |  |  | NO | Description |
| SWC_Owner | varchar |  |  | SI | Owner |
| SWC_UpdatedDate | date |  |  | SI | Updated Date |
| SWC_UpdatedTime | time |  |  | SI | Updated Time |
| SWC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*