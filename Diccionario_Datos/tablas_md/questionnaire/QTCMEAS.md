# questionnaire.QTCMEAS

> Menopause Assessment Sheet

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Menopause Assessment Sheet

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | Weight |
| Q10ObsDR | varchar |  | FK | SI | Weight DR |
| Q11 | varchar |  |  | SI | Height |
| Q11ObsDR | varchar |  | FK | SI | Height DR |
| Q12 | varchar |  |  | SI | Body mass index |
| Q12ObsDR | varchar |  | FK | SI | Body mass index DR |
| Q13 | numeric |  |  | SI | Fat (%) |
| Q14 | numeric |  |  | SI | Visceral fat (%) |
| Q15 | numeric |  |  | SI | Abdominal circumference (cm) |
| Q16 | numeric |  |  | SI | Hips circumference (cm) |
| Q17 | numeric |  |  | SI | Waist hip ratio |
| Q18 | varchar |  |  | SI | Gynecological examination |
| Q19 | varchar |  |  | SI | Papanicolaou test |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Previous test |
| Q21 | varchar |  |  | SI | Colposcopy |
| Q22 | varchar |  |  | SI | Mammography |
| Q23 | varchar |  |  | SI | Breast ultrasound |
| Q24 | varchar |  |  | SI | Computerized bone mineralometry  |
| Q25 | varchar |  |  | SI | Indications |
| Q26 | varchar |  |  | SI | Therapeutic indications |
| Q27 | date |  |  | SI | Papanicolaou test date |
| Q28 | date |  |  | SI | Colposcopy date |
| Q29 | date |  |  | SI | Mammography date |
| Q3 | varchar |  |  | SI | Menopause |
| Q30 | date |  |  | SI | Breast ultrasound date |
| Q31 | date |  |  | SI | Computerized bone mineralometry date |
| Q32 | varchar |  |  | SI | Note |
| Q33 | varchar |  |  | SI | Papanicolaou test date |
| Q34 | varchar |  |  | SI | Colposcopy date |
| Q35 | varchar |  |  | SI | Mammography date |
| Q36 | varchar |  |  | SI | Breast ultrasound date |
| Q37 | varchar |  |  | SI | Computerized bone mineralometry date |
| Q38 | varchar |  |  | SI | Papanicolaou test result |
| Q39 | varchar |  |  | SI | Colposcopy result |
| Q4 | varchar |  |  | SI | Iatrogenic |
| Q40 | varchar |  |  | SI | Mammography result |
| Q41 | varchar |  |  | SI | Breast ultrasound result |
| Q42 | varchar |  |  | SI | Computerized bone mineralometry result |
| Q43 | varchar |  |  | SI | Pelvic ultrasound |
| Q44 | date |  |  | SI | Pelvic ultrasound date |
| Q45 | varchar |  |  | SI | Pelvic ultrasound result |
| Q46 | varchar |  |  | SI | Pelvic ultrasound |
| Q47 | varchar |  |  | SI | Summary of recent clinical events |
| Q48 | varchar |  |  | SI | Note |
| Q5 | varchar |  |  | SI | Menopause onset date |
| Q6 | varchar |  |  | SI | Menopausal transition |
| Q7 | varchar |  |  | SI | Hormone replacement therapy (HRT) |
| Q8 | varchar |  |  | SI | Arterial systolic |
| Q8ObsDR | varchar |  | FK | SI | Arterial systolic DR |
| Q9 | varchar |  |  | SI | Arterial diastolic |
| Q9ObsDR | varchar |  | FK | SI | Arterial diastolic DR |
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