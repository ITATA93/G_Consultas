# SQLUser.PAC_SnomedRefSetMemberAssoc

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNORFSAS_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Eye |
| Q04 | - |  |  | SI | Anaesthetic |
| Q05 | - |  |  | SI | Preparation and drape |
| Q06 | - |  |  | SI | Main incision |
| Q07 | - |  |  | SI | Other incision notes |
| Q08 | - |  |  | SI | Paracentesis |
| Q09 | - |  |  | SI | Other paracentesis notes |
| Q10 | - |  |  | SI | Continuous curvilinear capsulo-rhexis (CCC) |
| Q10a | - |  |  | SI | Continuous curvilinear capsulorhexis (CCC) |
| Q11 | - |  |  | SI | Hydrodissection |
| Q12 | - |  |  | SI | Phacoemulsification |
| Q13 | - |  |  | SI | Irrigation / Aspiration |
| Q14 | - |  |  | SI | Vision blue |
| Q15 | - |  |  | SI | Intraocular lens implant |
| Q16 | - |  |  | SI | Position |
| Q17 | - |  |  | SI | Toric lens |
| Q18 | - |  |  | SI | Axis of toric (degrees) |
| Q19 | - |  |  | SI | Aphakic |
| Q20 | - |  |  | SI | Viscoelastic out |
| Q21 | - |  |  | SI | Intracameral cephazolin |
| Q22 | - |  |  | SI | Wound hydration |
| Q23 | - |  |  | SI | Suture |
| Q24 | - |  |  | SI | Number of sutures |
| Q25 | - |  |  | SI | Type of sutures |
| Q26 | - |  |  | SI | Subconjunctival dexamethasone |
| Q27 | - |  |  | SI | Pad |
| Q28 | - |  |  | SI | Notes |
| Q29 | - |  |  | SI | IOL specification |
| Q30 | - |  |  | SI | IOL model |
| Q31 | - |  |  | SI | Power |
| Q32 | - |  |  | SI | Cylinder |
| Q33 | - |  |  | SI | IOL specification notes |
| Q34 | - |  |  | SI | Operation Complication(s) |
| Q35 | - |  |  | SI | Operation complication(s) |
| Q36 | - |  |  | SI | Operation complication notes |
| Q37 | - |  |  | SI | new annotated image |
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
| SNORFSAS_CreatedDate | date |  |  | SI | Created Date |
| SNORFSAS_CreatedTime | time |  |  | SI | Created Time |
| SNORFSAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNORFSAS_RefSetMember_DR | bigint |  | FK | SI | Des Ref PACSnomedRefSetMember |
| SNORFSAS_TargetConcept_DR | bigint |  | FK | SI | Target Concept |
| SNORFSAS_TargetRelation_DR | bigint |  | FK | SI | Target Relation |
| SNORFSAS_TargetTerm_DR | bigint |  | FK | SI | Target Term |
| SNORFSAS_UpdatedDate | date |  |  | SI | Updated Date |
| SNORFSAS_UpdatedTime | time |  |  | SI | Updated Time |
| SNORFSAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*