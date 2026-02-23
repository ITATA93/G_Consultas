# SQLUser.PAC_SnomedBinaryAssociation

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOBAC_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient has mobilised |
| Q04 | - |  |  | SI | Patient has passed urine |
| Q05 | - |  |  | SI | Pruritus (itch) present |
| Q06 | - |  |  | SI | Neurological deficit |
| Q07 | - |  |  | SI | Patient is febrile |
| Q08 | - |  |  | SI | Post Dural Puncture Headache (PDPH) present |
| Q09 | - |  |  | SI | Back pain present |
| Q10 | - |  |  | SI | Notes |
| Q11 | - |  |  | SI | Redness noted at site |
| Q12 | - |  |  | SI | Swelling noted at site |
| Q13 | - |  |  | SI | Tenderness complaint at site |
| Q14 | - |  |  | SI | Discharge noted at site |
| Q15 | - |  |  | SI | Patient education provided |
| Q16 | - |  |  | SI | Notes |
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
| SNOBAC_AssoType | varchar |  |  | NO | Association Type |
| SNOBAC_Code | varchar |  |  | NO | Code |
| SNOBAC_ConceptX_DR | bigint |  | FK | NO | SNOMED Concept X DR |
| SNOBAC_ConceptY_DR | bigint |  | FK | NO | SNOMED Concept Y DR |
| SNOBAC_DateFrom | date |  |  | NO | Effective date for the record |
| SNOBAC_DateTo | date |  |  | SI | Last day the record is active |
| SNOBAC_Desc | varchar |  |  | NO | Description |
| SNOBAC_SDesc | varchar |  |  | SI | Short Description |
| SNOBAC_TermsX_DR | bigint |  | FK | NO | SNOMED Terms X DR  |
| SNOBAC_TermsY_DR | bigint |  | FK | NO | SNOMED Terms Y DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*