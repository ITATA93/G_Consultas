# SQLUser.PAC_BedDepartmentAllocation

**Schema:** SQLUser
**Columnas:** 132
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEP_ParRef | varchar | PK |  | NO | PAC_Bed Parent Reference |
| ChildQ06DR | - |  |  | SI | Child Reference: Daily Assessment |
| DEP_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DEP_Childsub | double |  |  | NO | Childsub |
| DEP_CreatedDate | date |  |  | SI | Created Date |
| DEP_CreatedTime | time |  |  | SI | Created Time |
| DEP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEP_DateFrom | date |  |  | NO | Date From |
| DEP_DateTo | date |  |  | SI | Date To |
| DEP_RowId | varchar |  |  | NO | - |
| DEP_UpdatedDate | date |  |  | SI | Updated Date |
| DEP_UpdatedTime | time |  |  | SI | Updated Time |
| DEP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Insertion date |
| Q02 | - |  |  | SI | Insertion time |
| Q03 | - |  |  | SI | Removal date |
| Q04 | - |  |  | SI | Removal time |
| Q05 | - |  |  | SI | Procedure notes |
| Q07 | - |  |  | SI | Size |
| Q08 | - |  |  | SI | Types |
| Q09 | - |  |  | SI | Emergency equipment in room |
| Q10 | - |  |  | SI | Securing device |
| Q10ObsDR | - |  |  | SI | Securing device DR |
| Q11 | - |  |  | SI | Inner cannula in situ |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | Time |
| Q14 | - |  |  | SI | Current Insertion Details |
| Q15 | - |  |  | SI | Insertion status |
| Q16 | - |  |  | SI | Pre Procedure Checklist |
| Q17 | - |  |  | SI | Tracheostomy Safety Checklist |
| Q18 | - |  |  | SI | Consent completed |
| Q19 | - |  |  | SI | Coagulation (INR <1.5, APTT < 50) or factors admin... |
| Q20 | - |  |  | SI | Platelets > 50 x 10<sup>9</sup> (or platelets tran... |
| Q21 | - |  |  | SI | Fraction of inspired oxygen (FiO2) ≥ 0.6 |
| Q22 | - |  |  | SI | Positive end-expiratory pressure (PEEP) ≤ 10cmH2O |
| Q23 | - |  |  | SI | Cervical spine stable |
| Q24 | - |  |  | SI | Site examined (nil infection, masses, acceptable a... |
| Q25 | - |  |  | SI | Bronchoscope available and working |
| Q26 | - |  |  | SI | End-tidal carbon dioxide (ETCO2) monitor available... |
| Q27 | - |  |  | SI | Feeds stopped > 4hrs ago |
| Q28 | - |  |  | SI | Difficult airway equipment available |
| Q29 | - |  |  | SI | Grade of previous intubation |
| Q30 | - |  |  | SI | Safety check notes |
| Q31 | - |  |  | SI | Pre Insertion Checks |
| Q32 | - |  |  | SI | Insertion site assessed and marked if appropriate |
| Q33 | - |  |  | SI | Barrier precautions used |
| Q34 | - |  |  | SI | Aseptic technique used |
| Q35 | - |  |  | SI | Skin disinfected with |
| Q36 | - |  |  | SI | Pre-procedure notes |
| Q37 | - |  |  | SI | Insertion Details |
| Q38 | - |  |  | SI | Reason for insertion |
| Q39 | - |  |  | SI | Indication for tracheostomy tube change |
| Q40 | - |  |  | SI | Type |
| Q41 | - |  |  | SI | Brand |
| Q42 | - |  |  | SI | Size of tracheostomy tube (mm) |
| Q43 | - |  |  | SI | Chest x-ray post procedure viewed and checked |
| Q44 | - |  |  | SI | Inserted by |
| Q45 | - |  |  | SI | Airway operator |
| Q46 | - |  |  | SI | Emergency Equipment in Room / Available |
| Q47 | - |  |  | SI | Tracheostomy tube of same size and type |
| Q48 | - |  |  | SI | Tracheostomy tube of same type but one size smalle... |
| Q49 | - |  |  | SI | Tracheal dilators |
| Q50 | - |  |  | SI | Bag valve mask |
| Q51 | - |  |  | SI | Suction equipment |
| Q52 | - |  |  | SI | Spare inner cannula |
| Q53 | - |  |  | SI | Dummy1 |
| Q54 | - |  |  | SI | Dummy2 |
| Q55 | - |  |  | SI | Equipment notes |
| Q56 | - |  |  | SI | Tracheostomy Tube Change Record |
| Q57 | - |  |  | SI | Date |
| Q58 | - |  |  | SI | Time |
| Q59 | - |  |  | SI | Consent |
| Q60 | - |  |  | SI | Indication for tracheostomy tube change |
| Q61 | - |  |  | SI | Other change indication |
| Q62 | - |  |  | SI | Type of tracheostomy tube |
| Q63 | - |  |  | SI | Size of tracheostomy tube |
| Q64 | - |  |  | SI | Cuffed |
| Q65 | - |  |  | SI | Fenestrated |
| Q66 | - |  |  | SI | Chest x-ray post procedure to confirm placement |
| Q67 | - |  |  | SI | Care provider 1 |
| Q68 | - |  |  | SI | Care provider 2 |
| Q69 | - |  |  | SI | Procedure notes |
| Q71 | - |  |  | SI | Assessments |
| Q72 | - |  |  | SI | Indications for removal |
| Q73 | - |  |  | SI | Other removal reason |
| Q74 | - |  |  | SI | Consent obtained |
| Q75 | - |  |  | SI | Removed by |
| Q76 | - |  |  | SI | Removal notes |
| Q77 | - |  |  | SI | Complications |
| Q78 | - |  |  | SI | Complication |
| Q79 | - |  |  | SI | Other complication |
| Q80 | - |  |  | SI | Complication notes |
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