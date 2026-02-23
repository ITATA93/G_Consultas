# questionnaire.QTCVBAC

> Vaginal Birth After Caesarean (VBAC) Assessment/Screening Tool

**Schema:** questionnaire
**Columnas:** 107
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Vaginal Birth After Caesarean (VBAC) Assessment/Screening Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Gestation age |
| Q04 | varchar |  |  | SI | weeks |
| Q05 | varchar |  |  | SI | Gestation age (days) |
| Q06 | varchar |  |  | SI | days |
| Q07 | numeric |  |  | SI | Current number of children |
| Q08 | varchar |  |  | SI | Anticipated / Desired number of children |
| Q09 | varchar |  |  | SI | Notes |
| Q10 | numeric |  |  | SI | Number of previous vaginal births |
| Q11 | numeric |  |  | SI | Number of previous Caesarean Sections (CS) |
| Q12 | varchar |  |  | SI | Was most recent birth a CS |
| Q13 | date |  |  | SI | Date of most recent CS |
| Q14 | varchar |  |  | SI | Estimated date |
| Q15 | varchar |  |  | SI | Indication for most recent CS |
| Q16 | varchar |  |  | SI | Previous CS operation report viewed |
| Q17 | varchar |  |  | SI | Notes |
| Q18 | varchar |  |  | SI | Previous CS urgency classification |
| Q19 | numeric |  |  | SI | Gestation at previous CS |
| Q20 | varchar |  |  | SI | Cervical dilation at previous CS (cm) |
| Q21 | varchar |  |  | SI | Type of uterine scar |
| Q22 | varchar |  |  | SI | Other uterine scar |
| Q23 | varchar |  |  | SI | History of other uterine surgery |
| Q24 | varchar |  |  | SI | Take into account individual factors associated wi... |
| Q25 | varchar |  |  | SI | • greater maternal height |
| Q26 | varchar |  |  | SI | • maternal age less than 40 |
| Q27 | varchar |  |  | SI | • Body mass index (BMI) less than 30 |
| Q28 | varchar |  |  | SI | • gestation of less than 40 weeks |
| Q29 | varchar |  |  | SI | • infant birth weight less than 4kg (or similar/lo... |
| Q30 | varchar |  |  | SI | • spontaneous onset of labour |
| Q31 | varchar |  |  | SI | • previous caesarean for non vertex presentation |
| Q32 | varchar |  |  | SI | Eligible for a VBAC |
| Q33 | varchar |  |  | SI | VBAC eligibility notes |
| Q34 | varchar |  |  | SI | Likelihood of successful VBAC |
| Q35 | varchar |  |  | SI | Unsuccessful VBAC more likely with |
| Q36 | varchar |  |  | SI | Likelihood discussion notes |
| Q37 | varchar |  |  | SI | Increased maternal risks associated with VBAC |
| Q38 | varchar |  |  | SI | Increased maternal risk associated with Planned Re... |
| Q39 | varchar |  |  | SI | Maternal risk discussion notes |
| Q40 | varchar |  |  | SI | Increased fetal risks associated with VBAC |
| Q41 | varchar |  |  | SI | Increased fetal risk associated with PRCS |
| Q42 | varchar |  |  | SI | Intrapartum management |
| Q43 | varchar |  |  | SI | Fetal risk discussion notes |
| Q44 | varchar |  |  | SI | Birth plan |
| Q45 | varchar |  |  | SI | Specify undecided birth plan |
| Q46 | varchar |  |  | SI | In the event of preterm labour (< 37 weeks) |
| Q47 | varchar |  |  | SI | In the event of spontaneous labour before the  PRC... |
| Q48 | varchar |  |  | SI | Discussion with obstetric consultant |
| Q49 | varchar |  |  | SI | Obstetric consultant discussed with |
| Q50 | varchar |  |  | SI | Management plan notes |
| Q51 | varchar |  |  | SI | I understand the risks and benefits of a VBAC |
| Q52 | varchar |  |  | SI | I acknowledge that I have been fully informed of t... |
| Q53 | varchar |  |  | SI | I have discussed my birth choice with my obstetric... |
| Q54 | longvarbinary |  |  | SI | Signature |
| Q54UDt | date |  |  | SI | Signature Last Updated Date |
| Q54UTm | time |  |  | SI | Signature Last Updated Time |
| Q55 | varchar |  |  | SI | Verbal consent gained (e.g. if telehealth consult) |
| Q56 | varchar |  |  | SI | Provided with VBAC information documents |
| Q57 | varchar |  |  | SI | Type of information documents provided |
| Q58 | varchar |  |  | SI | Patient acknowledgement notes |
| Q59 | varchar |  |  | SI | Specify other uterine surgery |
| Q60 | numeric |  |  | SI | Gestation age |
| Q61 | numeric |  |  | SI | Gestation age (days) |
| Q62 | varchar |  |  | SI | weeks |
| Q63 | numeric |  |  | SI | Gestation at previous CS |
| Q64 | varchar |  |  | SI | days |
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