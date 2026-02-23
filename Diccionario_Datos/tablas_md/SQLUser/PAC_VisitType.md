# SQLUser.PAC_VisitType

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VST_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Education provided by |
| Q04 | - |  |  | SI | Other educator comments |
| Q05 | - |  |  | SI | Education delivered |
| Q06 | - |  |  | SI | Other delivery |
| Q07 | - |  |  | SI | Education booklet provided |
| Q08 | - |  |  | SI | Renal Transplant Topics |
| Q09 | - |  |  | SI | Renal replacement therapy is lifelong |
| Q10 | - |  |  | SI | Functions of the kidney |
| Q11 | - |  |  | SI | Transplant is a renal replacement therapy option a... |
| Q12 | - |  |  | SI | Advantages of renal transplant |
| Q13 | - |  |  | SI | Transplant waiting list |
| Q14 | - |  |  | SI | Facts about live kidney donation |
| Q15 | - |  |  | SI | Staying healthy |
| Q16 | - |  |  | SI | Tests to expect before kidney transplant |
| Q17 | - |  |  | SI | Review by transplant assessment team |
| Q18 | - |  |  | SI | Kidney transplant surgery travel preparation |
| Q19 | - |  |  | SI | Patient and family education notes |
| Q20 | - |  |  | SI | Need to remain healthy |
| Q21 | - |  |  | SI | Must be adherent with treatment |
| Q22 | - |  |  | SI | Must always be contactable |
| Q23 | - |  |  | SI | Transplant waitlist patient responsibilities notes |
| Q24 | - |  |  | SI | Placement of the transplant kidney |
| Q25 | - |  |  | SI | Surgical procedure |
| Q26 | - |  |  | SI | Removal of Tenckhoff catheter |
| Q27 | - |  |  | SI | Post-operative care discussed |
| Q28 | - |  |  | SI | Possible complications post surgery discussed |
| Q29 | - |  |  | SI | Day of surgery and post-op care notes |
| Q30 | - |  |  | SI | Returning to home / community |
| Q31 | - |  |  | SI | Living a healthy lifestyle |
| Q32 | - |  |  | SI | Attending all medical check-ups and completing dia... |
| Q33 | - |  |  | SI | Immunosuppressants and importance of taking medica... |
| Q34 | - |  |  | SI | Risk of infection, cancer and diabetes |
| Q35 | - |  |  | SI | Possibility of kidney rejection |
| Q36 | - |  |  | SI | Kidney transplantation average life span of 10 to ... |
| Q37 | - |  |  | SI | Reinforce renal transplant is an alternative treat... |
| Q38 | - |  |  | SI | Life after kidney transplant notes |
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
| VST_Code | varchar |  |  | NO | Code |
| VST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VST_CreatedDate | date |  |  | SI | Created Date |
| VST_CreatedTime | time |  |  | SI | Created Time |
| VST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VST_DateFrom | date |  |  | SI | Date From |
| VST_DateTo | date |  |  | SI | Date To |
| VST_Desc | varchar |  |  | NO | Description |
| VST_NationalCode | varchar |  |  | SI | NationalCode |
| VST_Owner | varchar |  |  | SI | Owner |
| VST_UpdatedDate | date |  |  | SI | Updated Date |
| VST_UpdatedTime | time |  |  | SI | Updated Time |
| VST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*