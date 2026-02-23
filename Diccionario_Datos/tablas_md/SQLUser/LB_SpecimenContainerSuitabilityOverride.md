# SQLUser.LB_SpecimenContainerSuitabilityOverride

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Muestras de Laboratorio**. Gestión de especímenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSPCSO_ParRef | bigint | PK |  | NO | Parent |
| LBSPCSO_Date | date |  |  | SI | Date |
| LBSPCSO_Reason_DR | bigint |  | FK | SI | Reason |
| LBSPCSO_RowID | varchar |  |  | NO | - |
| LBSPCSO_SpecimenSuitabilityCondition_DR | bigint |  | FK | NO | Specimen Suitability Condition |
| LBSPCSO_Time | time |  |  | SI | Time |
| LBSPCSO_User_DR | bigint |  | FK | SI | User |
| Q01 | - |  |  | SI | Nivel de Conciencia |
| Q02 | - |  |  | SI | Control Neuromuscular |
| Q03 | - |  |  | SI | Tono Muscular |
| Q04 | - |  |  | SI | Postura |
| Q05 | - |  |  | SI | Reflejos de Estiramiento |
| Q06 | - |  |  | SI | Mioclonías Segmentarias |
| Q07 | - |  |  | SI | Reflejos Complejos |
| Q08 | - |  |  | SI | De Succión |
| Q09 | - |  |  | SI | De Moro |
| Q10 | - |  |  | SI | Oculovestibular |
| Q11 | - |  |  | SI | Tónico del cuello |
| Q12 | - |  |  | SI | Función Autonómica |
| Q13 | - |  |  | SI | Pupilas |
| Q14 | - |  |  | SI | Respiración |
| Q15 | - |  |  | SI | Frecuencia Cardíaca |
| Q16 | - |  |  | SI | Secreciones Bronquiales y Salivales |
| Q17 | - |  |  | SI | Motilidad Gastrointestinal |
| Q18 | - |  |  | SI | Convulsiones |
| Q19 | - |  |  | SI | Hallazgos del EEG |
| Q20 | - |  |  | SI | Duración de los síntomas |
| Q21 | - |  |  | SI | Evolución |
| Q22 | - |  |  | SI | Resultado |
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