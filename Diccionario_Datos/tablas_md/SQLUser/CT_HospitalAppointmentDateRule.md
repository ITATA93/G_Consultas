# SQLUser.CT_HospitalAppointmentDateRule

**Schema:** SQLUser
**Columnas:** 145
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APDR_ParRef | bigint | PK |  | NO | CT_Hospital Parent Reference |
| APDR_AppointmentARCIM_DR | varchar |  | FK | SI | Appointment, Des Ref ARCItmMast |
| APDR_CheckLastDaysFrom | integer |  |  | SI | Check Last Days From |
| APDR_CheckLastDaysTo | integer |  |  | SI | Check Last Days To |
| APDR_Childsub | double |  |  | NO | Childsub |
| APDR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APDR_CreatedDate | date |  |  | SI | Created Date |
| APDR_CreatedTime | time |  |  | SI | Created Time |
| APDR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APDR_DateFrom | date |  |  | SI | Date From |
| APDR_DateTo | date |  |  | SI | Date To |
| APDR_NotFound | varchar |  |  | SI | Appointment Not found |
| APDR_PrimaryAppointARCIM_DR | varchar |  | FK | SI | Primary Appointment, Des Ref ARCItmMast |
| APDR_Rowid | varchar |  |  | NO | - |
| APDR_SameCareProvider | varchar |  |  | SI | Same Care Provider |
| APDR_SameLocation | varchar |  |  | SI | Same Location |
| APDR_UpdatedDate | date |  |  | SI | Updated Date |
| APDR_UpdatedTime | time |  |  | SI | Updated Time |
| APDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ78DR | - |  |  | SI | Child Reference: Eyes open, firm surface |
| Q01 | - |  |  | SI | Date of examination |
| Q02 | - |  |  | SI | Symptoms are getting |
| Q03 | - |  |  | SI | Description of spells |
| Q04 | - |  |  | SI | If other, specify |
| Q05 | - |  |  | SI | Length of time spells occur |
| Q06 | - |  |  | SI | If other, specify |
| Q07 | - |  |  | SI | What increases symptoms? |
| Q08 | - |  |  | SI | What decreases symptoms? |
| Q09 | - |  |  | SI | Hearing impairments |
| Q10 | - |  |  | SI | If other, specify |
| Q11 | - |  |  | SI | Changes in hearing since onset |
| Q12 | - |  |  | SI | If other, specify |
| Q13 | - |  |  | SI | Visual changes since onset |
| Q14 | - |  |  | SI | If other, specify |
| Q15 | - |  |  | SI | Recent falls |
| Q16 | - |  |  | SI | If other, specify |
| Q17 | - |  |  | SI | History of migraines |
| Q18 | - |  |  | SI | If other, specify |
| Q19 | - |  |  | SI | Previous treatments |
| Q20 | - |  |  | SI | Vestibulo-Ocular Reflex (VOR) head thrust |
| Q21 | - |  |  | SI | Spontaneous nystagmus |
| Q22 | - |  |  | SI | Gaze-evoked nystagmus with fixation present |
| Q23 | - |  |  | SI | VOR head thrust (posterior canal function) |
| Q24 | - |  |  | SI | Primary |
| Q25 | - |  |  | SI | Right |
| Q26 | - |  |  | SI | Left |
| Q27 | - |  |  | SI | Post-horizontal head-shaking nystagmus (+/-) |
| Q28 | - |  |  | SI | Gaze-evoked nystagmus with fixation suppressed |
| Q29 | - |  |  | SI | Direction |
| Q30 | - |  |  | SI | Primary |
| Q31 | - |  |  | SI | Right |
| Q32 | - |  |  | SI | Left |
| Q33 | - |  |  | SI | Heave test (L) |
| Q34 | - |  |  | SI | Heave test (R) |
| Q35 | - |  |  | SI | Smooth pursuit |
| Q36 | - |  |  | SI | Saccades |
| Q37 | - |  |  | SI | Vestibulo-Ocular Reflex (VOR) cancellation |
| Q38 | - |  |  | SI | Static visual acuity using LogMAR scale |
| Q39 | - |  |  | SI | Dynamic visual acuity |
| Q40 | - |  |  | SI | Other oculomotor / vestibular test |
| Q41 | - |  |  | SI | Left Hallpike (+/-) |
| Q42 | - |  |  | SI | Right Hallpike (+/-) |
| Q43 | - |  |  | SI | Roll test (+/-) |
| Q44 | - |  |  | SI | Comments |
| Q45 | - |  |  | SI | Dizziness Handicap Inventory (DHI) |
| Q46 | - |  |  | SI | Dynamic Gait Index (DGI) |
| Q47 | - |  |  | SI | Berg balance score |
| Q48 | - |  |  | SI | Timed Up and Go (TUG) test |
| Q49 | - |  |  | SI | Activities-specific Balance Confidence (ABC) scale |
| Q50 | - |  |  | SI | Motion Sensitivity Quotient (MSQ) |
| Q51 | - |  |  | SI | Other |
| Q52 | - |  |  | SI | Cervical spine complaints |
| Q53 | - |  |  | SI | Cervical pain |
| Q54 | - |  |  | SI | Cervical spine Range of Motion (ROM) |
| Q55 | - |  |  | SI | If impaired, specify |
| Q56 | - |  |  | SI | Lower Extremities Range of Motion (ROM) |
| Q57 | - |  |  | SI | Hip (L) |
| Q58 | - |  |  | SI | Hip (R) |
| Q59 | - |  |  | SI | Knee (L) |
| Q60 | - |  |  | SI | Knee (R) |
| Q61 | - |  |  | SI | Ankle (L) |
| Q62 | - |  |  | SI | Ankle (R) |
| Q63 | - |  |  | SI | Lower Extremities Strength |
| Q64 | - |  |  | SI | Hip (L) |
| Q65 | - |  |  | SI | Hip (R) |
| Q66 | - |  |  | SI | Knee Extension (L) |
| Q67 | - |  |  | SI | Knee Extension (R) |
| Q68 | - |  |  | SI | Ankle (L) |
| Q69 | - |  |  | SI | Ankle (R) |
| Q70 | - |  |  | SI | Posture |
| Q71 | - |  |  | SI | Light touch |
| Q72 | - |  |  | SI | If impaired / absent, specify |
| Q73 | - |  |  | SI | Rapid alt movements |
| Q74 | - |  |  | SI | Heel to shin |
| Q75 | - |  |  | SI | Finger to nose |
| Q76 | - |  |  | SI | Past pointing |
| Q77 | - |  |  | SI | Clinical Test of Sensory Interaction for Balance (... |
| Q82 | - |  |  | SI | Gait |
| Q83 | - |  |  | SI | Problem list / functional limitations |
| Q84 | - |  |  | SI | If others, specify |
| Q85 | - |  |  | SI | Treatment plan (this is only a plan, you need to p... |
| Q86 | - |  |  | SI | If other plan, specify |
| Q87 | - |  |  | SI | Gaze-evoked nystagmus with fixation present (1st D... |
| Q88 | - |  |  | SI | Date |
| Q89 | - |  |  | SI | Time |
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