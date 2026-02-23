# questionnaire.QTCHDP

> Haemodialysis Prescription

**Schema:** questionnaire
**Columnas:** 143
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Haemodialysis Prescription

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Height |
| Q03ObsDR | varchar |  | FK | SI | Height DR |
| Q04 | varchar |  |  | SI | Treatment mode |
| Q05 | varchar |  |  | SI | Ideal body weight |
| Q05ObsDR | varchar |  | FK | SI | Ideal body weight DR |
| Q06 | varchar |  |  | SI | Dry body weight (Renal only) |
| Q06ObsDR | varchar |  | FK | SI | Dry body weight (Renal only) DR |
| Q07 | varchar |  |  | SI | Height |
| Q07ObsDR | varchar |  | FK | SI | Height DR |
| Q08 | varchar |  |  | SI | Hours (HH:MM) |
| Q09 | varchar |  |  | SI | Other hours note |
| Q10 | varchar |  |  | SI | Observations notes |
| Q11 | varchar |  |  | SI | Dialyser |
| Q12 | varchar |  |  | SI | Other dialyser note |
| Q13 | varchar |  |  | SI | Dialysate |
| Q14 | varchar |  |  | SI | Other dialysate note |
| Q15 | varchar |  |  | SI | Dialysate temperature |
| Q16 | varchar |  |  | SI | Dialysate flow rate |
| Q17 | varchar |  |  | SI | Ultrafiltration (UF) parameters |
| Q18 | varchar |  |  | SI | Blood Volume Monitor (BVM) control |
| Q19 | varchar |  |  | SI | Heparin bolus (units) |
| Q20 | varchar |  |  | SI | Heparin rate (units/hr) |
| Q21 | varchar |  |  | SI | Heparin off time (HH:MM) |
| Q22 | varchar |  |  | SI | Heparin off time other |
| Q23 | numeric |  |  | SI | Clexane (mg) |
| Q24 | numeric |  |  | SI | Heparin (iu) |
| Q25 | varchar |  |  | SI | Fistula / Graft |
| Q26 | varchar |  |  | SI | Other fistula / graft notes |
| Q27 | varchar |  |  | SI | Fistula / Graft site |
| Q28 | varchar |  |  | SI | Other fistula / graft site notes |
| Q29 | varchar |  |  | SI | Permacath site |
| Q30 | varchar |  |  | SI | Other Permacath site notes |
| Q31 | varchar |  |  | SI | Fistula / Graft details |
| Q32 | varchar |  |  | SI | Argyle fistula cannula gauge |
| Q33 | varchar |  |  | SI | Other argyle fistula cannula |
| Q34 | varchar |  |  | SI | Single needle 15g |
| Q35 | numeric |  |  | SI | Heparin lumen lock A (ml) |
| Q36 | numeric |  |  | SI | Heparin lumen lock V (ml) |
| Q37 | varchar |  |  | SI | Lumen lock (ml) |
| Q38 | numeric |  |  | SI | BFR (Blood flow rate) ml/min |
| Q39 | varchar |  |  | SI | BFR ml/min |
| Q40 | varchar |  |  | SI | Special instructions |
| Q42 | varchar |  |  | SI | Treatment modality |
| Q43 | varchar |  |  | SI | Specify other treatment mode |
| Q44 | numeric |  |  | SI | Weight of wheelchair (kg) |
| Q45 | numeric |  |  | SI | Weight of prosthesis (kg) |
| Q46 | numeric |  |  | SI | Total sessions per week |
| Q47 | varchar |  |  | SI | Specify other dialyser |
| Q48 | varchar |  |  | SI | Citrate content is 1mmol/L and glucose content is ... |
| Q49 | varchar |  |  | SI | Glucose |
| Q50 | varchar |  |  | SI | Select bag |
| Q51 | varchar |  |  | SI | Potassium (K+) / Calcium (Ca++ ) - Acetate |
| Q52 | varchar |  |  | SI | Specify other Potassium (K+) / Calcium (Ca++ )- Ac... |
| Q53 | varchar |  |  | SI | Potassium (K+) / Calcium (Ca++ )- Citrate |
| Q54 | varchar |  |  | SI | Specify other Potassium (K+) / Calcium (Ca++ )- Ci... |
| Q55 | numeric |  |  | SI | Sodium (Na+) mmol/L |
| Q56 | numeric |  |  | SI | Bicarbonate (Bic) mmol/L |
| Q57 | varchar |  |  | SI | Dialysate flow rate |
| Q58 | varchar |  |  | SI | Ultrafiltration (UF) Parameters |
| Q59 | numeric |  |  | SI | Maximum Ultrafiltration Rate (UFR) mls |
| Q60 | numeric |  |  | SI | Maximum Isolated ultrafiltration (ISO) mls |
| Q61 | varchar |  |  | SI | Haemo scan |
| Q62 | varchar |  |  | SI | Haemo control |
| Q63 | numeric |  |  | SI | Blood volume (- mls) |
| Q64 | varchar |  |  | SI | Type |
| Q65 | varchar |  |  | SI | Nil - give reason |
| Q66 | varchar |  |  | SI | Notes |
| Q67 | varchar |  |  | SI | Dialysis access location |
| Q68 | varchar |  |  | SI | New fistula cannulation regime |
| Q69 | varchar |  |  | SI | Refer to new fistula cannulation policy |
| Q70 | varchar |  |  | SI | Access notes |
| Q71 | varchar |  |  | SI | Cannulation |
| Q72 | varchar |  |  | SI | Needle type |
| Q73 | varchar |  |  | SI | Needle size - Arterial |
| Q74 | varchar |  |  | SI | Needle size - Venous |
| Q75 | varchar |  |  | SI | Specify other needle size |
| Q76 | varchar |  |  | SI | Local anaesthetic  |
| Q77 | varchar |  |  | SI | Additional Instructions |
| Q78 | varchar |  |  | SI | Please review medication chart for pre or post med... |
| Q79 | varchar |  |  | SI | Blood Glucose Levels (BGL) |
| Q80 | varchar |  |  | SI | Pressure injury device |
| Q81 | varchar |  |  | SI | Body water amputees calculation |
| Q82 | varchar |  |  | SI | Nursing / Cultural considerations |
| Q83 | varchar |  |  | SI | Registered Nurse (RN) name |
| Q84 | longvarbinary |  |  | SI | Signature |
| Q84UDt | date |  |  | SI | Signature Last Updated Date |
| Q84UTm | time |  |  | SI | Signature Last Updated Time |
| Q85 | varchar |  |  | SI | Clinical Nurse Specialist (CNS) name |
| Q86 | longvarbinary |  |  | SI | Signature |
| Q86UDt | date |  |  | SI | Signature Last Updated Date |
| Q86UTm | time |  |  | SI | Signature Last Updated Time |
| Q87 | varchar |  |  | SI | Doctor name |
| Q88 | longvarbinary |  |  | SI | Signature |
| Q88UDt | date |  |  | SI | Signature Last Updated Date |
| Q88UTm | time |  |  | SI | Signature Last Updated Time |
| Q89 | varchar |  |  | SI | Dialysate temperature |
| Q90 | varchar |  |  | SI | Ultrafiltration (UF) parameters |
| Q91 | varchar |  |  | SI | Other dialysis access location notes |
| Q92 | varchar |  |  | SI | Argyle fistula cannula gauge |
| Q93 | varchar |  |  | SI | Other needle size notes |
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