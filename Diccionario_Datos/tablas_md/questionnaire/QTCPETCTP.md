# questionnaire.QTCPETCTP

> PET CT Patient Questionnaire

**Schema:** questionnaire
**Columnas:** 129
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* PET CT Patient Questionnaire

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Procedure |
| Q02 | date |  |  | SI | If yes, date: |
| Q03 | varchar |  |  | SI | Previous PET CT |
| Q04 | varchar |  |  | SI | Patient Identification verified |
| Q05 | varchar |  |  | SI | Last Menstrual Period |
| Q06 | bit |  |  | SI | Not applicable |
| Q07 | varchar |  |  | SI | Is there any possibility that you may be pregnant? |
| Q08 | varchar |  |  | SI | Pregnancy test result |
| Q09 | varchar |  |  | SI | Are you breast feeding? |
| Q10 | varchar |  |  | SI | Breast feeding cessation advice given? |
| Q11 | varchar |  |  | SI | Height (cm) |
| Q11ObsDR | varchar |  | FK | SI | Height (cm) DR |
| Q12 | varchar |  |  | SI | Weight (kg) |
| Q12ObsDR | varchar |  | FK | SI | Weight (kg) DR |
| Q13 | varchar |  |  | SI | Are you diabetic? |
| Q14 | varchar |  |  | SI | Are you taking Metformin? |
| Q15 | varchar |  |  | SI | Are you Insulin dependent? |
| Q16 | date |  |  | SI | Date of last Insulin dose |
| Q17 | time |  |  | SI | Time of last Insulin dose |
| Q18 | varchar |  |  | SI | Last blood sugar reading |
| Q19 | date |  |  | SI | Date of reading |
| Q20 | time |  |  | SI | Time of reading |
| Q21 | varchar |  |  | SI | Recent surgeries / biopsies? (Last 12 months) |
| Q22 | date |  |  | SI | Date |
| Q23 | varchar |  |  | SI | Please describe |
| Q24 | varchar |  |  | SI | Add image |
| Q25 | varchar |  |  | SI | Are you allergic to any medications |
| Q26 | varchar |  |  | SI | Recent surgeries / biopsies? (last 12 months) |
| Q27 | date |  |  | SI | Most recent completion date |
| Q28 | varchar |  |  | SI | Cycles |
| Q29 | varchar |  |  | SI | Previous chemotherapy |
| Q30 | varchar |  |  | SI | Area |
| Q31 | date |  |  | SI | Most recent completion date |
| Q32 | numeric |  |  | SI | Sessions |
| Q33 | varchar |  |  | SI | Previous radiation therapy |
| Q34 | varchar |  |  | SI | Recent infections |
| Q35 | date |  |  | SI | When did you last eat? (Date) |
| Q36 | time |  |  | SI | When did you last eat? (Time) |
| Q37 | varchar |  |  | SI | Do you currently experience incontinence? |
| Q38 | varchar |  |  | SI | Do you have a history of any of the following cond... |
| Q39 | date |  |  | SI | Date |
| Q40 | date |  |  | SI | Date |
| Q41 | date |  |  | SI | Date |
| Q42 | date |  |  | SI | Date |
| Q43 | date |  |  | SI | Date |
| Q44 | varchar |  |  | SI | Procedure and dates |
| Q45 | varchar |  |  | SI | Have you had any of the following procedures recen... |
| Q46 | varchar |  |  | SI | Chest xray |
| Q47 | varchar |  |  | SI | CT / CT contrast |
| Q48 | varchar |  |  | SI | MRI |
| Q49 | varchar |  |  | SI | Bone scan |
| Q50 | varchar |  |  | SI | Other procedure |
| Q51 | longvarbinary |  |  | SI | Patient signature |
| Q51UDt | date |  |  | SI | Patient signature Last Updated Date |
| Q51UTm | time |  |  | SI | Patient signature Last Updated Time |
| Q52 | date |  |  | SI | Date |
| Q53 | longvarbinary |  |  | SI | Technologist signature |
| Q53UDt | date |  |  | SI | Technologist signature Last Updated Date |
| Q53UTm | time |  |  | SI | Technologist signature Last Updated Time |
| Q54 | date |  |  | SI | Date |
| Q55 | varchar |  |  | SI | Please list |
| Q56 | varchar |  |  | SI | Please list all medications you are currently taki... |
| Q57 | varchar |  |  | SI | Please describe |
| Q58 | varchar |  |  | SI | On antibiotics |
| Q59 | varchar |  |  | SI | Recent infections |
| Q60 | varchar |  |  | SI | Recent surgeries / biopsies? (Last 12 months) |
| Q61 | varchar |  |  | SI | Are you allergic to any medications? |
| Q62 | varchar |  |  | SI | Chest Xray |
| Q63 | varchar |  |  | SI | Dose information |
| Q64 | varchar |  |  | SI | Injection site |
| Q65 | varchar |  |  | SI | Injected by |
| Q66 | time |  |  | SI | Injection time |
| Q67 | numeric |  |  | SI | Post injection dose(MBq) |
| Q68 | time |  |  | SI | Post injection time |
| Q69 | time |  |  | SI | Scan time |
| Q70 | varchar |  |  | SI | Infiltration |
| Q71 | date |  |  | SI | Date |
| Q72 | time |  |  | SI | Time |
| Q73 | varchar |  |  | SI | Acquisition/Processing comments |
| Q74 | varchar |  |  | SI | Scan done by |
| Q75 | date |  |  | SI | Scan done date |
| Q76 | time |  |  | SI | Time |
| Q77 | varchar |  |  | SI | Delayed scan |
| Q78 | varchar |  |  | SI | Area |
| Q79 | date |  |  | SI | Date |
| Q80 | time |  |  | SI | Time |
| Q81 | varchar |  |  | SI | Dose Information |
| Q82 | varchar |  |  | SI | Acquisition/Processing Comments |
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