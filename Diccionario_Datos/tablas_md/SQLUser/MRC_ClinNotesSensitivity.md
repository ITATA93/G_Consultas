# SQLUser.MRC_ClinNotesSensitivity

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CNS_RowId | bigint | PK |  | NO | - |
| CNS_Code | varchar |  |  | NO | Code |
| CNS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CNS_CreatedDate | date |  |  | SI | Created Date |
| CNS_CreatedTime | time |  |  | SI | Created Time |
| CNS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CNS_DateFrom | date |  |  | SI | DateFrom |
| CNS_DateTo | date |  |  | SI | DateTo |
| CNS_Desc | varchar |  |  | NO | Description |
| CNS_Owner | varchar |  |  | SI | Owner |
| CNS_UpdatedDate | date |  |  | SI | Updated Date |
| CNS_UpdatedTime | time |  |  | SI | Updated Time |
| CNS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CQ11 | - |  |  | SI | (null) |
| Q11 | - |  |  | SI | Hay algún otro factor que deba ser considerado |
| Q12 | - |  |  | SI | ¿Ha pensado en interrumpir la gestación? o ¿Prefer... |
| Q13 | - |  |  | SI | Marque SI, si pensó en interrumpir o aún se siente... |
| Q14 | - |  |  | SI | (pareja, familia u otro que acompañe en el proceso... |
| Q15 | - |  |  | SI | ¿Se siente insatisfecha con el apoyo recibido de l... |
| Q16 | - |  |  | SI | Marque SI, si se siente insatisfecha |
| Q17 | - |  |  | SI | a. ¿Se ha sentido cansada(o) o decaída(o) casi tod... |
| Q18 | - |  |  | SI | b. ¿Se ha sentido triste o deprimida(o) o pesimist... |
| Q19 | - |  |  | SI | c. ¿Siente que ya no disfruta o ha perdido interés... |
| Q20 | - |  |  | SI | Marque SI, s i una o más respuestas son afirmativa... |
| Q21 | - |  |  | SI | ¿Ha consumido durante este embarazo alguna de esta... |
| Q22 | - |  |  | SI | a) Cigarrillo |
| Q23 | - |  |  | SI | b) Cerveza, vino, trago fuerte u otras bebidas con... |
| Q24 | - |  |  | SI | c) Tranquilizante sin receta médica |
| Q25 | - |  |  | SI | d) Marihuana, coca, pasta base, anfetamina u otra ... |
| Q26 | - |  |  | SI | Marque SI, si ha consumido cualquiera de estas sus... |
| Q27 | - |  |  | SI | a. ¿Alguien la ha insultado, humillado o amenazado... |
| Q28 | - |  |  | SI | b. ¿Alguien la ha golpeado o empujado? VIOLENCIA F... |
| Q29 | - |  |  | SI | c. ¿Este embarazo es consecuencia de una relación ... |
| Q30 | - |  |  | SI | Marque SI, si le ha sucedido cualquiera de estas m... |
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
| Qa1 | - |  |  | SI | Ingreso posterior a las 20 semanas |
| Qa2 | - |  |  | SI | Escolaridad <= 6º básico |
| Qa3 | - |  |  | SI | Edad <= a 17 años |
| Qps1 | - |  |  | SI | Rechazo al embarazo |
| Qps2 | - |  |  | SI | Insuficiente apoyo social familiar |
| Qps3 | - |  |  | SI | Síntomas depresivos |
| Qps4 | - |  |  | SI | Uso o abuso de sustancias |
| Qps5 | - |  |  | SI | Violencia de género - pareja o una figura masculin... |
| Qps6 | - |  |  | SI | Describa |
| Qqr | - |  |  | SI | Riesgo Psicosocial Abreviado |
| QqrObsDR | - |  |  | SI | Riesgo Psicosocial Abreviado DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*