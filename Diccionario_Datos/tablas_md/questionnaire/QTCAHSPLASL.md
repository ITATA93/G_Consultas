# questionnaire.QTCAHSPLASL

> Assessment - Speech and Language (Infant)

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Assessment - Speech and Language (Infant)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Is your child having any difficulty understanding ... |
| Q02 | varchar |  |  | SI | Is your child responding to his/her name when call... |
| Q03 | varchar |  |  | SI | Is your child able to answer simple questions? |
| Q04 | varchar |  |  | SI | Is your child able to follow simple directions aro... |
| Q05 | varchar |  |  | SI | Is your child showing an interest in what you or o... |
| Q06 | varchar |  |  | SI | Comprehension & Expressive Language |
| Q07 | varchar |  |  | SI | How does your child make his/her wants known? |
| Q08 | varchar |  |  | SI | Is your child communicating using true words? |
| Q09 | varchar |  |  | SI | Is your child combining words into sentences? |
| Q10 | varchar |  |  | SI | Is your child communicating using combination of w... |
| Q11 | varchar |  |  | SI | Is your child able to express his/her thoughts cle... |
| Q12 | varchar |  |  | SI | Is your child experiencing any frustration communi... |
| Q13 | varchar |  |  | SI | Speech Development |
| Q14 | varchar |  |  | SI | Is your child pronouncing words clearly? |
| Q15 | varchar |  |  | SI |  Is your child having trouble pronouncing certain ... |
| Q16 | varchar |  |  | SI | Do you understand what your child is saying? |
| Q17 | varchar |  |  | SI | Do others understand what your child is saying? |
| Q18 | varchar |  |  | SI | Is your child having any difficulties moving his/h... |
| Q19 | varchar |  |  | SI | Social Language |
| Q20 | varchar |  |  | SI | Does your child look at you and others during a co... |
| Q21 | varchar |  |  | SI |  Does your child request assistance or information... |
| Q22 | varchar |  |  | SI | Does your child appropriately respond to questions... |
| Q23 | varchar |  |  | SI |  Does your child naturally imitate phrases heard i... |
| Q24 | varchar |  |  | SI | Does your child enjoy / avoid communicative intera... |
| Q25 | varchar |  |  | SI | Used to assess speech and language development in ... |
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