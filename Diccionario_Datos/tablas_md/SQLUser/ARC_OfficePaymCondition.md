# SQLUser.ARC_OfficePaymCondition

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OFPC_RowId | bigint | PK |  | NO | - |
| OFPC_Code | varchar |  |  | NO | Code |
| OFPC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OFPC_CreatedDate | date |  |  | SI | Created Date |
| OFPC_CreatedTime | time |  |  | SI | Created Time |
| OFPC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OFPC_Desc | varchar |  |  | NO | Description |
| OFPC_Owner | varchar |  |  | SI | Owner |
| OFPC_UpdatedDate | date |  |  | SI | Updated Date |
| OFPC_UpdatedTime | time |  |  | SI | Updated Time |
| OFPC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. Durante la última semana, ¿cómo de rígido ha es... |
| Q02 | - |  |  | SI | 2. Durante la última semana, ¿cómo de hinchado ha ... |
| Q03 | - |  |  | SI | 3. ¿Caminar sobre superficies desniveladas? |
| Q04 | - |  |  | SI | 4. ¿Caminar sobre superficies planas? |
| Q05 | - |  |  | SI | 5. ¿Estando tumbado/a en la cama de noche? |
| Q06 | - |  |  | SI | 6. ¿Subir o bajar escaleras? |
| Q07 | - |  |  | SI | 7. Actividad fuerte |
| Q08 | - |  |  | SI | 8. Actividad moderada |
| Q09 | - |  |  | SI | 9. Actividad leve, ¿caminar, tareas de la casa, tr... |
| Q10 | - |  |  | SI | 10. ¿Cuál de las siguientes afirmaciones es la que... |
| Q11 | - |  |  | SI | 11. ¿Cuánta dificultad tuviste para mantener el eq... |
| Q12 | - |  |  | SI | 12. ¿Cuánta dificultad tuviste en la última semana... |
| Q13 | - |  |  | SI | 13. Actividad fuerte |
| Q14 | - |  |  | SI | 14.&nbsp |
| Q15 | - |  |  | SI | 15. Actividad leve, ¿caminar, tareas de la casa, t... |
| Q16 | - |  |  | SI | 16.&nbsp |
| Q17 | - |  |  | SI | 17.&nbsp |
| Q18 | - |  |  | SI | 18. ¿Cuánta dificultad tienes para caminar sobre s... |
| Q19 | - |  |  | SI | 19. Cualquier zapato de mujer (incluyendo tacones ... |
| Q20 | - |  |  | SI | 20. La mayoría de los zapatos de vestir de mujer (... |
| Q21 | - |  |  | SI | 21. Zapatillas deportivas, de paseo o calzado info... |
| Q22 | - |  |  | SI | 22.&nbsp |
| Q23 | - |  |  | SI | 23.&nbsp |
| Q24 | - |  |  | SI | 24.&nbsp |
| Q25 | - |  |  | SI | 25. ¿Cuánto interfiere tu problema de pie o tobill... |
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