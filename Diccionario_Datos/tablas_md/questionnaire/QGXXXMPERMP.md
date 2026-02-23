# questionnaire.QGXXXMPERMP

> Perinatal Mortality - Paediatric

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perinatal Mortality - Paediatric

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Lethal congenital abnormality |
| Q01ObsDR | varchar |  | FK | SI | Lethal congenital abnormality DR |
| Q02 | varchar |  |  | SI | Rhesus isoimmunisation |
| Q02ObsDR | varchar |  | FK | SI | Rhesus isoimmunisation DR |
| Q03 | varchar |  |  | SI | Non-isoimmunisation |
| Q03ObsDR | varchar |  | FK | SI | Non-isoimmunisation DR |
| Q04 | varchar |  |  | SI | Birth trauma |
| Q04ObsDR | varchar |  | FK | SI | Birth trauma DR |
| Q05 | varchar |  |  | SI | Antepartum anoxia |
| Q05ObsDR | varchar |  | FK | SI | Antepartum anoxia DR |
| Q06 | varchar |  |  | SI | Intrapartum anoxia |
| Q06ObsDR | varchar |  | FK | SI | Intrapartum anoxia DR |
| Q07 | varchar |  |  | SI | Lung maturity <27 weeks |
| Q07ObsDR | varchar |  | FK | SI | Lung maturity <27 weeks DR |
| Q08 | varchar |  |  | SI | HMD with significant IVH |
| Q08ObsDR | varchar |  | FK | SI | HMD with significant IVH DR |
| Q09 | varchar |  |  | SI | HMD without significant IVH |
| Q09ObsDR | varchar |  | FK | SI | HMD without significant IVH DR |
| Q10 | varchar |  |  | SI | IVH in absence of potentially lethal HMD |
| Q10ObsDR | varchar |  | FK | SI | IVH in absence of potentially lethal HMD DR |
| Q11 | varchar |  |  | SI | IVH in baby without HMD |
| Q11ObsDR | varchar |  | FK | SI | IVH in baby without HMD DR |
| Q12 | varchar |  |  | SI | Subarachnoid haemorrhage |
| Q12ObsDR | varchar |  | FK | SI | Subarachnoid haemorrhage DR |
| Q13 | varchar |  |  | SI | Subdural haemorrhage |
| Q13ObsDR | varchar |  | FK | SI | Subdural haemorrhage DR |
| Q14 | varchar |  |  | SI | Intracerebral haemorrhage |
| Q14ObsDR | varchar |  | FK | SI | Intracerebral haemorrhage DR |
| Q15 | varchar |  |  | SI | Necrotising enterocolitis |
| Q15ObsDR | varchar |  | FK | SI | Necrotising enterocolitis DR |
| Q16 | varchar |  |  | SI | Infection - antenatal |
| Q16ObsDR | varchar |  | FK | SI | Infection - antenatal DR |
| Q17 | varchar |  |  | SI | Infection - intrapartum |
| Q17ObsDR | varchar |  | FK | SI | Infection - intrapartum DR |
| Q18 | varchar |  |  | SI | Infection - postnatal |
| Q18ObsDR | varchar |  | FK | SI | Infection - postnatal DR |
| Q19 | varchar |  |  | SI | Disseminated intravascular coagulation |
| Q19ObsDR | varchar |  | FK | SI | Disseminated intravascular coagulation DR |
| Q20 | varchar |  |  | SI | Massive intra-alveolar hemorrhage |
| Q20ObsDR | varchar |  | FK | SI | Massive intra-alveolar hemorrhage DR |
| Q21 | varchar |  |  | SI | Haemorrhage - other |
| Q21ObsDR | varchar |  | FK | SI | Haemorrhage - other DR |
| Q22 | varchar |  |  | SI | Other paediatric factors |
| Q23 | varchar |  |  | SI | Unexplained |
| Q24 | varchar |  |  | SI | Comments |
| Q25 | varchar |  |  | SI | Paediatric / Obstetric |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*