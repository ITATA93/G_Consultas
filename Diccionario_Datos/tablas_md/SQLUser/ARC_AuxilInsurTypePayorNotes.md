# SQLUser.ARC_AuxilInsurTypePayorNotes

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLANNOTE_ParRef | bigint | PK |  | NO | ARC_AuxilInsurType Parent Reference |
| PLANNOTE_Childsub | double |  |  | NO | Childsub |
| PLANNOTE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLANNOTE_CreatedDate | date |  |  | SI | Created Date |
| PLANNOTE_CreatedTime | time |  |  | SI | Created Time |
| PLANNOTE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLANNOTE_DateFrom | date |  |  | SI | Date From |
| PLANNOTE_DateTo | date |  |  | SI | Date To |
| PLANNOTE_PayorNotes_DR | bigint |  | FK | NO | Plan Notes |
| PLANNOTE_RowId | varchar |  |  | NO | - |
| PLANNOTE_UpdatedDate | date |  |  | SI | Updated Date |
| PLANNOTE_UpdatedTime | time |  |  | SI | Updated Time |
| PLANNOTE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha de Evaluación |
| Q02 | - |  |  | SI | Hora de Evaluación |
| Q03 | - |  |  | SI | 1. ¿Has sentido como si la gente te lanzara indire... |
| Q04 | - |  |  | SI | 1. ¿Has sentido como si la gente te lanzara indire... |
| Q05 | - |  |  | SI | 2. ¿Has sentido como si algunas personas no son lo... |
| Q06 | - |  |  | SI | 2. ¿Has sentido como si algunas personas no son lo... |
| Q07 | - |  |  | SI | 3. ¿Has sentido como que te persiguen de alguna ma... |
| Q08 | - |  |  | SI | 3. ¿Has sentido como que te persiguen de alguna ma... |
| Q09 | - |  |  | SI | 4.¿Has sentido como si hubiera una conspiración en... |
| Q10 | - |  |  | SI | 4. ¿Has sentido como si hubiera una conspiración e... |
| Q11 | - |  |  | SI | 5.¿Has sentido que la gente te mira extraño debido... |
| Q12 | - |  |  | SI | 5. ¿Has sentido que la gente te mira extraño debid... |
| Q13 | - |  |  | SI | 6. ¿Has sentido que ciertos artefactos electrónico... |
| Q14 | - |  |  | SI | 6. ¿Has sentido que ciertos artefactos electrónico... |
| Q15 | - |  |  | SI | 7. ¿Has sentido como si te estuvieran sacando los ... |
| Q16 | - |  |  | SI | 7. ¿Has sentido como si te estuvieran sacando los ... |
| Q17 | - |  |  | SI | 8.¿Has sentido como si tus pensamientos no fueran ... |
| Q18 | - |  |  | SI | 8. ¿Has sentido como si tus pensamientos no fueran... |
| Q19 | - |  |  | SI | 9. ¿Has tenido pensamientos tan intensos que te pr... |
| Q20 | - |  |  | SI | 9. ¿Has tenido pensamientos tan intensos que te pr... |
| Q21 | - |  |  | SI | 10. ¿Sientes como si tus pensamientos se repitiera... |
| Q22 | - |  |  | SI | 10. ¿Sientes como si tus pensamientos se repitiera... |
| Q23 | - |  |  | SI | 11. ¿Has sentido como si estuvieras bajo el contro... |
| Q24 | - |  |  | SI | 11. ¿Has sentido como si estuvieras bajo el contro... |
| Q25 | - |  |  | SI | 12. ¿Has sentido como si un doble hubiera tomado e... |
| Q26 | - |  |  | SI | 12. ¿Has sentido como si un doble hubiera tomado e... |
| Q27 | - |  |  | SI | 13.¿Has escuchado voces cuando estas solo? |
| Q28 | - |  |  | SI | 13. ¿Has escuchado voces cuando estas solo? Cuánto... |
| Q29 | - |  |  | SI | 14. ¿Has escuchado voces hablando entre sí cuando ... |
| Q30 | - |  |  | SI | 14. ¿Has escuchado voces hablando entre sí cuando ... |
| Q31 | - |  |  | SI | 15. ¿Has vistos objetos, personas o animales que o... |
| Q32 | - |  |  | SI | 15. ¿Has vistos objetos, personas o animales que o... |
| Q33 | - |  |  | SI | Promedio de Frecuencia |
| Q34 | - |  |  | SI | Promedio de Estrés |
| Q35 | - |  |  | SI | Deberá realizarse derivación a Especialidad para e... |
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