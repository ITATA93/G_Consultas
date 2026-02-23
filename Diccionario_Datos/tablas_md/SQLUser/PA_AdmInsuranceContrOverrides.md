# SQLUser.PA_AdmInsuranceContrOverrides

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COV_ParRef | varchar | PK |  | NO | PA_AdmInsurance Parent Reference |
| COV_Childsub | double |  |  | NO | Childsub |
| COV_Date | date |  |  | SI | Date |
| COV_FixedPatShare | double |  |  | SI | Fixed Pat Share |
| COV_PayFrom | double |  |  | SI | Pay From |
| COV_PayUntil | double |  |  | SI | Pay Until |
| COV_PayorShare | double |  |  | SI | PayorShare |
| COV_RowId | varchar |  |  | NO | - |
| COV_Time | time |  |  | SI | Time |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of injury |
| Q04 | - |  |  | SI | Time of injury |
| Q05 | - |  |  | SI | Instructions |
| Q06 | - |  |  | SI | How old are you? |
| Q07 | - |  |  | SI | Score |
| Q08 | - |  |  | SI | The SYPTAS is administered daily. |
| Q09 | - |  |  | SI | What is your mother's / father's name? |
| Q10 | - |  |  | SI | Score |
| Q11 | - |  |  | SI | On the first day of testing, all orientation and m... |
| Q12 | - |  |  | SI | What is the name of this place? |
| Q13 | - |  |  | SI | Score |
| Q14 | - |  |  | SI | Hence, the maximal score on the first day of testi... |
| Q15 | - |  |  | SI | What photo did you have to remember? |
| Q16 | - |  |  | SI | Score |
| Q17 | - |  |  | SI | Memory items are only scored from the second day o... |
| Q18 | - |  |  | SI | What was her name? |
| Q19 | - |  |  | SI | Score |
| Q20 | - |  |  | SI | Orientation&nbsp |
| Q21 | - |  |  | SI | Memory sub score |
| Q22 | - |  |  | SI | Total score |
| Q23 | - |  |  | SI | Comments |
| Q24 | - |  |  | SI | Thus, the maximal score from the second day onward... |
| Q25 | - |  |  | SI | On assessment of orientation, each day of testing ... |
| Q26 | - |  |  | SI | If they fail to spontaneously answer a question, t... |
| Q27 | - |  |  | SI | On assessment of memory, on the first day of testi... |
| Q28 | - |  |  | SI | The child is asked to repeat the name after the ex... |
| Q29 | - |  |  | SI | The child is asked to remember the face and given ... |
| Q30 | - |  |  | SI | On subsequent days, the child is asked to pick the... |
| Q31 | - |  |  | SI | If the target face is not identified correctly, th... |
| Q32 | - |  |  | SI | If the name is not recalled, a choice of 3 names (... |
| Q33 | - |  |  | SI | If the name is not identified correctly, the child... |
| Q34 | - |  |  | SI | On subsequent days, the target face and the target... |
| Q35 | - |  |  | SI | Lah S, David P, Donohue H, Epps A, Tate R, Brookes... |
| Q36 | - |  |  | SI | Lah S, Parry L, Epps A, Brooks N. Sydney Post Trau... |
| Q37 | - |  |  | SI | https://www.sydney.edu.au/content/dam/corporate/do... |
| Q38 | - |  |  | SI | The Sydney Post-traumatic Amnesia scale (SYPTAS) i... |
| Q39 | - |  |  | SI | Score of 5/5 on three consecutive days |
| Q40 | - |  |  | SI | Children are deemed to be out of Post-Traumatic Am... |
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