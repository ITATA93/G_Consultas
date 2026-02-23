# questionnaire.QCLXXFRV

> Formulario de Registro de Violencia

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Registro de Violencia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Datos de la Víctima |
| Q02 | varchar |  |  | SI | Nombre |
| Q03 | varchar |  |  | SI | RUN |
| Q04 | varchar |  |  | SI | Edad old |
| Q05 | varchar |  |  | SI | Fecha de Nacimiento |
| Q06 | varchar |  |  | SI | Domicilio |
| Q07 | varchar |  |  | SI | Comuna |
| Q08 | varchar |  |  | SI | Relación con el Agresor |
| Q09 | varchar |  |  | SI | 2. Datos del Denunciante (completar en el caso de ... |
| Q10 | varchar |  |  | SI | Nombre |
| Q11 | varchar |  |  | SI | RUN |
| Q12 | numeric |  |  | SI | Edad |
| Q13 | date |  |  | SI | Fecha de Nacimiento |
| Q14 | varchar |  |  | SI | Domicilio |
| Q15 | varchar |  |  | SI | Comuna |
| Q16 | varchar |  |  | SI | 3. Datos del Agresor |
| Q17 | varchar |  |  | SI | Nombre |
| Q18 | varchar |  |  | SI | RUN |
| Q19 | numeric |  |  | SI | Edad |
| Q20 | date |  |  | SI | Fecha de Nacimiento |
| Q21 | varchar |  |  | SI | Domicilio |
| Q22 | varchar |  |  | SI | Comuna |
| Q23 | varchar |  |  | SI | 4. Entorno de Violencia |
| Q24 | varchar |  |  | SI | Especificar |
| Q25 | varchar |  |  | SI | 5. Tipo(s) de Violencia |
| Q26 | varchar |  |  | SI | 5. 1. Si se trata de Violencia Física, precisar |
| Q27 | varchar |  |  | SI | 6. Frecuencia de los actos de violencia |
| Q28 | varchar |  |  | SI | Especificar frecuencia |
| Q29 | date |  |  | SI | Fecha del Suceso |
| Q30 | date |  |  | SI | Fecha de Inicio |
| Q31 | varchar |  |  | SI | 7. Descripción de los hechos |
| Q32 | varchar |  |  | SI | 8. Conducta a realizar |
| Q33 | varchar |  |  | SI | Profesional de Salud |
| Q34 | varchar |  |  | SI | RUN del Profesional |
| Q35 | varchar |  |  | SI | Tipo de Profesional |
| Q36 | date |  |  | SI | Fecha / Hora de Registro |
| Q37 | time |  |  | SI | Hora de Registro |
| Q38 | varchar |  |  | SI | Apellido Paterno |
| Q39 | varchar |  |  | SI | Apellido Materno |
| Q40 | varchar |  |  | SI | Sexo del Agresor |
| Q41 | varchar |  |  | SI | Año |
| Q42 | varchar |  |  | SI | Mes |
| Q43 | varchar |  |  | SI | Día |
| Q44 | varchar |  |  | SI | Edad (AMD) |
| Q45 | varchar |  |  | SI | **Importante: En caso de tratarse de un caso de vi... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*