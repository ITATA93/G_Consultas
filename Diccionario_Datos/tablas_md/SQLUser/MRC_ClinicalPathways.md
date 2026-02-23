# SQLUser.MRC_ClinicalPathways

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPW_RowId | bigint | PK |  | NO | - |
| CPW_Active | varchar |  |  | SI | Active |
| CPW_AgeFrom | double |  |  | SI | AgeFrom |
| CPW_AgeTo | double |  |  | SI | AgeTo |
| CPW_CPWTypeDR | bigint |  | FK | SI | CPW Type DR |
| CPW_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| CPW_Code | varchar |  |  | NO | Code |
| CPW_CodeTableTags | varchar |  |  | SI | - |
| CPW_CreatedDate | date |  |  | SI | Created Date |
| CPW_CreatedTime | time |  |  | SI | Created Time |
| CPW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CPW_DateFrom | date |  |  | SI | Date From |
| CPW_DateTo | date |  |  | SI | Date To |
| CPW_Desc | varchar |  |  | NO | Description |
| CPW_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| CPW_NumberOfCycle | double |  |  | SI | NumberOfCycle |
| CPW_Owner | varchar |  |  | SI | - |
| CPW_ReviewDate | date |  |  | SI | ReviewDate |
| CPW_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| CPW_StartDay | double |  |  | SI | StartDay |
| CPW_UpdatedDate | date |  |  | SI | Updated Date |
| CPW_UpdatedTime | time |  |  | SI | Updated Time |
| CPW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CQVG | - |  |  | SI | (null) |
| Q10 | - |  |  | SI | Trata de Personas |
| Q11 | - |  |  | SI | Violencia Fisica |
| Q12 | - |  |  | SI | Violencia Sexual |
| Q13 | - |  |  | SI | Violencia Psicológica |
| QABSEX | - |  |  | SI | ABUSO SEXUAL |
| QAS | - |  |  | SI | Abuso Sexual |
| QCOH1 | - |  |  | SI | Resultado AUDIT |
| QCOH1ObsDR | - |  |  | SI | Resultado AUDIT DR |
| QCRDR | - |  |  | SI | CONSUMO DE RIESGO DE DROGAS |
| QMI | - |  |  | SI | Mujer (Adolescente) con Infante menor a 5 años |
| QMINF | - |  |  | SI | MALTRATO INFANTIL |
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
| QV | - |  |  | SI | Violencia |
| QVAM | - |  |  | SI | VIOLENCIA HACIA EL ADULTO MAYOR |
| QVG | - |  |  | SI | VIOLENCIA DE GÉNERO |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*