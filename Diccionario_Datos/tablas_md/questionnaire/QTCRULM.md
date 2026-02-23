# questionnaire.QTCRULM

> Revised Upper Limb Module for SMA (RULM)

**Schema:** questionnaire
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Revised Upper Limb Module for SMA (RULM)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Spinal Muscular Atrophy (SMA) |
| Q04 | varchar |  |  | SI | Tested side |
| Q05 | varchar |  |  | SI | Elbow retractions in flexion / extension tested si... |
| Q06 | numeric |  |  | SI | Elbow retractions (degrees) |
| Q07 | varchar |  |  | SI | ° |
| Q08 | varchar |  |  | SI | Elbow retractions in prone / tested side |
| Q09 | numeric |  |  | SI | Elbow retractions in prone (degrees) |
| Q10 | varchar |  |  | SI | ° |
| Q11 | varchar |  |  | SI | Bustier worn for the test |
| Q12 | varchar |  |  | SI | Type |
| Q13 | varchar |  |  | SI | A. Entry item |
| Q14 | varchar |  |  | SI | B. Bring hands from lap to table |
| Q15 | varchar |  |  | SI | Limited by contracture |
| Q16 | varchar |  |  | SI | C. Tracing a path |
| Q17 | varchar |  |  | SI | Limited by contracture |
| Q18 | varchar |  |  | SI | Can you complete the path bringing the car to the ... |
| Q19 | varchar |  |  | SI | RULM path |
| Q20 | varchar |  |  | SI | D. Pick up tokens |
| Q21 | varchar |  |  | SI | Limited by contracture |
| Q22 | varchar |  |  | SI | E. Place token into cup on table or shoulder heigh... |
| Q23 | varchar |  |  | SI | Limited by contracture |
| Q24 | varchar |  |  | SI | Place token into cup |
| Q25 | varchar |  |  | SI | • On table: horizontal |
| Q26 | varchar |  |  | SI | • At shoulder height: vertical |
| Q27 | varchar |  |  | SI | F. Reach to the side and touch token |
| Q28 | varchar |  |  | SI | Limited by contracture |
| Q29 | varchar |  |  | SI | Can you take the token from my hand? |
| Q30 | varchar |  |  | SI | G. Push a button light |
| Q31 | varchar |  |  | SI | Limited by contracture |
| Q32 | varchar |  |  | SI | Can you turn the light on by pushing it and hard e... |
| Q33 | varchar |  |  | SI | H. Tearing paper |
| Q34 | varchar |  |  | SI | Limited by contracture |
| Q35 | varchar |  |  | SI | I. Open ziploc container |
| Q36 | varchar |  |  | SI | Limited by contracture |
| Q37 | varchar |  |  | SI | J. Raise cup with 200g to mouth |
| Q38 | varchar |  |  | SI | Limited by contracture |
| Q39 | varchar |  |  | SI | K. Moving 200g weight on table horizontally |
| Q40 | varchar |  |  | SI | Limited by contracture |
| Q41 | varchar |  |  | SI | Can you lift this weight from the center circle to... |
| Q42 | varchar |  |  | SI | L. Moving 500g weight on table horizontally |
| Q43 | varchar |  |  | SI | Limited by contracture |
| Q44 | varchar |  |  | SI | Can you lift this weight from the center circle to... |
| Q45 | varchar |  |  | SI | M. Moving weight on table diagonally |
| Q46 | varchar |  |  | SI | Limited by contracture |
| Q47 | varchar |  |  | SI | Can you lift this weight from this circle to this ... |
| Q48 | varchar |  |  | SI | N. Bring 500g weight from lap to table |
| Q49 | varchar |  |  | SI | Limited by contracture |
| Q50 | varchar |  |  | SI | O. Bring both arms above head - shoulder abduction |
| Q51 | varchar |  |  | SI | Limited by contracture |
| Q52 | varchar |  |  | SI | Score from entry item (Brooke score) |
| Q53 | varchar |  |  | SI | P. Bring 500g above shoulder height with extended ... |
| Q54 | varchar |  |  | SI | Limited by contracture |
| Q55 | varchar |  |  | SI | Q. Bring 1kg above shoulder height with extended a... |
| Q56 | varchar |  |  | SI | Limited by contracture |
| Q57 | varchar |  |  | SI | R. Bring hand above shoulder height with extended ... |
| Q58 | varchar |  |  | SI | Limited by contracture |
| Q59 | varchar |  |  | SI | S. Bring 500g above shoulder height with extended ... |
| Q60 | varchar |  |  | SI | Limited by contracture |
| Q61 | varchar |  |  | SI | T. Bring 1kg weight above shoulder height with ext... |
| Q62 | varchar |  |  | SI | Limited by contracture |
| Q63 | varchar |  |  | SI | Score |
| Q64 | varchar |  |  | SI | Classification |
| Q65 | varchar |  |  | SI | 0 - 37 |
| Q66 | varchar |  |  | SI | Lower scores correspond to higher level of disabil... |
| Q67 | varchar |  |  | SI | 0 - 37: Lower scores correspond to higher level of... |
| Q68 | varchar |  |  | SI | The Revised Upper Limb Module (RULM) FOR SMA has b... |
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