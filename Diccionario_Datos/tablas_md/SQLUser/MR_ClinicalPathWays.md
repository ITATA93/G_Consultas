# SQLUser.MR_ClinicalPathWays

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPW_ParREf | bigint | PK |  | NO | MR_Adm Parent Reference |
| CPW_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| CPW_CancelReason_DR | bigint |  | FK | SI | Des Ref VarianceReason |
| CPW_CareProvider_DR | varchar |  | FK | SI | Des Ref CareProvider |
| CPW_Childsub | double |  |  | NO | Childsub |
| CPW_Comments | varchar |  |  | SI | Comments |
| CPW_Date | date |  |  | SI | Date Added |
| CPW_GoalTargetDate | date |  |  | SI | GoalTargetDate |
| CPW_GoalText | varchar |  |  | SI | Goal text |
| CPW_GovernDepart_DR | varchar |  | FK | SI | Des Ref CTNFMICategDepart |
| CPW_IDDate | date |  |  | SI | ID Date |
| CPW_IDTime | time |  |  | SI | ID Time |
| CPW_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| CPW_IsBrokerage | varchar |  |  | SI | IsBrokerage |
| CPW_Number | double |  |  | SI | Number |
| CPW_NurseAction | varchar |  |  | SI | NurseAction |
| CPW_Outcome_DR | bigint |  | FK | SI | Des Ref Outcome |
| CPW_Pathway_DR | bigint |  | FK | SI | Des Ref Pathway |
| CPW_Pathways_DR | varchar |  | FK | SI | Des Ref Pathways |
| CPW_ProblemEndDate | date |  |  | SI | ProblemEndDate |
| CPW_ProblemReviewDate | date |  |  | SI | ProblemReviewDate |
| CPW_ProblemStartDate | date |  |  | SI | ProblemStartDate |
| CPW_ReviewDate | date |  |  | SI | ReviewDate |
| CPW_RowId | varchar |  |  | NO | - |
| CPW_Status_DR | bigint |  | FK | SI | Des Ref Status |
| CPW_SuspendReason_DR | bigint |  | FK | SI | Des Ref VarianceReason |
| CPW_UsedFlag | date |  |  | SI | Used Flag |
| CPW_VarianceReason_DR | bigint |  | FK | SI | Des Ref VarianceReason |
| CPW_YesNo1 | varchar |  |  | SI | YesNo1 |
| CPW_YesNo2 | varchar |  |  | SI | YesNo2 |
| CPW_YesNo3 | varchar |  |  | SI | YesNo3 |
| Q01 | - |  |  | SI | RUT |
| Q02 | - |  |  | SI | Nombre |
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
| Q15 | - |  |  | SI | Dirección |
| Q16 | - |  |  | SI | Región |
| Q17 | - |  |  | SI | Ciudad/Localidad |
| Q18 | - |  |  | SI | Comuna |
| Q19 | - |  |  | SI | Profesional Responsable |
| Q20 | - |  |  | SI | Correo Laboratorio |
| Q21 | - |  |  | SI | Fono Laboratorio |
| Q22 | - |  |  | SI | Fax Laboratorio |
| Q23 | - |  |  | SI | Servicio de Salud |
| Q24 | - |  |  | SI | Dirección |
| Q25 | - |  |  | SI | Región |
| Q26 | - |  |  | SI | Ciudad/Localidad |
| Q27 | - |  |  | SI | Tipo de Despacho |
| Q28 | - |  |  | SI | Comuna |
| Q29 | - |  |  | SI | Correo Laboratorio |
| Q30 | - |  |  | SI | Fax Laboratorio |
| Q31 | - |  |  | SI | Examen |
| Q32 | - |  |  | SI | Fecha de la Obtención de la Muestra |
| Q33 | - |  |  | SI | Hora de Obtención |
| Q34 | - |  |  | SI | Tipo de Muestra |
| Q35 | - |  |  | SI | N° Muestra Original |
| Q36 | - |  |  | SI | Fecha Envío ISPCH |
| Q37 | - |  |  | SI | Observaciones |
| Q38 | - |  |  | SI | Diagnóstico Clinico |
| Q39 | - |  |  | SI | Fecha Inicio de Diarrea |
| Q40 | - |  |  | SI | Antecedentes Epidemiológicos |
| Q41 | - |  |  | SI | N° ID Brotel |
| Q42 | - |  |  | SI | Tipo de Paciente |
| Q43 | - |  |  | SI | Seleccione si Corresponde a un Brote |
| Q44 | - |  |  | SI | Especifique Otra |
| Q45 | - |  |  | SI | Télefono |
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