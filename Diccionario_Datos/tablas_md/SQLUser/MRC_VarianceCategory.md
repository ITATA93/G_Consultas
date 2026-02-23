# SQLUser.MRC_VarianceCategory

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VC_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | RUT |
| Q02 | - |  |  | SI | Nombres |
| Q03 | - |  |  | SI | Apellido Paterno |
| Q04 | - |  |  | SI | Apellido Materno |
| Q05 | - |  |  | SI | Sexo |
| Q06 | - |  |  | SI | Fecha de Nacimiento |
| Q07 | - |  |  | SI | Edad |
| Q08 | - |  |  | SI | Dirección |
| Q09 | - |  |  | SI | Región |
| Q10 | - |  |  | SI | Ciudad / Localidad |
| Q11 | - |  |  | SI | Comuna |
| Q12 | - |  |  | SI | Teléfono |
| Q13 | - |  |  | SI | Previsión |
| Q14 | - |  |  | SI | Establecimiento |
| Q15 | - |  |  | SI | Unidad |
| Q16 | - |  |  | SI | Dirección |
| Q17 | - |  |  | SI | Región |
| Q18 | - |  |  | SI | Ciudad / Localidad |
| Q19 | - |  |  | SI | Comuna |
| Q20 | - |  |  | SI | Profesional Responsable |
| Q21 | - |  |  | SI | Correo Laboratorio |
| Q22 | - |  |  | SI | Fono Laboratorio |
| Q23 | - |  |  | SI | Correo Laboratorio |
| Q24 | - |  |  | SI | Servicio de Salud |
| Q25 | - |  |  | SI | Dirección |
| Q26 | - |  |  | SI | Región |
| Q27 | - |  |  | SI | Ciudad / Localidad |
| Q28 | - |  |  | SI | Tipo Despacho |
| Q29 | - |  |  | SI | Comuna |
| Q30 | - |  |  | SI | Correo Laboratorio |
| Q31 | - |  |  | SI | Examen |
| Q32 | - |  |  | SI | Fecha de la Muestra |
| Q33 | - |  |  | SI | Hora de Obtención |
| Q34 | - |  |  | SI | Tipo de Muestra |
| Q35 | - |  |  | SI | N° Muestra Original |
| Q36 | - |  |  | SI | N° Muestra |
| Q37 | - |  |  | SI | Fecha envío ISPCH |
| Q38 | - |  |  | SI | Observaciones |
| Q39 | - |  |  | SI | Diagnóstico Clínico |
| Q40 | - |  |  | SI | Fecha Inicio de Sintomas |
| Q41 | - |  |  | SI | Tratamiento Antibiótico |
| Q42 | - |  |  | SI | Fecha Inicio de Tratamiento |
| Q43 | - |  |  | SI | Fax Laboratorio |
| Q44 | - |  |  | SI | Fax Laboratorio |
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
| VC_Code | varchar |  |  | NO | Code |
| VC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VC_Colour | varchar |  |  | SI | Colour |
| VC_CreatedDate | date |  |  | SI | Created Date |
| VC_CreatedTime | time |  |  | SI | Created Time |
| VC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VC_DateFrom | date |  |  | SI | Date from |
| VC_DateTo | date |  |  | SI | Date To |
| VC_Desc | varchar |  |  | NO | Description |
| VC_Owner | varchar |  |  | SI | Owner |
| VC_UpdatedDate | date |  |  | SI | Updated Date |
| VC_UpdatedTime | time |  |  | SI | Updated Time |
| VC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*