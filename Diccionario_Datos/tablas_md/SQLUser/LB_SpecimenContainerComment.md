# SQLUser.LB_SpecimenContainerComment

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Muestras de Laboratorio**. Gestión de especímenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSPCC_ParRef | bigint | PK |  | NO | Parent |
| LBSPCC_Reportable | varchar |  |  | SI | Reportable |
| LBSPCC_RowID | varchar |  |  | NO | - |
| LBSPCC_SpecimenComment_DR | bigint |  | FK | SI | Comment |
| Q01 | - |  |  | SI | Criterios de un Paciente con Alto Riesgo Cardiovas... |
| Q02 | - |  |  | SI | Criterios que Aumentan una Categoría de Riesgo |
| Q03 | - |  |  | SI | Fumador (a) |
| Q04 | - |  |  | SI | Diabetes Mellitus |
| Q05 | - |  |  | SI | Colesterol Total (mg/dl) |
| Q06 | - |  |  | SI | Colesterol HDL (mg/dl) |
| Q07 | - |  |  | SI | Presión Arterial Sistólica (mmHg) |
| Q08 | - |  |  | SI | Presión Arterial Diastólica (mmHg) |
| Q09 | - |  |  | SI | Porcentaje de Riesgo Cardiovascular |
| Q09ObsDR | - |  |  | SI | Porcentaje de Riesgo Cardiovascular DR |
| Q10 | - |  |  | SI | Riesgo Cardiovascular |
| Q10ObsDR | - |  |  | SI | Riesgo Cardiovascular DR |
| Q11 | - |  |  | SI | Albuminuria |
| Q12 | - |  |  | SI | Etapa ERC |
| Q13 | - |  |  | SI | Circunferencia Cintura |
| Q14 | - |  |  | SI | Triglicéridos |
| Q15 | - |  |  | SI | Glicemia |
| Q16 | - |  |  | SI | RAC |
| Q17 | - |  |  | SI | VFG MDRD-4 |
| Q18 | - |  |  | SI | VFG Cockroft-Gault |
| Q19 | - |  |  | SI | Colesterol LDL |
| Q20 | - |  |  | SI | Categoría ERC |
| Q21 | - |  |  | SI | Age |
| Q22 | - |  |  | SI | Sex |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*