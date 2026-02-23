# questionnaire.QTCCVCIB

> Central venous catheter (CVC) insertion bundle score

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Central venous catheter (CVC) insertion bundle score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Bundle compliance percentage |
| Q04 | varchar |  |  | SI |  % |
| Q05 | varchar |  |  | SI | Has the patient been identified? |
| Q06 | varchar |  |  | SI | Has the correct indication of central venous acces... |
| Q07 | varchar |  |  | SI | Has the patient been informed about the indication... |
| Q08 | varchar |  |  | SI | Has all the necessary material for the procedure b... |
| Q09 | varchar |  |  | SI | Was the pre-procedural ultrasound study of the pat... |
| Q10 | varchar |  |  | SI | Was the patient positioned correctly? |
| Q11 | varchar |  |  | SI | Was hand hygiene performed according to protocol? |
| Q12 | varchar |  |  | SI | Has skin antisepsis been performed with 2% chlorhe... |
| Q13 | varchar |  |  | SI | Have the maximum barrier precautions been implemen... |
| Q14 | varchar |  |  | SI | Is the use of local anesthesia and / or sedation a... |
| Q15 | varchar |  |  | SI | Is venipuncture ultrasound-guided? |
| Q16 | varchar |  |  | SI | Has the correct intravenous position of the guide ... |
| Q17 | varchar |  |  | SI | Has intravascular placement of the catheter been v... |
| Q18 | varchar |  |  | SI | Was intra-procedural control of catheter tip posit... |
| Q19 | varchar |  |  | SI | Was the flush and lock of the catheter performed? |
| Q20 | varchar |  |  | SI | Has the catheter been closed with the needlefree c... |
| Q21 | varchar |  |  | SI | Has the catheter been secured with sutureless anco... |
| Q22 | varchar |  |  | SI | Was histoacrylic glue used to seal the insertion s... |
| Q23 | varchar |  |  | SI | Was it covered with transparent semi-permeable adh... |
| Q24 | varchar |  |  | SI | Confirmed the maintenance of the sterile field for... |
| Q25 | varchar |  |  | SI | Notes |
| Q26 | varchar |  |  | SI | Score |
| Q27 | varchar |  |  | SI | Classification |
| Q28 | varchar |  |  | SI | 0 - 100 |
| Q29 | varchar |  |  | SI | Higher percentages represent higher compliance to ... |
| Q30 | varchar |  |  | SI | 0 - 100: Higher percentages represent higher compl... |
| Q31 | varchar |  |  | SI | CVCs are the leading cause of device-related bacte... |
| Q32 | varchar |  |  | SI | The aim of the Central venous catheter CVC inserti... |
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