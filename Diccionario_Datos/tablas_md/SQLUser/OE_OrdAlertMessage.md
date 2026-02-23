# SQLUser.OE_OrdAlertMessage

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALM_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ALM_AlertResponseType | varchar |  |  | SI | Alert Response Type |
| ALM_AlertType | varchar |  |  | SI | AlertType |
| ALM_AllergyID | varchar |  |  | SI | Allergy Match ID |
| ALM_Arcim_DR | varchar |  | FK | SI | DR to ARCIM: Interacting Arcim (this order) |
| ALM_Childsub | double |  |  | NO | Childsub |
| ALM_ConfMessage | varchar |  |  | SI | Conflict Message |
| ALM_DSSActionItem_DR | varchar |  | FK | SI | Alert Action Item from websys_DecisionSupport.Audi... |
| ALM_DateUpdate | date |  |  | SI | DateUpdate |
| ALM_Fatal | varchar |  |  | SI | Fatal alert |
| ALM_FullMessage | varchar |  |  | SI | Full Message |
| ALM_HardStop | bit |  |  | SI | Hard Stop |
| ALM_IntArcim_DR | varchar |  | FK | SI | DR to ARCIM: Arcim interacting with (other order) |
| ALM_Message | varchar |  |  | SI | Message |
| ALM_MonoGraphLink | varchar |  |  | SI | Monograph link parameters |
| ALM_Note_DR | varchar |  | FK | SI | Alert Disagreement Notes ID |
| ALM_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| ALM_OverrideReason_DR | bigint |  | FK | SI | Des Ref OverrideReason |
| ALM_Priority | varchar |  |  | SI | Priority |
| ALM_ReasonRequired | varchar |  |  | SI | ReasonRequired |
| ALM_ResultID | varchar |  |  | SI | ResultID - Used to display link to current result ... |
| ALM_RowId | varchar |  |  | NO | - |
| ALM_Severity | varchar |  |  | SI | Severity |
| ALM_SeverityColour | varchar |  |  | SI | SeverityColour |
| ALM_TimeUpdate | time |  |  | SI | TimeUpdate |
| ALM_UserUpdate_DR | bigint |  | FK | SI | Des Ref UserUpdate |
| Q01 | - |  |  | SI | Tympanometry |
| Q02 | - |  |  | SI | Right |
| Q03 | - |  |  | SI | Left |
| Q04 | - |  |  | SI | Type |
| Q05 | - |  |  | SI | Type (Right) |
| Q06 | - |  |  | SI | Type (Left) |
| Q07 | - |  |  | SI | Middle ear pressure |
| Q08 | - |  |  | SI | Middle ear pressure (Right) |
| Q09 | - |  |  | SI | Middle Ear Pressure (Left) |
| Q10 | - |  |  | SI | Static compliance |
| Q11 | - |  |  | SI | Static Compliance (Right) |
| Q12 | - |  |  | SI | Static Compliance (Left) |
| Q13 | - |  |  | SI | Ear canal volume |
| Q14 | - |  |  | SI | Ear Canal Volume (Right) |
| Q15 | - |  |  | SI | Ear Canal Volume (Left) |
| Q16 | - |  |  | SI | Hearing Case History |
| Q17 | - |  |  | SI | Date of assessment |
| Q18 | - |  |  | SI | Reason for referral |
| Q19 | - |  |  | SI | Passed newborn hearing screening? |
| Q20 | - |  |  | SI | Note |
| Q21 | - |  |  | SI | Speech pathology involved? |
| Q22 | - |  |  | SI | If yes, provide details |
| Q23 | - |  |  | SI | Family history of hearing loss |
| Q24 | - |  |  | SI | Family history detail |
| Q25 | - |  |  | SI | Tinnitus |
| Q26 | - |  |  | SI | Tinnitus detail |
| Q27 | - |  |  | SI | Otorrhea |
| Q28 | - |  |  | SI | Vertigo |
| Q29 | - |  |  | SI | Ear nose & throat involvement / Operations |
| Q30 | - |  |  | SI | Noise exposure |
| Q31 | - |  |  | SI | Further information |
| Q32 | - |  |  | SI | Date |
| Q33 | - |  |  | SI | Time |
| Q34 | - |  |  | SI | Middle ear pressure (Right) |
| Q35 | - |  |  | SI | Middle ear pressure (Left) |
| Q36 | - |  |  | SI | Static compliance (Right) |
| Q37 | - |  |  | SI | Static compliance (Left) |
| Q38 | - |  |  | SI | Ear canal volume (Right) |
| Q39 | - |  |  | SI | Ear canal volume (Left) |
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