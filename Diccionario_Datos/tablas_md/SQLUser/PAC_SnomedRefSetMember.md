# SQLUser.PAC_SnomedRefSetMember

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNORFS_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Outcome |
| Q04 | - |  |  | SI | Message left |
| Q05 | - |  |  | SI | Person spoken to |
| Q06 | - |  |  | SI | Relationship |
| Q07 | - |  |  | SI | Call notes |
| Q08 | - |  |  | SI | Wound / Site of surgery status |
| Q09 | - |  |  | SI | Wound comments / advice given |
| Q10 | - |  |  | SI | Pain score |
| Q10ObsDR | - |  |  | SI | Pain score DR |
| Q11 | - |  |  | SI | Pain control |
| Q12 | - |  |  | SI | Sought additional pain medication |
| Q13 | - |  |  | SI | Pain comments / advice given |
| Q14 | - |  |  | SI | Nausea and vomiting |
| Q15 | - |  |  | SI | Nausea comments / advice given |
| Q16 | - |  |  | SI | Patients mobility post operatively |
| Q17 | - |  |  | SI | Compare mobility to pre-procedure baseline |
| Q18 | - |  |  | SI | Mobility comments / advice |
| Q19 | - |  |  | SI | Did you require further treatment after discharge? |
| Q20 | - |  |  | SI | Were you happy with your treatment on the day of y... |
| Q21 | - |  |  | SI | Were the information pamphlets given to you prior ... |
| Q22 | - |  |  | SI | Follow-up comments / advice given |
| Q23 | - |  |  | SI | Other outcome |
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
| SNORFS_CreatedDate | date |  |  | SI | Created Date |
| SNORFS_CreatedTime | time |  |  | SI | Created Time |
| SNORFS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNORFS_EffectiveDate | date |  |  | SI | Effective Date |
| SNORFS_Module_DR | bigint |  | FK | SI | Module ID |
| SNORFS_RefCompDesc | varchar |  |  | SI | Referenced Component Desription |
| SNORFS_RefSetType | varchar |  |  | SI | RefSet Type |
| SNORFS_RefSet_DR | bigint |  | FK | SI | RefSet ID |
| SNORFS_ReferencedComponent | varchar |  |  | SI | Referenced Component |
| SNORFS_Status | varchar |  |  | SI | Status |
| SNORFS_UUID | varchar |  |  | SI | UUID |
| SNORFS_UpdatedDate | date |  |  | SI | Updated Date |
| SNORFS_UpdatedTime | time |  |  | SI | Updated Time |
| SNORFS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*