# SQLUser.PA_Adm2OutcomeStage

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STOPST_ParRef | varchar | PK |  | NO | PA_Adm2Outcome Parent Reference |
| Q01 | - |  |  | SI | Please score based on what best represents your ex... |
| Q02 | - |  |  | SI | How severe is your pain? |
| Q03 | - |  |  | SI | Best describe your pain where: 0 = no pain and 10 ... |
| Q04 | - |  |  | SI | At its worst? |
| Q05 | - |  |  | SI | When lying on the involved side? |
| Q06 | - |  |  | SI | Reaching for something on a high shelf? |
| Q07 | - |  |  | SI | Touching the back of your neck? |
| Q08 | - |  |  | SI | Pushing with the involved arm? |
| Q09 | - |  |  | SI | How much difficulty do you have? |
| Q10 | - |  |  | SI | Best describe your experience where: 0 = no diffic... |
| Q11 | - |  |  | SI | Washing your hair? |
| Q12 | - |  |  | SI | Washing your back? |
| Q13 | - |  |  | SI | Putting on an undershirt or jumper? |
| Q14 | - |  |  | SI | Putting on a shirt that buttons down the front? |
| Q15 | - |  |  | SI | Putting on your pants? |
| Q16 | - |  |  | SI | Placing an object on a high shelf? |
| Q17 | - |  |  | SI | Carrying a heavy object of 10 pounds (4.5 kilogram... |
| Q18 | - |  |  | SI | Removing something from your back pocket? |
| Q19 | - |  |  | SI | Pain Score |
| Q20 | - |  |  | SI | Disability Score |
| Q21 | - |  |  | SI | Total Pain Score (%) |
| Q22 | - |  |  | SI | Total Disability Score (%) |
| Q23 | - |  |  | SI | Total SPADI Score (%) |
| Q24 | - |  |  | SI | Total score ranging from 0 (best) to 100 (worst) |
| Q25 | - |  |  | SI | Score |
| Q26 | - |  |  | SI | Classification |
| Q27 | - |  |  | SI | Score ranges from 1% (no Shoulder pain) to 100 % (... |
| Q28 | - |  |  | SI | Score ranges from 1% (no Disability) to 100 % (sev... |
| Q29 | - |  |  | SI | The Shoulder Pain and Disability Index (SPADI) is ... |
| Q30 | - |  |  | SI | Date |
| Q31 | - |  |  | SI | Time |
| Q32 | - |  |  | SI | Total Pain Score (%) - Display only |
| Q33 | - |  |  | SI | Total Disability Score (%) - Display only |
| Q34 | - |  |  | SI | Total SPADI Score (%) - Display only |
| Q35 | - |  |  | SI | Total Pain Score (%) Caption |
| Q36 | - |  |  | SI | Total Disability Score (%) Caption |
| Q37 | - |  |  | SI | Total SPADI Score (%) Caption |
| Q38 | - |  |  | SI | Total SPADI Score (%) Caption |
| Q39 | - |  |  | SI | Total Pain Score (%) |
| Q40 | - |  |  | SI | Total Disability Score (%) |
| Q41 | - |  |  | SI | Total SPADI Score (%) |
| Q42 | - |  |  | SI | Please click Apply then Update to get the score ca... |
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
| STOPST_Childsub | double |  |  | NO | Childsub |
| STOPST_RowId | varchar |  |  | NO | - |
| STOPST_StageStop_DR | varchar |  | FK | SI | Des Ref PACRefTemplateStageType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*