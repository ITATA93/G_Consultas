# SQLUser.PAC_Puerperium

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PUER_RowId | bigint | PK |  | NO | - |
| ChildQ12DR | - |  |  | SI | Child Reference: Oral trials completed |
| PUER_Active | varchar |  |  | SI | Active flag |
| PUER_Code | varchar |  |  | NO | Code |
| PUER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PUER_CreatedDate | date |  |  | SI | Created Date |
| PUER_CreatedTime | time |  |  | SI | Created Time |
| PUER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PUER_DateFrom | date |  |  | SI | Date From |
| PUER_DateTo | date |  |  | SI | Date To |
| PUER_Desc | varchar |  |  | NO | Description |
| PUER_NationalCode | varchar |  |  | SI | National Code |
| PUER_Owner | varchar |  |  | SI | Owner |
| PUER_UpdatedDate | date |  |  | SI | Updated Date |
| PUER_UpdatedTime | time |  |  | SI | Updated Time |
| PUER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Respiratory sufficiency and coordination during or... |
| Q04ObsDR | - |  |  | SI | Respiratory sufficiency and coordination during or... |
| Q05 | - |  |  | SI | Respiratory sufficiency and coordination comments |
| Q06 | - |  |  | SI | Oral trial finding |
| Q07 | - |  |  | SI | Phase of dysphagia |
| Q08 | - |  |  | SI | Severity of dysphagia |
| Q09 | - |  |  | SI | Contributing factors |
| Q10 | - |  |  | SI | Contributing factors comments |
| Q11 | - |  |  | SI | Impression |
| Q13 | - |  |  | SI | Overall impression |
| Q14 | - |  |  | SI | Diet |
| Q15 | - |  |  | SI | Recommended diet |
| Q16 | - |  |  | SI | Texture |
| Q17 | - |  |  | SI | Fluids |
| Q18 | - |  |  | SI | Diet comments |
| Q19 | - |  |  | SI | Precautions |
| Q20 | - |  |  | SI | Diet safety precautions |
| Q21 | - |  |  | SI | Diet safety precautions notes |
| Q22 | - |  |  | SI | Review |
| Q23 | - |  |  | SI | Review in |
| Q24 | - |  |  | SI | Ear Nose and Throat (ENT) investigation indicated? |
| Q25 | - |  |  | SI | Videofluoroscopy indicated? |
| Q26 | - |  |  | SI | Plan comments |
| Q27 | - |  |  | SI | Intervention program |
| Q28 | - |  |  | SI | Referrals |
| Q29 | - |  |  | SI | Referral orders placed in TrakCare? |
| Q30 | - |  |  | SI | Referral(s) external to TrakCare comment |
| Q31 | - |  |  | SI | Referral(s) external to TrakCare completed? |
| Q32 | - |  |  | SI | Referral detail |
| Q33 | - |  |  | SI | Education provided to |
| Q34 | - |  |  | SI | Type of education provided |
| Q35 | - |  |  | SI | Education details |
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