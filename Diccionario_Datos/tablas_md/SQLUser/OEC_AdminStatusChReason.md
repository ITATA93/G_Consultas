# SQLUser.OEC_AdminStatusChReason

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ASCR_RowId | bigint | PK |  | NO | - |
| ASCR_Code | varchar |  |  | NO | Code |
| ASCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ASCR_CreatedDate | date |  |  | SI | Created Date |
| ASCR_CreatedTime | time |  |  | SI | Created Time |
| ASCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ASCR_Desc | varchar |  |  | NO | Description |
| ASCR_Owner | varchar |  |  | SI | Owner |
| ASCR_UpdatedDate | date |  |  | SI | Updated Date |
| ASCR_UpdatedTime | time |  |  | SI | Updated Time |
| ASCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Lethal congenital abnormality |
| Q01ObsDR | - |  |  | SI | Lethal congenital abnormality DR |
| Q02 | - |  |  | SI | Rhesus isoimmunisation |
| Q02ObsDR | - |  |  | SI | Rhesus isoimmunisation DR |
| Q03 | - |  |  | SI | Non-isoimmunisation |
| Q03ObsDR | - |  |  | SI | Non-isoimmunisation DR |
| Q04 | - |  |  | SI | Birth trauma |
| Q04ObsDR | - |  |  | SI | Birth trauma DR |
| Q05 | - |  |  | SI | Antepartum anoxia |
| Q05ObsDR | - |  |  | SI | Antepartum anoxia DR |
| Q06 | - |  |  | SI | Intrapartum anoxia |
| Q06ObsDR | - |  |  | SI | Intrapartum anoxia DR |
| Q07 | - |  |  | SI | Lung maturity <27 weeks |
| Q07ObsDR | - |  |  | SI | Lung maturity <27 weeks DR |
| Q08 | - |  |  | SI | HMD with significant IVH |
| Q08ObsDR | - |  |  | SI | HMD with significant IVH DR |
| Q09 | - |  |  | SI | HMD without significant IVH |
| Q09ObsDR | - |  |  | SI | HMD without significant IVH DR |
| Q10 | - |  |  | SI | IVH in absence of potentially lethal HMD |
| Q10ObsDR | - |  |  | SI | IVH in absence of potentially lethal HMD DR |
| Q11 | - |  |  | SI | IVH in baby without HMD |
| Q11ObsDR | - |  |  | SI | IVH in baby without HMD DR |
| Q12 | - |  |  | SI | Subarachnoid haemorrhage |
| Q12ObsDR | - |  |  | SI | Subarachnoid haemorrhage DR |
| Q13 | - |  |  | SI | Subdural haemorrhage |
| Q13ObsDR | - |  |  | SI | Subdural haemorrhage DR |
| Q14 | - |  |  | SI | Intracerebral haemorrhage |
| Q14ObsDR | - |  |  | SI | Intracerebral haemorrhage DR |
| Q15 | - |  |  | SI | Necrotising enterocolitis |
| Q15ObsDR | - |  |  | SI | Necrotising enterocolitis DR |
| Q16 | - |  |  | SI | Infection - antenatal |
| Q16ObsDR | - |  |  | SI | Infection - antenatal DR |
| Q17 | - |  |  | SI | Infection - intrapartum |
| Q17ObsDR | - |  |  | SI | Infection - intrapartum DR |
| Q18 | - |  |  | SI | Infection - postnatal |
| Q18ObsDR | - |  |  | SI | Infection - postnatal DR |
| Q19 | - |  |  | SI | Disseminated intravascular coagulation |
| Q19ObsDR | - |  |  | SI | Disseminated intravascular coagulation DR |
| Q20 | - |  |  | SI | Massive intra-alveolar hemorrhage |
| Q20ObsDR | - |  |  | SI | Massive intra-alveolar hemorrhage DR |
| Q21 | - |  |  | SI | Haemorrhage - other |
| Q21ObsDR | - |  |  | SI | Haemorrhage - other DR |
| Q22 | - |  |  | SI | Other paediatric factors |
| Q23 | - |  |  | SI | Unexplained |
| Q24 | - |  |  | SI | Comments |
| Q25 | - |  |  | SI | Paediatric / Obstetric |
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