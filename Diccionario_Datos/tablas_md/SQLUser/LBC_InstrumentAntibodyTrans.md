# SQLUser.LBC_InstrumentAntibodyTrans

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINANT_ParRef | bigint | PK |  | NO | Parent instrument DR |
| LBCINANT_Antibody_DR | bigint |  | FK | SI | Internal Antibody |
| LBCINANT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINANT_DateFrom | date |  |  | SI | Date From |
| LBCINANT_DateTo | date |  |  | SI | Date To |
| LBCINANT_InstrumentAntibody | varchar |  |  | SI | Instrument antibody |
| LBCINANT_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | COVID-19 screening tool complete and reviewed |
| Q04 | - |  |  | SI | Does the patient consent to a follow up phone call |
| Q05 | - |  |  | SI | Discharge destination |
| Q06 | - |  |  | SI | Specify other |
| Q07 | - |  |  | SI | Discharge details |
| Q08 | - |  |  | SI | Responsible adult |
| Q09 | - |  |  | SI | Contact details |
| Q10 | - |  |  | SI | Planned transport home with responsible adult by |
| Q11 | - |  |  | SI | Transport details |
| Q12 | - |  |  | SI | Patient requires |
| Q13 | - |  |  | SI | Documentation details |
| Q14 | - |  |  | SI | Did patient bring their own medication |
| Q15 | - |  |  | SI | Has the patient's regular medications been charted |
| Q16 | - |  |  | SI | Pre-anaesthetic screening tool completed |
| Q17 | - |  |  | SI | Consent form reviewed and complete |
| Q18 | - |  |  | SI | Admission assessment complete |
| Q19 | - |  |  | SI | Dummy1 |
| Q20 | - |  |  | SI | Dummy2 |
| Q21 | - |  |  | SI | Dummy3 |
| Q22 | - |  |  | SI | Dummy4 |
| Q23 | - |  |  | SI | Dummy5 |
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