# questionnaire.QTCPDTFU

> Post Discharge Telephone Follow-Up

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Post Discharge Telephone Follow-Up

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bit |  |  | SI | Within 24 Hours of Discharge |
| Q02 | bit |  |  | SI | Within 5 Days of Discharge  |
| Q03 | varchar |  |  | SI | Note:  |
| Q04 | varchar |  |  | SI | If you have any concerns with the patient's condit... |
| Q05 | varchar |  |  | SI | Your action needs to be prompt and documented on t... |
| Q06 | varchar |  |  | SI | General Information |
| Q07 | varchar |  |  | SI | Discharge Date |
| Q08 | date |  |  | SI | Date of Call |
| Q09 | varchar |  |  | SI | Call made by |
| Q10 | varchar |  |  | SI | Home Visit |
| Q11 | varchar |  |  | SI | Hello, my name is  |
| Q12 | varchar |  |  | SI | Name |
| Q13 | varchar |  |  | SI | , and I am calling from  |
| Q14 | varchar |  |  | SI | I'm following up on your discharge and I wanted to... |
| Q15 | varchar |  |  | SI | Pain |
| Q16 | varchar |  |  | SI | How you are coping at home? |
| Q17 | varchar |  |  | SI | Are you in pain? |
| Q18 | varchar |  |  | SI | Please rate your pain on a scale from 1 to 10. (10... |
| Q19 | varchar |  |  | SI | If so, how do you manage it? |
| Q20 | varchar |  |  | SI | Are you taking your medication as your doctor orde... |
| Q21 | varchar |  |  | SI | Comment on medication |
| Q22 | varchar |  |  | SI | Are you taking any other medications that are not ... |
| Q23 | varchar |  |  | SI | Comment medication list |
| Q24 | varchar |  |  | SI | Do you have any questions about your medication?  |
| Q25 | varchar |  |  | SI | Is there any discharge coming from the wound? |
| Q26 | varchar |  |  | SI | Has redness or inflammation increased since you we... |
| Q27 | varchar |  |  | SI | Comments on wound care |
| Q28 | varchar |  |  | SI | Do you know which symptoms to watch for that would... |
| Q29 | varchar |  |  | SI | Comments on warning signs |
| Q30 | bit |  |  | SI | Patient is reminded to call  |
| Q31 | varchar |  |  | SI | (Call instruction) |
| Q32 | varchar |  |  | SI | in case of warning sign. |
| Q33 | varchar |  |  | SI | Do you have fever? |
| Q34 | varchar |  |  | SI | Did you make your follow-up appointment? |
| Q35 | varchar |  |  | SI | Do you feel you are improving and recovering well? |
| Q36 | varchar |  |  | SI | Do you think you were well prepared before the ope... |
| Q37 | varchar |  |  | SI | Do you have any other questions about your conditi... |
| Q38 | varchar |  |  | SI | Do you have any questions about the follow up proc... |
| Q39 | varchar |  |  | SI | Thank you for speaking with me today. If you have ... |
| Q40 | varchar |  |  | SI | General comment |
| Q41 | varchar |  |  | SI | Comments |
| Q42 | date |  |  | SI | Doctor informed on |
| Q43 | varchar |  |  | SI | Doctor feedback |
| Q44 | varchar |  |  | SI | Action taken with patient |
| Q45 | varchar |  |  | SI | Comments on actions |
| Q46 | varchar |  |  | SI | Comments on fever |
| Q47 | varchar |  |  | SI | Comments on other questions |
| Q48 | date |  |  | SI | Date |
| Q49 | time |  |  | SI | Time |
| Q50 | varchar |  |  | SI | Discharge telephone call |
| Q51 | varchar |  |  | SI | Did you make your follow-up appointment? |
| Q52 | varchar |  |  | SI | Do you feel you are improving and recovering well? |
| Q53 | varchar |  |  | SI | Do you think you were well prepared before the ope... |
| Q54 | varchar |  |  | SI | Comments |
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