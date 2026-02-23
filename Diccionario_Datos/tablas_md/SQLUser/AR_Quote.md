# SQLUser.AR_Quote

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QT_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | COMPLEJIDAD ALTA |
| Q02 | - |  |  | SI | COMPLEJIDAD INTERMEDIA |
| Q03 | - |  |  | SI | COMPLEJIDAD BAJA |
| Q04 | - |  |  | SI | Resultado de Nivel de Complejidad |
| Q05 | - |  |  | SI | Fecha de Evaluación |
| Q06 | - |  |  | SI | Hora de Evaluación |
| Q07 | - |  |  | SI | Comentarios |
| QT_AdditionICDList | varchar |  |  | SI | Additional Diagnosis List |
| QT_AdmCategory_DR | bigint |  | FK | SI | Des Ref PACAdmCategory |
| QT_AnaestMethod_DR | bigint |  | FK | SI | Des Ref ORCAnaestMethod |
| QT_AppServTaxToAccom | varchar |  |  | SI | Apply Service Tax to Accommodation |
| QT_BedType_DR | bigint |  | FK | SI | Des Ref PACBedType - Bed Type |
| QT_BillServiceTaxToPatient | varchar |  |  | SI | Bill Service Tax to Patient |
| QT_CareProvClaimID | varchar |  |  | SI | Care Provider Claim ID |
| QT_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| QT_CoPaymentAmount | double |  |  | SI | Co-Payments Amount |
| QT_CoPaymentDays | double |  |  | SI | Co-Payments Days |
| QT_CoPaymentMaxDays | double |  |  | SI | Co-Payment Maximum Days |
| QT_CommentDisc | varchar |  |  | SI | Discount Comment |
| QT_Comments | varchar |  |  | SI | Comments |
| QT_DRGBilling | varchar |  |  | SI | DRG Billing |
| QT_DRGCode_DR | bigint |  | FK | SI | Des Ref MRCDRGCodes |
| QT_DRGWeight | double |  |  | SI | DRG Weight |
| QT_DVAWhitCareAppr | varchar |  |  | SI | DVA White Card Approval Record |
| QT_DailyCopaymentAmt | double |  |  | SI | DailyCopaymentAmt |
| QT_DailyPrivRoomCopayment | double |  |  | SI | Daily private room co-payment |
| QT_Date | date |  |  | SI | Date |
| QT_DiscType_DR | bigint |  | FK | SI | Des Ref DiscType |
| QT_Dob | date |  |  | SI | Dob |
| QT_EpisodeSubType_DR | bigint |  | FK | SI | Des Ref PACEpisodeSubType - Episode Sub Type |
| QT_EpisodeType | varchar |  |  | SI | Episode Type |
| QT_EpisodicBilling | varchar |  |  | SI | Episodic Billing |
| QT_Excess | double |  |  | SI | Excess |
| QT_ExpAdmDate | date |  |  | SI | Exp Adm Date |
| QT_ExpAnaestTime | double |  |  | SI | Expected Anaesthetic Time |
| QT_ExpLOS | double |  |  | SI | Exp LOS |
| QT_ExpiryDate | date |  |  | SI | Expiry Date |
| QT_GivenName | varchar |  |  | SI | GivenName |
| QT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| QT_ICD_DR | bigint |  | FK | SI | Des Ref MRCICDDx - Primary Diagnosis |
| QT_MaxCopaymentDays | double |  |  | SI | maximum co-payment days |
| QT_MaxPrivRoomCopaymentDays | double |  |  | SI | maximum private room co-payment days |
| QT_Number | varchar |  |  | SI | Number |
| QT_OperCateg_DR | bigint |  | FK | SI | Des Ref ORCOperationCategory |
| QT_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| QT_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPMI |
| QT_PEAFormRequire | varchar |  |  | SI | PEA Form Required |
| QT_PaidUpTo | date |  |  | SI | Paid Up To  |
| QT_PaidUpToDate | varchar |  |  | SI | Paid Up To Date |
| QT_PatIsFinancial | varchar |  |  | SI | Patient is Financial |
| QT_PatientDiscAmount | double |  |  | SI | Patient Discount Amount |
| QT_PatientDiscPerc | double |  |  | SI | Patient Discount Percentage |
| QT_PatientWeight | double |  |  | SI | Patient Weight |
| QT_PayorDiscAmount | double |  |  | SI | Payor Discount Amount |
| QT_PayorDiscPerc | double |  |  | SI | Payor Discount Percentage |
| QT_PayorPlan | varchar |  |  | SI | PayorPlan |
| QT_PayorShare | double |  |  | SI | Payor Share |
| QT_QualPeriods | varchar |  |  | SI | Qualifying Periods |
| QT_RefDoc_DR | bigint |  | FK | SI | Des Ref PACRefDoctor - External Referral Doctor |
| QT_RespUnit_DR | bigint |  | FK | SI | Des Ref RespUnit |
| QT_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| QT_SameDay | varchar |  |  | SI | Same Day |
| QT_SameDayCopayment | double |  |  | SI | Same day co-payment  |
| QT_ServiceTax | bigint |  |  | SI | Service Tax |
| QT_Surname | varchar |  |  | SI | Surname |
| QT_TheatreCopayment | double |  |  | SI | Theatre co-payment  |
| QT_Time | time |  |  | SI | Time |
| QT_User_DR | bigint |  | FK | SI | Des Ref User |
| QT_WCLetterOfAppr | varchar |  |  | SI | WC Letter of Approval Form Record |
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