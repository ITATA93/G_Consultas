# questionnaire.QTCCFPFTRF

> Pulmonary Function Test Request Form

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pulmonary Function Test Request Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Respiratory problem |
| Q02 | varchar |  |  | SI | Other problems |
| Q03 | varchar |  |  | SI | Reason for request (please tick appropriate reason... |
| Q03A | varchar |  |  | SI | Other |
| Q04 | varchar |  |  | SI | Duration of smoking  |
| Q05 | varchar |  |  | SI | months |
| Q06 | varchar |  |  | SI | years |
| Q07 | varchar |  |  | SI | No. of cigs/day |
| Q08 | varchar |  |  | SI | If ex-smoker: duration of smoking  |
| Q09 | varchar |  |  | SI | months |
| Q10 | varchar |  |  | SI | years |
| Q11 | varchar |  |  | SI | Stopped |
| Q12 | varchar |  |  | SI | months |
| Q13 | varchar |  |  | SI | years |
| Q13A | varchar |  |  | SI | ago |
| Q14 | varchar |  |  | SI | History of Tuberculosis |
| Q15 | varchar |  |  | SI | History of Tuberculosis (if psoitive - when) |
| Q16 | varchar |  |  | SI | History of Tuberculosis (if psoitive - state) |
| Q17 | varchar |  |  | SI | History of exposure to asbestos |
| Q18 | varchar |  |  | SI | Other type of dust |
| Q18A | varchar |  |  | SI | Organic dust : Pigeon dropping |
| Q19 | varchar |  |  | SI | History of bronchial hyper responsiveness (cough /... |
| Q20 | varchar |  |  | SI | Dust |
| Q21 | varchar |  |  | SI | Strong perfumes |
| Q22 | varchar |  |  | SI | Incense |
| Q23 | varchar |  |  | SI | Insecticides |
| Q24 | varchar |  |  | SI | Cigarette smoke |
| Q25 | varchar |  |  | SI | History of upper respiratory tract problem |
| Q26 | varchar |  |  | SI | History of thoracic surgery |
| Q27 | varchar |  |  | SI | History of snoring |
| Q28 | varchar |  |  | SI | Duration of illness |
| Q28A | varchar |  |  | SI | Other |
| Q29 | varchar |  |  | SI | years |
| Q30 | varchar |  |  | SI | months |
| Q31 | varchar |  |  | SI | Productive cough  |
| Q32 | varchar |  |  | SI | Nonproductive cough |
| Q33 | varchar |  |  | SI | Wheezing |
| Q34 | varchar |  |  | SI | Breathlessness at rest |
| Q35 | varchar |  |  | SI | Breathlessness during exertion |
| Q36 | varchar |  |  | SI | Wheeze |
| Q37 | varchar |  |  | SI | Crackles |
| Q38 | varchar |  |  | SI | Tachypnoea |
| Q39 | varchar |  |  | SI | Sputum - routine organism |
| Q40 | varchar |  |  | SI | Sputum - Acid Fast Bacilli |
| Q41 | varchar |  |  | SI | Medical Imaging (please enclose if Yes) |
| Q46 | varchar |  |  | SI | Other |
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