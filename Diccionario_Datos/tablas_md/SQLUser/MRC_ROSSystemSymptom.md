# SQLUser.MRC_ROSSystemSymptom

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTROSS_ParRef | varchar | PK |  | NO | OEC_ConsultCateg Parent Reference |
| CTROSS_Childsub | double |  |  | NO | Childsub |
| CTROSS_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CTROSS_CreatedDate | date |  |  | SI | Created Date |
| CTROSS_CreatedTime | time |  |  | SI | Created Time |
| CTROSS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTROSS_DateFrom | date |  |  | SI | Date From |
| CTROSS_DateTo | date |  |  | SI | Date To |
| CTROSS_ICDCode_DR | bigint |  | FK | SI | Des Ref ICDCode |
| CTROSS_ICPCCode_DR | bigint |  | FK | SI | Des Ref PACICPCCode |
| CTROSS_RowId | varchar |  |  | NO | - |
| CTROSS_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| CTROSS_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| CTROSS_UpdatedDate | date |  |  | SI | Updated Date |
| CTROSS_UpdatedTime | time |  |  | SI | Updated Time |
| CTROSS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nivel de Sedación |
| Q02 | - |  |  | SI | Estado Del Paciente |
| Q03 | - |  |  | SI | Estado de la Piel |
| Q04 | - |  |  | SI | Otra |
| Q05 | - |  |  | SI | Localización de la Lesión |
| Q06 | - |  |  | SI | Tipo de Lesión |
| Q07 | - |  |  | SI | Uso de Oxígeno |
| Q08 | - |  |  | SI | Dispositivo Vía Aérea |
| Q09 | - |  |  | SI | Otro |
| Q10 | - |  |  | SI | FiO2 |
| Q11 | - |  |  | SI | Frecuencia del Flujo |
| Q12 | - |  |  | SI | Imágenes Placas y Digitales |
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