# SQLUser.MR_DiagnosLymphInvasion

**Schema:** SQLUser
**Columnas:** 57
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Diagnósticos**. Códigos CIE-10 asociados al episodio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DLI_ParRef | varchar | PK |  | NO | MR_Diagnos Parent Reference |
| DLI_BodySite_DR | bigint |  | FK | SI | Des Ref BodySite |
| DLI_Childsub | double |  |  | NO | Childsub |
| DLI_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Violencia de Género |
| Q02 | - |  |  | SI | Violencia hacia el Adulto Mayor |
| Q03 | - |  |  | SI | Abuso Sexual (antiguo) |
| Q04 | - |  |  | SI | Resultado AUDIT |
| Q04ObsDR | - |  |  | SI | Resultado AUDIT DR |
| Q05 | - |  |  | SI | Consumo Riesgoso de Drogas |
| Q09 | - |  |  | SI | Trata de Personas |
| Q10 | - |  |  | SI | Violencia Física |
| Q11 | - |  |  | SI | Violencia Sexual |
| Q12 | - |  |  | SI | Violencia Psicológica |
| QAS | - |  |  | SI | Abuso Sexual |
| QMI | - |  |  | SI | Mujer con Infante menor a 5 años |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*