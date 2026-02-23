# questionnaire.QGXXXREC

> Rectal

**Schema:** questionnaire
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(Rectal)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Rectum |
| Q01N | varchar |  |  | SI | Note |
| Q01ObsDR | varchar |  | FK | SI | Rectum DR |
| Q03 | varchar |  |  | SI | Faecal impaction |
| Q03N | varchar |  |  | SI | Note |
| Q03ObsDR | varchar |  | FK | SI | Faecal impaction DR |
| Q05 | varchar |  |  | SI | Melena |
| Q05N | varchar |  |  | SI | Note |
| Q05ObsDR | varchar |  | FK | SI | Melena DR |
| Q07 | varchar |  |  | SI | Bright red blood |
| Q07N | varchar |  |  | SI | Note |
| Q07ObsDR | varchar |  | FK | SI | Bright red blood DR |
| Q09 | varchar |  |  | SI | Mass |
| Q09N | varchar |  |  | SI | Note |
| Q09ObsDR | varchar |  | FK | SI | Mass DR |
| Q11 | varchar |  |  | SI | Hemorrhoids |
| Q11N | varchar |  |  | SI | Note |
| Q11ObsDR | varchar |  | FK | SI | Hemorrhoids DR |
| Q13 | varchar |  |  | SI | Sphincter tone |
| Q13N | varchar |  |  | SI | Note |
| Q13ObsDR | varchar |  | FK | SI | Sphincter tone DR |
| Q15 | varchar |  |  | SI | Perianal fistula |
| Q15N | varchar |  |  | SI | Note |
| Q15ObsDR | varchar |  | FK | SI | Perianal fistula DR |
| Q17 | varchar |  |  | SI | Abscess |
| Q17N | varchar |  |  | SI | Note |
| Q17ObsDR | varchar |  | FK | SI | Abscess DR |
| Q19 | varchar |  |  | SI | Pilonidal Sinus |
| Q19N | varchar |  |  | SI | Note |
| Q19ObsDR | varchar |  | FK | SI | Pilonidal Sinus DR |
| Q21 | varchar |  |  | SI | Prostate |
| Q21C | varchar |  |  | SI | Consistency |
| Q21L | varchar |  |  | SI | Limits |
| Q21N | varchar |  |  | SI | Note |
| Q21ObsDR | varchar |  | FK | SI | Prostate DR |
| Q21P | varchar |  |  | SI | Pain |
| Q21S | varchar |  |  | SI | Size |
| Q21SU | varchar |  |  | SI | Surface |
| Q29 | varchar |  |  | SI | Seminal vesicles |
| Q29N | varchar |  |  | SI | Note |
| Q31 | varchar |  |  | SI | Anal fissures |
| Q31N | varchar |  |  | SI | Note |
| Q31ObsDR | varchar |  | FK | SI | Anal fissures DR |
| Q33 | varchar |  |  | SI | Cervix |
| Q33N | varchar |  |  | SI | Note |
| Q33ObsDR | varchar |  | FK | SI | Cervix DR |
| Q35 | varchar |  |  | SI | Uterus |
| Q35N | varchar |  |  | SI | Note |
| Q35ObsDR | varchar |  | FK | SI | Uterus DR |
| Q37 | varchar |  |  | SI | Parameters |
| Q37N | varchar |  |  | SI | Note |
| Q37ObsDR | varchar |  | FK | SI | Parameters DR |
| Q39 | varchar |  |  | SI | Annexes |
| Q39N | varchar |  |  | SI | Note |
| Q39ObsDR | varchar |  | FK | SI | Annexes DR |
| Q41 | varchar |  |  | SI | Douglas and pelvis |
| Q41N | varchar |  |  | SI | Note |
| Q41ObsDR | varchar |  | FK | SI | Douglas and pelvis DR |
| Q42 | varchar |  |  | SI | Other |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*