# SQLUser.ARC_ItemPayorCode

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PCODE_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| PCODE_Childsub | double |  |  | NO | Childsub |
| PCODE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PCODE_CreatedDate | date |  |  | SI | Created Date |
| PCODE_CreatedTime | time |  |  | SI | Created Time |
| PCODE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PCODE_DateFrom | date |  |  | SI | DateFrom |
| PCODE_DateTo | date |  |  | SI | DateTo |
| PCODE_InsType_DR | bigint |  | FK | SI | Des Ref ARCInsuranceType |
| PCODE_PayorCode | varchar |  |  | SI | Payor Code |
| PCODE_RowId | varchar |  |  | NO | - |
| PCODE_UpdatedDate | date |  |  | SI | Updated Date |
| PCODE_UpdatedTime | time |  |  | SI | Updated Time |
| PCODE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q103 | - |  |  | SI | Otra Religión |
| Q220 | - |  |  | SI | Profesional de Salud |
| Q25 | - |  |  | SI | Religión |
| Q26 | - |  |  | SI | Consumo de Alcohol |
| Q27 | - |  |  | SI | Tiempo Consumo Alcohol |
| Q28 | - |  |  | SI | Tabaquismo |
| Q29 | - |  |  | SI | N° Cigarrillos por Día |
| Q30 | - |  |  | SI | N° de años de Consumo |
| Q31 | - |  |  | SI | Paquete Cigarrillos/Año |
| Q32 | - |  |  | SI | Consumo de Droga |
| Q33 | - |  |  | SI | Otra Droga |
| Q34 | - |  |  | SI | Tiempo de Consumo Drogas |
| Q35 | - |  |  | SI | Discapacidad Física/Cognitiva (Vulnerabilidad) |
| Q36 | - |  |  | SI | Nivel de Dependencia |
| Q37 | - |  |  | SI | Nivel Educacional |
| Q38 | - |  |  | SI | Forma  de Comunicación |
| Q39 | - |  |  | SI | Otra Forma de Comunicación |
| Q40 | - |  |  | SI | Necesita Intérprete |
| Q41 | - |  |  | SI | Comentario Necesita Intérprete |
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