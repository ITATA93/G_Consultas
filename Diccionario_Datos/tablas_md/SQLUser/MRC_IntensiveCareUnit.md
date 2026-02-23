# SQLUser.MRC_IntensiveCareUnit

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICU_RowId | bigint | PK |  | NO | - |
| ICU_Code | varchar |  |  | NO | Code |
| ICU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ICU_CreatedDate | date |  |  | SI | Created Date |
| ICU_CreatedTime | time |  |  | SI | Created Time |
| ICU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ICU_Desc | varchar |  |  | NO | Description |
| ICU_InterfaceName | varchar |  |  | SI | Interface Name |
| ICU_NumericValueOnly | varchar |  |  | SI | Numeric Value Only |
| ICU_Owner | varchar |  |  | SI | Owner |
| ICU_UpdatedDate | date |  |  | SI | Updated Date |
| ICU_UpdatedTime | time |  |  | SI | Updated Time |
| ICU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ICU_YAxisName | varchar |  |  | SI | Y Axis Name on Graph |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Nombres del Recién Nacido (RN) |
| Q04 | - |  |  | SI | Apellido Paterno RN |
| Q05 | - |  |  | SI | Apellido Materno RN |
| Q06 | - |  |  | SI | Fecha de Nacimiento |
| Q07 | - |  |  | SI | Hora de Nacimiento |
| Q08 | - |  |  | SI | RUT |
| Q09 | - |  |  | SI | Dirección |
| Q10 | - |  |  | SI | Comuna |
| Q11 | - |  |  | SI | Teléfono |
| Q12 | - |  |  | SI | Consultorio |
| Q13 | - |  |  | SI | Previsión |
| Q14 | - |  |  | SI | Nombres de la Madre |
| Q15 | - |  |  | SI | Apellido Paterno de la Madre |
| Q16 | - |  |  | SI | Apellido Materno de la Madre |
| Q17 | - |  |  | SI | Edad de la Madre |
| Q18 | - |  |  | SI | RUT |
| Q19 | - |  |  | SI | Grupo Sanguíneo AB0 materno |
| Q20 | - |  |  | SI | Grupo Sanguíneo Rh Materno |
| Q21 | - |  |  | SI | Gestaciones |
| Q22 | - |  |  | SI | Partos |
| Q23 | - |  |  | SI | Abortos |
| Q24 | - |  |  | SI | VDRL |
| Q25 | - |  |  | SI | VIH |
| Q26 | - |  |  | SI | Antecedentes Mórbidos |
| Q27 | - |  |  | SI | Uso de Corticoides |
| Q28 | - |  |  | SI | Uso de Corticoides |
| Q29 | - |  |  | SI | Uso de Antibióticos |
| Q30 | - |  |  | SI | Uso de Antibióticos |
| Q31 | - |  |  | SI | Uso de Otros Fármacos |
| Q32 | - |  |  | SI | Uso de Otros fármacos |
| Q33 | - |  |  | SI | Controles médicos de embarazo |
| Q34 | - |  |  | SI | Número de controles de embarazo realizados |
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