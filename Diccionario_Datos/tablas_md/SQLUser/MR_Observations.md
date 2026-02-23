# SQLUser.MR_Observations

**Schema:** SQLUser
**Columnas:** 154
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Observaciones**. Datos de observación clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBS_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| OBS_BottleChanged | varchar |  |  | SI | BottleChanged  |
| OBS_BottleCount | double |  |  | SI | BottleCount   |
| OBS_BottleSession | double |  |  | SI | Bottle session value ( current bottle total - prev... |
| OBS_BottleValue | double |  |  | SI | BottleValue   |
| OBS_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| OBS_Childsub | double |  |  | NO | Childsub |
| OBS_CollectionStatus | varchar |  |  | SI | Collection Status |
| OBS_Consult_DR | varchar |  | FK | SI | Des Ref Consult |
| OBS_CopiedSource_DR | varchar |  | FK | SI | CopiedSource |
| OBS_Date | date |  |  | SI | Date |
| OBS_Device_DR | bigint |  | FK | SI | Des Ref CTMonitoringDevice |
| OBS_EWSScore | double |  |  | SI | EWSScore  |
| OBS_Entry_DR | varchar |  | FK | SI | Des Ref Observ Entry |
| OBS_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| OBS_ExternalId | varchar |  |  | SI | A reference to external systems |
| OBS_IsPartogram | varchar |  |  | SI | IsPartogram |
| OBS_IsPregnant | varchar |  |  | SI | Was the Patient Pregnant at the time of the observ... |
| OBS_IsSystemCalculatedIVFB | varchar |  |  | SI | Is System Calculated IV Fluid Balance |
| OBS_Item_DR | bigint |  | FK | SI | Des Ref Observ Item |
| OBS_LongDescription | varchar |  |  | SI | Long Description |
| OBS_OBSStatus_DR | bigint |  | FK | SI | Des Ref OBSStatus |
| OBS_OEExec_DR | varchar |  | FK | SI | Des Ref OEExec |
| OBS_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref ReasonForCorrection |
| OBS_RowId | varchar |  |  | NO | - |
| OBS_ShortDesc | varchar |  |  | SI | Short Description |
| OBS_Time | time |  |  | SI | Time |
| OBS_UniqueId | varchar |  |  | SI | Unique Identifier |
| OBS_UpdateDate | date |  |  | SI | UpdateDate |
| OBS_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| OBS_UpdateTime | time |  |  | SI | UpdateTime |
| OBS_User_DR | bigint |  | FK | SI | Des Ref User |
| OBS_Value | varchar |  |  | SI | Value |
| OBS_Verified | varchar |  |  | SI | Verified |
| Q01 | - |  |  | SI | Menarche |
| Q01ObsDR | - |  |  | SI | Menarche DR |
| Q02 | - |  |  | SI | since |
| Q03 | - |  |  | SI | Menstruation |
| Q03ObsDR | - |  |  | SI | Menstruation DR |
| Q04 | - |  |  | SI | Normal length of cycle |
| Q04ObsDR | - |  |  | SI | Normal length of cycle DR |
| Q05 | - |  |  | SI | Nature of periods |
| Q05ObsDR | - |  |  | SI | Nature of periods DR |
| Q06 | - |  |  | SI | Pain score (0 to 10) |
| Q06ObsDR | - |  |  | SI | Pain score (0 to 10) DR |
| Q07 | - |  |  | SI | Date of last menstruation |
| Q08 | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Past pregnancies |
| Q10 | - |  |  | SI | Full term |
| Q10ObsDR | - |  |  | SI | Full term DR |
| Q10a | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Number of living child |
| Q11ObsDR | - |  |  | SI | Number of living child DR |
| Q11a | - |  |  | SI | Note |
| Q12 | - |  |  | SI | Miscarriage |
| Q12ObsDR | - |  |  | SI | Miscarriage DR |
| Q12a | - |  |  | SI | Note |
| Q13 | - |  |  | SI | Previous abortions |
| Q13ObsDR | - |  |  | SI | Previous abortions DR |
| Q13a | - |  |  | SI | Note |
| Q18 | - |  |  | SI | PARA |
| Q18ObsDR | - |  |  | SI | PARA DR |
| Q19 | - |  |  | SI | Current pregnancy |
| Q19ObsDR | - |  |  | SI | Current pregnancy DR |
| Q20 | - |  |  | SI | Menopause |
| Q20ObsDR | - |  |  | SI | Menopause DR |
| Q20a | - |  |  | SI | since |
| Q23 | - |  |  | SI | Hormone replacement therapy (HRT) |
| Q23ObsDR | - |  |  | SI | Hormone replacement therapy (HRT) DR |
| Q23a | - |  |  | SI | Note |
| Q25 | - |  |  | SI | Progestogens |
| Q25ObsDR | - |  |  | SI | Progestogens DR |
| Q25a | - |  |  | SI | Note |
| Q27 | - |  |  | SI | Dyspareunia |
| Q27ObsDR | - |  |  | SI | Dyspareunia DR |
| Q28 | - |  |  | SI | Last cervical smear date |
| Q29 | - |  |  | SI | Cervical smear result |
| Q29ObsDR | - |  |  | SI | Cervical smear result DR |
| Q29a | - |  |  | SI | Note |
| Q31 | - |  |  | SI | Previous episodes of genital or pelvic inflammatio... |
| Q31ObsDR | - |  |  | SI | Previous episodes of genital or pelvic inflammatio... |
| Q31a | - |  |  | SI | Note |
| Q33 | - |  |  | SI | Sexually transmitted diseases |
| Q33ObsDR | - |  |  | SI | Sexually transmitted diseases DR |
| Q33a | - |  |  | SI | Note |
| Q35 | - |  |  | SI | Last gynaecological examination date |
| Q35a | - |  |  | SI | Note |
| Q37 | - |  |  | SI | Involuntary infertility support. 2 years (diagnose... |
| Q38 | - |  |  | SI | Weight trend |
| Q38ObsDR | - |  |  | SI | Weight trend DR |
| Q40 | - |  |  | SI | Weight difference in kg |
| Q40ObsDR | - |  |  | SI | Weight difference in kg DR |
| Q40a | - |  |  | SI | since |
| Q40b | - |  |  | SI | Note |
| Q42 | - |  |  | SI | Bowel movements |
| Q42ObsDR | - |  |  | SI | Bowel movements DR |
| Q43 | - |  |  | SI | Urinary frequency |
| Q43ObsDR | - |  |  | SI | Urinary frequency DR |
| Q44 | - |  |  | SI | Urinary incontinence |
| Q44ObsDR | - |  |  | SI | Urinary incontinence DR |
| Q45 | - |  |  | SI | Urinary catheter |
| Q45ObsDR | - |  |  | SI | Urinary catheter DR |
| Q46 | - |  |  | SI | Urinary incontinence pads |
| Q46ObsDR | - |  |  | SI | Urinary incontinence pads DR |
| Q47 | - |  |  | SI | Premature or overdue |
| Q47ObsDR | - |  |  | SI | Premature or overdue DR |
| Q47a | - |  |  | SI | Note |
| Q48 | - |  |  | SI | Contraception |
| Q48N | - |  |  | SI | Note |
| Q48ObsDR | - |  |  | SI | Contraception DR |
| Q50 | - |  |  | SI | Prior treatment for infertility |
| Q50N | - |  |  | SI | Note |
| Q52 | - |  |  | SI | Date of last HPV Test |
| Q53 | - |  |  | SI | Date of Last Pelvic Exam |
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