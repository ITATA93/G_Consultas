# questionnaire.QGXXXBECKSD

> Beck's Depression

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Beck's Depression

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q22 | varchar |  |  | SI | 0 - 13: minimal depression |
| Q23 | varchar |  |  | SI | 14 - 19: mild depression |
| Q24 | varchar |  |  | SI | 20 - 28: moderate depression |
| Q25 | varchar |  |  | SI | 29 - 63: severe depression |
| Q26 | varchar |  |  | SI | The Beck Depression Inventory BDI is a self-report... |
| Q27 | varchar |  |  | SI | BDI-II contains 21 questions, each answer being sc... |
| Q28 | date |  |  | SI | Date |
| Q29 | time |  |  | SI | Time |
| Q30 | varchar |  |  | SI | Beck, A.T., Ward, C. H., Mendelson, M., Mock, J., ... |
| Q31 | varchar |  |  | SI | Beck, A. T., Steer, R.A., and Garbin, M.G. (1988) ... |
| Q32 | varchar |  |  | SI | Groth-Marnat G. (1990). The handbook of psychologi... |
| Q33 | varchar |  |  | SI | Hojat, M., Shapurian, R., Mehrya, A.H., (1986). Ps... |
| Q34 | varchar |  |  | SI | Steer, R. A., Rissmiller, D. J. and Beck, A.T., (2... |
| QApp | varchar |  |  | SI | Appearance |
| QAppe | varchar |  |  | SI | Appetite |
| QCry | varchar |  |  | SI | Crying |
| QDec | varchar |  |  | SI | Decisions |
| QDis | varchar |  |  | SI | Discouragement |
| QDisa | varchar |  |  | SI | Disappointment |
| QFai | varchar |  |  | SI | Failure |
| QGui | varchar |  |  | SI | Guilt |
| QInt | varchar |  |  | SI | Interest |
| QIrr | varchar |  |  | SI | Irritation |
| QPun | varchar |  |  | SI | Punishment |
| QSad | varchar |  |  | SI | Sadness |
| QSat | varchar |  |  | SI | Satisfaction |
| QSex | varchar |  |  | SI | Sex |
| QSle | varchar |  |  | SI | Sleep |
| QSui | varchar |  |  | SI | Suicide |
| QTir | varchar |  |  | SI | Tiredness |
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
| QWea | varchar |  |  | SI | Weakness |
| QWei | varchar |  |  | SI | Weight |
| QWor | varchar |  |  | SI | Work |
| QWorr | varchar |  |  | SI | Worry |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*