# SQLUser.PAC_SnomedRefSetMemberAttrib

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ATTRIB_ParRef | bigint | PK |  | NO | PAC_SnomedRefSetMember Parent Reference |
| ATTRIB_Childsub | double |  |  | NO | Childsub |
| ATTRIB_Concept_DR | bigint |  | FK | SI | Des Ref Concept |
| ATTRIB_RowId | varchar |  |  | NO | - |
| ATTRIB_Type_DR | bigint |  | FK | SI | Des Ref Concept |
| ATTRIB_Value | varchar |  |  | SI | Value |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of procedure |
| Q04 | - |  |  | SI | Cardiology notified |
| Q05 | - |  |  | SI | Discharge summary received |
| Q06 | - |  |  | SI | Primary health care provider notified of discharge |
| Q07 | - |  |  | SI | Discharge summary forwarded to primary health care... |
| Q08 | - |  |  | SI | Discharge summary forwarded to the referring cardi... |
| Q09 | - |  |  | SI | If applicable, discharge summary forwarded to Rheu... |
| Q10 | - |  |  | SI | Notification notes |
| Q11 | - |  |  | SI | Referral made to cardiology services for follow up |
| Q12 | - |  |  | SI | Referral made to cardiac rehabilitation |
| Q13 | - |  |  | SI | Referral made for exercise therapy |
| Q14 | - |  |  | SI | Referral made to other services |
| Q15 | - |  |  | SI | Other referral |
| Q16 | - |  |  | SI | Referral notes |
| Q17 | - |  |  | SI | HITH pathway commenced |
| Q18 | - |  |  | SI | Client reviewed by cardiology |
| Q19 | - |  |  | SI | Client cleared to return to community |
| Q20 | - |  |  | SI | Primary health care provider notified of return to... |
| Q21 | - |  |  | SI | Recall added for follow up |
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