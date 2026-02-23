# SQLUser.LB_TMRuntimeParameter

**Schema:** SQLUser
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTMRP_RowID | bigint | PK |  | NO | - |
| LBTMRP_LastBPAutoDisposalDate | date |  |  | SI | Last blood product disposal date |
| LBTMRP_LastBPAutoDisposalTime | time |  |  | SI | Last blood product disposal time |
| LBTMRP_LastBPAutoDisposalUser_DR | bigint |  | FK | SI | Last blood product auto disposal user |
| Q01 | - |  |  | SI | Edad |
| Q02 | - |  |  | SI | Tipo Cirugía |
| Q03 | - |  |  | SI | Condición Clínica |
| Q04 | - |  |  | SI | Condición Clínica (Sólo Mujeres) |
| Q05 | - |  |  | SI | Clasificación de Riesgo |
| Q05ObsDR | - |  |  | SI | Clasificación de Riesgo DR |
| Q06 | - |  |  | SI | Riesgo Muy Bajo |
| Q07 | - |  |  | SI | Riesgo Bajo |
| Q08 | - |  |  | SI | Riesgo Moderado |
| Q09 | - |  |  | SI | Riesgo Alto |
| Q10 | - |  |  | SI | ¿Se Realizan Medidas Según Riesgo Evaluado? |
| Q11 | - |  |  | SI | Tipo de Tromboprofilaxis No Realizada |
| Q12 | - |  |  | SI | Razón de No Realización (Mecánica) |
| Q13 | - |  |  | SI | Otra Razón de No Realización (Mecánica) |
| Q14 | - |  |  | SI | Razón de No Realización (Farmacológica) |
| Q15 | - |  |  | SI | Otra Razón de No Realización (Farmacológica) |
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