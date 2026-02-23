# SQLUser.CT_HospitalAssignedGroup

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTHAG_ParRef | bigint | PK |  | NO | CT_Hospital Parent Reference |
| CTHAG_Category | varchar |  |  | SI | Category |
| CTHAG_Childsub | double |  |  | NO | Childsub |
| CTHAG_Code | varchar |  |  | NO | Code |
| CTHAG_CodeTableTags | varchar |  |  | SI | List of code table tags |
| CTHAG_DateFrom | date |  |  | SI | Date From |
| CTHAG_DateTo | date |  |  | SI | Date To |
| CTHAG_Desc | varchar |  |  | NO | Description |
| CTHAG_NationalPPPList | varchar |  |  | SI | National PPP List |
| CTHAG_Range | varchar |  |  | SI | Range |
| CTHAG_RowId | varchar |  |  | NO | - |
| CTHAG_Users | varchar |  |  | SI | List of users |
| Q01 | - |  |  | SI | Does the patient have an Advance Care Directive? |
| Q02 | - |  |  | SI | Medical treatment decision maker? |
| Q03 | - |  |  | SI | Please view the Advance Care Directive, Medical Tr... |
| Q04 | - |  |  | SI | Does the patient have an enduring power of attorne... |
| Q05 | - |  |  | SI | Does the patient have an appointed guardian? |
| Q06 | - |  |  | SI | • A copy of the Advance Care Directive should be s... |
| Q07 | - |  |  | SI | • Please ensure an Advance Care Directive alert is... |
| Q08 | - |  |  | SI | Does the patient have an Advance Care Directive? |
| Q09 | - |  |  | SI | Does the patient have a Medical Treatment Decision... |
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