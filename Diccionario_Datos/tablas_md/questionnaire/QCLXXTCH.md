# questionnaire.QCLXXTCH

> Tamizaje de Chagas

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Tamizaje de Chagas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Vivió ó trabajó Ud. en algún pais latinoamericano ... |
| Q02 | varchar |  |  | SI | Vivió ó trabajó su madre o abuela en pais latinoam... |
| Q03 | varchar |  |  | SI | Habitó Ud. alguna vez en algún lugar donde vió vin... |
| Q04 | varchar |  |  | SI | Fué Ud. alguna vez picada por vinchuca? |
| Q05 | varchar |  |  | SI | Ha recibido tranfusiones de sangre en Chile antes ... |
| Q06 | varchar |  |  | SI | Ha sido alguna vez diagnosticada de problemas card... |
| Q07 | varchar |  |  | SI | Ha sido alguna vez diagnosticada de problemas inte... |
| Q08 | varchar |  |  | SI | Ha tenido abortos, pérdidas, hijos prematuros?(***... |
| Q09 | varchar |  |  | SI | Sabe Ud. si es hija, hermana ó nieta de mujer con ... |
| Q10 | varchar |  |  | SI | Sabe Ud. si tiene algún otro familiar (padre, tíos... |
| Q11 | varchar |  |  | SI | Observación 01 |
| Q12 | varchar |  |  | SI | Observación 02 |
| Q13 | varchar |  |  | SI | Observación 03 |
| Q14 | varchar |  |  | SI | Observación 04 |
| Q15 | varchar |  |  | SI | Observación 05 |
| Q16 | varchar |  |  | SI | Observación 06 |
| Q17 | varchar |  |  | SI | Observación 07 |
| Q18 | varchar |  |  | SI | Observación 08 |
| Q19 | varchar |  |  | SI | Observación 09 |
| Q20 | varchar |  |  | SI | Observación 10 |
| Q21 | varchar |  |  | SI | Profesional |
| Q22 | varchar |  |  | SI | (*): Bloqueos, arritmias, angina de esfuerzo que s... |
| Q23 | varchar |  |  | SI | (**): Megacolon, constipación, megaesófago u otra ... |
| Q24 | varchar |  |  | SI | (***): Este criterio por si solo no debe considera... |
| Q25 | varchar |  |  | SI | que ha vivido en zona endémica. |
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