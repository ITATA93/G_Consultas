# questionnaire.QGXXXMANBV

> Antenatal Booking Visit

**Schema:** questionnaire
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antenatal Booking Visit

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Have you received any early pregnancy advice |
| Q02 | varchar |  |  | SI | Have you had a previous booking for this pregnancy |
| Q02A | varchar |  |  | SI | Location of previous booking |
| Q02B | varchar |  |  | SI | Reason for new booking |
| Q02T | varchar |  |  | SI | Details |
| Q03 | varchar |  |  | SI | Are you intending to move out of the area in the n... |
| Q04 | varchar |  |  | SI | Seen within 2 weeks of first contact (Gestation at... |
| Q04A | varchar |  |  | SI | Details |
| Q05 | varchar |  |  | SI | Have you been admitted to hospital recently |
| Q05A | varchar |  |  | SI | Details |
| Q06 | varchar |  |  | SI | Place of birth |
| Q07 | varchar |  |  | SI | Are your family origins Mediterranean, Africa, Car... |
| Q08 | varchar |  |  | SI | Mothers family origins are South Asia, Caribbean o... |
| Q09 | varchar |  |  | SI | Preferred method of contact |
| Q12 | varchar |  |  | SI | Is English your first language |
| Q13 | varchar |  |  | SI | Do you have any language or literacy issues |
| Q13A | varchar |  |  | SI | Literacy issues |
| Q13B | varchar |  |  | SI | Language spoken |
| Q14 | varchar |  |  | SI | Interpreter required |
| Q15 | varchar |  |  | SI | Preferred methods of communication |
| Q16 | varchar |  |  | SI | Learning disabilities details |
| Q17 | varchar |  |  | SI | What is your sexuality |
| Q18 | varchar |  |  | SI | Height |
| Q18ObsDR | varchar |  | FK | SI | Height DR |
| Q19 | varchar |  |  | SI | Weight (kg) |
| Q19ObsDR | varchar |  | FK | SI | Weight (kg) DR |
| Q20 | varchar |  |  | SI | BMI |
| Q21 | varchar |  |  | SI | Systolic BP |
| Q21ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q22 | varchar |  |  | SI | Diastolic BP |
| Q22ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q23 | varchar |  |  | SI | Was your pregnancy planned |
| Q24 | varchar |  |  | SI | Is VBAC intended for this pregnancy |
| Q25 | varchar |  |  | SI | Is the uterus palpable |
| Q26 | varchar |  |  | SI | Have you had any vaginal bleeding |
| Q26A | varchar |  |  | SI | Type of vaginal bleeding |
| Q27 | varchar |  |  | SI | Do you have pain on passing urine |
| Q27T | varchar |  |  | SI | Details |
| Q28 | varchar |  |  | SI | Have you had recent contact with anyone with Chick... |
| Q28T | varchar |  |  | SI | Details |
| Q29 | varchar |  |  | SI | Do you take regular journeys by car, plane or trai... |
| Q30 | varchar |  |  | SI | Have you received advice about your weight |
| Q31 | varchar |  |  | SI | Do you have any tattoos or piercings |
| Q31T | varchar |  |  | SI | Details |
| Q32 | varchar |  |  | SI | Medications taken during this pregnancy |
| Q32A | varchar |  |  | SI | Medications |
| Q32T | varchar |  |  | SI | Details |
| Q33 | varchar |  |  | SI | Do you have support in pregnancy and childcare |
| Q33A | varchar |  |  | SI | Type of support |
| Q33T | varchar |  |  | SI | Details |
| Q34 | varchar |  |  | SI | Are there any accommodation issues |
| Q34A | varchar |  |  | SI | Accommodation issues |
| Q34T | varchar |  |  | SI | Details |
| Q35 | varchar |  |  | SI | Occupation |
| Q36 | varchar |  |  | SI | Employment status |
| Q36T | varchar |  |  | SI | Details |
| Q37 | varchar |  |  | SI | Does anyone you live with have personal issues |
| Q37A | varchar |  |  | SI | Personal issues |
| Q37T | varchar |  |  | SI | Details |
| Q38 | varchar |  |  | SI | Are there any broader family issues |
| Q38A | varchar |  |  | SI | Broader issues |
| Q38T | varchar |  |  | SI | Details |
| Q39 | varchar |  |  | SI | Any agencies involved |
| Q39A | varchar |  |  | SI | Agencies |
| Q39T | varchar |  |  | SI | Details |
| Q40 | varchar |  |  | SI | How are things at home |
| Q41 | varchar |  |  | SI | Is there anybody at home who is not happy about th... |
| Q41T | varchar |  |  | SI | Details |
| Q42 | varchar |  |  | SI | Will this baby be in the CONI programme |
| Q43 | varchar |  |  | SI | In the past month have you been bothered by |
| Q43A | varchar |  |  | SI | Feeling down, depressed or hopeless |
| Q43AObsDR | varchar |  | FK | SI | Feeling down, depressed or hopeless DR |
| Q43B | varchar |  |  | SI | Having little interest or pleasure in doing things |
| Q43BObsDR | varchar |  | FK | SI | Having little interest or pleasure in doing things... |
| Q43C | varchar |  |  | SI | Do you want help with any mental health issues |
| Q43CObsDR | varchar |  | FK | SI | Do you want help with any mental health issues DR |
| Q43T | varchar |  |  | SI | Details |
| Q44 | varchar |  |  | SI | Have you made/will you be making any referrals |
| Q44A | varchar |  |  | SI | Referrals |
| Q44T | varchar |  |  | SI | Details |
| Q74 | varchar |  |  | SI | Do you have any learning disabilities |
| Q75 | numeric |  |  | SI | Number of years in education |
| Q76 | varchar |  |  | SI | Referral Required |
| Q76ObsDR | varchar |  | FK | SI | Referral Required DR |
| Q77 | varchar |  |  | SI | Worrying or feeling anxious |
| Q77ObsDR | varchar |  | FK | SI | Worrying or feeling anxious DR |
| Q78 | varchar |  |  | SI | Does your partner have any history |
| Q78ObsDR | varchar |  | FK | SI | Does your partner have any history DR |
| Q79 | varchar |  |  | SI | Family History |
| Q79ObsDR | varchar |  | FK | SI | Family History DR |
| Q80 | varchar |  |  | SI | Previous treatment/in-patient care |
| Q80ObsDR | varchar |  | FK | SI | Previous treatment/in-patient care DR |
| Q81 | varchar |  |  | SI | Past or present mental illness |
| Q81ObsDR | varchar |  | FK | SI | Past or present mental illness DR |
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