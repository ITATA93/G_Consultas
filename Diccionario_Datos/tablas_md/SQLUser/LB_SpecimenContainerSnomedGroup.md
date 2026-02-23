# SQLUser.LB_SpecimenContainerSnomedGroup

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Muestras de Laboratorio**. Gestión de especímenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSCSG_ParRef | bigint | PK |  | NO | - |
| LBSCSG_FullySpecifiedName | varchar |  |  | SI | Fully Specified Name |
| LBSCSG_RowID | varchar |  |  | NO | - |
| LBSCSG_SnomedTermDR | bigint |  | FK | SI | referance to PACSnomedTerms(SNOMED CT)  |
| LBSCSG_SpecimenContainer_DR | bigint |  | FK | SI | Specimen Container |
| LBSCSG_TestSetSnomedGroup_DR | varchar |  | FK | SI | Test Set SNOMED Group |
| Q01 | - |  |  | SI | Estado ansioso |
| Q02 | - |  |  | SI | Tensión |
| Q03 | - |  |  | SI | Temores |
| Q04 | - |  |  | SI | Funciones Intelectuales (Cognitivas) |
| Q05 | - |  |  | SI | Humor depresivo |
| Q06 | - |  |  | SI | Síntomas somáticos musculares |
| Q07 | - |  |  | SI | Síntomas somáticos sensoriales |
| Q08 | - |  |  | SI | Síntomas cardiovasculares |
| Q09 | - |  |  | SI | Síntomas respiratorios |
| Q10 | - |  |  | SI | Síntomas gastrointestinales |
| Q11 | - |  |  | SI | Síntomas genitourinarios |
| Q12 | - |  |  | SI | Síntomas del sistema nervioso autónomo |
| Q13 | - |  |  | SI | Conducta en el transcurso del test |
| Q14 | - |  |  | SI | Insomnio |
| Q15 | - |  |  | SI | Puntaje Ansiedad síquica |
| Q16 | - |  |  | SI | Puntaje Asiedad somática |
| Q17 | - |  |  | SI | Puntaje de Preguntas: Ausencia=0, Leve=1, Moderado... |
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
| ToBeDelated | bit |  |  | SI | A flag to indicator the recored will be removed wh... |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*