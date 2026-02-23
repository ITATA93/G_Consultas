# questionnaire.QPREADMSC

> Pre-Admission Anaesthetic Assessment

**Schema:** questionnaire
**Columnas:** 115
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pre-Admission Anaesthetic Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQQ12 | varchar |  |  | SI | - |
| CQQ14 | varchar |  |  | SI | - |
| CQQ15 | varchar |  |  | SI | - |
| CQQ17 | varchar |  |  | SI | - |
| CQQ19 | varchar |  |  | SI | - |
| CQQ20 | varchar |  |  | SI | - |
| CQQ22 | varchar |  |  | SI | - |
| CQQ23 | varchar |  |  | SI | - |
| CQQ26 | varchar |  |  | SI | - |
| CQQ27 | varchar |  |  | SI | - |
| CQQ29 | varchar |  |  | SI | - |
| CQQ40 | varchar |  |  | SI | - |
| CQQ41 | varchar |  |  | SI | - |
| CQQ42 | varchar |  |  | SI | - |
| CQQ44 | varchar |  |  | SI | - |
| CQQ45 | varchar |  |  | SI | - |
| CQQ48 | varchar |  |  | SI | - |
| Q50 | varchar |  |  | SI | Planned procedure |
| QQ1 | date |  |  | SI | Date |
| QQ10 | varchar |  |  | SI | Respiratory Rate |
| QQ10ObsDR | varchar |  | FK | SI | Respiratory Rate DR |
| QQ11 | varchar |  |  | SI | SaO2 |
| QQ11ObsDR | varchar |  | FK | SI | SaO2 DR |
| QQ12 | varchar |  |  | SI | Has the patient had an anaesthetic before? |
| QQ13 | varchar |  |  | SI | Were there any difficulties with previous anaesthe... |
| QQ14 | varchar |  |  | SI | Is there any family history of difficulties with a... |
| QQ15 | varchar |  |  | SI | What was the difficulty? |
| QQ16 | varchar |  |  | SI | Comments on family History of difficulties with an... |
| QQ17 | varchar |  |  | SI | Do you ever get any chest pain? |
| QQ18 | varchar |  |  | SI | Chest pain assessment |
| QQ19 | varchar |  |  | SI | Do you get shortness of breath? |
| QQ2 | time |  |  | SI | Time |
| QQ20 | varchar |  |  | SI | Activities when experienceing shortness of breath |
| QQ21 | varchar |  |  | SI | Comments on short of breath assessment |
| QQ22 | varchar |  |  | SI | Do you take any illicit drugs? |
| QQ23 | varchar |  |  | SI | What have you used? |
| QQ24 | varchar |  |  | SI | When did you last use illicit drugs? |
| QQ25 | varchar |  |  | SI | How much do you use? |
| QQ26 | varchar |  |  | SI | Do you, or have you ever smoked? |
| QQ27 | varchar |  |  | SI | How much do you smoke? |
| QQ28 | varchar |  |  | SI | Comments on smoking |
| QQ29 | varchar |  |  | SI | How much alcohol do you drink each day? |
| QQ3 | varchar |  |  | SI | Clinic location |
| QQ30 | varchar |  |  | SI | Height in cm |
| QQ30ObsDR | varchar |  | FK | SI | Height in cm DR |
| QQ31 | varchar |  |  | SI | Weight in kg |
| QQ31ObsDR | varchar |  | FK | SI | Weight in kg DR |
| QQ32 | varchar |  |  | SI | BMI |
| QQ33 | varchar |  |  | SI | Do you have any allergies? |
| QQ34 | varchar |  |  | SI | Do you take any regular prescription medications? |
| QQ35 | varchar |  |  | SI | Do you take any regular non prescription medicatio... |
| QQ36 | varchar |  |  | SI | Do you have any medical problems? |
| QQ37 | varchar |  |  | SI | Do you have any dentures? |
| QQ38 | varchar |  |  | SI | Do you have any caps / crowns / loose teeth? |
| QQ39 | varchar |  |  | SI | Do you have any cultural beliefs that we should be... |
| QQ4 | varchar |  |  | SI | Anaesthetist conducting assessment |
| QQ40 | varchar |  |  | SI | Mallampatti assessment |
| QQ41 | varchar |  |  | SI | ASA score |
| QQ42 | varchar |  |  | SI | Planned anaesthetic method/s discussed with patien... |
| QQ43 | varchar |  |  | SI | Details of anaesthetic risks explained to patient |
| QQ44 | varchar |  |  | SI | Fasting instructions given to patient |
| QQ45 | varchar |  |  | SI | Do you suffer from any reflux or gastric discomfor... |
| QQ46 | varchar |  |  | SI | History of gastric reflux details |
| QQ47 | varchar |  |  | SI | Details of discussion with patient |
| QQ48 | varchar |  |  | SI | Follow up investigations required |
| QQ49 | bit |  |  | SI | These investigations have been ordered? |
| QQ5 | varchar |  |  | SI | Planned procedure |
| QQ6 | date |  |  | SI | Planned date of procedure |
| QQ7 | varchar |  |  | SI | Pulse |
| QQ7ObsDR | varchar |  | FK | SI | Pulse DR |
| QQ8 | varchar |  |  | SI | BP Systolic |
| QQ8ObsDR | varchar |  | FK | SI | BP Systolic DR |
| QQ9 | varchar |  |  | SI | BP Diastolic |
| QQ9ObsDR | varchar |  | FK | SI | BP Diastolic DR |
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