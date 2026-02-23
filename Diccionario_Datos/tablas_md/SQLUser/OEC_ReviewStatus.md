# SQLUser.OEC_ReviewStatus

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REVST_RowId | bigint | PK |  | NO | - |
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
| Q21 | - |  |  | SI | Prostate |
| Q21C | - |  |  | SI | Consistency |
| Q21L | - |  |  | SI | Limits |
| Q21N | - |  |  | SI | Note |
| Q21ObsDR | - |  |  | SI | Prostate DR |
| Q21P | - |  |  | SI | Pain |
| Q21S | - |  |  | SI | Size |
| Q21SU | - |  |  | SI | Surface |
| Q29 | - |  |  | SI | Seminal vesicles |
| Q29N | - |  |  | SI | Note |
| Q31 | - |  |  | SI | Anal fissures |
| Q31N | - |  |  | SI | Note |
| Q31ObsDR | - |  |  | SI | Anal fissures DR |
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
| REVST_Code | varchar |  |  | NO | Code |
| REVST_Colour | varchar |  |  | SI | Colour |
| REVST_CreatedDate | date |  |  | SI | Created Date |
| REVST_CreatedTime | time |  |  | SI | Created Time |
| REVST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REVST_Desc | varchar |  |  | NO | Description |
| REVST_UpdatedDate | date |  |  | SI | Updated Date |
| REVST_UpdatedTime | time |  |  | SI | Updated Time |
| REVST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*