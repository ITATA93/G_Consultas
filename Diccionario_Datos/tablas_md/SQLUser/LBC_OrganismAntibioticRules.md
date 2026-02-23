# SQLUser.LBC_OrganismAntibioticRules

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCOAR_RowID | bigint | PK |  | NO | - |
| LBCOAR_AdmType | varchar |  |  | SI | - |
| LBCOAR_AgeFrom | double |  |  | SI | Age Range From (format [yy].mmdd)
Optional
If pr... |
| LBCOAR_AgeTo | double |  |  | SI | Age Range To (format [yy].mmdd )
If present, AgeF... |
| LBCOAR_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCOAR_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCOAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCOAR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCOAR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCOAR_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCOAR_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCOAR_Owner | varchar |  |  | SI | Owner |
| LBCOAR_PathogenGroup_DR | bigint |  | FK | SI | Pathogen Group |
| LBCOAR_PathogenGrowthQualifier_DR | bigint |  | FK | SI | Growth Qualifier of Pathogen |
| LBCOAR_Pathogen_DR | bigint |  | FK | SI | Pathogen |
| LBCOAR_PatientType | varchar |  |  | SI | The patient type for the lab episode |
| LBCOAR_PatientType_DR | bigint |  | FK | SI | Patient Type DR |
| LBCOAR_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCOAR_ReportList | varchar |  |  | SI | Report List |
| LBCOAR_Sequence | double |  |  | SI | Rule Sequence |
| LBCOAR_Species | varchar |  |  | SI | List of Species IDs |
| LBCOAR_SpecifiedAntibioticPanel_DR | bigint |  | FK | SI | Antibiotic Panel  |
| LBCOAR_SpecifiedPathogen_DR | bigint |  | FK | SI | Specified Pathogen |
| LBCOAR_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCOAR_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCOAR_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCOAR_SupressList | varchar |  |  | SI | Supress List |
| Q01 | - |  |  | SI | Appointment type |
| Q02 | - |  |  | SI | Seen by |
| Q03 | - |  |  | SI | Diagnosis |
| Q04 | - |  |  | SI | Year of diagnosis |
| Q05 | - |  |  | SI | Complications |
| Q06 | - |  |  | SI | Other |
| Q07 | - |  |  | SI | Please ensure any other medical conditions have be... |
| Q08 | - |  |  | SI | Systolic BP |
| Q08ObsDR | - |  |  | SI | Systolic BP DR |
| Q09 | - |  |  | SI | Diastolic BP |
| Q09ObsDR | - |  |  | SI | Diastolic BP DR |
| Q11 | - |  |  | SI | Height |
| Q11ObsDR | - |  |  | SI | Height DR |
| Q12 | - |  |  | SI | QRISK2 (Cardiovascular Risk Score) |
| Q13 | - |  |  | SI | Eye screen tested |
| Q14 | - |  |  | SI | Month of last screen (eye) |
| Q15 | - |  |  | SI | Year of last screen (eye) |
| Q16 | - |  |  | SI | Footscreen tested |
| Q17 | - |  |  | SI | Month of last screen (foot) |
| Q18 | - |  |  | SI | Year of last screen (foot) |
| Q19 | - |  |  | SI | Is the patient a smoker |
| Q20 | - |  |  | SI | Smoking advice given |
| Q21 | - |  |  | SI | Is the patient a driver |
| Q22 | - |  |  | SI | Driving guidance given |
| Q23 | - |  |  | SI | Insulin passport |
| Q24 | - |  |  | SI | Structured education |
| Q25 | - |  |  | SI | Treatment goals and plan agreed |
| Q26 | - |  |  | SI | Written information or advice given |
| Q27 | - |  |  | SI | Management plan / Comments |
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