# questionnaire.QTCFCSTEMI

> Thrombolytic / Fibrinolytic Checklist for STEMI

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Thrombolytic / Fibrinolytic Checklist for STEMI

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Cannot be treated with primary percutaneous corona... |
| Q04 | varchar |  |  | SI | Chest pain for greater than 30 minutes and less th... |
| Q05 | varchar |  |  | SI | ECG |
| Q06 | varchar |  |  | SI | Persistent ST-elevation ≥ 1mm in 2 contiguous limb... |
| Q07 | varchar |  |  | SI | Persistent ST-elevation ≥ 2mm in 2 contiguous ches... |
| Q08 | varchar |  |  | SI | New or presumed new Left Bundle Branch Block (LBBB... |
| Q09 | varchar |  |  | SI | Myocardial infarct likely from history |
| Q10 | varchar |  |  | SI | If answered NO for any of the above questions pati... |
| Q11 | varchar |  |  | SI | Active bleeding or bleeding diathesis (excluding m... |
| Q12 | varchar |  |  | SI | Suspected aortic dissection |
| Q13 | varchar |  |  | SI | Significant closed head or facial trauma within 3 ... |
| Q14 | varchar |  |  | SI | Any prior intracranial haemorrhage |
| Q15 | varchar |  |  | SI | Ischaemic stroke within 3 months |
| Q16 | varchar |  |  | SI | Known cerebral vascular lesion |
| Q17 | varchar |  |  | SI | Known malignant intracranial neoplasm |
| Q18 | varchar |  |  | SI | If answered YES for any of the above questions pat... |
| Q19 | varchar |  |  | SI | Current anticoagulants (including novel anticoagul... |
| Q20 | varchar |  |  | SI | Non-compressible vascular puncture |
| Q21 | varchar |  |  | SI | Recent major surgery (<3 weeks) |
| Q22 | varchar |  |  | SI | Traumatic or prolonged (>10 minutes) CPR |
| Q23 | varchar |  |  | SI | Recent internal bleeding (within 4 weeks) / Active... |
| Q24 | varchar |  |  | SI | Suspected pericarditis |
| Q25 | varchar |  |  | SI | Advanced liver disease / Advanced metastatic cance... |
| Q26 | varchar |  |  | SI | History of chronic, severe, poorly controlled hype... |
| Q27 | varchar |  |  | SI | Severe uncontrolled hypertension on this presentat... |
| Q28 | varchar |  |  | SI | Ischaemic stroke > 3 months ago / known intracrani... |
| Q29 | varchar |  |  | SI | Pregnancy or within 1 week postpartum |
| Q30 | varchar |  |  | SI | If answered YES for any of the above questions pat... |
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