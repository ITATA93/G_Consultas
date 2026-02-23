# SQLUser.PA_AdmInsurance

**Schema:** SQLUser
**Columnas:** 169
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INS_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| INS_AccidentDate | date |  |  | SI | Accident Date |
| INS_AccomRate | double |  |  | SI | AccomRate |
| INS_AdminCategory_DR | bigint |  | FK | SI | Des Ref AccountClass |
| INS_ApplyGST | varchar |  |  | SI | Apply GST |
| INS_ApplyShareTotalAmount | varchar |  |  | SI | Apply Share of TotalAmount |
| INS_ApprovedGuarDate | date |  |  | SI | Approved Guarant Date |
| INS_AuthorizationCode | varchar |  |  | SI | Authorization Code |
| INS_AutoAssignedFlg | varchar |  |  | SI | Auto Assigned Flag |
| INS_AuxInsType_DR | bigint |  | FK | SI | Des Ref to AuxInsType |
| INS_BenefitPackage_DR | varchar |  | FK | SI | Des Ref ARCAuxilInsurTypeBenefitPackage |
| INS_BillServiceTaxToPatient | varchar |  |  | SI | Bill Service Tax to Patient |
| INS_BillingMethod_DR | bigint |  | FK | SI | Des Ref BillingMethod |
| INS_CTREL_DR | bigint |  | FK | SI | Des Ref to CTREL |
| INS_CarRegoNo | varchar |  |  | SI | Car Rego No |
| INS_CardInitDate | date |  |  | SI | CardInitDate |
| INS_CardNo | varchar |  |  | SI | Insurance Card No |
| INS_CardType_DR | bigint |  | FK | SI | Des Ref CardType |
| INS_CardholderAddress | varchar |  |  | SI | Cardholder Address |
| INS_CardholderCity_DR | bigint |  | FK | SI | Des Ref City |
| INS_CardholderId | varchar |  |  | SI | Cardholder Id |
| INS_CardholderName | varchar |  |  | SI | Cardholder Name |
| INS_CardholderZip_DR | bigint |  | FK | SI | Des Ref Zip |
| INS_CaseClaimNo | varchar |  |  | SI | Case Claim No |
| INS_Childsub | double |  |  | NO | Childsub |
| INS_CoPaymentPercentage | double |  |  | SI | CoPaymentPercentage |
| INS_CommReportedDate | date |  |  | SI | Commissioning Reported Date |
| INS_CompensationClaim | varchar |  |  | SI | Compensation Claim |
| INS_ConcessionCardExpDate | date |  |  | SI | Concession Card Exp Date |
| INS_ConcessionCardNo | varchar |  |  | SI | Concession Card No |
| INS_ContactInsurCo | varchar |  |  | SI | Contact to Insur.Co |
| INS_CoordinationOfBenefits | varchar |  |  | SI | Coordination of benefits |
| INS_CopiedIns_DR | varchar |  | FK | SI | Des Ref CopiedIns |
| INS_DVAnumber | varchar |  |  | SI | DVA number |
| INS_DailyCopaymentAmt | double |  |  | SI | DailyCopaymentAmt |
| INS_DailyCover | varchar |  |  | SI | Daily Cover |
| INS_DailyICUCover | double |  |  | SI | Daily ICU Cover |
| INS_DailyPrivRoomCopayment | double |  |  | SI | Daily private room co-payment |
| INS_DateFirstHaveInsur | date |  |  | SI | Date First Have Insur |
| INS_DateTypeFrom | date |  |  | SI | Date Type From |
| INS_DateTypeTo | date |  |  | SI | Date Type To |
| INS_DateValidFrom | date |  |  | SI | Date Valid From |
| INS_DateValidTo | date |  |  | SI | Date Valid To |
| INS_EstimIPEndDate | date |  |  | SI | Estim InPat End Date |
| INS_EstimIPStartDate | date |  |  | SI | Estim InPat Start Date |
| INS_EstimOPEndDate | date |  |  | SI | Estim OutPat End Date |
| INS_EstimOPStartDate | date |  |  | SI | Estim OutPat Start Date |
| INS_Excess | varchar |  |  | SI | Excess |
| INS_FixedPatShare | double |  |  | SI | Fixed Pat Share |
| INS_GroupName | varchar |  |  | SI | Insurance Group Name |
| INS_GroupNumber | varchar |  |  | SI | Insurance Group Number |
| INS_InsAssoc_DR | bigint |  | FK | SI | Des Ref to InsAssoc |
| INS_InsType_DR | bigint |  | FK | NO | Des Ref to InsType |
| INS_InsuranceStatus_DR | bigint |  | FK | SI | Des Ref ARCInsuranceStatus |
| INS_LastVerifiedDate | date |  |  | SI | Last verified date |
| INS_MainInsuranceFlag | varchar |  |  | SI | Main Insurance Flag |
| INS_MaxAmountPercentage | double |  |  | SI | MaxAmountPercentage |
| INS_MaxCopaymentAmt | double |  |  | SI | MaxCopaymentAmt |
| INS_MaxCopaymentDays | double |  |  | SI | maximum co-payment days |
| INS_MaxDailyAmount | double |  |  | SI | MaxDailyAmount |
| INS_MaxPrivRoomCopaymentDays | double |  |  | SI | maximum private room co-payment days |
| INS_MinSurmountAmt | double |  |  | SI | Min Surmount Amt |
| INS_NotificationDate | date |  |  | SI | Notification Date |
| INS_OfficeNo | varchar |  |  | SI | OfficeNo |
| INS_PayFrom | double |  |  | SI | PayFrom |
| INS_PayUntill | double |  |  | SI | PayUntill |
| INS_PayorContactType_DR | bigint |  | FK | SI | Des Ref PayorContactType |
| INS_PayorShare | double |  |  | SI | Payor Share |
| INS_PayorVariationComments | varchar |  |  | SI | Payor Variation Comments |
| INS_PersonPackage_DR | varchar |  | FK | SI | Des Ref PAPersonPackage |
| INS_PreCertificationRequirement | varchar |  |  | SI | Pre-certification requirement |
| INS_Rank | varchar |  |  | SI | Rank |
| INS_RoomType_DR | bigint |  | FK | SI | Des Ref PACRoomType |
| INS_RowId | varchar |  |  | NO | - |
| INS_RoyalOrderNo | varchar |  |  | SI | RoyalOrderNo |
| INS_RoyalOrder_DR | varchar |  | FK | SI | Des Ref RoyalOrder |
| INS_SafetyNetCardExpDate | date |  |  | SI | Safety Net Card Exp Date |
| INS_SafetyNetCardNo | varchar |  |  | SI | Safety Net Card No |
| INS_SameDayCopayment | double |  |  | SI | Same day co-payment  |
| INS_SharedRoomCopaymentAmt | double |  |  | SI | Shared Room Copayment Amt |
| INS_StampDutyPercentage | varchar |  |  | SI | Stamp Duty Percentage |
| INS_SurmountingAmount | double |  |  | SI | SurmountingAmount |
| INS_SurmountingLimit | double |  |  | SI | SurmountingLimit |
| INS_SurmountingPercentage | double |  |  | SI | SurmountingPercentage |
| INS_TheatreCopayment | double |  |  | SI | Theatre co-payment  |
| INS_TimeFrom | time |  |  | SI | Time From |
| INS_TimeTo | time |  |  | SI | TimeTo |
| INS_TotalChargeCover | varchar |  |  | SI | Total Charge Cover |
| INS_TypeOfPolicy | varchar |  |  | SI | Type of policy |
| INS_UpdateDate | date |  |  | SI | UpdateDate |
| INS_UpdateTime | time |  |  | SI | UpdateTime |
| INS_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| INS_UpdateUser_DR | bigint |  | FK | SI | Des REf UpdateUser |
| INS_UseOwnTariff | varchar |  |  | SI | UseOwnTariff |
| INS_VCFeeRate | double |  |  | SI | VCFeeRate |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Have you noticed any difficulty remembering things... |
| Q04 | - |  |  | SI | Do you have difficulty remembering information tha... |
| Q05 | - |  |  | SI | Do you have difficulty memorizing things, such as ... |
| Q06 | - |  |  | SI | Do you have difficulty remembering the names of yo... |
| Q07 | - |  |  | SI | Do you ever forget things, such as a date with a f... |
| Q08 | - |  |  | SI | Do you forget to take your medication? |
| Q09 | - |  |  | SI | Do you have difficulty remembering information tha... |
| Q10 | - |  |  | SI | Do you have difficulty doing household chores or r... |
| Q11 | - |  |  | SI | Do you have difficulty remembering how to get to t... |
| Q12 | - |  |  | SI | Do you have difficulty remembering the names of we... |
| Q13 | - |  |  | SI | Do you have difficulty remembering national capita... |
| Q14 | - |  |  | SI | Are you absent - minded or up in the clouds? For e... |
| Q15 | - |  |  | SI | Do you have difficulty being on the alert or react... |
| Q16 | - |  |  | SI | Do you have difficulty making out what’s important... |
| Q17 | - |  |  | SI | Are you unable to do two things at once? For examp... |
| Q18 | - |  |  | SI | Do you have trouble focusing your attention on the... |
| Q19 | - |  |  | SI | Do you have difficulty planning out your activitie... |
| Q20 | - |  |  | SI | Do you have difficulty coordinating your movements... |
| Q21 | - |  |  | SI | Do you have difficulty changing your movements, de... |
| Q22 | - |  |  | SI | Do you have difficulty finding your words, forming... |
| Q23 | - |  |  | SI | Do you have difficulty getting dressed or eating? ... |
| Q24 | - |  |  | SI | For example, the name of your medication or your n... |
| Q25 | - |  |  | SI | preparing meals, doing housework, doing laundry, u... |
| Q26 | - |  |  | SI | Score |
| Q27 | - |  |  | SI | Classification |
| Q28 | - |  |  | SI | 0 - 84 |
| Q29 | - |  |  | SI | 0 - 84: Higher the score, higher could be the cogn... |
| Q30 | - |  |  | SI | Subjective Scale to Investigate Cognition in Schiz... |
| Q31 | - |  |  | SI | Higher the score, higher could be the cognitive im... |
| Q32 | - |  |  | SI | The aim of the study is the validation of the Subj... |
| Q33 | - |  |  | SI | 0 - 84: Higher the score, higher could be the cogn... |
| Q34 | - |  |  | SI | Higher the score, higher could be the cognitive im... |
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