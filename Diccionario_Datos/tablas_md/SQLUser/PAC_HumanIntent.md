# SQLUser.PAC_HumanIntent

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HUMINT_RowId | bigint | PK |  | NO | - |
| HUMINT_Code | varchar |  |  | NO | Code |
| HUMINT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HUMINT_CreatedDate | date |  |  | SI | Created Date |
| HUMINT_CreatedTime | time |  |  | SI | Created Time |
| HUMINT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HUMINT_DateFrom | date |  |  | SI | Date From |
| HUMINT_DateTo | date |  |  | SI | Date To |
| HUMINT_Desc | varchar |  |  | NO | Description |
| HUMINT_Owner | varchar |  |  | SI | Owner |
| HUMINT_UpdatedDate | date |  |  | SI | Updated Date |
| HUMINT_UpdatedTime | time |  |  | SI | Updated Time |
| HUMINT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Posture / Tone	 |
| Q04 | - |  |  | SI | Cry |
| Q05 | - |  |  | SI | Sleep pattern |
| Q06 | - |  |  | SI | Expression |
| Q07 | - |  |  | SI | Color |
| Q08 | - |  |  | SI | Respirations |
| Q09 | - |  |  | SI | Heart rate |
| Q10 | - |  |  | SI | Oxygen saturation |
| Q11 | - |  |  | SI | Blood pressure |
| Q12 | - |  |  | SI | Nurse perception |
| Q13 | - |  |  | SI | Hodgkinson K, Bear M, Thorn J, Blaricum SV. Measur... |
| Q14 | - |  |  | SI | O’Sullivan AT, Rowley S, Ellis S, Faasse K, Petrie... |
| Q15 | - |  |  | SI | Clin J Pain 2016 |
| Q16 | - |  |  | SI | Comfort Measures |
| Q17 | - |  |  | SI | Gently repositioning the neonate to make him/her m... |
| Q18 | - |  |  | SI | Wrapping / containment of the infant to provide su... |
| Q19 | - |  |  | SI | Decreasing environmental stressors |
| Q20 | - |  |  | SI | Tactile soothing |
| Q21 | - |  |  | SI | Talking softly to the baby. |
| Q22 | - |  |  | SI | Changing the baby's nappy. |
| Q23 | - |  |  | SI | Using a pacifier/dummy to provide non-nutritive su... |
| Q24 | - |  |  | SI | The mPAT is an observational scale designed to ass... |
| Q25 | - |  |  | SI | It is recommended that mPAT can be utilised for bo... |
| Q26 | - |  |  | SI | The mPAT scale focuses on behavioural and physiolo... |
| Q27 | - |  |  | SI | > 5 |
| Q28 | - |  |  | SI | > 10 |
| Q29 | - |  |  | SI | Recommend comfort measures such as soothing, use o... |
| Q30 | - |  |  | SI | Recommend analgesia |
| Q31 | - |  |  | SI | Dummy1 |
| Q32 | - |  |  | SI | Dummy2 |
| Q33 | - |  |  | SI | Dummy3 |
| Q34 | - |  |  | SI | Dummy4 |
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