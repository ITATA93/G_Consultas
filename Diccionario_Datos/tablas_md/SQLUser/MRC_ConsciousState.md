# SQLUser.MRC_ConsciousState

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONST_RowId | bigint | PK |  | NO | - |
| CONST_Code | varchar |  |  | NO | Code |
| CONST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONST_CreatedDate | date |  |  | SI | Created Date |
| CONST_CreatedTime | time |  |  | SI | Created Time |
| CONST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONST_DateFrom | date |  |  | SI | Date From |
| CONST_DateTo | date |  |  | SI | Date To |
| CONST_Desc | varchar |  |  | NO | Description |
| CONST_Owner | varchar |  |  | SI | Owner |
| CONST_UpdatedDate | date |  |  | SI | Updated Date |
| CONST_UpdatedTime | time |  |  | SI | Updated Time |
| CONST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | KCAL Total |
| Q02 | - |  |  | SI | Peso |
| Q02ObsDR | - |  |  | SI | Peso DR |
| Q03 | - |  |  | SI | Proteínas % Molécula Calórica |
| Q04 | - |  |  | SI | Carbohidratos % Molécula Calórica |
| Q05 | - |  |  | SI | Lípidos % Molécula Calórica |
| Q06 | - |  |  | SI | Proteínas Gramos / Día |
| Q07 | - |  |  | SI | Carbohidratos Gramos / Día |
| Q08 | - |  |  | SI | Lípidos Gramos / Día |
| Q09 | - |  |  | SI | Proteína GR. Por Kg de Peso |
| Q10 | - |  |  | SI | Carbohidratos GR. Por Kg de Peso |
| Q11 | - |  |  | SI | Lípidos GR. Por Kg de Peso |
| Q12 | - |  |  | SI | Proteínas Gramos / Día (A) |
| Q13 | - |  |  | SI | Proteínas % Molécula Calórica (A) |
| Q14 | - |  |  | SI | Proteína GR. Por Kg de Peso (A) |
| Q15 | - |  |  | SI | Carbohidratos Gramos / Día (A) |
| Q16 | - |  |  | SI | Carbohidratos % Molécula Calórica (A) |
| Q17 | - |  |  | SI | Carbohidratos GR. Por Kg de Peso (A) |
| Q18 | - |  |  | SI | Lípidos Gramos / Día (A) |
| Q19 | - |  |  | SI | Lípidos % Molécula Calórica (A) |
| Q20 | - |  |  | SI | Lípidos GR. Por kg de peso |
| Q21 | - |  |  | SI | Proteínas % |
| Q22 | - |  |  | SI | Carbohidratos % |
| Q23 | - |  |  | SI | Lípidos % |
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