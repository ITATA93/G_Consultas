# SQLUser.MHC_DetTypeRevokeDet

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REVDET_ParRef | bigint | PK |  | NO | MHC_DetentionType Parent Reference |
| Q01 | - |  |  | SI | Objetivo Registro |
| Q02 | - |  |  | SI | Total |
| Q03 | - |  |  | SI | Parcial (Incapacidad de Autorecuperacion) |
| Q04 | - |  |  | SI | Incapacidad de solicitar ayuda |
| Q05 | - |  |  | SI | Alergias |
| Q06 | - |  |  | SI | Detalle |
| Q07 | - |  |  | SI | Riesgo Caida |
| Q08 | - |  |  | SI | Riesgo Infeccion |
| Q09 | - |  |  | SI | Riesgo de Ulcera-Escala de Bradem |
| Q10 | - |  |  | SI | No maneja adecuadamente el regimenterapeutico |
| Q11 | - |  |  | SI | Conductas de Riesgo |
| Q12 | - |  |  | SI | Detalle |
| Q13 | - |  |  | SI | Toxicos |
| Q14 | - |  |  | SI | Detalle |
| Q15 | - |  |  | SI | Automedicacion |
| Q16 | - |  |  | SI | Afrontamiento |
| Q17 | - |  |  | SI | Negacion |
| Q18 | - |  |  | SI | Minimizacion |
| Q19 | - |  |  | SI | Proyeccion |
| Q20 | - |  |  | SI | Ansiedad |
| Q21 | - |  |  | SI | Dolor |
| Q22 | - |  |  | SI | En |
| Q23 | - |  |  | SI | A la movilizacion |
| Q24 | - |  |  | SI | Agudo |
| Q25 | - |  |  | SI | Cronico |
| Q26 | - |  |  | SI | Intensidad del Dolor EVA |
| Q27 | - |  |  | SI | Vacunacion |
| Q28 | - |  |  | SI | Detalle |
| Q29 | - |  |  | SI | Implantes |
| Q30 | - |  |  | SI | Detalle |
| Q31 | - |  |  | SI | Realiza medidas de prevencion en salud |
| Q32 | - |  |  | SI | Detalle |
| Q33 | - |  |  | SI | Diagnostico 1 |
| Q34 | - |  |  | SI | Diagnostico 2 |
| Q35 | - |  |  | SI | Conclusion |
| Q36 | - |  |  | SI | Rieso |
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
| REVDET_Childsub | double |  |  | NO | Childsub |
| REVDET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REVDET_CreatedDate | date |  |  | SI | Created Date |
| REVDET_CreatedTime | time |  |  | SI | Created Time |
| REVDET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REVDET_DetentionType_DR | bigint |  | FK | SI | Des Ref MHCDetentionType |
| REVDET_RowId | varchar |  |  | NO | - |
| REVDET_UpdatedDate | date |  |  | SI | Updated Date |
| REVDET_UpdatedTime | time |  |  | SI | Updated Time |
| REVDET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*