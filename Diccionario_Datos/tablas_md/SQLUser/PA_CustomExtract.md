# SQLUser.PA_CustomExtract

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EX_RowId | bigint | PK |  | NO | - |
| EX_CustomExtract_DR | bigint |  | FK | SI | Des Ref PAC CustomExtract |
| EX_DateFrom | date |  |  | SI | Date From |
| EX_DateRun | date |  |  | SI | Date Run |
| EX_DateTo | date |  |  | SI | Date To |
| EX_Number | varchar |  |  | SI | Number |
| EX_Status | varchar |  |  | SI | Status |
| EX_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Dyspnoea on exertion |
| Q04 | - |  |  | SI | Palpitation |
| Q05 | - |  |  | SI | Tiredness |
| Q06 | - |  |  | SI | Preference for heat |
| Q07 | - |  |  | SI | Preference for cold |
| Q08 | - |  |  | SI | Excessive sweating |
| Q09 | - |  |  | SI | Nervousness |
| Q10 | - |  |  | SI | Increased appetite |
| Q11 | - |  |  | SI | Decreased appetite |
| Q12 | - |  |  | SI | Increased weight |
| Q13 | - |  |  | SI | Decreased weight |
| Q14 | - |  |  | SI | Palpable thyroid |
| Q15 | - |  |  | SI | Bruit over thyroid |
| Q16 | - |  |  | SI | Exophthalmos |
| Q17 | - |  |  | SI | Lid retraction |
| Q18 | - |  |  | SI | Lid lag |
| Q19 | - |  |  | SI | Hyperkinesis |
| Q20 | - |  |  | SI | Hands: hot |
| Q21 | - |  |  | SI | Hands: moist |
| Q22 | - |  |  | SI | Casual pulse rate > 80/min |
| Q23 | - |  |  | SI | Casual pulse rate > 90/min |
| Q24 | - |  |  | SI | Atrial fibrillation |
| Q25 | - |  |  | SI | Score |
| Q26 | - |  |  | SI | Classification |
| Q27 | - |  |  | SI | > 19 |
| Q28 | - |  |  | SI | Toxic hyperthyroidism |
| Q29 | - |  |  | SI | 11 - 19 |
| Q30 | - |  |  | SI | Equivocal |
| Q31 | - |  |  | SI | < 11 |
| Q32 | - |  |  | SI | Euthyroidism |
| Q33 | - |  |  | SI | > 19: Toxic hyperthyroidism |
| Q34 | - |  |  | SI | 11 - 19: Equivocal |
| Q35 | - |  |  | SI | < 11: Euthyroidism |
| Q36 | - |  |  | SI | It is a diagnostic index that scores the presence ... |
| Q37 | - |  |  | SI | The Wayne’s score is a clinical score that may be ... |
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