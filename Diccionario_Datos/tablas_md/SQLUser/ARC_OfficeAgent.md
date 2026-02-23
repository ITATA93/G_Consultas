# SQLUser.ARC_OfficeAgent

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AGN_RowId | bigint | PK |  | NO | - |
| AGN_Code | varchar |  |  | NO | Code |
| AGN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AGN_CreatedDate | date |  |  | SI | Created Date |
| AGN_CreatedTime | time |  |  | SI | Created Time |
| AGN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AGN_Desc | varchar |  |  | NO | description |
| AGN_Owner | varchar |  |  | SI | Owner |
| AGN_UpdatedDate | date |  |  | SI | Updated Date |
| AGN_UpdatedTime | time |  |  | SI | Updated Time |
| AGN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. ¿Vive solo? |
| Q02 | - |  |  | SI | 2. ¿Se encuentra sin nadie a quien acudir si preci... |
| Q03 | - |  |  | SI | 3. ¿Necesita de alguien que le ayude a menudo? |
| Q04 | - |  |  | SI | 4. ¿Hay más de 2 días a la semana que no come cali... |
| Q05 | - |  |  | SI | 5. ¿Le impide su salud salir a la calle? |
| Q06 | - |  |  | SI | 6. ¿Tiene a menudo problemas de salud que le impid... |
| Q07 | - |  |  | SI | 7. ¿Tiene dificultades con la vista para realizar ... |
| Q08 | - |  |  | SI | 8. ¿Le supone mucha dificultad la conversación por... |
| Q09 | - |  |  | SI | 9. ¿Ha estado ingresado en el hospital en el últim... |
| Q10 | - |  |  | SI | Puntaje |
| Q11 | - |  |  | SI | Resultado |
| Q12 | - |  |  | SI | = 0 |
| Q13 | - |  |  | SI | >= 1 |
| Q14 | - |  |  | SI | Negativo |
| Q15 | - |  |  | SI | Positivo |
| Q16 | - |  |  | SI | Se considera positivo si contesta afirmativamente ... |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*