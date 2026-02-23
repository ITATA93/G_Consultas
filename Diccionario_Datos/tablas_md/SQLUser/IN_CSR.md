# SQLUser.IN_CSR

**Schema:** SQLUser
**Columnas:** 143
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCSR_RowId | bigint | PK |  | NO | - |
| INCSR_ChangeStatus | varchar |  |  | SI | Change Status |
| INCSR_Completed | varchar |  |  | SI | Completed flag |
| INCSR_Date | date |  |  | NO | Date of Transaction |
| INCSR_INCSR_DR | bigint |  | FK | SI | Des Ref to INCSR (CSR Request) |
| INCSR_Laundry_DR | bigint |  | FK | SI | Des Ref to CTLOC(Laundry) |
| INCSR_No | varchar |  |  | NO | Transaction No |
| INCSR_Priority_DR | bigint |  | FK | SI | Des Ref INCPriority |
| INCSR_Remarks | varchar |  |  | SI | Remarks |
| INCSR_Time | time |  |  | NO | Time |
| INCSR_UserCompleted | varchar |  |  | SI | User Completed |
| INCSR_User_DR | bigint |  | FK | NO | Des Ref to SSU |
| INCSR_Ward_DR | bigint |  | FK | SI | Des Ref to CTLOC(Ward) |
| Q01 | - |  |  | SI | Ask 'Do you feel sick to your stomach? Have you vo... |
| Q02 | - |  |  | SI | Nausea / Vomiting |
| Q03 | - |  |  | SI | Arms extended and fingers spread apart |
| Q04 | - |  |  | SI | Tremor |
| Q05 | - |  |  | SI | Paroxysmal sweats - Observe |
| Q06 | - |  |  | SI | Ask 'Does your head feel different? Does it feel l... |
| Q07 | - |  |  | SI | Headache / fullness in head |
| Q08 | - |  |  | SI | Ask 'What day is this? Where are you? Who am I? |
| Q09 | - |  |  | SI | Orientation / clouding of sensorium |
| Q10 | - |  |  | SI | Ask, 'Do you feel nervous? |
| Q11 | - |  |  | SI | Anxiety |
| Q12 | - |  |  | SI | Agitation |
| Q13 | - |  |  | SI | Ask 'Does the light appear to be too bright? Is it... |
| Q14 | - |  |  | SI | Visual disturbances |
| Q15 | - |  |  | SI | Ask, 'Have you any itching, pins and needles sensa... |
| Q16 | - |  |  | SI | Tactile disturbances |
| Q17 | - |  |  | SI | Auditory disturbances |
| Q18 | - |  |  | SI | CIWA-Ar score |
| Q19 | - |  |  | SI | Interpretation (Withdrawal severity) |
| Q20 | - |  |  | SI | 0 – 9 |
| Q21 | - |  |  | SI | Absent or minimal |
| Q22 | - |  |  | SI | 10 – 15 |
| Q23 | - |  |  | SI | Mild |
| Q24 | - |  |  | SI | 16 – 20 |
| Q25 | - |  |  | SI | Moderate |
| Q26 | - |  |  | SI | 21 – 67 |
| Q27 | - |  |  | SI | Severe |
| Q28 | - |  |  | SI | 0 – 9: Absent or minimal |
| Q29 | - |  |  | SI | 10 – 15: Mild |
| Q30 | - |  |  | SI | 16 – 20: Moderate |
| Q31 | - |  |  | SI | 21 – 67: Severe |
| Q32 | - |  |  | SI | The CIWA-Ar is a shortened version of a previous 1... |
| Q33 | - |  |  | SI | This program to improve recognition and treatment ... |
| Q34 | - |  |  | SI | Symptom |
| Q35 | - |  |  | SI | Nausea / vomiting |
| Q36 | - |  |  | SI | Tremor |
| Q37 | - |  |  | SI | Paroxysmal sweats |
| Q38 | - |  |  | SI | Headache / sensation of fullness in head |
| Q39 | - |  |  | SI | Orientation / clouding of sensorium |
| Q40 | - |  |  | SI | Anxiety |
| Q41 | - |  |  | SI | Agitation |
| Q42 | - |  |  | SI | Visual disturbances |
| Q43 | - |  |  | SI | Tactile disturbances |
| Q44 | - |  |  | SI | Auditory disturbances |
| Q45 | - |  |  | SI | Possible questions to accompany evaluation |
| Q46 | - |  |  | SI | Do you feel sick to your stomach? Have you vomited... |
| Q47 | - |  |  | SI | n/a |
| Q48 | - |  |  | SI | n/a |
| Q49 | - |  |  | SI | Does your head feel different? Does it feel like t... |
| Q50 | - |  |  | SI | Questions about current date and time, recognition... |
| Q51 | - |  |  | SI | Are you feeling anxious? Does something worry you? |
| Q52 | - |  |  | SI | n/a |
| Q53 | - |  |  | SI | Does the light appear to be too bright? Is its col... |
| Q54 | - |  |  | SI | Have you any itching, pins and needles sensations,... |
| Q55 | - |  |  | SI | Are you more aware of sounds around you? Are they ... |
| Q56 | - |  |  | SI | Other information |
| Q57 | - |  |  | SI | Assessor to ask about symptom frequency |
| Q58 | - |  |  | SI | Observation of tremor state, in relaxed position a... |
| Q59 | - |  |  | SI | Observation of sweating degree, localization and t... |
| Q60 | - |  |  | SI | Headache severity should be accounted for |
| Q61 | - |  |  | SI | Evaluation of orientation degree |
| Q62 | - |  |  | SI | Evaluation of general degree of nervousness and th... |
| Q63 | - |  |  | SI | Observation of agitation degree |
| Q64 | - |  |  | SI | Checks for visual or hallucinatory events |
| Q65 | - |  |  | SI | Checks for abnormal tactile sensations |
| Q66 | - |  |  | SI | Evaluation of auditory sensations |
| Q67 | - |  |  | SI | Date |
| Q68 | - |  |  | SI | Time |
| Q69 | - |  |  | SI | Ask, 'Are you more aware of sounds around you? Are... |
| Q70 | - |  |  | SI | Generic description label1 |
| Q71 | - |  |  | SI | Generic description label2 |
| Q72 | - |  |  | SI | Generic description label3 |
| Q73 | - |  |  | SI | Generic description label4 |
| Q74 | - |  |  | SI | Generic description label5 |
| Q75 | - |  |  | SI | The Clinical Institute Withdrawal Assessment for A... |
| Q76 | - |  |  | SI | Shaw JM, Kolesar GS, Sellers EM, Kaplan HL, Sandor... |
| Q77 | - |  |  | SI | Sullivan JT, Sykora K, Schneiderman J, Naranjo CA,... |
| Q78 | - |  |  | SI | Vital signs observation chart is required when com... |
| Q79 | - |  |  | SI | Heart rate |
| Q79ObsDR | - |  |  | SI | Heart rate DR |
| Q80 | - |  |  | SI | Respirations |
| Q80ObsDR | - |  |  | SI | Respirations DR |
| Q81 | - |  |  | SI | Saturation |
| Q81ObsDR | - |  |  | SI | Saturation DR |
| Q82 | - |  |  | SI | Systolic |
| Q82ObsDR | - |  |  | SI | Systolic DR |
| Q83 | - |  |  | SI | Diastolic |
| Q83ObsDR | - |  |  | SI | Diastolic DR |
| Q84 | - |  |  | SI | Breath alcohol content |
| Q84ObsDR | - |  |  | SI | Breath alcohol content DR |
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