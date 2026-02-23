# SQLUser.PAC_AdmSourceDet

**Schema:** SQLUser
**Columnas:** 161
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PAC_AdmSource Parent Reference |
| DET_AdmReason | varchar |  |  | SI | AdmReason |
| DET_CareType | varchar |  |  | SI | CareType |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | DateFrom |
| DET_DateTo | date |  |  | SI | DateTo |
| DET_EpisodeType | varchar |  |  | SI | EpisodeType |
| DET_InpatAdmType | varchar |  |  | SI | InpatAdmType |
| DET_IntentReadmit | varchar |  |  | SI | IntentReadmit |
| DET_QualificationStatus | varchar |  |  | SI | QualificationStatus |
| DET_ReasonForCritCareTransfe | varchar |  |  | SI | ReasonForCritCareTransfer |
| DET_RowId | varchar |  |  | NO | - |
| DET_TransferSource | varchar |  |  | SI | TransferSource |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Height |
| Q03ObsDR | - |  |  | SI | Height DR |
| Q04 | - |  |  | SI | Treatment mode |
| Q05 | - |  |  | SI | Ideal body weight |
| Q05ObsDR | - |  |  | SI | Ideal body weight DR |
| Q06 | - |  |  | SI | Dry body weight (Renal only) |
| Q06ObsDR | - |  |  | SI | Dry body weight (Renal only) DR |
| Q07 | - |  |  | SI | Height |
| Q07ObsDR | - |  |  | SI | Height DR |
| Q08 | - |  |  | SI | Hours (HH:MM) |
| Q09 | - |  |  | SI | Other hours note |
| Q10 | - |  |  | SI | Observations notes |
| Q11 | - |  |  | SI | Dialyser |
| Q12 | - |  |  | SI | Other dialyser note |
| Q13 | - |  |  | SI | Dialysate |
| Q14 | - |  |  | SI | Other dialysate note |
| Q15 | - |  |  | SI | Dialysate temperature |
| Q16 | - |  |  | SI | Dialysate flow rate |
| Q17 | - |  |  | SI | Ultrafiltration (UF) parameters |
| Q18 | - |  |  | SI | Blood Volume Monitor (BVM) control |
| Q19 | - |  |  | SI | Heparin bolus (units) |
| Q20 | - |  |  | SI | Heparin rate (units/hr) |
| Q21 | - |  |  | SI | Heparin off time (HH:MM) |
| Q22 | - |  |  | SI | Heparin off time other |
| Q23 | - |  |  | SI | Clexane (mg) |
| Q24 | - |  |  | SI | Heparin (iu) |
| Q25 | - |  |  | SI | Fistula / Graft |
| Q26 | - |  |  | SI | Other fistula / graft notes |
| Q27 | - |  |  | SI | Fistula / Graft site |
| Q28 | - |  |  | SI | Other fistula / graft site notes |
| Q29 | - |  |  | SI | Permacath site |
| Q30 | - |  |  | SI | Other Permacath site notes |
| Q31 | - |  |  | SI | Fistula / Graft details |
| Q32 | - |  |  | SI | Argyle fistula cannula gauge |
| Q33 | - |  |  | SI | Other argyle fistula cannula |
| Q34 | - |  |  | SI | Single needle 15g |
| Q35 | - |  |  | SI | Heparin lumen lock A (ml) |
| Q36 | - |  |  | SI | Heparin lumen lock V (ml) |
| Q37 | - |  |  | SI | Lumen lock (ml) |
| Q38 | - |  |  | SI | BFR (Blood flow rate) ml/min |
| Q39 | - |  |  | SI | BFR ml/min |
| Q40 | - |  |  | SI | Special instructions |
| Q42 | - |  |  | SI | Treatment modality |
| Q43 | - |  |  | SI | Specify other treatment mode |
| Q44 | - |  |  | SI | Weight of wheelchair (kg) |
| Q45 | - |  |  | SI | Weight of prosthesis (kg) |
| Q46 | - |  |  | SI | Total sessions per week |
| Q47 | - |  |  | SI | Specify other dialyser |
| Q48 | - |  |  | SI | Citrate content is 1mmol/L and glucose content is ... |
| Q49 | - |  |  | SI | Glucose |
| Q50 | - |  |  | SI | Select bag |
| Q51 | - |  |  | SI | Potassium (K+) / Calcium (Ca++ ) - Acetate |
| Q52 | - |  |  | SI | Specify other Potassium (K+) / Calcium (Ca++ )- Ac... |
| Q53 | - |  |  | SI | Potassium (K+) / Calcium (Ca++ )- Citrate |
| Q54 | - |  |  | SI | Specify other Potassium (K+) / Calcium (Ca++ )- Ci... |
| Q55 | - |  |  | SI | Sodium (Na+) mmol/L |
| Q56 | - |  |  | SI | Bicarbonate (Bic) mmol/L |
| Q57 | - |  |  | SI | Dialysate flow rate |
| Q58 | - |  |  | SI | Ultrafiltration (UF) Parameters |
| Q59 | - |  |  | SI | Maximum Ultrafiltration Rate (UFR) mls |
| Q60 | - |  |  | SI | Maximum Isolated ultrafiltration (ISO) mls |
| Q61 | - |  |  | SI | Haemo scan |
| Q62 | - |  |  | SI | Haemo control |
| Q63 | - |  |  | SI | Blood volume (- mls) |
| Q64 | - |  |  | SI | Type |
| Q65 | - |  |  | SI | Nil - give reason |
| Q66 | - |  |  | SI | Notes |
| Q67 | - |  |  | SI | Dialysis access location |
| Q68 | - |  |  | SI | New fistula cannulation regime |
| Q69 | - |  |  | SI | Refer to new fistula cannulation policy |
| Q70 | - |  |  | SI | Access notes |
| Q71 | - |  |  | SI | Cannulation |
| Q72 | - |  |  | SI | Needle type |
| Q73 | - |  |  | SI | Needle size - Arterial |
| Q74 | - |  |  | SI | Needle size - Venous |
| Q75 | - |  |  | SI | Specify other needle size |
| Q76 | - |  |  | SI | Local anaesthetic |
| Q77 | - |  |  | SI | Additional Instructions |
| Q78 | - |  |  | SI | Please review medication chart for pre or post med... |
| Q79 | - |  |  | SI | Blood Glucose Levels (BGL) |
| Q80 | - |  |  | SI | Pressure injury device |
| Q81 | - |  |  | SI | Body water amputees calculation |
| Q82 | - |  |  | SI | Nursing / Cultural considerations |
| Q83 | - |  |  | SI | Registered Nurse (RN) name |
| Q84 | - |  |  | SI | Signature |
| Q84UDt | - |  |  | SI | Signature Last Updated Date |
| Q84UTm | - |  |  | SI | Signature Last Updated Time |
| Q85 | - |  |  | SI | Clinical Nurse Specialist (CNS) name |
| Q86 | - |  |  | SI | Signature |
| Q86UDt | - |  |  | SI | Signature Last Updated Date |
| Q86UTm | - |  |  | SI | Signature Last Updated Time |
| Q87 | - |  |  | SI | Doctor name |
| Q88 | - |  |  | SI | Signature |
| Q88UDt | - |  |  | SI | Signature Last Updated Date |
| Q88UTm | - |  |  | SI | Signature Last Updated Time |
| Q89 | - |  |  | SI | Dialysate temperature |
| Q90 | - |  |  | SI | Ultrafiltration (UF) parameters |
| Q91 | - |  |  | SI | Other dialysis access location notes |
| Q92 | - |  |  | SI | Argyle fistula cannula gauge |
| Q93 | - |  |  | SI | Other needle size notes |
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