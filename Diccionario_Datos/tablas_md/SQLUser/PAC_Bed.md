# SQLUser.PAC_Bed

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BED_WARD_ParRef | bigint | PK |  | NO | Des Ref to WARD  |
| BED_Available | varchar |  |  | SI | Available flag |
| BED_BedType_DR | bigint |  | FK | SI | Des Ref to PACBT |
| BED_BillFlag1 | varchar |  |  | SI | BillFlag1 |
| BED_BillFlag2 | varchar |  |  | SI | BillFlag2 |
| BED_BillFlag3 | varchar |  |  | SI | BillFlag3 |
| BED_Childsub | double |  |  | NO | Child Sub |
| BED_Code | varchar |  |  | NO | Bed Code / No |
| BED_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| BED_CreatedDate | date |  |  | SI | Created Date |
| BED_CreatedTime | time |  |  | SI | Created Time |
| BED_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BED_DateFrom | date |  |  | SI | Date From |
| BED_DateTo | date |  |  | SI | Date To |
| BED_ExtNo | varchar |  |  | SI | Extension No |
| BED_Isolated | varchar |  |  | SI | Isolated Flag |
| BED_IsolatedDateFrom | date |  |  | SI | Isolated Date From |
| BED_IsolatedDateTo | date |  |  | SI | Isolated Date To |
| BED_IsolatedTimeFrom | time |  |  | SI | Isolated Time From |
| BED_IsolatedTimeTo | time |  |  | SI | Isolated Time To |
| BED_PositionHeight | double |  |  | SI | Position Height |
| BED_PositionLeft | double |  |  | SI | Position Left |
| BED_PositionTop | double |  |  | SI | Position Top |
| BED_PositionWidth | double |  |  | SI | Position Width |
| BED_RcFlag | varchar |  |  | SI | Archived Flag |
| BED_Room_DR | bigint |  | FK | SI | Des Ref to ROOM |
| BED_RowID | varchar |  |  | NO | - |
| BED_SNAP | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare 2011+ (Log:8010... |
| BED_SignFacilDateFrom | date |  |  | SI | Signif Facil Date From |
| BED_SignifFacilDateTo | date |  |  | SI | Signif Facil DateTo |
| BED_SignifFacility_DR | bigint |  | FK | SI | Des Ref Signif Facility |
| BED_SortingOrder | double |  |  | SI | Sorting Order |
| BED_Status_DR | bigint |  | FK | SI | Des Ref Bed Status |
| BED_UpdatedDate | date |  |  | SI | Updated Date |
| BED_UpdatedTime | time |  |  | SI | Updated Time |
| BED_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Liaison admission date and time |
| Q04 | - |  |  | SI | Liaison admission time |
| Q05 | - |  |  | SI | Referral source |
| Q06 | - |  |  | SI | Reason for referral |
| Q07 | - |  |  | SI | Other reason for referral |
| Q08 | - |  |  | SI | Escalation of care required |
| Q09 | - |  |  | SI | Escalated to |
| Q10 | - |  |  | SI | Other escalation |
| Q11 | - |  |  | SI | Liaison admission by |
| Q12 | - |  |  | SI | Liaison admission notes |
| Q13 | - |  |  | SI | Liaison discharge date and time |
| Q14 | - |  |  | SI | Liaison discharge time |
| Q15 | - |  |  | SI | Outcome |
| Q16 | - |  |  | SI | Liaison discharge by |
| Q17 | - |  |  | SI | Liaison discharge notes |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*