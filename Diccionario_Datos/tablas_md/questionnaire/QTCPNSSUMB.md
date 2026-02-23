# questionnaire.QTCPNSSUMB

> Signs and Symptoms of an Unwell Baby and Mother

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Signs and Symptoms of an Unwell Baby and Mother

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Please discuss the following urgent situations and... |
| Q02 | varchar |  |  | SI | Baby looks pale or blue in colour |
| Q03 | varchar |  |  | SI | Baby stops breathing |
| Q04 | varchar |  |  | SI | Baby is unresponsive when you try to wake them |
| Q05 | varchar |  |  | SI | Baby has glazed-over eyes, not focusing on anythin... |
| Q06 | varchar |  |  | SI | Baby has a fit or seizure |
| Q07 | varchar |  |  | SI | Baby has a rash that does not disappear under pres... |
| Q08 | varchar |  |  | SI | Baby has an abnormal temperature (below 36C or abo... |
| Q09 | varchar |  |  | SI | Mother has a sudden / heavy blood loss |
| Q10 | varchar |  |  | SI | Mother has difficulty breathing / shortness of bre... |
| Q11 | varchar |  |  | SI | Mother has red / swollen / tender calf or calves |
| Q12 | varchar |  |  | SI | Mother feels faint/has fast heartbeat |
| Q13 | varchar |  |  | SI | Mother has severe headaches / sudden swelling of t... |
| Q14 | varchar |  |  | SI | Mother has an abnormal temperature (below 35C or a... |
| Q15 | varchar |  |  | SI | Mother has a smelly or discoloured vaginal loss, a... |
| Q16 | varchar |  |  | SI | Mother experiences shivering, vomiting or confusio... |
| Q17 | varchar |  |  | SI | Parent(s) aware of postnatal booklet information |
| Q18 | varchar |  |  | SI | Additional comments |
| Q19 | date |  |  | SI | Date |
| Q20 | time |  |  | SI | Time |
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