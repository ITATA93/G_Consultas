# SQLUser.OR_AnaestSurgPathwayUrinaryCatheter

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| URCTH_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Select a number from 1 to 7, depending on how appr... |
| Q04 | - |  |  | SI | A low value indicates that the statement is not ve... |
| Q05 | - |  |  | SI | During the past week, I have found that: |
| Q06 | - |  |  | SI | My motivation is lower when I am fatigued. |
| Q07 | - |  |  | SI | Exercise brings on my fatigue. |
| Q08 | - |  |  | SI | I am easily fatigued. |
| Q09 | - |  |  | SI | Fatigue interferes with my physical functioning. |
| Q10 | - |  |  | SI | Fatigue causes frequent problems for me. |
| Q11 | - |  |  | SI | My fatigue prevents sustained physical functioning... |
| Q12 | - |  |  | SI | Fatigue interferes with carrying out certain dutie... |
| Q13 | - |  |  | SI | Fatigue is among my three most disabling symptoms. |
| Q14 | - |  |  | SI | Fatigue interferes with my work, family, or social... |
| Q15 | - |  |  | SI | The scoring is done by calculating the average res... |
| Q16 | - |  |  | SI | People with depression alone score about 4.5. But ... |
| Q17 | - |  |  | SI | The Fatigue Severity Scale (FSS) is a scored quest... |
| Q18 | - |  |  | SI | Please find the details of the score interpretatio... |
| Q19 | - |  |  | SI | Please find the details of the score interpretatio... |
| Q20 | - |  |  | SI | Minimum Score = 1 |
| Q21 | - |  |  | SI | Maximum Score = 7 |
| Q22 | - |  |  | SI | People with depression alone score about 4.5. |
| Q23 | - |  |  | SI | People with fatigue related to Multiple Sclerosis ... |
| Q24 | - |  |  | SI | FSS Score |
| Q25 | - |  |  | SI | Score |
| Q26 | - |  |  | SI | Classification |
| Q27 | - |  |  | SI | 1 - 7 |
| Q28 | - |  |  | SI | 1 - 7: Please find the details of the score interp... |
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
| URCTH_BalloonVolume | double |  |  | SI | Balloon Volume (mL) |
| URCTH_CatheterComments | varchar |  |  | SI | Catheter Comments  |
| URCTH_CatheterInserted | varchar |  |  | SI | Catheter Inserted |
| URCTH_CatheterMaterial_DR | bigint |  | FK | SI | Des Ref ORCCatheterMaterial |
| URCTH_CatheterRoute_DR | bigint |  | FK | SI |  Des Ref ORC_CatheterRoute |
| URCTH_CatheterType_DR | bigint |  | FK | SI |  Des Ref ORC_CatheterType |
| URCTH_Childsub | double |  |  | NO | Childsub |
| URCTH_InsituFromWard | varchar |  |  | SI | Insitu from Ward |
| URCTH_LumenCatheter_DR | bigint |  | FK | SI | Des Ref ORCLumenCatheter |
| URCTH_RowId | varchar |  |  | NO | - |
| URCTH_Size | varchar |  |  | SI | Size |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*