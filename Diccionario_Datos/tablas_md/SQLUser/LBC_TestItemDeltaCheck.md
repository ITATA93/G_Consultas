# SQLUser.LBC_TestItemDeltaCheck

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTIDC_ParRef | bigint | PK |  | NO | Parent TestItem DR |
| LBCTIDC_AbsoluteValue | double |  |  | SI | Absolute Value  |
| LBCTIDC_AbsoluteValueComments | varchar |  |  | SI | Absolute Value Comments |
| LBCTIDC_AdmType | varchar |  |  | SI | Admission Type
AdmType Standard Type   |
| LBCTIDC_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCTIDC_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTIDC_ClinicalCondition_DR | bigint |  | FK | SI | Clinical Condition |
| LBCTIDC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTIDC_Container_DR | bigint |  | FK | SI | Container |
| LBCTIDC_DateFrom | date |  |  | NO | Effective date from for the record |
| LBCTIDC_DateTo | date |  |  | SI | Effective date to for the record |
| LBCTIDC_Direction | varchar |  |  | SI | Direction of Change
LabResultDirection Standard T... |
| LBCTIDC_Interpretation_DR | bigint |  | FK | SI | Delta Check Interpretation |
| LBCTIDC_IntervalFrom | integer |  |  | SI | Interval From  |
| LBCTIDC_IntervalFromUnit | varchar |  |  | SI | Interval From Unit  |
| LBCTIDC_IntervalTo | integer |  |  | SI | Interval To |
| LBCTIDC_IntervalToUnit | varchar |  |  | SI | Interval From Unit  |
| LBCTIDC_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTIDC_PatType_DR | bigint |  | FK | SI | Patient Type |
| LBCTIDC_PatientLocation_DR | bigint |  | FK | SI | Patient Location |
| LBCTIDC_Percentage | double |  |  | SI | Percentage Value  |
| LBCTIDC_PercentageComments | varchar |  |  | SI | Percentage Comments |
| LBCTIDC_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCTIDC_RateOfChange | double |  |  | SI | Rate of Change |
| LBCTIDC_RateOfChangeComments | varchar |  |  | SI | Rate Of Change Comments |
| LBCTIDC_RateOfChangeUnit | varchar |  |  | SI | Rate of Change Unit |
| LBCTIDC_RowID | varchar |  |  | NO | - |
| LBCTIDC_Sequence | double |  |  | SI | Priority  Sequence |
| LBCTIDC_Sex_DR | bigint |  | FK | SI | Sex |
| LBCTIDC_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBCTIDC_Species_DR | bigint |  | FK | SI | Species |
| LBCTIDC_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTIDC_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTIDC_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCTIDC_TextChange | varchar |  |  | SI | Text Change |
| LBCTIDC_TextChangeComments | varchar |  |  | SI | Text Change Comments |
| Q01 | - |  |  | SI | Síntomas Diurnos |
| Q02 | - |  |  | SI | Limitación de Actividades |
| Q03 | - |  |  | SI | Síntomas Nocturnos Despiertan Paciente |
| Q04 | - |  |  | SI | Necesidad Medicamentos de Rescate |
| Q05 | - |  |  | SI | Función Pulmonar (PEF/FEV1) |
| Q06 | - |  |  | SI | Exacerbaciones |
| Q07 | - |  |  | SI | Resultado |
| Q07ObsDR | - |  |  | SI | Resultado DR |
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