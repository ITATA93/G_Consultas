# SQLUser.MRC_VarianceReason

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | NOMBRE |
| Q02 | - |  |  | SI | APELLIDO PATERNO |
| Q03 | - |  |  | SI | APELLIDO MATERNO |
| Q04 | - |  |  | SI | Sexo |
| Q05 | - |  |  | SI | RUT |
| Q06 | - |  |  | SI | Fecha de Nacimiento |
| Q07 | - |  |  | SI | Edad |
| Q08 | - |  |  | SI | Nacionalidad |
| Q09 | - |  |  | SI | Coinfección Retroviral |
| Q10 | - |  |  | SI | Dirección |
| Q11 | - |  |  | SI | Comuna |
| Q12 | - |  |  | SI | Ciudad |
| Q13 | - |  |  | SI | Teléfono |
| Q14 | - |  |  | SI | V.T |
| Q15 | - |  |  | SI | C.T |
| Q16 | - |  |  | SI | N° DE MESES C.T. |
| Q17 | - |  |  | SI | A.T.RECAIDA |
| Q18 | - |  |  | SI | A.T. ABANDONO |
| Q19 | - |  |  | SI | Medicamentos |
| Q20 | - |  |  | SI | N° de Muestra |
| Q21 | - |  |  | SI | Tipo de Muestra |
| Q22 | - |  |  | SI | Fecha Toma de Muestra |
| Q23 | - |  |  | SI | Hora Toma de Muestra |
| Q24 | - |  |  | SI | Fecha de Envío Muestra |
| Q25 | - |  |  | SI | Hora de Envío Muestra |
| Q26 | - |  |  | SI | Baciloscopía |
| Q27 | - |  |  | SI | Cultivo |
| Q28 | - |  |  | SI | N° de Cultivo |
| Q29 | - |  |  | SI | Tipo Muestra del Cultivo |
| Q30 | - |  |  | SI | Resultado de Baciloscopia |
| Q31 | - |  |  | SI | Fecha de Siembra Cultivo |
| Q32 | - |  |  | SI | Fecha de Lectura Cultivo |
| Q33 | - |  |  | SI | Fecha de Envío Cultivo |
| Q34 | - |  |  | SI | Identificación |
| Q35 | - |  |  | SI | Suceptibilidad |
| Q36 | - |  |  | SI | Responsable del Envío |
| Q37 | - |  |  | SI | Establecimiento |
| Q38 | - |  |  | SI | Teléfono/Red Minsal |
| Q39 | - |  |  | SI | E-Mail |
| Q40 | - |  |  | SI | Descripción |
| Q41 | - |  |  | SI | Técnica |
| Q42 | - |  |  | SI | Región |
| Q43 | - |  |  | SI | Previsión |
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
| VR_BillingReason | varchar |  |  | SI | BillingReason |
| VR_Code | varchar |  |  | NO | Code |
| VR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VR_CreatedDate | date |  |  | SI | Created Date |
| VR_CreatedTime | time |  |  | SI | Created Time |
| VR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VR_DateFrom | date |  |  | SI | Date From |
| VR_DateTo | date |  |  | SI | Date To |
| VR_DefLabTrakRecollectReason | varchar |  |  | SI | DefLabTrakRecollectReason |
| VR_Desc | varchar |  |  | NO | Description |
| VR_EnteredInError | varchar |  |  | SI | Entered in Error |
| VR_IsModifyReason | varchar |  |  | SI | Is Modify Reason |
| VR_Owner | varchar |  |  | SI | Owner |
| VR_ReceivingLocHospital | varchar |  |  | SI | Receiving Location Hospital |
| VR_SuppressModifAlert | varchar |  |  | SI | Suppress modification alert |
| VR_UpdatedDate | date |  |  | SI | Updated Date |
| VR_UpdatedTime | time |  |  | SI | Updated Time |
| VR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| VR_VarCateg_DR | bigint |  | FK | SI | Des Ref VarCateg |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*