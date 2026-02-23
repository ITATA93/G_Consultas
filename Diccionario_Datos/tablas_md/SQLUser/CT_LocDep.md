# SQLUser.CT_LocDep

**Schema:** SQLUser
**Columnas:** 107
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLD_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| CTLD_Childsub | double |  |  | NO | Childsub |
| CTLD_CodeTableTags | varchar |  |  | SI | - |
| CTLD_CreatedDate | date |  |  | SI | Created Date |
| CTLD_CreatedTime | time |  |  | SI | Created Time |
| CTLD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTLD_DateFrom | date |  |  | SI | Effective date for the record |
| CTLD_DateTo | date |  |  | SI | Last day the record is active  |
| CTLD_Department_DR | bigint |  | FK | SI | Des Ref Department |
| CTLD_DocCourier_DR | bigint |  | FK | SI | The default Courier to use for Lab Doctors Reports... |
| CTLD_LocCourier_DR | bigint |  | FK | SI | The default Courier to use for Lab Doctors Reports... |
| CTLD_ReferringDoctorCourier_DR | bigint |  | FK | SI | The default Courier to use for Lab Doctors Reports... |
| CTLD_RowId | varchar |  |  | NO | - |
| CTLD_ThirdPartyCourier_DR | bigint |  | FK | SI | The default Courier to use for Lab Doctors Reports... |
| CTLD_UpdatedDate | date |  |  | SI | Updated Date |
| CTLD_UpdatedTime | time |  |  | SI | Updated Time |
| CTLD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ32DR | - |  |  | SI | Child Reference: Additional intubation attempt det... |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient consented |
| Q04 | - |  |  | SI | Barrier precautions used |
| Q05 | - |  |  | SI | Artificial airway prior to procedure |
| Q06 | - |  |  | SI | History relevant to intubation |
| Q07 | - |  |  | SI | Other history relevant to intubation |
| Q08 | - |  |  | SI | Pre-oxygenation |
| Q09 | - |  |  | SI | Bag mask ventilation |
| Q10 | - |  |  | SI | Two handed technique |
| Q11 | - |  |  | SI | Insertion date |
| Q12 | - |  |  | SI | Insertion time |
| Q13 | - |  |  | SI | Final airway type |
| Q14 | - |  |  | SI | Insertion reason |
| Q15 | - |  |  | SI | Other insertion reason |
| Q16 | - |  |  | SI | Laryngoscope |
| Q17 | - |  |  | SI | Grade of view - direct |
| Q18 | - |  |  | SI | Percentage of Glottic Opening (POGO) |
| Q19 | - |  |  | SI | Laryngoscope blade |
| Q20 | - |  |  | SI | Laryngoscope video blade |
| Q21 | - |  |  | SI | Airway adjuncts |
| Q22 | - |  |  | SI | ETT location |
| Q23 | - |  |  | SI | ETT type |
| Q24 | - |  |  | SI | ETT size (mm) |
| Q25 | - |  |  | SI | LMA type |
| Q26 | - |  |  | SI | LMA size (mm) |
| Q27 | - |  |  | SI | Tube passage |
| Q28 | - |  |  | SI | Double - lumen tube type |
| Q29 | - |  |  | SI | Double - lumen tube size (Fr) |
| Q30 | - |  |  | SI | Bronchial blocker type |
| Q31 | - |  |  | SI | Number of attempts |
| Q33 | - |  |  | SI | Post Procedure |
| Q34 | - |  |  | SI | Post-procedure checks |
| Q35 | - |  |  | SI | Airway device position checks |
| Q36 | - |  |  | SI | Airway device re-positioned |
| Q37 | - |  |  | SI | Post-procedure notes |
| Q38 | - |  |  | SI | Inserted by |
| Q39 | - |  |  | SI | Designation |
| Q40 | - |  |  | SI | Specialist present |
| Q41 | - |  |  | SI | Designation |
| Q43 | - |  |  | SI | Date |
| Q44 | - |  |  | SI | Time |
| Q45 | - |  |  | SI | Removal reason |
| Q46 | - |  |  | SI | Other removal reason |
| Q47 | - |  |  | SI | Removed by |
| Q48 | - |  |  | SI | Removal notes |
| Q49 | - |  |  | SI | Complications |
| Q50 | - |  |  | SI | Other complications |
| Q51 | - |  |  | SI | Complication notes |
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