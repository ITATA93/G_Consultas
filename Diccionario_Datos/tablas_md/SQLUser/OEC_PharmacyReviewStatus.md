# SQLUser.OEC_PharmacyReviewStatus

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHARMREVST_RowId | bigint | PK |  | NO | - |
| PHARMREVST_Code | varchar |  |  | NO | Code |
| PHARMREVST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHARMREVST_Colour | varchar |  |  | SI | Colour |
| PHARMREVST_CreatedDate | date |  |  | SI | Created Date |
| PHARMREVST_CreatedTime | time |  |  | SI | Created Time |
| PHARMREVST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHARMREVST_Desc | varchar |  |  | NO | Description |
| PHARMREVST_Owner | varchar |  |  | SI | Owner |
| PHARMREVST_Rank | double |  |  | SI | Rank |
| PHARMREVST_UpdatedDate | date |  |  | SI | Updated Date |
| PHARMREVST_UpdatedTime | time |  |  | SI | Updated Time |
| PHARMREVST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q13 | - |  |  | SI | Cooling device |
| Q14 | - |  |  | SI | Monitors used |
| Q15 | - |  |  | SI | Nurses notes |
| Q16 | - |  |  | SI | Dressing comments |
| Q17 | - |  |  | SI | Drainage comments |
| Q18 | - |  |  | SI | Handover received from |
| Q19 | - |  |  | SI | Conscious at |
| Q20 | - |  |  | SI | Conscious at |
| Q21 | - |  |  | SI | Conscious on arrival |
| Q22 | - |  |  | SI | Airway |
| Q23 | - |  |  | SI | Anaesthetic type |
| Q24 | - |  |  | SI | Intravenous (IV) access in situ |
| Q25 | - |  |  | SI | IV comment |
| Q26 | - |  |  | SI | Neurovascular status |
| Q27 | - |  |  | SI | Neurovascular comments |
| Q28 | - |  |  | SI | Post Anaesthetic Care (PAC) |
| Q29 | - |  |  | SI | Sedation Score (RASS) |
| Q30 | - |  |  | SI | PAC comments |
| Q31 | - |  |  | SI | Wound drainage on arrival |
| Q32 | - |  |  | SI | Pulse |
| Q32ObsDR | - |  |  | SI | Pulse DR |
| Q33 | - |  |  | SI | Dressings |
| Q34 | - |  |  | SI | Date |
| Q35 | - |  |  | SI | O2 administered l/min |
| Q35ObsDR | - |  |  | SI | O2 administered l/min DR |
| Q36 | - |  |  | SI | Time |
| Q37 | - |  |  | SI | Catheter in situ |
| Q38 | - |  |  | SI | Catheter comments |
| Q39 | - |  |  | SI | For catheters remaining in situ, please complete i... |
| Q40 | - |  |  | SI | Irrigation checked |
| Q41 | - |  |  | SI | O2 flow rate (L/min) |
| Q41ObsDR | - |  |  | SI | O2 flow rate (L/min) DR |
| Q42 | - |  |  | SI | Pain score |
| Q42ObsDR | - |  |  | SI | Pain score DR |
| Q46 | - |  |  | SI | Airway comments |
| QQ10 | - |  |  | SI | Dressing status |
| QQ11 | - |  |  | SI | Catheter checked |
| QQ12 | - |  |  | SI | Irrigation checked |
| QQ13 | - |  |  | SI | Mouth care given |
| QQ22 | - |  |  | SI | Warming Blanket / Machine |
| QQ23 | - |  |  | SI | IV cannula removed |
| QQ25 | - |  |  | SI | Pain score |
| QQ3 | - |  |  | SI | Initial Assessment |
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