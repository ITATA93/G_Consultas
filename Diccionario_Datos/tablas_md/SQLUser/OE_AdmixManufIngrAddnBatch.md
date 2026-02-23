# SQLUser.OE_AdmixManufIngrAddnBatch

**Schema:** SQLUser
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BAT_ParRef | varchar | PK |  | NO | OE_OrdAdmix Parent Reference |
| BAT_Childsub | double |  |  | NO | Childsub |
| BAT_ExtStkBatchID | varchar |  |  | SI | External Stock BatchID |
| BAT_ExtStkDetails | varchar |  |  | SI | External Stock Details |
| BAT_INCIRN_DR | varchar |  | FK | SI | Des Ref INCItmRegNo |
| BAT_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| BAT_Quantity | double |  |  | SI | Quantity |
| BAT_RowId | varchar |  |  | NO | - |
| CQQ12 | - |  |  | SI | (null) |
| CQQ14 | - |  |  | SI | (null) |
| CQQ15 | - |  |  | SI | (null) |
| CQQ17 | - |  |  | SI | (null) |
| CQQ19 | - |  |  | SI | (null) |
| CQQ20 | - |  |  | SI | (null) |
| CQQ22 | - |  |  | SI | (null) |
| CQQ23 | - |  |  | SI | (null) |
| CQQ26 | - |  |  | SI | (null) |
| CQQ27 | - |  |  | SI | (null) |
| CQQ29 | - |  |  | SI | (null) |
| CQQ40 | - |  |  | SI | (null) |
| CQQ41 | - |  |  | SI | (null) |
| CQQ42 | - |  |  | SI | (null) |
| CQQ44 | - |  |  | SI | (null) |
| CQQ45 | - |  |  | SI | (null) |
| CQQ48 | - |  |  | SI | (null) |
| Q50 | - |  |  | SI | Planned procedure |
| QQ1 | - |  |  | SI | Date |
| QQ10 | - |  |  | SI | Respiratory Rate |
| QQ10ObsDR | - |  |  | SI | Respiratory Rate DR |
| QQ11 | - |  |  | SI | SaO2 |
| QQ11ObsDR | - |  |  | SI | SaO2 DR |
| QQ12 | - |  |  | SI | Has the patient had an anaesthetic before? |
| QQ13 | - |  |  | SI | Were there any difficulties with previous anaesthe... |
| QQ14 | - |  |  | SI | Is there any family history of difficulties with a... |
| QQ15 | - |  |  | SI | What was the difficulty? |
| QQ16 | - |  |  | SI | Comments on family History of difficulties with an... |
| QQ17 | - |  |  | SI | Do you ever get any chest pain? |
| QQ18 | - |  |  | SI | Chest pain assessment |
| QQ19 | - |  |  | SI | Do you get shortness of breath? |
| QQ2 | - |  |  | SI | Time |
| QQ20 | - |  |  | SI | Activities when experienceing shortness of breath |
| QQ21 | - |  |  | SI | Comments on short of breath assessment |
| QQ22 | - |  |  | SI | Do you take any illicit drugs? |
| QQ23 | - |  |  | SI | What have you used? |
| QQ24 | - |  |  | SI | When did you last use illicit drugs? |
| QQ25 | - |  |  | SI | How much do you use? |
| QQ26 | - |  |  | SI | Do you, or have you ever smoked? |
| QQ27 | - |  |  | SI | How much do you smoke? |
| QQ28 | - |  |  | SI | Comments on smoking |
| QQ29 | - |  |  | SI | How much alcohol do you drink each day? |
| QQ3 | - |  |  | SI | Clinic location |
| QQ30 | - |  |  | SI | Height in cm |
| QQ30ObsDR | - |  |  | SI | Height in cm DR |
| QQ31 | - |  |  | SI | Weight in kg |
| QQ31ObsDR | - |  |  | SI | Weight in kg DR |
| QQ32 | - |  |  | SI | BMI |
| QQ33 | - |  |  | SI | Do you have any allergies? |
| QQ34 | - |  |  | SI | Do you take any regular prescription medications? |
| QQ35 | - |  |  | SI | Do you take any regular non prescription medicatio... |
| QQ36 | - |  |  | SI | Do you have any medical problems? |
| QQ37 | - |  |  | SI | Do you have any dentures? |
| QQ38 | - |  |  | SI | Do you have any caps / crowns / loose teeth? |
| QQ39 | - |  |  | SI | Do you have any cultural beliefs that we should be... |
| QQ4 | - |  |  | SI | Anaesthetist conducting assessment |
| QQ40 | - |  |  | SI | Mallampatti assessment |
| QQ41 | - |  |  | SI | ASA score |
| QQ42 | - |  |  | SI | Planned anaesthetic method/s discussed with patien... |
| QQ43 | - |  |  | SI | Details of anaesthetic risks explained to patient |
| QQ44 | - |  |  | SI | Fasting instructions given to patient |
| QQ45 | - |  |  | SI | Do you suffer from any reflux or gastric discomfor... |
| QQ46 | - |  |  | SI | History of gastric reflux details |
| QQ47 | - |  |  | SI | Details of discussion with patient |
| QQ48 | - |  |  | SI | Follow up investigations required |
| QQ49 | - |  |  | SI | These investigations have been ordered? |
| QQ5 | - |  |  | SI | Planned procedure |
| QQ6 | - |  |  | SI | Planned date of procedure |
| QQ7 | - |  |  | SI | Pulse |
| QQ7ObsDR | - |  |  | SI | Pulse DR |
| QQ8 | - |  |  | SI | BP Systolic |
| QQ8ObsDR | - |  |  | SI | BP Systolic DR |
| QQ9 | - |  |  | SI | BP Diastolic |
| QQ9ObsDR | - |  |  | SI | BP Diastolic DR |
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