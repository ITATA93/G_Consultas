# SQLUser.ARC_Tariff

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TAR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | 1. Datos de la Víctima |
| Q02 | - |  |  | SI | Nombre |
| Q03 | - |  |  | SI | RUN |
| Q04 | - |  |  | SI | Edad old |
| Q05 | - |  |  | SI | Fecha de Nacimiento |
| Q06 | - |  |  | SI | Domicilio |
| Q07 | - |  |  | SI | Comuna |
| Q08 | - |  |  | SI | Relación con el Agresor |
| Q09 | - |  |  | SI | 2. Datos del Denunciante (completar en el caso de ... |
| Q10 | - |  |  | SI | Nombre |
| Q11 | - |  |  | SI | RUN |
| Q12 | - |  |  | SI | Edad |
| Q13 | - |  |  | SI | Fecha de Nacimiento |
| Q14 | - |  |  | SI | Domicilio |
| Q15 | - |  |  | SI | Comuna |
| Q16 | - |  |  | SI | 3. Datos del Agresor |
| Q17 | - |  |  | SI | Nombre |
| Q18 | - |  |  | SI | RUN |
| Q19 | - |  |  | SI | Edad |
| Q20 | - |  |  | SI | Fecha de Nacimiento |
| Q21 | - |  |  | SI | Domicilio |
| Q22 | - |  |  | SI | Comuna |
| Q23 | - |  |  | SI | 4. Entorno de Violencia |
| Q24 | - |  |  | SI | Especificar |
| Q25 | - |  |  | SI | 5. Tipo(s) de Violencia |
| Q26 | - |  |  | SI | 5. 1. Si se trata de Violencia Física, precisar |
| Q27 | - |  |  | SI | 6. Frecuencia de los actos de violencia |
| Q28 | - |  |  | SI | Especificar frecuencia |
| Q29 | - |  |  | SI | Fecha del Suceso |
| Q30 | - |  |  | SI | Fecha de Inicio |
| Q31 | - |  |  | SI | 7. Descripción de los hechos |
| Q32 | - |  |  | SI | 8. Conducta a realizar |
| Q33 | - |  |  | SI | Profesional de Salud |
| Q34 | - |  |  | SI | RUN del Profesional |
| Q35 | - |  |  | SI | Tipo de Profesional |
| Q36 | - |  |  | SI | Fecha / Hora de Registro |
| Q37 | - |  |  | SI | Hora de Registro |
| Q38 | - |  |  | SI | Apellido Paterno |
| Q39 | - |  |  | SI | Apellido Materno |
| Q40 | - |  |  | SI | Sexo del Agresor |
| Q41 | - |  |  | SI | Año |
| Q42 | - |  |  | SI | Mes |
| Q43 | - |  |  | SI | Día |
| Q44 | - |  |  | SI | Edad (AMD) |
| Q45 | - |  |  | SI | **Importante: En caso de tratarse de un caso de vi... |
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
| TAR_Code | varchar |  |  | NO | Code |
| TAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TAR_CreatedDate | date |  |  | SI | Created Date |
| TAR_CreatedTime | time |  |  | SI | Created Time |
| TAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TAR_Desc | varchar |  |  | NO | Description |
| TAR_Owner | varchar |  |  | SI | Owner |
| TAR_UpdatedDate | date |  |  | SI | Updated Date |
| TAR_UpdatedTime | time |  |  | SI | Updated Time |
| TAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*