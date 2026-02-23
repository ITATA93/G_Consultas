# SQLUser.LBC_TestSetRevisionLinking

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRL_ParRef | bigint | PK |  | NO | Parent Reference LBCTestSetRevisionDR |
| LBCTSRL_ClinicalConditions | varchar |  |  | SI | Clinical Condition(s) - may be multiple |
| LBCTSRL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRL_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRL_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRL_Interval | integer |  |  | SI | Interval |
| LBCTSRL_IntervalUnit | varchar |  |  | SI | Interval Unit  |
| LBCTSRL_LastSpecimen | varchar |  |  | SI | Last Sample Only |
| LBCTSRL_RowID | varchar |  |  | NO | - |
| LBCTSRL_SamePatient | varchar |  |  | SI | Same Patient |
| LBCTSRL_SameSpecimen | varchar |  |  | SI | Same Specimen |
| LBCTSRL_SameTestSet | varchar |  |  | SI | Same Test Set |
| LBCTSRL_Sequence | double |  |  | SI | Priority  Sequence |
| LBCTSRL_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRL_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRL_TestSets | varchar |  |  | SI | Test sets for link
List of possible test sets tha... |
| Q01 | - |  |  | SI | Sex: Sexo masculino |
| Q02 | - |  |  | SI | Age: Edad <20 ó > 45 años |
| Q03 | - |  |  | SI | Depresión |
| Q04 | - |  |  | SI | Previous attempt: Tentativa suicida previa |
| Q05 | - |  |  | SI | Ethanol abuse: Abuso de alcohol |
| Q06 | - |  |  | SI | Rational thinking loss: Falta de pensamiento racio... |
| Q07 | - |  |  | SI | Social supports lacking: Carencia de soporte socia... |
| Q08 | - |  |  | SI | Organised plan: Plan organizado de suicidio |
| Q09 | - |  |  | SI | No spouse sickness: No pareja o conyuge |
| Q10 | - |  |  | SI | Somatic disease: Enfermedad somática |
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