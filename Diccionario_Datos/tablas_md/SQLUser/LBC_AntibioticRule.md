# SQLUser.LBC_AntibioticRule

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCARS_RowID | bigint | PK |  | NO | - |
| ChildQ14DR | - |  |  | SI | Child Reference: Basal rate settings (units / hour... |
| LBCARS_AntibioticPanel_DR | bigint |  | FK | SI | Antibiotics Panel
Des Ref Antibiotics Panel |
| LBCARS_Code | varchar |  |  | SI | Code |
| LBCARS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCARS_DateFrom | date |  |  | SI | Effective date for the record |
| LBCARS_DateTo | date |  |  | SI | Last day the record is active  |
| LBCARS_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCARS_Owner | varchar |  |  | SI | Owner |
| LBCARS_PathGroupPathRule_DR | varchar |  | FK | SI | Organism Group Pathogenicity |
| LBCARS_PathogenGroup_DR | bigint |  | FK | SI | Pathogen Group
Des Ref Antibiotics |
| LBCARS_PathogenPathRule_DR | varchar |  | FK | SI | Organism Pathogenicity |
| LBCARS_Pathogen_DR | bigint |  | FK | SI | Pathogen
Des Ref Pathogen |
| LBCARS_Priority | numeric |  |  | SI | Priority |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Glucose Monitor Details |
| Q04 | - |  |  | SI | Type of monitoring |
| Q05 | - |  |  | SI | Equipment details |
| Q06 | - |  |  | SI | Continuous glucose monitor make and model |
| Q07 | - |  |  | SI | Flash glucose smart meter make and model |
| Q08 | - |  |  | SI | Skin prick glucose smart meter make and model |
| Q09 | - |  |  | SI | Glucose monitor detail notes |
| Q10 | - |  |  | SI | Insulin Pump Settings |
| Q11 | - |  |  | SI | Insulin pump make and model |
| Q12 | - |  |  | SI | Basal rate settings |
| Q13 | - |  |  | SI | 24 hour total units |
| Q15 | - |  |  | SI | Bolus settings |
| Q16 | - |  |  | SI | Active insulin time (h:mm) |
| Q19 | - |  |  | SI | Insulin pump setting notes |
| Q20 | - |  |  | SI | Smart Meter Settings |
| Q21 | - |  |  | SI | Insulin to carbohydrate ratio (grams / Unit) - bre... |
| Q22 | - |  |  | SI | Insulin to carbohydrate ratio (grams / Unit)  - lu... |
| Q23 | - |  |  | SI | Insulin to carbohydrate ratio (grams / Unit)  - di... |
| Q24 | - |  |  | SI | Insulin sensitivity factor (mmol / L per Unit) |
| Q25 | - |  |  | SI | Blood glucose level (BGL) target - daytime vs over... |
| Q26 | - |  |  | SI | Insulin on board |
| Q27 | - |  |  | SI | Smart meter setting notes |
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