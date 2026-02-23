# questionnaire.QGXXXGYNE

> Gynaecological Assessment

**Schema:** questionnaire
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Gynaecological Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Menarche |
| Q01ObsDR | varchar |  | FK | SI | Menarche DR |
| Q02 | varchar |  |  | SI | since |
| Q03 | varchar |  |  | SI | Menstruation |
| Q03ObsDR | varchar |  | FK | SI | Menstruation DR |
| Q04 | varchar |  |  | SI | Normal length of cycle |
| Q04ObsDR | varchar |  | FK | SI | Normal length of cycle DR |
| Q05 | varchar |  |  | SI | Nature of periods |
| Q05ObsDR | varchar |  | FK | SI | Nature of periods DR |
| Q06 | varchar |  |  | SI | Pain score (0 to 10) |
| Q06ObsDR | varchar |  | FK | SI | Pain score (0 to 10) DR |
| Q07 | date |  |  | SI | Date of last menstruation |
| Q08 | varchar |  |  | SI | Note |
| Q09 | varchar |  |  | SI | Past pregnancies |
| Q10 | varchar |  |  | SI | Full term |
| Q10ObsDR | varchar |  | FK | SI | Full term DR |
| Q10a | varchar |  |  | SI | Note |
| Q11 | varchar |  |  | SI | Number of living child |
| Q11ObsDR | varchar |  | FK | SI | Number of living child DR |
| Q11a | varchar |  |  | SI | Note |
| Q12 | varchar |  |  | SI | Miscarriage |
| Q12ObsDR | varchar |  | FK | SI | Miscarriage DR |
| Q12a | varchar |  |  | SI | Note |
| Q13 | varchar |  |  | SI | Previous abortions |
| Q13ObsDR | varchar |  | FK | SI | Previous abortions DR |
| Q13a | varchar |  |  | SI | Note |
| Q18 | varchar |  |  | SI | PARA |
| Q18ObsDR | varchar |  | FK | SI | PARA DR |
| Q19 | varchar |  |  | SI | Current pregnancy |
| Q19ObsDR | varchar |  | FK | SI | Current pregnancy DR |
| Q20 | varchar |  |  | SI | Menopause |
| Q20ObsDR | varchar |  | FK | SI | Menopause DR |
| Q20a | date |  |  | SI | since |
| Q23 | varchar |  |  | SI | Hormone replacement therapy (HRT) |
| Q23ObsDR | varchar |  | FK | SI | Hormone replacement therapy (HRT) DR |
| Q23a | varchar |  |  | SI | Note |
| Q25 | varchar |  |  | SI | Progestogens |
| Q25ObsDR | varchar |  | FK | SI | Progestogens DR |
| Q25a | varchar |  |  | SI | Note |
| Q27 | varchar |  |  | SI | Dyspareunia |
| Q27ObsDR | varchar |  | FK | SI | Dyspareunia DR |
| Q28 | date |  |  | SI | Last cervical smear date |
| Q29 | varchar |  |  | SI | Cervical smear result |
| Q29ObsDR | varchar |  | FK | SI | Cervical smear result DR |
| Q29a | varchar |  |  | SI | Note |
| Q31 | varchar |  |  | SI | Previous episodes of genital or pelvic inflammatio... |
| Q31ObsDR | varchar |  | FK | SI | Previous episodes of genital or pelvic inflammatio... |
| Q31a | varchar |  |  | SI | Note |
| Q33 | varchar |  |  | SI | Sexually transmitted diseases |
| Q33ObsDR | varchar |  | FK | SI | Sexually transmitted diseases DR |
| Q33a | varchar |  |  | SI | Note |
| Q35 | date |  |  | SI | Last gynaecological examination date |
| Q35a | varchar |  |  | SI | Note |
| Q37 | varchar |  |  | SI | Involuntary infertility support. 2 years (diagnose... |
| Q38 | varchar |  |  | SI | Weight trend |
| Q38ObsDR | varchar |  | FK | SI | Weight trend DR |
| Q40 | varchar |  |  | SI | Weight difference in kg |
| Q40ObsDR | varchar |  | FK | SI | Weight difference in kg DR |
| Q40a | date |  |  | SI | since |
| Q40b | varchar |  |  | SI | Note |
| Q42 | varchar |  |  | SI | Bowel movements |
| Q42ObsDR | varchar |  | FK | SI | Bowel movements DR |
| Q43 | varchar |  |  | SI | Urinary frequency |
| Q43ObsDR | varchar |  | FK | SI | Urinary frequency DR |
| Q44 | varchar |  |  | SI | Urinary incontinence |
| Q44ObsDR | varchar |  | FK | SI | Urinary incontinence DR |
| Q45 | varchar |  |  | SI | Urinary catheter |
| Q45ObsDR | varchar |  | FK | SI | Urinary catheter DR |
| Q46 | varchar |  |  | SI | Urinary incontinence pads |
| Q46ObsDR | varchar |  | FK | SI | Urinary incontinence pads DR |
| Q47 | varchar |  |  | SI | Premature or overdue |
| Q47ObsDR | varchar |  | FK | SI | Premature or overdue DR |
| Q47a | varchar |  |  | SI | Note |
| Q48 | varchar |  |  | SI | Contraception |
| Q48N | varchar |  |  | SI | Note |
| Q48ObsDR | varchar |  | FK | SI | Contraception DR |
| Q50 | varchar |  |  | SI | Prior treatment for infertility |
| Q50N | varchar |  |  | SI | Note |
| Q52 | date |  |  | SI | Date of last HPV Test |
| Q53 | date |  |  | SI | Date of Last Pelvic Exam |
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