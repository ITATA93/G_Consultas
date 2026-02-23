# SQLUser.LBC_QCRule

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCQCR_RowID | bigint | PK |  | NO | - |
| LBCQCR_Action | varchar |  |  | SI | Action
StandardType: LabQCRuleAction |
| LBCQCR_Code | varchar |  |  | SI | Code |
| LBCQCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCQCR_Colour | varchar |  |  | SI | Colour |
| LBCQCR_CreatedDate | date |  |  | SI | Created Date |
| LBCQCR_CreatedTime | time |  |  | SI | Created Time |
| LBCQCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCQCR_Desc | varchar |  |  | SI | Description |
| LBCQCR_LongDescription | varchar |  |  | SI | Long Description |
| LBCQCR_Owner | varchar |  |  | SI | Owner |
| LBCQCR_SequenceNumber | numeric |  |  | SI | Sequence Number |
| LBCQCR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCQCR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCQCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Objetivo Registro |
| Q02 | - |  |  | SI | Estudios |
| Q03 | - |  |  | SI | Ocupacion |
| Q04 | - |  |  | SI | Unidad Familiar |
| Q05 | - |  |  | SI | Personas significativas |
| Q06 | - |  |  | SI | Cuidador principal |
| Q07 | - |  |  | SI | Insatifaccion con rol laboral |
| Q08 | - |  |  | SI | Auto percepcion negativa |
| Q09 | - |  |  | SI | Pacividad, apatia |
| Q10 | - |  |  | SI | Disminucion en las relaciones sociales |
| Q11 | - |  |  | SI | Influencia de la salud en ocupaciones laborales, f... |
| Q12 | - |  |  | SI | Depende de otra persona para satifacer necesidades... |
| Q13 | - |  |  | SI | Lactancia |
| Q14 | - |  |  | SI | Detalle |
| Q15 | - |  |  | SI | Estudia |
| Q16 | - |  |  | SI | Curso |
| Q17 | - |  |  | SI | Diagnostico 1 |
| Q18 | - |  |  | SI | Diagnostico 2 |
| Q19 | - |  |  | SI | Conclusion |
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