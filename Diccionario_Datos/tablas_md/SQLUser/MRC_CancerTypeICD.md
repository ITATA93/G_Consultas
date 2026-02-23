# SQLUser.MRC_CancerTypeICD

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTICD_ParRef | bigint | PK |  | NO | Parent Reference |
| CTICD_Childsub | double |  |  | NO | Childsub |
| CTICD_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| CTICD_CreatedDate | date |  |  | SI | Created Date |
| CTICD_CreatedTime | time |  |  | SI | Created Time |
| CTICD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTICD_DateFrom | date |  |  | SI | Date From |
| CTICD_DateTo | date |  |  | SI | Date To |
| CTICD_ICDCode_DR | bigint |  | FK | SI | ICD Code |
| CTICD_RowId | varchar |  |  | NO | - |
| CTICD_UpdatedDate | date |  |  | SI | Updated Date |
| CTICD_UpdatedTime | time |  |  | SI | Updated Time |
| CTICD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Médico |
| Q02 | - |  |  | SI | Enfermera(o) |
| Q03 | - |  |  | SI | Técnico Paramédico |
| Q04 | - |  |  | SI | Familiar |
| Q05 | - |  |  | SI | Camilla |
| Q06 | - |  |  | SI | Oxígeno |
| Q07 | - |  |  | SI | Aspiración |
| Q08 | - |  |  | SI | Monitorización |
| Q09 | - |  |  | SI | Maletín de Traslado |
| Q10 | - |  |  | SI | Motivo del Traslado |
| Q11 | - |  |  | SI | Especificar |
| Q12 | - |  |  | SI | Tipo de Ambulancia (Complejidad) |
| Q13 | - |  |  | SI | Fecha de Citación |
| Q14 | - |  |  | SI | Hora de Citación |
| Q15 | - |  |  | SI | Observaciones |
| Q16 | - |  |  | SI | Matrón(a) |
| Q17 | - |  |  | SI | Elementos Invasivos |
| Q18 | - |  |  | SI | Dispositivos Invasivos |
| Q19 | - |  |  | SI | Diagnóstico |
| Q20 | - |  |  | SI | Destino |
| Q21 | - |  |  | SI | Aislamiento |
| Q22 | - |  |  | SI | Transportar en |
| Q23 | - |  |  | SI | Tipo Aislamiento |
| Q24 | - |  |  | SI | Otro |
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