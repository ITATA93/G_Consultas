# SQLUser.PA_ComplaintHistory

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIS_ParRef | bigint | PK |  | NO | PA_Complaints Parent Reference |
| HIS_Childsub | double |  |  | NO | Childsub |
| HIS_Date | date |  |  | SI | Date |
| HIS_Details | varchar |  |  | SI | Details |
| HIS_RowId | varchar |  |  | NO | - |
| HIS_Status_DR | bigint |  | FK | SI | Des Ref Status |
| HIS_Time | time |  |  | SI | Time |
| HIS_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Gestation age |
| Q04 | - |  |  | SI | weeks |
| Q05 | - |  |  | SI | Gestation age (days) |
| Q06 | - |  |  | SI | days |
| Q07 | - |  |  | SI | Current number of children |
| Q08 | - |  |  | SI | Anticipated / Desired number of children |
| Q09 | - |  |  | SI | Notes |
| Q10 | - |  |  | SI | Number of previous vaginal births |
| Q11 | - |  |  | SI | Number of previous Caesarean Sections (CS) |
| Q12 | - |  |  | SI | Was most recent birth a CS |
| Q13 | - |  |  | SI | Date of most recent CS |
| Q14 | - |  |  | SI | Estimated date |
| Q15 | - |  |  | SI | Indication for most recent CS |
| Q16 | - |  |  | SI | Previous CS operation report viewed |
| Q17 | - |  |  | SI | Notes |
| Q18 | - |  |  | SI | Previous CS urgency classification |
| Q19 | - |  |  | SI | Gestation at previous CS |
| Q20 | - |  |  | SI | Cervical dilation at previous CS (cm) |
| Q21 | - |  |  | SI | Type of uterine scar |
| Q22 | - |  |  | SI | Other uterine scar |
| Q23 | - |  |  | SI | History of other uterine surgery |
| Q24 | - |  |  | SI | Take into account individual factors associated wi... |
| Q25 | - |  |  | SI | • greater maternal height |
| Q26 | - |  |  | SI | • maternal age less than 40 |
| Q27 | - |  |  | SI | • Body mass index (BMI) less than 30 |
| Q28 | - |  |  | SI | • gestation of less than 40 weeks |
| Q29 | - |  |  | SI | • infant birth weight less than 4kg (or similar/lo... |
| Q30 | - |  |  | SI | • spontaneous onset of labour |
| Q31 | - |  |  | SI | • previous caesarean for non vertex presentation |
| Q32 | - |  |  | SI | Eligible for a VBAC |
| Q33 | - |  |  | SI | VBAC eligibility notes |
| Q34 | - |  |  | SI | Likelihood of successful VBAC |
| Q35 | - |  |  | SI | Unsuccessful VBAC more likely with |
| Q36 | - |  |  | SI | Likelihood discussion notes |
| Q37 | - |  |  | SI | Increased maternal risks associated with VBAC |
| Q38 | - |  |  | SI | Increased maternal risk associated with Planned Re... |
| Q39 | - |  |  | SI | Maternal risk discussion notes |
| Q40 | - |  |  | SI | Increased fetal risks associated with VBAC |
| Q41 | - |  |  | SI | Increased fetal risk associated with PRCS |
| Q42 | - |  |  | SI | Intrapartum management |
| Q43 | - |  |  | SI | Fetal risk discussion notes |
| Q44 | - |  |  | SI | Birth plan |
| Q45 | - |  |  | SI | Specify undecided birth plan |
| Q46 | - |  |  | SI | In the event of preterm labour (< 37 weeks) |
| Q47 | - |  |  | SI | In the event of spontaneous labour before the  PRC... |
| Q48 | - |  |  | SI | Discussion with obstetric consultant |
| Q49 | - |  |  | SI | Obstetric consultant discussed with |
| Q50 | - |  |  | SI | Management plan notes |
| Q51 | - |  |  | SI | I understand the risks and benefits of a VBAC |
| Q52 | - |  |  | SI | I acknowledge that I have been fully informed of t... |
| Q53 | - |  |  | SI | I have discussed my birth choice with my obstetric... |
| Q54 | - |  |  | SI | Signature |
| Q54UDt | - |  |  | SI | Signature Last Updated Date |
| Q54UTm | - |  |  | SI | Signature Last Updated Time |
| Q55 | - |  |  | SI | Verbal consent gained (e.g. if telehealth consult) |
| Q56 | - |  |  | SI | Provided with VBAC information documents |
| Q57 | - |  |  | SI | Type of information documents provided |
| Q58 | - |  |  | SI | Patient acknowledgement notes |
| Q59 | - |  |  | SI | Specify other uterine surgery |
| Q60 | - |  |  | SI | Gestation age |
| Q61 | - |  |  | SI | Gestation age (days) |
| Q62 | - |  |  | SI | weeks |
| Q63 | - |  |  | SI | Gestation at previous CS |
| Q64 | - |  |  | SI | days |
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