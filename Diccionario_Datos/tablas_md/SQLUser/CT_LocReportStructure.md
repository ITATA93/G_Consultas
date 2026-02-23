# SQLUser.CT_LocReportStructure

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REPSTR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Religión |
| Q02 | - |  |  | SI | Consumo de Alcohol |
| Q03 | - |  |  | SI | Tiempo Consumo Alcohol |
| Q04 | - |  |  | SI | Tabaquismo |
| Q05 | - |  |  | SI | Cigarrillos por día |
| Q06 | - |  |  | SI | Años de Consumo |
| Q07 | - |  |  | SI | Paquete Cigarrillos/Año |
| Q08 | - |  |  | SI | Consumo de Drogas |
| Q09 | - |  |  | SI | Otra Droga |
| Q10 | - |  |  | SI | Discapacidad Física/Cognitiva (Vulnerabilidad) |
| Q11 | - |  |  | SI | Nivel de Dependencia |
| Q12 | - |  |  | SI | Nivel Educacional |
| Q13 | - |  |  | SI | Forma de Comunicación |
| Q14 | - |  |  | SI | Otra Forma de Comunicación |
| Q15 | - |  |  | SI | Necesita Intérprete |
| Q16 | - |  |  | SI | Comentarios NI |
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
| REPSTR_Code | varchar |  |  | NO | Code |
| REPSTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REPSTR_CreatedDate | date |  |  | SI | Created Date |
| REPSTR_CreatedTime | time |  |  | SI | Created Time |
| REPSTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REPSTR_DateFrom | date |  |  | SI | DateFrom |
| REPSTR_DateTo | date |  |  | SI | DateTo |
| REPSTR_Desc | varchar |  |  | NO | Description |
| REPSTR_Owner | varchar |  |  | SI | Owner |
| REPSTR_Text1 | varchar |  |  | SI | Text1 |
| REPSTR_UpdatedDate | date |  |  | SI | Updated Date |
| REPSTR_UpdatedTime | time |  |  | SI | Updated Time |
| REPSTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*