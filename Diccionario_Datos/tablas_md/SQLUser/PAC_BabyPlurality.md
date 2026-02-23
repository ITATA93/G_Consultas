# SQLUser.PAC_BabyPlurality

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLUR_RowId | bigint | PK |  | NO | - |
| PLUR_BabyCount | double |  |  | SI | Count of Babies  |
| PLUR_Code | varchar |  |  | NO | Code |
| PLUR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLUR_CreatedDate | date |  |  | SI | Created Date |
| PLUR_CreatedTime | time |  |  | SI | Created Time |
| PLUR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLUR_DateFrom | date |  |  | SI | Date From |
| PLUR_DateTo | date |  |  | SI | Date To |
| PLUR_Desc | varchar |  |  | NO | Description |
| PLUR_Owner | varchar |  |  | SI | Owner |
| PLUR_UpdatedDate | date |  |  | SI | Updated Date |
| PLUR_UpdatedTime | time |  |  | SI | Updated Time |
| PLUR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Catheter insertion site |
| Q04 | - |  |  | SI | Variance |
| Q05 | - |  |  | SI | Insertions sites remain free of ooze and haematoma |
| Q06 | - |  |  | SI | Variance |
| Q07 | - |  |  | SI | Femoral sheath removed as per protocol |
| Q08 | - |  |  | SI | Variance |
| Q09 | - |  |  | SI | Femoral compression device removed as per protocol |
| Q10 | - |  |  | SI | Variance |
| Q11 | - |  |  | SI | Radial&nbsp |
| Q12 | - |  |  | SI | Variance |
| Q13 | - |  |  | SI | Observations remained within normal parameters |
| Q14 | - |  |  | SI | Variance |
| Q15 | - |  |  | SI | Neurovascular observations remained within normal ... |
| Q16 | - |  |  | SI | Variance |
| Q17 | - |  |  | SI | Intravenous cannula patent |
| Q18 | - |  |  | SI | Variance |
| Q19 | - |  |  | SI | Medications administered as prescribed |
| Q20 | - |  |  | SI | Variance |
| Q21 | - |  |  | SI | Gastrointestinal / Urinary |
| Q22 | - |  |  | SI | Tolerating ordered diet |
| Q23 | - |  |  | SI | Variance |
| Q24 | - |  |  | SI | Passed urine post procedure |
| Q25 | - |  |  | SI | Variance |
| Q26 | - |  |  | SI | Hygiene Care |
| Q27 | - |  |  | SI | Showered with assistance |
| Q28 | - |  |  | SI | Variance |
| Q29 | - |  |  | SI | Activity / Mobility |
| Q30 | - |  |  | SI | Mobilised after 1 hour |
| Q31 | - |  |  | SI | Variance |
| Q32 | - |  |  | SI | Arterial Femoral approach - rest in bed 6 hours po... |
| Q33 | - |  |  | SI | Variance |
| Q34 | - |  |  | SI | Venous Femoral approach - mobilise as directed by ... |
| Q35 | - |  |  | SI | Variance |
| Q36 | - |  |  | SI | Education |
| Q37 | - |  |  | SI | Complete cardiac education phase 1 and post proced... |
| Q38 | - |  |  | SI | Variance |
| Q39 | - |  |  | SI | Referrals |
| Q40 | - |  |  | SI | Internal consult request made to appropriate servi... |
| Q41 | - |  |  | SI | Variance |
| Q42 | - |  |  | SI | Referrals made to external providers as appropriat... |
| Q43 | - |  |  | SI | Variance |
| Q44 | - |  |  | SI | Variance |
| Q45 | - |  |  | SI | Variance |
| Q46 | - |  |  | SI | Variance |
| Q47 | - |  |  | SI | Variance |
| Q48 | - |  |  | SI | Variance |
| Q49 | - |  |  | SI | Variance |
| Q50 | - |  |  | SI | Variance |
| Q51 | - |  |  | SI | Variance |
| Q52 | - |  |  | SI | Variance |
| Q53 | - |  |  | SI | Variance |
| Q54 | - |  |  | SI | Variance |
| Q55 | - |  |  | SI | Variance |
| Q56 | - |  |  | SI | Variance |
| Q57 | - |  |  | SI | Variance |
| Q58 | - |  |  | SI | Variance |
| Q59 | - |  |  | SI | Variance |
| Q60 | - |  |  | SI | Variance |
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