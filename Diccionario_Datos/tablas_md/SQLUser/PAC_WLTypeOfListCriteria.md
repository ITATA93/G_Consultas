# SQLUser.PAC_WLTypeOfListCriteria

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRIT_ParREf | bigint | PK |  | NO | PAC_WaitingListType Parent Reference |
| CRIT_Childsub | double |  |  | NO | Childsub |
| CRIT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CRIT_CreatedDate | date |  |  | SI | Created Date |
| CRIT_CreatedTime | time |  |  | SI | Created Time |
| CRIT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CRIT_EffDate | date |  |  | SI | Eff Date |
| CRIT_OfListCriteria | varchar |  |  | SI | Of List Criteria |
| CRIT_RowId | varchar |  |  | NO | - |
| CRIT_UpdatedDate | date |  |  | SI | Updated Date |
| CRIT_UpdatedTime | time |  |  | SI | Updated Time |
| CRIT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Are you sick today |
| Q02 | - |  |  | SI | Do you have allergies to medications, food, a vacc... |
| Q03 | - |  |  | SI | Have you ever had a serious reaction after receivi... |
| Q04 | - |  |  | SI | Do you have a long-term health problem with heart ... |
| Q05 | - |  |  | SI | Do you have cancer, leukemia, HIV/AIDS, or any oth... |
| Q06 | - |  |  | SI | In the past 3 months, have you taken medication th... |
| Q07 | - |  |  | SI | drugs for the treatment of rheumatoid arthritis, C... |
| Q08 | - |  |  | SI | Have you had a seizure or a brain or other nervous... |
| Q09 | - |  |  | SI | During the past year, have you received a transfus... |
| Q10 | - |  |  | SI | Are you pregnant or is there a chance you could be... |
| Q11 | - |  |  | SI | Have you received any vaccinations in the past 4 w... |
| Q12 | - |  |  | SI | Did you bring your Immunization Record Card with y... |
| Q13 | - |  |  | SI | Patient's signature |
| Q13UDt | - |  |  | SI | Patient's signature Last Updated Date |
| Q13UTm | - |  |  | SI | Patient's signature Last Updated Time |
| Q14 | - |  |  | SI | For patients: The above questions will help us det... |
| Q15 | - |  |  | SI | answer “yes” to any question, it does not necessar... |
| Q16 | - |  |  | SI | additional questions must be asked. If a question ... |
| Q17P1 | - |  |  | SI | drugs for the treatment of rheumatoid arthritis, C... |
| Q17P2 | - |  |  | SI | or psoriasis |
| Q19 | - |  |  | SI | Date |
| Q20 | - |  |  | SI | Time |
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