# SQLUser.IN_GdRec

**Schema:** SQLUser
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INGR_RowId | bigint | PK |  | NO | - |
| INGR_APCVM_DR | bigint |  | FK | NO | Des Ref to APCVM |
| INGR_CTCUR_DR | bigint |  | FK | NO | Des Ref to CTCUR |
| INGR_Completed | varchar |  |  | SI | Completed Flag |
| INGR_DO_No | varchar |  |  | NO | Delivery Order No |
| INGR_Date | date |  |  | NO | Date Of Delivery (DO Date) |
| INGR_DateLastUpdated | date |  |  | SI | DateLastUpdated |
| INGR_DocketDate | date |  |  | SI | Docket Date |
| INGR_ExRate | double |  |  | NO | Exchange Rate |
| INGR_HandChg | double |  |  | SI | Handling Charges |
| INGR_Hospital_DR | bigint |  | FK | SI | Des Ref to CTHospital |
| INGR_INPO_DR | bigint |  | FK | SI | Purchase Order |
| INGR_InvoiceNumber | varchar |  |  | SI | Invoice Number |
| INGR_No | varchar |  |  | NO | Goods Receive Note No |
| INGR_OverallDiscount | double |  |  | SI | Overall Discount |
| INGR_Remarks | varchar |  |  | SI | Remarks |
| INGR_SSUSR_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| INGR_Time | time |  |  | NO | Time of Delivery |
| INGR_TimeLastUpdated | time |  |  | SI | TimeLastUpdated |
| Q01 | - |  |  | SI | Sweating |
| Q02 | - |  |  | SI | Tremor |
| Q03 | - |  |  | SI | Yawning |
| Q04 | - |  |  | SI | Bone or joint aches |
| Q05 | - |  |  | SI | Gooseflesh skin |
| Q06 | - |  |  | SI | Pupil size	 |
| Q07 | - |  |  | SI | Restleness |
| Q08 | - |  |  | SI | GI upset |
| Q09 | - |  |  | SI | Anxiety or irritability |
| Q10 | - |  |  | SI | Runny nose or tearing	 |
| Q11 | - |  |  | SI | Resting&nbsp |
| Q12 | - |  |  | SI | Pupil Size (L) mm	 |
| Q12ObsDR | - |  |  | SI | Pupil Size (L) mm	 DR |
| Q13 | - |  |  | SI | Pupil Reaction (L) |
| Q13ObsDR | - |  |  | SI | Pupil Reaction (L) DR |
| Q14 | - |  |  | SI | Pupil Size (R) mm	 |
| Q14ObsDR | - |  |  | SI | Pupil Size (R) mm	 DR |
| Q15 | - |  |  | SI | Pupil Reaction (R) |
| Q15ObsDR | - |  |  | SI | Pupil Reaction (R) DR |
| Q16 | - |  |  | SI | Temperature |
| Q16ObsDR | - |  |  | SI | Temperature DR |
| Q17 | - |  |  | SI | Systolic BP |
| Q17ObsDR | - |  |  | SI | Systolic BP DR |
| Q18 | - |  |  | SI | Diastolic BP |
| Q18ObsDR | - |  |  | SI | Diastolic BP DR |
| Q19 | - |  |  | SI | Respiration |
| Q19ObsDR | - |  |  | SI | Respiration DR |
| Q20 | - |  |  | SI | Heart rate |
| Q20ObsDR | - |  |  | SI | Heart rate DR |
| Q21 | - |  |  | SI | SCORING |
| Q22 | - |  |  | SI | SCORING |
| Q23 | - |  |  | SI | SYMPTOM |
| Q24 | - |  |  | SI | SYMPTOM |
| Q25 | - |  |  | SI | Score |
| Q26 | - |  |  | SI | Classification	 |
| Q27 | - |  |  | SI | 5 to12 |
| Q28 | - |  |  | SI | 13 to&nbsp |
| Q29 | - |  |  | SI | 25 to&nbsp |
| Q30 | - |  |  | SI | > 36 	 |
| Q31 | - |  |  | SI | Total scores are indicative of increasing or decre... |
| Q32 | - |  |  | SI | Clinical opiate withdrawal scale is used to assess... |
| Q33 | - |  |  | SI | 0 to&nbsp |
| Q34 | - |  |  | SI | No significant signs of withdrawal |
| Q35 | - |  |  | SI | Mild withdrawal |
| Q36 | - |  |  | SI | Moderate withdrawal |
| Q37 | - |  |  | SI | Moderately severe withdrawal	 |
| Q38 | - |  |  | SI | Severe withdrawal |
| Q39 | - |  |  | SI | Date |
| Q40 | - |  |  | SI | Time |
| Q41 | - |  |  | SI | Vital signs observation chart is required when com... |
| Q42 | - |  |  | SI | Resting heart rate |
| Q43 | - |  |  | SI | Sweating: over past 1/2 hour not accounted for by ... |
| Q44 | - |  |  | SI | Restlessness: Observation during assessment |
| Q45 | - |  |  | SI | Pupil size |
| Q46 | - |  |  | SI | Bone or joint aches:&nbsp |
| Q47 | - |  |  | SI | Runny nose or tearing: not accounted for by cold s... |
| Q48 | - |  |  | SI | GI upset: over last 1/2 hour |
| Q49 | - |  |  | SI | Tremor: observation of outstretched hands |
| Q50 | - |  |  | SI | Yawning: observation of outstretched hands |
| Q51 | - |  |  | SI | Anxiety or irritability |
| Q52 | - |  |  | SI | Gooseflesh skin |
| Q53 | - |  |  | SI | Wesson DR, Ling W. The Clinical Opiate Withdrawal ... |
| Q54 | - |  |  | SI | Restlessness |
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