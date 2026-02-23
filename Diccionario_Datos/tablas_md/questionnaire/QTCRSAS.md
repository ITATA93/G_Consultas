# questionnaire.QTCRSAS

> Riker Sedation-Agitation Scale

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Riker Sedation-Agitation Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Riker Sedation-Agitation Scale	 |
| Q02 | varchar |  |  | SI | Agitated patients are scored by their most severe ... |
| Q03 | varchar |  |  | SI | If patient is awake or awakens easily to voice (re... |
| Q04 | varchar |  |  | SI | If more stimuli (e.g. shaking) is required to awak... |
| Q05 | varchar |  |  | SI | to the point of responding or following commands, ... |
| Q06 | varchar |  |  | SI | Little or no response to noxious physical stimuli ... |
| Q07 | varchar |  |  | SI | Score |
| Q08 | varchar |  |  | SI | Classification |
| Q09 | varchar |  |  | SI | 7 - Dangerous Agitation |
| Q10 | varchar |  |  | SI | 6 - Very Agitated |
| Q11 | varchar |  |  | SI | 5 - Agitated |
| Q12 | varchar |  |  | SI | 4 - Calm and Cooperative |
| Q13 | varchar |  |  | SI | 3 - Sedated |
| Q14 | varchar |  |  | SI | 2 - Very Sedated |
| Q15 | varchar |  |  | SI | 1 - Unarousable |
| Q16 | varchar |  |  | SI | Riker Sedation-Agitation Scale clearly define and ... |
| Q17 | varchar |  |  | SI | Riker Sedation-Agitation Scale |
| Q18 | date |  |  | SI | Date |
| Q19 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Riker Sedation-Agitation Scale |
| Q21 | varchar |  |  | SI | Riker RR, Picard JT, Fraser GL. Prospective evalua... |
| Q22 | varchar |  |  | SI | Simmons LE, Riker RR, Prato BS, Fraser GL. Assessi... |
| Q23 | varchar |  |  | SI | Crit Care Med. 1999 Aug;27(8):1499-504. doi: 10.10... |
| Q24 | varchar |  |  | SI | Brandl KM, Langley KA, Riker RR, Dork LA, Quails C... |
| Q25 | varchar |  |  | SI | Pharmacotherapy. 2001 Apr;21(4):431-6. doi: 10.159... |
| Q26 | varchar |  |  | SI | Riker RR, Fraser GL, Simmons LE, Wilkins ML. Valid... |
| Q27 | varchar |  |  | SI | Intensive Care Med. 2001 May;27(5):853-8. doi: 10.... |
| Q28 | varchar |  |  | SI | Khan BA, Guzman O, Campbell NL, Walroth T, Tricker... |
| Q29 | varchar |  |  | SI | Comparison and agreement between the Richmond Agit... |
| Q30 | varchar |  |  | SI | Chest. 2012 Jul;142(1):48-54. doi: 10.1378/chest.1... |
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