# SQLUser.MRC_ICPC2Codes

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICPC2_RowId | bigint | PK |  | NO | - |
| ICPC2_Code | varchar |  |  | SI | Code |
| ICPC2_Component | double |  |  | SI | Component |
| ICPC2_Consider | varchar |  |  | SI | Consider |
| ICPC2_CreatedDate | date |  |  | SI | Created Date |
| ICPC2_CreatedTime | time |  |  | SI | Created Time |
| ICPC2_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ICPC2_Criteria | varchar |  |  | SI | Criteria |
| ICPC2_Desc | varchar |  |  | SI | Description |
| ICPC2_Exclusions | varchar |  |  | SI | Exclusions |
| ICPC2_ICD10 | varchar |  |  | SI | ICD10 |
| ICPC2_Inclusions | varchar |  |  | SI | Inclusions |
| ICPC2_Note | varchar |  |  | SI | Note |
| ICPC2_ShortDesc | varchar |  |  | SI | Short Description |
| ICPC2_UpdatedDate | date |  |  | SI | Updated Date |
| ICPC2_UpdatedTime | time |  |  | SI | Updated Time |
| ICPC2_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Toma de muestra |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Responsable |
| Q04 | - |  |  | SI | Observación |
| Q05 | - |  |  | SI | Establecimiento |
| Q06 | - |  |  | SI | Servicio |
| Q07 | - |  |  | SI | Nombre Médico Solicitante |
| Q08 | - |  |  | SI | Rut |
| Q09 | - |  |  | SI | Firma |
| Q10 | - |  |  | SI | Fecha |
| Q11 | - |  |  | SI | N° de Fax |
| Q12 | - |  |  | SI | E-mail |
| Q13 | - |  |  | SI | Fecha lab |
| Q14 | - |  |  | SI | Hora Lab |
| Q15 | - |  |  | SI | Responsable |
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