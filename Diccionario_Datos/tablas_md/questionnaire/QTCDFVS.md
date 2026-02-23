# questionnaire.QTCDFVS

> Domestic and Family Violence (D&FV) Screening

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Domestic and Family Violence (D&FV) Screening

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Patient alone for screening process |
| Q04 | varchar |  |  | SI | Mandatory reporting obligations explained and unde... |
| Q05 | varchar |  |  | SI | Privacy and confidentiality limits discussed |
| Q06 | varchar |  |  | SI | Explained information will be saved in their elect... |
| Q07 | varchar |  |  | SI | Explained, in own words, purpose of questions and ... |
| Q08 | varchar |  |  | SI | Please refer to Guidelines section below for detai... |
| Q09 | varchar |  |  | SI | Pre-screening notes |
| Q10 | varchar |  |  | SI | If the patient answers ''yes'' to any of the below... |
| Q11 | varchar |  |  | SI | For example, ask ''Would you like to talk more abo... |
| Q12 | varchar |  |  | SI | Within the last year has your partner, ex-partner ... |
| Q13 | varchar |  |  | SI | Yelled at you, talked down to you or called you ba... |
| Q14 | varchar |  |  | SI | Become jealous or tried to control what you do |
| Q15 | varchar |  |  | SI | Within the last year, have you been: |
| Q16 | varchar |  |  | SI | Afraid of your partner, ex-partner or anyone in yo... |
| Q17 | varchar |  |  | SI | Hit, kicked, punched or hurt by your partner, ex-p... |
| Q18 | varchar |  |  | SI | Made to have sex or have any sexual activity when ... |
| Q19 | varchar |  |  | SI | D&FV screening outcome |
| Q20 | varchar |  |  | SI | Reason for no screening |
| Q21 | varchar |  |  | SI | Screening outcome notes |
| Q22 | varchar |  |  | SI | Before screening, please explain the following con... |
| Q23 | varchar |  |  | SI | 1. Many people experience problems with their fami... |
| Q24 | varchar |  |  | SI | OR, if pregnant: |
| Q25 | varchar |  |  | SI | 1a. Women who are pregnant commonly experience vio... |
| Q26 | varchar |  |  | SI | 2. Domestic and family violence is any type of abu... |
| Q27 | varchar |  |  | SI | 3. Abuse does not have to be physical to be domest... |
| Q28 | varchar |  |  | SI | 4. It can take many forms. Examples include: |
| Q29 | varchar |  |  | SI | • Controlling behaviours |
| Q30 | varchar |  |  | SI | • Financial abuse (denying access to money) |
| Q31 | varchar |  |  | SI | • Emotional abuse (name calling) |
| Q32 | varchar |  |  | SI | • Intimidation (smashing things) |
| Q33 | varchar |  |  | SI | • Isolation (preventing you from having contact wi... |
| Q34 | varchar |  |  | SI | • Sexual abuse (forcing you to have sex, touching ... |
| Q35 | varchar |  |  | SI | • Spiritual abuse (putting down your culture or yo... |
| Q36 | varchar |  |  | SI | Explained to patient participation is voluntary |
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