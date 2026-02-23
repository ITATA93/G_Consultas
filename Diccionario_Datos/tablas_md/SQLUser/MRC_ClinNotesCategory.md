# SQLUser.MRC_ClinNotesCategory

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLNOTCAT_RowId | bigint | PK |  | NO | - |
| CLNOTCAT_Code | varchar |  |  | NO | Code |
| CLNOTCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLNOTCAT_CreatedDate | date |  |  | SI | Created Date |
| CLNOTCAT_CreatedTime | time |  |  | SI | Created Time |
| CLNOTCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLNOTCAT_DateFrom | date |  |  | SI | Date From |
| CLNOTCAT_DateTo | date |  |  | SI | Date To |
| CLNOTCAT_Desc | varchar |  |  | NO | Description |
| CLNOTCAT_Owner | varchar |  |  | SI | Owner |
| CLNOTCAT_UpdatedDate | date |  |  | SI | Updated Date |
| CLNOTCAT_UpdatedTime | time |  |  | SI | Updated Time |
| CLNOTCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CQ1 | - |  |  | SI | (null) |
| CQ10 | - |  |  | SI | (null) |
| CQ2 | - |  |  | SI | (null) |
| CQ3 | - |  |  | SI | (null) |
| CQ4 | - |  |  | SI | (null) |
| CQ5 | - |  |  | SI | (null) |
| CQ6 | - |  |  | SI | (null) |
| CQ7 | - |  |  | SI | (null) |
| CQ8 | - |  |  | SI | (null) |
| CQ9 | - |  |  | SI | (null) |
| CQEV | - |  |  | SI | (null) |
| CQTEV | - |  |  | SI | (null) |
| Q1 | - |  |  | SI | ¿Ha sido capaz de reírse y ver el lado divertido d... |
| Q10 | - |  |  | SI | ¿Se le ha ocurrido la idea de hacerse daño? |
| Q13 | - |  |  | SI | Condición |
| Q14 | - |  |  | SI | Resultado de la Evaluación |
| Q14ObsDR | - |  |  | SI | Resultado de la Evaluación DR |
| Q17 | - |  |  | SI | ¿Se deriva a programa de Salud Mental? |
| Q18 | - |  |  | SI | 0-12: Normal |
| Q19 | - |  |  | SI | 13 o más: Probablilidad de depresión |
| Q2 | - |  |  | SI | ¿Ha disfrutado mirar hacia delante? |
| Q20 | - |  |  | SI | Puérpera |
| Q21 | - |  |  | SI | 0-10: Normal |
| Q22 | - |  |  | SI | 11 o más: Probabilidad de depresión |
| Q23 | - |  |  | SI | ¿Se deriva a programa de Salud Mental? old |
| Q24 | - |  |  | SI | Gestante |
| Q3 | - |  |  | SI | ¿Cuándo las cosas le han salido mal se ha culpado ... |
| Q4 | - |  |  | SI | ¿Ha estado nerviosa o inquieta sin tener motivo? |
| Q5 | - |  |  | SI | ¿Ha sentido miedo o ha estado asustada sin motivo? |
| Q6 | - |  |  | SI | ¿Las cosas le han estado abrumando o agobiando? |
| Q7 | - |  |  | SI | ¿Se ha sentido tan desdichada que ha tenido dificu... |
| Q8 | - |  |  | SI | ¿Se ha sentido triste o desgraciada? |
| Q9 | - |  |  | SI | ¿Se ha sentido tan desdichada que ha estado lloran... |
| QEV | - |  |  | SI | Tipo de Evaluación |
| QTEV | - |  |  | SI | Tipo de Evaluación |
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
| Qder | - |  |  | SI | Derivación inmediata a Médico |
| Qqr | - |  |  | SI | Resultado Edimburgo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*