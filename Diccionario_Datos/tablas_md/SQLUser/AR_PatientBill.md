# SQLUser.AR_PatientBill

**Schema:** SQLUser
**Columnas:** 272
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARPBL_RowId | bigint | PK |  | NO | - |
| ARPBL_AccountingPeriod_DR | bigint |  | FK | SI | Des Ref AccountingPeriod |
| ARPBL_AccrualAccountPeriod_DR | bigint |  | FK | SI | Des Ref AccrualAccountPeriod |
| ARPBL_AdmDate | date |  |  | SI | Adm Date |
| ARPBL_AdvPaymInvApplied_DR | bigint |  | FK | SI | Des REf ARPBL Advance Payment invoice was applied. |
| ARPBL_AmountPayorPaid | double |  |  | SI | Amount Payor Paid |
| ARPBL_AmountToPay | double |  |  | SI | AmountToPay |
| ARPBL_AmountToPay1 | double |  |  | SI | Amount To Pay1 |
| ARPBL_AmountToPayStored | double |  |  | SI | Amount To Pay Stored |
| ARPBL_AppointmentDate | date |  |  | SI | AppointmentDate |
| ARPBL_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| ARPBL_AuxInstype1_DR | bigint |  | FK | SI | Des Ref AuxInstype1 |
| ARPBL_BatchProcess | varchar |  |  | SI | Batch Process |
| ARPBL_Batch_DR | bigint |  | FK | SI | Des Ref Batch |
| ARPBL_BillClaimStatus_DR | bigint |  | FK | SI | Des Ref ARCBillClaimStatus |
| ARPBL_BillDateFrom | date |  |  | SI | Bill DateFrom |
| ARPBL_BillDateTo | date |  |  | SI | Bill Date To |
| ARPBL_BillDesc_DR | bigint |  | FK | SI | Des Ref ARCBillDescription |
| ARPBL_BillNo | varchar |  |  | SI | Bill No |
| ARPBL_BillPeriodDateFrom | date |  |  | SI | Bill PeriodDateFrom |
| ARPBL_BillPeriodDateTo | date |  |  | SI | Bill Date To |
| ARPBL_BillRefund | varchar |  |  | SI | Bill/Refund |
| ARPBL_BillTimeFrom | time |  |  | SI | Bill Time From |
| ARPBL_BillTimeTo | time |  |  | SI | Bill Time To |
| ARPBL_BillType | varchar |  |  | SI | Bill Type |
| ARPBL_BillingType | varchar |  |  | SI | Billing Type |
| ARPBL_BloodCoupons320 | double |  |  | SI | Blood Coupons 320 |
| ARPBL_BloodCoupons400 | double |  |  | SI | Blood Coupons 400 |
| ARPBL_CTLOCPrinted_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ARPBL_CancelComments | varchar |  |  | SI | CancelComments |
| ARPBL_CancelHospital_DR | bigint |  | FK | SI | Des Ref CancelHospital |
| ARPBL_CareProvClaimID | varchar |  |  | SI | Care Provider Claim ID |
| ARPBL_CareProvLoc_DR | bigint |  | FK | SI | CareProviderLoc |
| ARPBL_CareProv_DR | varchar |  | FK | SI | CareProvider |
| ARPBL_ClaimComments | varchar |  |  | SI | Claim Comments |
| ARPBL_ClaimID | varchar |  |  | SI | Claim ID |
| ARPBL_ClaimRADateSettle | date |  |  | SI | Claim RA Date Settlement |
| ARPBL_ClaimRADenialComments | varchar |  |  | SI | Claim RA Denial Comments |
| ARPBL_ClaimRAIDPayor | varchar |  |  | SI | Claim RA ID Payor |
| ARPBL_ClaimRAPaymRef | varchar |  |  | SI | Claim RA Payment Reference |
| ARPBL_ClaimStored | varchar |  |  | SI | StoredClaim |
| ARPBL_CoPaymentAmount | double |  |  | SI | Co-Payment Amount |
| ARPBL_CoPaymentWithoutTax | double |  |  | SI | Co-Payment Without Tax |
| ARPBL_CommentDiscount | varchar |  |  | SI | Comment Discount |
| ARPBL_CommentOuts | varchar |  |  | SI | Comments Outstand |
| ARPBL_CreditAmt | double |  |  | SI | Credit Amt |
| ARPBL_CreditCmt | varchar |  |  | SI | Credit Comments |
| ARPBL_CreditRemaining | double |  |  | SI | Credit Remaining |
| ARPBL_Currency_DR | bigint |  | FK | SI | Des Ref Currency |
| ARPBL_DateCancelled | date |  |  | SI | DateCancelled |
| ARPBL_DateFrom | date |  |  | SI | Date From |
| ARPBL_DateOfService | date |  |  | SI | Date Of Service (Lab) |
| ARPBL_DatePrinted | date |  |  | SI | Date Bill Printed |
| ARPBL_DateReportPrinted | date |  |  | SI | DateReportPrinted |
| ARPBL_DateStatusChanged | date |  |  | SI | DateStatusChanged |
| ARPBL_DateTo | date |  |  | SI | Date To |
| ARPBL_DepartDisc | varchar |  |  | SI | Department Discount |
| ARPBL_DepartOuts | varchar |  |  | SI | Department Outstanding |
| ARPBL_DiscPerc | double |  |  | SI | Discount Percentage |
| ARPBL_DiscType_DR | bigint |  | FK | SI | Des Ref Discret DiscType |
| ARPBL_DischDate | date |  |  | SI | DischDate |
| ARPBL_DiscretAmt | double |  |  | SI | Discret Amt |
| ARPBL_DiscretDiscountWithoutTax | double |  |  | SI | Discretionary Discount Without Tax |
| ARPBL_DiscretOutstType_DR | bigint |  | FK | SI | Des Ref DiscretOutstType |
| ARPBL_EDISentDate | date |  |  | SI | EDISentDate |
| ARPBL_EmplNameDisc | varchar |  |  | SI | Empl Name Discount |
| ARPBL_EmplNameOuts | varchar |  |  | SI | Empl Name Outstanding |
| ARPBL_EmployeeDisc_DR | bigint |  | FK | SI | Des Ref EmployeeDisc |
| ARPBL_ExternalPaymentID | varchar |  |  | SI | External Payment ID |
| ARPBL_Flag1 | varchar |  |  | SI | Flag 1 |
| ARPBL_FollowUpIdentifier | varchar |  |  | SI | FollowUpIdentifier |
| ARPBL_FullCancelBill_DR | bigint |  | FK | SI | Des Ref ARPBL |
| ARPBL_GLBatch_DR | bigint |  | FK | SI | Des Ref GLBatch |
| ARPBL_GLWOBatch_DR | bigint |  | FK | SI | Des Ref GL Write off Batch |
| ARPBL_GrossAmount | double |  |  | SI | Gross Amount |
| ARPBL_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| ARPBL_InsAssociation_DR | bigint |  | FK | SI | Des Ref InsAssociation |
| ARPBL_InsType1_DR | bigint |  | FK | SI | Des Ref InsType1 |
| ARPBL_InsTypeFollowUpSeq_DR | varchar |  | FK | SI | Des Ref ARCInsTypeFollowUpSeq |
| ARPBL_InsuranceType_DR | bigint |  | FK | SI | Insurance Type DR |
| ARPBL_InsuranceUplift | double |  |  | SI | Insurance Uplift |
| ARPBL_InvoicedFlag | varchar |  |  | SI | Invoiced Flag |
| ARPBL_LabEpisodes | varchar |  |  | SI | Lab Episodes (Lab) |
| ARPBL_MasterLabEpisode_DR | bigint |  | FK | SI | Master Lab Episode (Lab)
The Patient details are ... |
| ARPBL_NetAmount | double |  |  | SI | Net Amount |
| ARPBL_NextDateReportPrinted | date |  |  | SI | NextDateReportPrinted |
| ARPBL_NextInsTypeFollowUpSeq_DR | varchar |  | FK | SI | Des Ref ARCInsTypeFollowUpSeq |
| ARPBL_Notes | varchar |  |  | SI | Notes |
| ARPBL_OEORD_DR | numeric |  | FK | SI | Des Ref OEORD |
| ARPBL_Original_Bill_DR | bigint |  | FK | SI | Des REf ARPBL Original_Bill_DR |
| ARPBL_OutstandAmt | double |  |  | SI | Outstanding Amt |
| ARPBL_OverrideAuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| ARPBL_OverrideCareProvClaimID | varchar |  |  | SI | Override Care Provider Claim ID  |
| ARPBL_OverridePayorCardNumber | varchar |  |  | SI | Override Payor Card Number |
| ARPBL_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| ARPBL_PatientBill_DR | bigint |  | FK | SI | Des Ref PatientBill |
| ARPBL_PatientMaster_DR | bigint |  | FK | SI | Patient Master (Lab) |
| ARPBL_PatientUplift | double |  |  | SI | Patient Uplift |
| ARPBL_PayedFlag | varchar |  |  | SI | Payed Flag |
| ARPBL_PaymAgreementDiscount | double |  |  | SI | Payment Agreement Discount |
| ARPBL_PaymentAgreement_DR | bigint |  | FK | SI | Payment Agreement (Lab) |
| ARPBL_PaymentDueDate | date |  |  | SI | Payment Due Date |
| ARPBL_PaymentLink | varchar |  |  | SI | Payment Link |
| ARPBL_PayorCardNumber | varchar |  |  | SI | Payor Card Number |
| ARPBL_PayorType | varchar |  |  | SI | Payor Type |
| ARPBL_PersonPackage_DR | varchar |  | FK | SI | Des Ref PAPersonPackage |
| ARPBL_PrelimBatch_DR | bigint |  | FK | SI | Preliminary Batch Number |
| ARPBL_PrincipalCPNumber | varchar |  |  | SI | Principal Care Provider Number |
| ARPBL_PrintCreditNote | varchar |  |  | SI | PrintCreditNote |
| ARPBL_ProgressStatus_DR | bigint |  | FK | SI | Des Ref ARCBillProgressStatus |
| ARPBL_QuoteUsed_DR | bigint |  | FK | SI | Quote Used Des Ref ARQuote |
| ARPBL_Quote_DR | bigint |  | FK | SI | Des Ref ARQuote |
| ARPBL_RADeniedAmount | double |  |  | SI | RA Denied Amount |
| ARPBL_ReasonCancel_DR | bigint |  | FK | SI | Des Ref ReasonCancel |
| ARPBL_ReasonClaimDenial_DR | bigint |  | FK | SI | Des Ref ARCReasonForClaimDenial |
| ARPBL_ReasonForRefund_DR | bigint |  | FK | SI | Des Ref ReasonForRefund |
| ARPBL_ReasonWriteOff_DR | bigint |  | FK | SI | Des Ref ReasonWriteOff |
| ARPBL_RefDoctor_DR | bigint |  | FK | SI | Des Ref PACRefDoctor |
| ARPBL_RefundBill_DR | bigint |  | FK | SI | Des Ref ARPBL_RefundBill_DR |
| ARPBL_RemainingDiscount | double |  |  | SI | Remaining Discount |
| ARPBL_ReportDateFrom | date |  |  | SI | Report Date From |
| ARPBL_ReportDateTo | date |  |  | SI | Report Date To |
| ARPBL_ResubmissionAmount | double |  |  | SI | Resubmission Amount |
| ARPBL_ResubmissionDate | date |  |  | SI | Resubmission Date |
| ARPBL_RoyalOrder_DR | varchar |  | FK | SI | Des Ref RoyalOrder |
| ARPBL_Signature | longvarbinary |  |  | SI | Signature |
| ARPBL_SundryDebtor_DR | bigint |  | FK | SI | Des Ref SundryDebtor |
| ARPBL_TimeCancelled | time |  |  | SI | Time Cancelled |
| ARPBL_TimePrinted | time |  |  | SI | TimePrinted |
| ARPBL_TimeStatusChanged | time |  |  | SI | TimeStatusChanged |
| ARPBL_TotalActRAPaymAmount | double |  |  | SI | Total Activity RA Payment amount  |
| ARPBL_TotalAllowed | double |  |  | SI | Total Allowed |
| ARPBL_TotalBillTax | double |  |  | SI | Total Bill Tax |
| ARPBL_TotalBloodDisc | double |  |  | SI | Total Blood Discount |
| ARPBL_TotalDRGCost | double |  |  | SI | Total DRG Cost |
| ARPBL_TotalDisallowed | double |  |  | SI | Total Disallowed |
| ARPBL_TotalEmployeeDisc | double |  |  | SI | Total Employee Discount |
| ARPBL_TotalInsCo | double |  |  | SI | Total InsCo |
| ARPBL_TotalMaterialAD | double |  |  | SI | Total Material AD |
| ARPBL_TotalMaterialAllowed | double |  |  | SI | Total Material Allowed |
| ARPBL_TotalMaterialDisallow | double |  |  | SI | Total Material Disallow |
| ARPBL_TotalMaterialUnauthor | double |  |  | SI | Total Material Unauthorised |
| ARPBL_TotalPatServiceAllowed | double |  |  | SI | Total Pat Service Allowed |
| ARPBL_TotalPatient | double |  |  | SI | Total Patient |
| ARPBL_TotalPatientOfAllowed | double |  |  | SI | Total Patient Of Allowed |
| ARPBL_TotalServiceAD | double |  |  | SI | Total Service AD |
| ARPBL_TotalServiceAllowed | double |  |  | SI | Total Service Allowed |
| ARPBL_TotalServiceUnauthor | double |  |  | SI | Total Service Unauthorised |
| ARPBL_TotalSpecialist | double |  |  | SI | Total Specialist |
| ARPBL_UnSettled | varchar |  |  | SI | UnSettled |
| ARPBL_UpdateDate | date |  |  | SI | UpdateDate |
| ARPBL_UpdateTime | time |  |  | SI | Update Time |
| ARPBL_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| ARPBL_UserBillerAssign_DR | bigint |  | FK | SI | Des Ref User Biller Assign |
| ARPBL_UserCancelBill_DR | bigint |  | FK | SI | Des Ref User |
| ARPBL_UserCoderAssign_DR | bigint |  | FK | SI | Des Ref User Coder Assign |
| ARPBL_UserPrinted_DR | bigint |  | FK | SI | Des Ref UserPrinted |
| ARPBL_UserStatusChanged_DR | bigint |  | FK | SI | Des Ref User |
| ARPBL_Version_DR | bigint |  | FK | SI | Des Ref Version |
| ARPBL_WriteOffAmount | double |  |  | SI | Write Off Amount |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Evaluador/a |
| Q03 | - |  |  | SI | ANTICIPATORIO |
| Q04 | - |  |  | SI | 1. SENTADO DE PIE |
| Q05 | - |  |  | SI | Instrucción: Cruce los brazos sobre el tórax. Inte... |
| Q06 | - |  |  | SI | 2. PONERSE DE PUNTILLAS |
| Q07 | - |  |  | SI | Instrucción: Coloque sus pies separados a la anchu... |
| Q08 | - |  |  | SI | Intente mantenerse en esa posición al menos 3 segu... |
| Q09 | - |  |  | SI | 3. APOYO MONOPODAL |
| Q10 | - |  |  | SI | Instrucción: Mire al frente. Mantenga las manos en... |
| Q11 | - |  |  | SI | Mire al frente. Levante ahora. |
| Q12 | - |  |  | SI | Izquierdo |
| Q13 | - |  |  | SI | Derecho |
| Q14 | - |  |  | SI | Tiempo Prueba 1 |
| Q15 | - |  |  | SI | segundos |
| Q16 | - |  |  | SI | Tiempo Prueba 2 |
| Q17 | - |  |  | SI | segundos |
| Q18 | - |  |  | SI | Tiempo Prueba 1 |
| Q19 | - |  |  | SI | segundos |
| Q20 | - |  |  | SI | Tiempo Prueba 2 |
| Q21 | - |  |  | SI | segundos |
| Q22 | - |  |  | SI | Para registrar cada lado por separado use la prueb... |
| Q23 | - |  |  | SI | SUBPUNTUACIÓN ANTICIPATORIO |
| Q24 | - |  |  | SI | /6 |
| Q25 | - |  |  | SI | CONTROL POSTURAL REACTIVO |
| Q26 | - |  |  | SI | 4. CORRECCIÓN COMPENSATORIA CON UN PASO-HACIA DELA... |
| Q27 | - |  |  | SI | Instrucción: Coloque sus pies separados a la anchu... |
| Q28 | - |  |  | SI | Cuando lo suelte haga lo que sea necesario, inclui... |
| Q29 | - |  |  | SI | 5. CORRECCIÓN COMPENSATORIA CON UN PASO-HACIA ATRÁ... |
| Q30 | - |  |  | SI | Instrucción: Coloque sus pies separados a la anchu... |
| Q31 | - |  |  | SI | Cuando lo suelte haga lo que sea necesario, inclui... |
| Q32 | - |  |  | SI | 6. CORRECCIÓN COMPENSATORIA CON UN PASO-LATERAL |
| Q33 | - |  |  | SI | Instrucción: De pie con los pies juntos, brazos a ... |
| Q34 | - |  |  | SI | Use el lado con la puntuación más baja para calcul... |
| Q35 | - |  |  | SI | Izquierda |
| Q36 | - |  |  | SI | Derecha |
| Q37 | - |  |  | SI | SUBPUNTUACIÓN CONTROL POSTURAL REACTIVO |
| Q38 | - |  |  | SI | /6 |
| Q39 | - |  |  | SI | ORIENTACIÓN SENSORIAL |
| Q40 | - |  |  | SI | 7. DE PIE (PIES JUNTOS) |
| Q41 | - |  |  | SI | Instrucción: Coloque sus manos en sus caderas. Col... |
| Q42 | - |  |  | SI | 8. DE PIE (PIES JUNTOS): OJOS CERRADOS. SUPERFICIE... |
| Q43 | - |  |  | SI | Instrucción Póngase en la gomaespuma. Coloque sus ... |
| Q44 | - |  |  | SI | Comenzaré a cronometrar cuando cierre sus ojos. |
| Q45 | - |  |  | SI | 9. INCLINADO OJOS CERRADOS |
| Q46 | - |  |  | SI | Intrucción: Sitúese en la rampa inclinada. Coloque... |
| Q47 | - |  |  | SI | Comenzaré a cronometrar cuando cierre sus ojos. |
| Q48 | - |  |  | SI | SUBPUNTUACIÓN ORIENTACIÓN SENSORIAL |
| Q49 | - |  |  | SI | /6 |
| Q50 | - |  |  | SI | MARCHA DINÁMICA |
| Q51 | - |  |  | SI | 10. CAMBIO EN LA VELOCIDAD DE MARCHA |
| Q52 | - |  |  | SI | Instrucción: Comience a caminar a su velocidad nor... |
| Q53 | - |  |  | SI | 11. CAMINAR CON GIROS DE CABEZA – HORIZONTAL |
| Q54 | - |  |  | SI | Instrucción: Comience caminando a su velocidad hab... |
| Q55 | - |  |  | SI | Intente mantenerse caminando en línea recta. |
| Q56 | - |  |  | SI | 12. CAMINAR CON GIROS DE PIVOTE |
| Q57 | - |  |  | SI | 13. PASO POR ENCIMA DE OBSTÁCULOS |
| Q58 | - |  |  | SI | Instrucción: Comience caminando a su velocidad hab... |
| Q59 | - |  |  | SI | 14. TEST UP &amp |
| Q60 | - |  |  | SI | Instrucción TUG: Cuando le diga “vaya”, levántese ... |
| Q61 | - |  |  | SI | Instrucción TUG con doble tarea: “Cuente hacia atr... |
| Q62 | - |  |  | SI | dé la vuelta y siéntese en la silla. Continúe cont... |
| Q63 | - |  |  | SI | TUG |
| Q64 | - |  |  | SI | segundos |
| Q65 | - |  |  | SI | TUG doble tarea |
| Q66 | - |  |  | SI | segundos |
| Q67 | - |  |  | SI | SUBPUNTUACIÓN MARCHA DINÁMICA |
| Q68 | - |  |  | SI | /10 |
| Q69 | - |  |  | SI | PUNTUACIÓN TOTAL&nbsp |
| Q70 | - |  |  | SI | /28 |
| Q71 | - |  |  | SI | Instrucción: Comience caminando a su velocidad hab... |
| Q72 | - |  |  | SI | Cuando puntúe el ítem 14, si la velocidad del suje... |
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