# SQLUser.OEC_ResultStatus

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESST_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Rectum |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Rectum DR |
| Q03 | - |  |  | SI | Faecal impaction |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Faecal impaction DR |
| Q05 | - |  |  | SI | Melena |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Melena DR |
| Q07 | - |  |  | SI | Bright red blood |
| Q07N | - |  |  | SI | Note |
| Q07ObsDR | - |  |  | SI | Bright red blood DR |
| Q09 | - |  |  | SI | Mass |
| Q09N | - |  |  | SI | Note |
| Q09ObsDR | - |  |  | SI | Mass DR |
| Q11 | - |  |  | SI | Hemorrhoids |
| Q11N | - |  |  | SI | Note |
| Q11ObsDR | - |  |  | SI | Hemorrhoids DR |
| Q13 | - |  |  | SI | Sphincter tone |
| Q13N | - |  |  | SI | Note |
| Q13ObsDR | - |  |  | SI | Sphincter tone DR |
| Q15 | - |  |  | SI | Perianal fistula |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Perianal fistula DR |
| Q17 | - |  |  | SI | Abscess |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Abscess DR |
| Q19 | - |  |  | SI | Pilonidal Sinus |
| Q19N | - |  |  | SI | Note |
| Q19ObsDR | - |  |  | SI | Pilonidal Sinus DR |
| Q31 | - |  |  | SI | Anal fissures |
| Q31N | - |  |  | SI | Note |
| Q31ObsDR | - |  |  | SI | Anal fissures DR |
| Q33 | - |  |  | SI | Cervix |
| Q33N | - |  |  | SI | Note |
| Q33ObsDR | - |  |  | SI | Cervix DR |
| Q35 | - |  |  | SI | Uterus |
| Q35N | - |  |  | SI | Note |
| Q35ObsDR | - |  |  | SI | Uterus DR |
| Q37 | - |  |  | SI | Parameters |
| Q37N | - |  |  | SI | Note |
| Q37ObsDR | - |  |  | SI | Parameters DR |
| Q39 | - |  |  | SI | Annexes |
| Q39N | - |  |  | SI | Note |
| Q39ObsDR | - |  |  | SI | Annexes DR |
| Q41 | - |  |  | SI | Douglas and pelvis |
| Q41N | - |  |  | SI | Note |
| Q41ObsDR | - |  |  | SI | Douglas and pelvis DR |
| Q42 | - |  |  | SI | Other |
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
| RESST_Code | varchar |  |  | NO | Code |
| RESST_CreatedDate | date |  |  | SI | Created Date |
| RESST_CreatedTime | time |  |  | SI | Created Time |
| RESST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESST_Desc | varchar |  |  | NO | Description |
| RESST_UpdatedDate | date |  |  | SI | Updated Date |
| RESST_UpdatedTime | time |  |  | SI | Updated Time |
| RESST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*