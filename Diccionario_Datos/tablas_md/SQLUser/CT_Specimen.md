# SQLUser.CT_Specimen

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Especialidades**. Especialidades médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPEC_RowId | varchar | PK |  | NO | - |
| Q01 | - |  |  | SI | Maintaining patient safety with use of bedrails ou... |
| Q02 | - |  |  | SI | Please state who the discussion / decision has bee... |
| Q03 | - |  |  | SI | Ensure patient information leaflet is given |
| Q04 | - |  |  | SI | State reason as to why bedrails are being used on ... |
| Q05 | - |  |  | SI | The use of bedrails will be reviewed on a daily ba... |
| Q06 | - |  |  | SI | Ensure the need for the use of bedrails is communi... |
| Q07 | - |  |  | SI | Please state the reason why the use of bedrails is... |
| Q08 | - |  |  | SI | Ensure that the appropriate use of bed rails is as... |
| Q09 | - |  |  | SI | Mental State |
| Q10 | - |  |  | SI | Patient is confused and disorientated |
| Q11 | - |  |  | SI | Patient is drowsy |
| Q12 | - |  |  | SI | Patient is orientated and alert |
| Q13 | - |  |  | SI | Patient is unconscious |
| Q14 | - |  |  | SI | Mobility |
| Q15 | - |  |  | SI | Patient is very immobile (bedfast or hoist depende... |
| Q16 | - |  |  | SI | Patient is neither independent nor immobile |
| Q17 | - |  |  | SI | Patient can mobilise without help from staff |
| Q18 | - |  |  | SI | Use bedrails with care |
| Q19 | - |  |  | SI | Bedrails NOT recommended (use low profile bed) |
| Q20 | - |  |  | SI | Bedrails NOT recommended (use low profile bed) |
| Q21 | - |  |  | SI | Bedrails recommended |
| Q22 | - |  |  | SI | Use bedrails with care |
| Q23 | - |  |  | SI | Bedrails NOT recommended |
| Q24 | - |  |  | SI | Bedrails recommended |
| Q25 | - |  |  | SI | Bedrails recommended |
| Q26 | - |  |  | SI | Bedrails recommended |
| Q27 | - |  |  | SI | Bedrails NOT recommended |
| Q28 | - |  |  | SI | Bedrails NOT recommended |
| Q29 | - |  |  | SI | N/A |
| Q30 | - |  |  | SI | N/A |
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
| SPEC_Code | varchar |  |  | NO | Code |
| SPEC_CreatedDate | date |  |  | SI | Created Date |
| SPEC_CreatedTime | time |  |  | SI | Created Time |
| SPEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SPEC_DateFrom | date |  |  | SI | DateFrom |
| SPEC_DateTo | date |  |  | SI | DateTo |
| SPEC_Desc | varchar |  |  | NO | Description |
| SPEC_UpdatedDate | date |  |  | SI | Updated Date |
| SPEC_UpdatedTime | time |  |  | SI | Updated Time |
| SPEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*