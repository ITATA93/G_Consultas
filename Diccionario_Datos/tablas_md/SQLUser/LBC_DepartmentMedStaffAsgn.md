# SQLUser.LBC_DepartmentMedStaffAsgn

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDEPMSA_ParRef | bigint | PK |  | NO | Parent Reference to LBCDepartment |
| LBCDEPMSA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDEPMSA_CreatedDate | date |  |  | SI | Created Date |
| LBCDEPMSA_CreatedTime | time |  |  | SI | Created Time |
| LBCDEPMSA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCDEPMSA_DateFrom | date |  |  | SI | Date From |
| LBCDEPMSA_DateTo | date |  |  | SI | Date To |
| LBCDEPMSA_LabContactPhone | varchar |  |  | SI | Lab Contact Phone |
| LBCDEPMSA_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCDEPMSA_RowID | varchar |  |  | NO | - |
| LBCDEPMSA_Sequence | numeric |  |  | SI | Sequence |
| LBCDEPMSA_UpdatedDate | date |  |  | SI | Updated Date |
| LBCDEPMSA_UpdatedTime | time |  |  | SI | Updated Time |
| LBCDEPMSA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCDEPMSA_UserCareProv_DR | bigint |  | FK | SI | Care Provider |
| Q02 | - |  |  | SI | 1. Tener poco interés o placer en hacer las cosas |
| Q03 | - |  |  | SI | 2. Sentirse desanimado/a, deprimido/a, o sin esper... |
| Q04 | - |  |  | SI | 3. Con problemas en dormirse o en mantenerse dormi... |
| Q05 | - |  |  | SI | 4. Sentirse cansado/a o tener poca energía |
| Q06 | - |  |  | SI | 5. Tener poco apetito o comer en exceso |
| Q07 | - |  |  | SI | 6. Sentir falta de amor propio - o que sea un frac... |
| Q08 | - |  |  | SI | 7. Tener dificultad para concentrarse en cosas tal... |
| Q09 | - |  |  | SI | 8. Se mueve o habla tan lentamente que otra gente ... |
| Q1 | - |  |  | SI | Resultado PHQ9 |
| Q10 | - |  |  | SI | 9. Se le han ocurrido pensamientos de que sería me... |
| Q11 | - |  |  | SI | Si usted se identificó con cualquier problema en e... |
| Q12 | - |  |  | SI | Resultado de Planificación |
| Q13 | - |  |  | SI | La puntuación indica que, probablemente, el pacien... |
| Q14 | - |  |  | SI | El médico debe utilizar su juicio clínico sobre el... |
| Q15 | - |  |  | SI | Se justifica el tratamiento de la depresión con an... |
| Q16 | - |  |  | SI | La pregunta 9 tiene un valor mayor a 0, independie... |
| Q17 | - |  |  | SI | Resultado |
| Q1ObsDR | - |  |  | SI | Resultado PHQ9 DR |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*