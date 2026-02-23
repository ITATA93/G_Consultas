# SQLUser.OEC_Order_AdminStatus

**Schema:** SQLUser
**Columnas:** 143
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STAT_RowId | bigint | PK |  | NO | - |
| Q03 | - |  |  | SI | Treatment / Procedure / Operations / Investigation... |
| Q04 | - |  |  | SI | List the treatment(s)/ operation(s)/ investigation... |
| Q04a | - |  |  | SI | List the treatment(s)/ procedure(s)/ investigation... |
| Q05 | - |  |  | SI | This procedure may require |
| Q06 | - |  |  | SI | Doctor |
| Q08 | - |  |  | SI | Signature Doctor |
| Q08UDt | - |  |  | SI | Signature Doctor Last Updated Date |
| Q08UTm | - |  |  | SI | Signature Doctor Last Updated Time |
| Q09 | - |  |  | SI | Laterality: Note which side of the body the proced... |
| Q10 | - |  |  | SI | Any extra procedures that might become necessary d... |
| Q10a | - |  |  | SI | Note |
| Q11 | - |  |  | SI | The following information leaflet has been provide... |
| Q12 | - |  |  | SI | Creutzfeldt Jakob disease (CJD) |
| Q13 | - |  |  | SI | Have you ever been notified that you are at risk o... |
| Q14 | - |  |  | SI | Photography, Audio or Visual Recording |
| Q15 | - |  |  | SI | I agree to the use of any of the above type of rec... |
| Q16 | - |  |  | SI | I agree to unidentified versions of any of the abo... |
| Q17 | - |  |  | SI | Medical Training |
| Q18 | - |  |  | SI | I agree to the involvement of medical and other st... |
| Q19 | - |  |  | SI | Use of Tissue |
| Q20 | - |  |  | SI | I agree that tissue (including blood) not needed f... |
| Q21 | - |  |  | SI | Where additional clinical information is needed fo... |
| Q22 | - |  |  | SI | I have informed the patient of the treatment optio... |
| Q23 | - |  |  | SI | I have recommended the treatment(s) / procedure(s)... |
| Q24 | - |  |  | SI | I have explained the treatment(s) / procedure(s) /... |
| Q25 | - |  |  | SI | I have provided the patient with information speci... |
| Q26 | - |  |  | SI | I have given the patient the opportunity to discus... |
| Q27 | - |  |  | SI | The doctor has explained my medical condition and ... |
| Q28 | - |  |  | SI | The risks of the procedure have been explained to ... |
| Q30 | - |  |  | SI | I understand that the result / outcome of the trea... |
| Q31 | - |  |  | SI | I understand that if immediate life-threating even... |
| Q32 | - |  |  | SI | I consent to undergo the procedure(s) treatment(s)... |
| Q33 | - |  |  | SI | My questions have been answered to my satisfaction... |
| Q34 | - |  |  | SI | Any procedures that the patient DOES NOT wish to b... |
| Q35 | - |  |  | SI | I have read and understood the Patient Information... |
| Q36 | - |  |  | SI | Signed Patient |
| Q36UDt | - |  |  | SI | Signed Patient Last Updated Date |
| Q36UTm | - |  |  | SI | Signed Patient Last Updated Time |
| Q37 | - |  |  | SI | Signing for a child or young person |
| Q37a | - |  |  | SI | I confirm I am a person with parental / guardiansh... |
| Q37b | - |  |  | SI | Signed (Parent / guardian) |
| Q37bUDt | - |  |  | SI | Signed (Parent / guardian) Last Updated Date |
| Q37bUTm | - |  |  | SI | Signed (Parent / guardian) Last Updated Time |
| Q37c | - |  |  | SI | Name (Parent / guardian) |
| Q37d | - |  |  | SI | Relationship to patient |
| Q40 | - |  |  | SI | If the patient is unable to sign but has indicated... |
| Q41 | - |  |  | SI | Signed (Witness) |
| Q41UDt | - |  |  | SI | Signed (Witness) Last Updated Date |
| Q41UTm | - |  |  | SI | Signed (Witness) Last Updated Time |
| Q41c | - |  |  | SI | Name of witness |
| Q45 | - |  |  | SI | Confirmation of consent |
| Q46 | - |  |  | SI | Confirmation of consent (where the treatment / pro... |
| Q46a | - |  |  | SI | and consents to the treatment |
| Q47 | - |  |  | SI | Signed (Care Provider) |
| Q47UDt | - |  |  | SI | Signed (Care Provider) Last Updated Date |
| Q47UTm | - |  |  | SI | Signed (Care Provider) Last Updated Time |
| Q49 | - |  |  | SI | Name |
| Q50 | - |  |  | SI | Interpreter’s statement |
| Q51 | - |  |  | SI | I have interpreted the information to the best of ... |
| Q52 | - |  |  | SI | Signed (Interpreter) |
| Q52UDt | - |  |  | SI | Signed (Interpreter) Last Updated Date |
| Q52UTm | - |  |  | SI | Signed (Interpreter) Last Updated Time |
| Q52c | - |  |  | SI | Name |
| Q52d | - |  |  | SI | Or, please note the intepreter service reference I... |
| Q56 | - |  |  | SI | Withdrawal of patient consent |
| Q56b | - |  |  | SI | The patient has withdrawn consent (Check this box ... |
| Q56c | - |  |  | SI | Signed (Patient) |
| Q56cUDt | - |  |  | SI | Signed (Patient) Last Updated Date |
| Q56cUTm | - |  |  | SI | Signed (Patient) Last Updated Time |
| Q56d | - |  |  | SI | Reason given to withdraw consent (if known) |
| Q56e | - |  |  | SI | Signed (Care Provider) |
| Q56eUDt | - |  |  | SI | Signed (Care Provider) Last Updated Date |
| Q56eUTm | - |  |  | SI | Signed (Care Provider) Last Updated Time |
| Q61 | - |  |  | SI | Date |
| Q62 | - |  |  | SI | Name (CP) |
| Q63 | - |  |  | SI | I hereby authorize and consent to the presence of ... |
| Q63a | - |  |  | SI | They have no role or responsibility in performing ... |
| Q64 | - |  |  | SI | Time |
| Q65 | - |  |  | SI | Planned operation |
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
| STAT_AdminWorkflowDecision | varchar |  |  | SI | Administration Workflow Decision |
| STAT_Bill | varchar |  |  | SI | Bill flag |
| STAT_CanAdminSkinTest | varchar |  |  | SI | CanAdminSkinTest |
| STAT_Code | varchar |  |  | NO | Code |
| STAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STAT_CreatedDate | date |  |  | SI | Created Date |
| STAT_CreatedTime | time |  |  | SI | Created Time |
| STAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STAT_DateFrom | date |  |  | SI | DateFrom |
| STAT_DateTo | date |  |  | SI | DateTo |
| STAT_DeductStock | varchar |  |  | SI | Deduct Stock flag |
| STAT_Desc | varchar |  |  | NO | Description |
| STAT_IVCompleted | varchar |  |  | SI | IVCompleted |
| STAT_Icon | varchar |  |  | SI | Icon |
| STAT_IconLate | varchar |  |  | SI | IconLate |
| STAT_Owner | varchar |  |  | SI | Owner |
| STAT_ResolveNotReq | varchar |  |  | SI | Resolve Not Required flag |
| STAT_SecondSignature | varchar |  |  | SI | Suppression of Second Signature |
| STAT_SystemAdminStatus | varchar |  |  | SI | System Administration Status |
| STAT_UpdatedDate | date |  |  | SI | Updated Date |
| STAT_UpdatedTime | time |  |  | SI | Updated Time |
| STAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| STAT_VarianceReasonMandatory | varchar |  |  | SI | Variance Reason Mandatory |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*