# SQLUser.PAC_VitaminKGiven

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VITK_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Riker Sedation-Agitation Scale	 |
| Q02 | - |  |  | SI | Agitated patients are scored by their most severe ... |
| Q03 | - |  |  | SI | If patient is awake or awakens easily to voice (re... |
| Q04 | - |  |  | SI | If more stimuli (e.g. shaking) is required to awak... |
| Q05 | - |  |  | SI | to the point of responding or following commands, ... |
| Q06 | - |  |  | SI | Little or no response to noxious physical stimuli ... |
| Q07 | - |  |  | SI | Score |
| Q08 | - |  |  | SI | Classification |
| Q09 | - |  |  | SI | 7 - Dangerous Agitation |
| Q10 | - |  |  | SI | 6 - Very Agitated |
| Q11 | - |  |  | SI | 5 - Agitated |
| Q12 | - |  |  | SI | 4 - Calm and Cooperative |
| Q13 | - |  |  | SI | 3 - Sedated |
| Q14 | - |  |  | SI | 2 - Very Sedated |
| Q15 | - |  |  | SI | 1 - Unarousable |
| Q16 | - |  |  | SI | Riker Sedation-Agitation Scale clearly define and ... |
| Q17 | - |  |  | SI | Riker Sedation-Agitation Scale |
| Q18 | - |  |  | SI | Date |
| Q19 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Riker Sedation-Agitation Scale |
| Q21 | - |  |  | SI | Riker RR, Picard JT, Fraser GL. Prospective evalua... |
| Q22 | - |  |  | SI | Simmons LE, Riker RR, Prato BS, Fraser GL. Assessi... |
| Q23 | - |  |  | SI | Crit Care Med. 1999 Aug |
| Q24 | - |  |  | SI | Brandl KM, Langley KA, Riker RR, Dork LA, Quails C... |
| Q25 | - |  |  | SI | Pharmacotherapy. 2001 Apr |
| Q26 | - |  |  | SI | Riker RR, Fraser GL, Simmons LE, Wilkins ML. Valid... |
| Q27 | - |  |  | SI | Intensive Care Med. 2001 May |
| Q28 | - |  |  | SI | Khan BA, Guzman O, Campbell NL, Walroth T, Tricker... |
| Q29 | - |  |  | SI | Comparison and agreement between the Richmond Agit... |
| Q30 | - |  |  | SI | Chest. 2012 Jul |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| VITK_Code | varchar |  |  | NO | Code |
| VITK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VITK_CreatedDate | date |  |  | SI | Created Date |
| VITK_CreatedTime | time |  |  | SI | Created Time |
| VITK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VITK_DateFrom | date |  |  | SI | Date From |
| VITK_DateTo | date |  |  | SI | Date To |
| VITK_Desc | varchar |  |  | NO | Description |
| VITK_Owner | varchar |  |  | SI | Owner |
| VITK_UpdatedDate | date |  |  | SI | Updated Date |
| VITK_UpdatedTime | time |  |  | SI | Updated Time |
| VITK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*