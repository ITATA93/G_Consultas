# questionnaire.QTCPUSH

> Pressure Ulcer Scale for Healing (PUSH)

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pressure Ulcer Scale for Healing (PUSH)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | varchar |  |  | SI | Ulcer location |
| Q03 | varchar |  |  | SI | Directions: |
| Q04 | varchar |  |  | SI | Observe and measure the pressure ulcer. Categorize... |
| Q06 | varchar |  |  | SI | Other location: |
| Q07 | varchar |  |  | SI | Length x Width:  |
| Q08 | varchar |  |  | SI | Exudate Amount: |
| Q09 | varchar |  |  | SI | Tissue Type: |
| Q10 | varchar |  |  | SI |  Measure the greatest length (head to toe) and the... |
| Q11 | varchar |  |  | SI | : Do not guess! Always use a centimeter ruler and ... |
| Q12 | varchar |  |  | SI | Estimate the amount of exudate (drainage) present ... |
| Q13 | varchar |  |  | SI |  This refers to the types of tissue that are prese... |
| Q14 | varchar |  |  | SI | Score as a “3” if there is any amount of slough pr... |
| Q15 | varchar |  |  | SI | Score as a “2” if the wound is clean and contains ... |
| Q16 | varchar |  |  | SI | A superficial wound that is reepithelializing is s... |
| Q17 | varchar |  |  | SI | Length x width |
| Q18 | varchar |  |  | SI | Exudate amount |
| Q19 | varchar |  |  | SI | Tissue Type |
| Q20 | varchar |  |  | SI | The National Pressure Ulcer Advisory Panel (NPUAP)... |
| Q21 | varchar |  |  | SI | The PUSH is a quick, reliable tool to monitor the ... |
| Q22 | varchar |  |  | SI | 0 :  Healed |
| Q23 | varchar |  |  | SI | 1 to 17: Severity of the wound |
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