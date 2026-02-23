# questionnaire.QCLXXFAOS

> Cuestionario FAOS (Pie y Tobillo)

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cuestionario FAOS (Pie y Tobillo)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Durante la última semana, ¿cómo de rígido ha es... |
| Q02 | varchar |  |  | SI | 2. Durante la última semana, ¿cómo de hinchado ha ... |
| Q03 | varchar |  |  | SI | 3. ¿Caminar sobre superficies desniveladas? |
| Q04 | varchar |  |  | SI | 4. ¿Caminar sobre superficies planas? |
| Q05 | varchar |  |  | SI | 5. ¿Estando tumbado/a en la cama de noche? |
| Q06 | varchar |  |  | SI | 6. ¿Subir o bajar escaleras? |
| Q07 | varchar |  |  | SI | 7. Actividad fuerte; ¿trabajo físico pesado, esqui... |
| Q08 | varchar |  |  | SI | 8. Actividad moderada; ¿trabajo físico moderado, f... |
| Q09 | varchar |  |  | SI | 9. Actividad leve, ¿caminar, tareas de la casa, tr... |
| Q10 | varchar |  |  | SI | 10. ¿Cuál de las siguientes afirmaciones es la que... |
| Q11 | varchar |  |  | SI | 11. ¿Cuánta dificultad tuviste para mantener el eq... |
| Q12 | varchar |  |  | SI | 12. ¿Cuánta dificultad tuviste en la última semana... |
| Q13 | varchar |  |  | SI | 13. Actividad fuerte; ¿trabajo físico pesado, esqu... |
| Q14 | varchar |  |  | SI | 14.&nbsp;Actividad moderada; ¿trabajo físico moder... |
| Q15 | varchar |  |  | SI | 15. Actividad leve, ¿caminar, tareas de la casa, t... |
| Q16 | varchar |  |  | SI | 16.&nbsp;Permanecer de pie durante una hora |
| Q17 | varchar |  |  | SI | 17.&nbsp;Permanecer de pie durante unos minutos |
| Q18 | varchar |  |  | SI | 18. ¿Cuánta dificultad tienes para caminar sobre s... |
| Q19 | varchar |  |  | SI | 19. Cualquier zapato de mujer (incluyendo tacones ... |
| Q20 | varchar |  |  | SI | 20. La mayoría de los zapatos de vestir de mujer (... |
| Q21 | varchar |  |  | SI | 21. Zapatillas deportivas, de paseo o calzado info... |
| Q22 | varchar |  |  | SI | 22.&nbsp;Zapatos ortopédicos o de prescripción méd... |
| Q23 | varchar |  |  | SI | 23.&nbsp;Todos los zapatos |
| Q24 | varchar |  |  | SI | 24.&nbsp;¿Cuánto ha interferido tu problema de pie... |
| Q25 | varchar |  |  | SI | 25. ¿Cuánto interfiere tu problema de pie o tobill... |
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