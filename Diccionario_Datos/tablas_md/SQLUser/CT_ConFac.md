# SQLUser.CT_ConFac

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCF_RowID | bigint | PK |  | NO | - |
| CTCF_ActiveFlag | varchar |  |  | NO | Record In Use |
| CTCF_Code | varchar |  |  | SI | Code |
| CTCF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTCF_CreatedDate | date |  |  | SI | Created Date |
| CTCF_CreatedTime | time |  |  | SI | Created Time |
| CTCF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTCF_Factor | double |  |  | NO | Conversion Factor |
| CTCF_FrUOM_DR | bigint |  | FK | NO | Des Ref to CTUOM |
| CTCF_Owner | varchar |  |  | SI | Owner |
| CTCF_System | varchar |  |  | SI | System created |
| CTCF_ToUOM_DR | bigint |  | FK | NO | Des Ref to CTUOM |
| CTCF_UpdatedDate | date |  |  | SI | Updated Date |
| CTCF_UpdatedTime | time |  |  | SI | Updated Time |
| CTCF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. ¿Como  diría  que  es  su  visión  hoy?  excele... |
| Q02 | - |  |  | SI | 2. ¿Con qué frecuencia su vista es una preocupació... |
| Q03 | - |  |  | SI | 3. ¿Cuánto  dolor  o  molestias  ha  tenido  en  l... |
| Q04 | - |  |  | SI | Dificultad con actividades |
| Q05 | - |  |  | SI | Las siguientes preguntas tratan sobre el grado de ... |
| Q06 | - |  |  | SI | 4. ¿Qué grado  de  dificultad  tiene  usted  para ... |
| Q07 | - |  |  | SI | 5. ¿Qué grado de dificultad tiene para realizar tr... |
| Q08 | - |  |  | SI | 6. A causa de su vista, ¿Qué grado de dificultadti... |
| Q09 | - |  |  | SI | 7. A causa de su vista, ¿Qué grado de dificultad t... |
| Q10 | - |  |  | SI | 8. A causa de su vista, ¿Qué grado de dificultad t... |
| Q11 | - |  |  | SI | 9. A causa de su vista, ¿Qué grado de dificultad t... |
| Q12 | - |  |  | SI | 10. A causa de su vista, ¿Qué grado de dificultad ... |
| Q13 | - |  |  | SI | 11. A causa de su vista, ¿cuánta dificultad tiene ... |
| Q14 | - |  |  | SI | 12. A causa de su vista, ¿Cuánta dificultad tiene ... |
| Q15 | - |  |  | SI | 13. A causa de su vista, ¿cuánta dificultad tiene ... |
| Q16 | - |  |  | SI | 14. Ahora quisiera hacerle unas preguntas sobre co... |
| Q17 | - |  |  | SI | 14.A ¿Es porque nunca ha manejado un auto, o porqu... |
| Q18 | - |  |  | SI | 14.B Si ha dejado de conducir, pregunte: ¿Fue prin... |
| Q19 | - |  |  | SI | 14.C ¿Cuánta dificultad tiene usted para manejar d... |
| Q20 | - |  |  | SI | 14.D ¿Qué grado de dificultad tiene usted para man... |
| Q21 | - |  |  | SI | Respuestas a los problemas de la visión |
| Q22 | - |  |  | SI | Las siguientes preguntas tratan sobre cómo puede v... |
| Q23 | - |  |  | SI | 15. ¿Logra menos cosas de lo que le gustaría a cau... |
| Q24 | - |  |  | SI | 16. ¿Sus problemas de vista limitan su tiempo de t... |
| Q25 | - |  |  | SI | 17. ¿Qué tan seguido el dolor o molestias en los o... |
| Q26 | - |  |  | SI | Indique su grado de acuerdo o desacuerdo sobre las... |
| Q27 | - |  |  | SI | 18. Me quedo en casa la mayor parte del tiempo a c... |
| Q28 | - |  |  | SI | 19. Me siento frustrado/a gran parte del tiempo a ... |
| Q29 | - |  |  | SI | 20. Tengo mucho menos control sobre lo que hago ac... |
| Q30 | - |  |  | SI | 21. A causa de mi vista, tengo que confiar demasia... |
| Q31 | - |  |  | SI | 22. Necesito mucha ayuda de otras personas a causa... |
| Q32 | - |  |  | SI | 23. Me preocupa hacer cosas que puedan avergonzarm... |
| Q33 | - |  |  | SI | Fecha Evaluación |
| Q34 | - |  |  | SI | Resultado Porcentual (%) |
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