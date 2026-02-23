# SQLUser.ORC_IVAntibioticDuringDelivery

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IVANDU_RowId | bigint | PK |  | NO | - |
| IVANDU_Code | varchar |  |  | NO | Code |
| IVANDU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| IVANDU_CreatedDate | date |  |  | SI | Created Date |
| IVANDU_CreatedTime | time |  |  | SI | Created Time |
| IVANDU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IVANDU_DateFrom | date |  |  | SI | Date From |
| IVANDU_DateTo | date |  |  | SI | Date To |
| IVANDU_Desc | varchar |  |  | NO | Description |
| IVANDU_Owner | varchar |  |  | SI | Owner |
| IVANDU_UpdatedDate | date |  |  | SI | Updated Date |
| IVANDU_UpdatedTime | time |  |  | SI | Updated Time |
| IVANDU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Se le pide al paciente que responda cada pregunta ... |
| Q04 | - |  |  | SI | Las preguntas están diseñadas para incorporar impa... |
| Q05 | - |  |  | SI | FI1. ¿Cúando usted mira hacia arriba se siente más... |
| Q06 | - |  |  | SI | E2. ¿Debido a su problema o, mareo ¿se siente como... |
| Q07 | - |  |  | SI | F3. ¿Debido a su mareo o problema ¿evita hacer via... |
| Q08 | - |  |  | SI | FI4. Cuando camina por los pasillos de un supermer... |
| Q09 | - |  |  | SI | F5. ¿A causa de su problema, o del mareo le cuesta... |
| Q10 | - |  |  | SI | F6. ¿Debido a su problema o el mareo, trata de par... |
| Q11 | - |  |  | SI | F7. ¿A causa de su problema o mareo le cuesta leer... |
| Q12 | - |  |  | SI | FI8. ¿Al tener que realizar actividades más exigen... |
| Q13 | - |  |  | SI | E9. ¿Debido a su problema o por el mareo tiene mie... |
| Q14 | - |  |  | SI | E10. ¿A causa de su problema o mareo se siente inc... |
| Q15 | - |  |  | SI | FI11. ¿Al hacer movimientos rápidos de su cabeza n... |
| Q16 | - |  |  | SI | F12. ¿Debido a su problema o mareo evita las altur... |
| Q17 | - |  |  | SI | FI13. ¿Al darse vuelta en la cama siente que aumen... |
| Q18 | - |  |  | SI | F14. ¿Debido a su problema o mareo le cuesta hacer... |
| Q19 | - |  |  | SI | E15. ¿Debido a su problema o mareo se avergüenza a... |
| Q20 | - |  |  | SI | F16. ¿A consecuencias de su problema o mareo le cu... |
| Q21 | - |  |  | SI | FI17. ¿Al bajar de la vereda a la calle o calzada ... |
| Q22 | - |  |  | SI | E18. ¿Debido a su problema o mareo le cuesta conce... |
| Q23 | - |  |  | SI | F19. ¿Debido a su problema o mareo le cuesta camin... |
| Q24 | - |  |  | SI | E20. ¿A consecuencias de su problema o mareo tiene... |
| Q25 | - |  |  | SI | E21. ¿Debido a su problema o mareo se siente incap... |
| Q26 | - |  |  | SI | E22. ¿A consecuencias de su problema o mareo ha te... |
| Q27 | - |  |  | SI | E23. ¿Debido a su problema o mareo se encuentra qu... |
| Q28 | - |  |  | SI | F24. ¿El problema que usted tiene o el mareo que s... |
| Q29 | - |  |  | SI | FI25. ¿Al agacharse o inclinarse hacia delante com... |
| Q30 | - |  |  | SI | Comentarios |
| Q31 | - |  |  | SI | Total Puntaje Funcional (F) |
| Q32 | - |  |  | SI | /36 |
| Q33 | - |  |  | SI | Total Puntaje Emocional (E) |
| Q34 | - |  |  | SI | /36 |
| Q35 | - |  |  | SI | Total Puntaje Fisico (FI) |
| Q36 | - |  |  | SI | /28 |
| Q37 | - |  |  | SI | Total |
| Q38 | - |  |  | SI | /100 |
| Q39 | - |  |  | SI | Cuanto mayor sea la puntuación, mayor será la disc... |
| Q40 | - |  |  | SI | Total |
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