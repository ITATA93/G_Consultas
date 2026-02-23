# SQLUser.LBC_CollectionSpecimenContainer

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCOLSC_ParRef | bigint | PK |  | NO | Parent TestItem DR |
| LBCCOLSC_AnatomicalSiteMandatory | varchar |  |  | SI | Anatomical Site Mandatory
Flag to indicate if a a... |
| LBCCOLSC_AnatomicalSiteQualifierMandatory | varchar |  |  | SI | Anatomical Site Qualifier Mandatory
Flag to indic... |
| LBCCOLSC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCOLSC_Container_DR | bigint |  | FK | SI | Container DR |
| LBCCOLSC_DefaultAnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCCOLSC_DefaultAnatomicalSite_DR | bigint |  | FK | SI | Default anatomical site |
| LBCCOLSC_DefaultLesion_DR | bigint |  | FK | SI | Lesion |
| LBCCOLSC_DefaultVolume | double |  |  | SI | Default Collected Volume |
| LBCCOLSC_LesionMandatory | varchar |  |  | SI | Lesion Mandatory
Flag to indicate if a lesion is ... |
| LBCCOLSC_MinVolume | double |  |  | SI | Min Volume |
| LBCCOLSC_RowID | varchar |  |  | NO | - |
| LBCCOLSC_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCCOLSC_SpecimenReusable | varchar |  |  | SI | Specimen Reusable
Specimen Reusability Type to in... |
| LBCCOLSC_Specimen_DR | bigint |  | FK | SI | Specimen DR |
| LBCCOLSC_ValidityTime | integer |  |  | SI | Validity Time
A Specimen received in a Collection... |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Baseline hematocrit (%) |
| Q04 | - |  |  | SI | Creatinine clearance (mL/min) |
| Q05 | - |  |  | SI | Heart rate (beats / minute) |
| Q06 | - |  |  | SI | Systolic BP (mmHg) |
| Q07 | - |  |  | SI | Sex |
| Q08 | - |  |  | SI | Signs of congestive heart failure at presentation |
| Q09 | - |  |  | SI | Prior vascular disease |
| Q10 | - |  |  | SI | Diabetes mellitus |
| Q11 | - |  |  | SI | In the original study: |
| Q12 | - |  |  | SI | Creatinine clearance was estimated using the Cockc... |
| Q13 | - |  |  | SI | Prior vascular disease was defined as history of p... |
| Q14 | - |  |  | SI | Score Interpretation: |
| Q15 | - |  |  | SI | The CRUSADE bleeding score (range 1–100 points) wa... |
| Q16 | - |  |  | SI | 3.1% very low risk (≤ 20) |
| Q17 | - |  |  | SI | 5.5% low risk (21 – 30) |
| Q18 | - |  |  | SI | 8.6% moderate risk (31 – 40) |
| Q19 | - |  |  | SI | 11.9% high risk (41 – 50) |
| Q20 | - |  |  | SI | and 19.5% very high risk (> 50) |
| Q21 | - |  |  | SI | Score |
| Q22 | - |  |  | SI | Classification |
| Q23 | - |  |  | SI | ≤ 20 |
| Q24 | - |  |  | SI | Very low risk |
| Q25 | - |  |  | SI | 21 - 30 |
| Q26 | - |  |  | SI | Low risk |
| Q27 | - |  |  | SI | 31 - 40 |
| Q28 | - |  |  | SI | Moderate risk |
| Q29 | - |  |  | SI | 41 - 50 |
| Q30 | - |  |  | SI | High risk |
| Q31 | - |  |  | SI | > 50 |
| Q32 | - |  |  | SI | Very high risk |
| Q33 | - |  |  | SI | ≤ 20: 3.1% very low risk |
| Q34 | - |  |  | SI | 21 - 30: 5.5% low risk |
| Q35 | - |  |  | SI | 31 - 40: 8.6% moderate risk |
| Q36 | - |  |  | SI | 41 - 50: 11.9% high risk |
| Q37 | - |  |  | SI | > 50: 19.5% very high risk |
| Q38 | - |  |  | SI | The CRUSADE bleeding score quantifies risk for in-... |
| Q39 | - |  |  | SI | Creatinine clearance (mL/min) |
| Q40 | - |  |  | SI | 1.Subherwal S, Bach RG, Chen AY, et al. Baseline R... |
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