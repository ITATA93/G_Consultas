# SQLUser.PAC_RoomStatus

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROOMST_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Medication usually managed by |
| Q04 | - |  |  | SI | If other specify |
| Q05 | - |  |  | SI | Preferred administration method? |
| Q06 | - |  |  | SI | If other specify |
| Q07 | - |  |  | SI | Did the patient bring own medicines? |
| Q08 | - |  |  | SI | Location of own medicines |
| Q09 | - |  |  | SI | Patient's immunisation up to date? |
| Q10 | - |  |  | SI | Community pharmacy details |
| Q11 | - |  |  | SI | General practitioner details |
| Q12 | - |  |  | SI | Level of independence |
| Q13 | - |  |  | SI | Lives alone |
| Q14 | - |  |  | SI | Lives in residential care facility |
| Q15 | - |  |  | SI | Residential care facility details |
| Q16 | - |  |  | SI | Uses dose administration device? |
| Q17 | - |  |  | SI | Administration device |
| Q18 | - |  |  | SI | Uses a dose administration aid? |
| Q19 | - |  |  | SI | Dose administration aid |
| Q20 | - |  |  | SI | Uses a medication list? |
| Q21 | - |  |  | SI | Swallowing issues |
| Q22 | - |  |  | SI | Impairment(s) |
| Q23 | - |  |  | SI | Other information |
| Q24 | - |  |  | SI | Patient Assessment |
| Q25 | - |  |  | SI | Can read / comprehend labels? |
| Q26 | - |  |  | SI | Can understand english? |
| Q27 | - |  |  | SI | Language spoken |
| Q28 | - |  |  | SI | Can open bottles? |
| Q29 | - |  |  | SI | Can measure liquids? |
| Q30 | - |  |  | SI | Recent home medicines review? |
| Q31 | - |  |  | SI | Home medicines review date |
| Q32 | - |  |  | SI | Supply medication list on discharge? |
| Q33 | - |  |  | SI | Suspected non-adherence? |
| Q34 | - |  |  | SI | Other information |
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
| ROOMST_Code | varchar |  |  | NO | Code |
| ROOMST_CreatedDate | date |  |  | SI | Created Date |
| ROOMST_CreatedTime | time |  |  | SI | Created Time |
| ROOMST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROOMST_Desc | varchar |  |  | NO | Description |
| ROOMST_UpdatedDate | date |  |  | SI | Updated Date |
| ROOMST_UpdatedTime | time |  |  | SI | Updated Time |
| ROOMST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*