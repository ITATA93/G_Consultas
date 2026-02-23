# questionnaire.QTCEFR

> Enteral Feeding Regimen

**Schema:** questionnaire
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Enteral Feeding Regimen

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Enteral feeding regimen |
| Q02 | varchar |  |  | SI | Is the patient at risk of refeeding syndrome? |
| Q03 | varchar |  |  | SI | Feed is initiated slowly as per instructions and n... |
| Q04 | varchar |  |  | SI | Please refer to the “Refeeding Syndrome in Adults ... |
| Q05 | varchar |  |  | SI | Location |
| Q06 | varchar |  |  | SI | Other |
| Q07 | varchar |  |  | SI | Feed name |
| Q08 | varchar |  |  | SI | Feeding regimen |
| Q10 | date |  |  | SI | From (date) |
| Q12 | varchar |  |  | SI | Method of delivery |
| Q13 | varchar |  |  | SI | Commence at |
| Q14 | varchar |  |  | SI | Increase by |
| Q15 | varchar |  |  | SI | Every |
| Q16 | varchar |  |  | SI | Target rate of |
| Q17 | varchar |  |  | SI | Total feed per day of |
| Q18 | varchar |  |  | SI | Times of feeding |
| Q19 | varchar |  |  | SI | Water flush |
| Q20 | bit |  |  | SI | Water flush |
| Q21 | varchar |  |  | SI | Water flush text |
| Q22 | varchar |  |  | SI | every |
| Q23 | bit |  |  | SI | Water flush 2 |
| Q24 | varchar |  |  | SI | Water flush 2 text |
| Q25 | varchar |  |  | SI | Also flush with at least 50mL before and after eac... |
| Q26 | varchar |  |  | SI | Monitoring gastric residual volume (aspirates) |
| Q27 | date |  |  | SI | Date |
| Q28 | varchar |  |  | SI | Monitoring gastric residual volume (aspirates) 2 |
| Q29 | date |  |  | SI | Date |
| Q30 | varchar |  |  | SI | Comments |
| Q31 | varchar |  |  | SI | Total nutrition provided at target rate |
| Q32 | varchar |  |  | SI | Energy |
| Q33 | varchar |  |  | SI | Protein |
| Q34 | varchar |  |  | SI | Other |
| Q35 | varchar |  |  | SI | Fluid from feed |
| Q36 | varchar |  |  | SI | Fluid from flushes |
| Q37 | varchar |  |  | SI | Total fluids |
| Q38 | varchar |  |  | SI | Dietitian |
| Q39 | date |  |  | SI | Date |
| Q40 | longvarbinary |  |  | SI | Signature |
| Q40UDt | date |  |  | SI | Signature Last Updated Date |
| Q40UTm | time |  |  | SI | Signature Last Updated Time |
| Q41 | numeric |  |  | SI | Pager no / Phone no |
| Q42 | varchar |  |  | SI | mL/hr |
| Q43 | varchar |  |  | SI | mL/hr every |
| Q44 | varchar |  |  | SI | hrs, as tolerated, until, |
| Q45 | varchar |  |  | SI | mL/hr (total feed per day of |
| Q46 | varchar |  |  | SI | mL) |
| Q47 | varchar |  |  | SI | mL every |
| Q48 | varchar |  |  | SI | hours |
| Q49 | varchar |  |  | SI | Feeding regimen |
| Q50 | varchar |  |  | SI | Tube type / diameter |
| Q51 | varchar |  |  | SI | mL pre and post feeding |
| Q52 | varchar |  |  | SI | KJ/day |
| Q53 | varchar |  |  | SI | g/day |
| Q54 | varchar |  |  | SI | /day |
| Q55 | varchar |  |  | SI | mL/day |
| Q56 | varchar |  |  | SI | mL/day |
| Q57 | varchar |  |  | SI | mL/day |
| Q58 | varchar |  |  | SI | Other |
| Q59 | varchar |  |  | SI | Monitoring gastric residual volume (aspirates) |
| Q60 | varchar |  |  | SI | Monitoring gastric residual volume (aspirates) 2 |
| Q61 | varchar |  |  | SI | Status of enteral feeding regimen |
| Q62 | varchar |  |  | SI | Reason for voiding |
| Q63 | varchar |  |  | SI | Voided by |
| Q64 | date |  |  | SI | Void date |
| Q65 | time |  |  | SI | Void time |
| Q66 | date |  |  | SI | Date |
| Q67 | time |  |  | SI | Time |
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