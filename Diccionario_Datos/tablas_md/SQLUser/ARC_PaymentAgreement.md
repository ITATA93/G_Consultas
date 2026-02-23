# SQLUser.ARC_PaymentAgreement

**Schema:** SQLUser
**Columnas:** 235
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAY_RowId | bigint | PK |  | NO | - |
| PAY_ARCIM1_DR | varchar |  | FK | SI | Des Ref ARCIM1 |
| PAY_ARCIM2_DR | varchar |  | FK | SI | Des Ref ARCIM2 |
| PAY_AccomBillLineWardRoomType | varchar |  |  | SI | Accommodation Bill Line Per Ward/Room Type |
| PAY_AccountCode | varchar |  |  | SI | AccountCode |
| PAY_AgreemCode | varchar |  |  | SI | AgreemCode |
| PAY_ApplyContrToOrdItemInOrdSet | varchar |  |  | SI | Apply Contract to Order Items in Order Set  |
| PAY_ApplyDRGAllInpatEpis | varchar |  |  | SI | Apply DRG to All Inpatient Episodes |
| PAY_ApplyDRGOutlierCalc | varchar |  |  | SI | Apply DRG Outlier Calculation |
| PAY_ApplyPADiscHighestProcOnly | varchar |  |  | SI | Apply Payment Agreement Discount to Highest Proced... |
| PAY_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| PAY_BillByOrderGroup | varchar |  |  | SI | Bill By Order Group |
| PAY_BillByTariffPrices | varchar |  |  | SI | Bill by Tariff Prices |
| PAY_BillPerDay | varchar |  |  | SI | Bill Per Day |
| PAY_BillServiceTaxToPatient | varchar |  |  | SI | Bill Service Tax to Patient |
| PAY_BillingSchedule_DR | bigint |  | FK | SI | Billing Schedule |
| PAY_BulkBillingIncentive | varchar |  |  | SI | Bulk Billing Incentive |
| PAY_CalcCopaymentEpisLevel | varchar |  |  | SI | Calculate Copayment On Episode Level |
| PAY_CalcCopaymentGrossAmount | varchar |  |  | SI | Calculate Copayment From Gross Amount |
| PAY_CancelInvIfOrdItemDiscont | varchar |  |  | SI | Cancel Invoice If an Order item Discontinued |
| PAY_ClaimType | varchar |  |  | SI | Claim Type |
| PAY_Code | varchar |  |  | SI | Code
Required for lab billing |
| PAY_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAY_ContractDRG_DR | bigint |  | FK | SI | Des Ref ContractDRG |
| PAY_Contract_DR | bigint |  | FK | SI | Des Ref Contract |
| PAY_CreatedDate | date |  |  | SI | Created Date |
| PAY_CreatedTime | time |  |  | SI | Created Time |
| PAY_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAY_Currency_DR | bigint |  | FK | SI | Des Ref Currency |
| PAY_DateFrom | date |  |  | NO | Date From |
| PAY_DateTo | date |  |  | SI | Date To |
| PAY_DeductAmtBeforeSplit | varchar |  |  | SI | Deduct amount before splitting  |
| PAY_Desc | varchar |  |  | SI | Description
Required for lab billing |
| PAY_DiscApplyPayorPaysUntil | varchar |  |  | SI | Discounts applied to Payor Pays Until |
| PAY_EndDateDefaultNumber | double |  |  | SI | EndDateDefaultNumber |
| PAY_EnddateDetaultUnit | varchar |  |  | SI | EnddateDetaultUnit |
| PAY_EnddateTrigger | varchar |  |  | SI | EnddateTrigger |
| PAY_EpisDailyLimitOPEpisodes | varchar |  |  | SI | Set Episode Daily Limit for OPD Episodes |
| PAY_FixedAmt | double |  |  | SI | Fixed Amt |
| PAY_FixedPatientShare | double |  |  | SI | Fixed Patient Share |
| PAY_ICDCodesListOfOrderRestr | varchar |  |  | SI | Apply ICD Codes List of Order Restrictions |
| PAY_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| PAY_InvoiceType | varchar |  |  | SI | InvoiceType |
| PAY_MVHoursPerDay | double |  |  | SI | MV Hours per Days |
| PAY_MultEpisChargesNumber1 | double |  |  | SI | Multiple Episodic Charges Number1 |
| PAY_MultEpisChargesNumber2 | double |  |  | SI | Multiple Episodic Charges Number2 |
| PAY_MultEpisChargesNumber3 | double |  |  | SI | Multiple Episodic Charges Number3 |
| PAY_MultEpisChargesNumber4 | double |  |  | SI | Multiple Episodic Charges Number4 |
| PAY_MultEpisOrderItems | varchar |  |  | SI | Multiple Episodic Order Items |
| PAY_MultText1 | varchar |  |  | SI | MultText1 |
| PAY_MultText2 | varchar |  |  | SI | MultText2 |
| PAY_NoBundleShortOutlier | varchar |  |  | SI | Do Not Bundle Short Outlier |
| PAY_NumOfVisits | double |  |  | SI | NumofVisits |
| PAY_Number1 | double |  |  | SI | Number1 |
| PAY_Number2 | double |  |  | SI | Number2 |
| PAY_Number3 | double |  |  | SI | Number3 |
| PAY_Number4 | double |  |  | SI | Number4 |
| PAY_Number5 | double |  |  | SI | Number5 |
| PAY_Number6 | double |  |  | SI | OverrideServTax |
| PAY_OIEpisBillOverrideDayOnly | varchar |  |  | SI | Order Item Episodic Billing Override – Day Only |
| PAY_OIEpisBillOverrideInp | varchar |  |  | SI | Order Item Episodic Billing Override – INP |
| PAY_OIEpisodicBillingOverride | varchar |  |  | SI | OI Episodic Billing Override |
| PAY_OutOfContractPlan_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| PAY_OverrideBillGrp1_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| PAY_OverrideBillGrp2_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| PAY_OverrideBillGrp3_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| PAY_OverrideBillGrp4_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| PAY_OverrideBillGrpC_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| PAY_OverrideBillGrpPICC_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| PAY_OverrideBillSub1_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| PAY_OverrideBillSub2_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| PAY_OverrideBillSub3_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| PAY_OverrideBillSub4_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| PAY_OverrideBillSubC_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| PAY_OverrideBillSubPICC_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| PAY_Owner | varchar |  |  | SI | Owner |
| PAY_PatClassif1 | varchar |  |  | SI | Patient Classification1 |
| PAY_PatClassif2 | varchar |  |  | SI | Patient Classification2 |
| PAY_PatClassif3 | varchar |  |  | SI | Patient Classification3 |
| PAY_PatClassif4 | varchar |  |  | SI | Patient Classification4 |
| PAY_PatientPays | varchar |  |  | SI | Patient Pays |
| PAY_PatientPaysStampDuty | varchar |  |  | SI | Patient Always Pays Stamp Duty |
| PAY_PaymentAgreementOnly | varchar |  |  | SI | Payment Agreement Only |
| PAY_PayorApprovLimitAmount | varchar |  |  | SI | Payor Approval Limit Amount |
| PAY_PayorApprovRequestAmount | varchar |  |  | SI | Payor Approval Requesting Amount |
| PAY_PayorApprovalICDDiag_DR | bigint |  | FK | SI | Des Ref ARCPayorApprovalDiag |
| PAY_PayorApprovalOrdItem | varchar |  |  | SI | Apply PA Payor Approval Order Item |
| PAY_PayorShare | double |  |  | SI | Patient Share |
| PAY_PaysFrom | double |  |  | SI | Pays From |
| PAY_PrimProcBasedOnTariffPrice | varchar |  |  | SI | Primary Procedure based on Tariff Price |
| PAY_PrimProcBasedTarPricePerDiem | varchar |  |  | SI | Primary Procedure based on Tariff Price Per Diem |
| PAY_PrimProcTariff_DR | bigint |  | FK | SI | Des Ref ARCTariff |
| PAY_RestrictOverride | varchar |  |  | SI | RestrictOverride |
| PAY_RoomType_DR | bigint |  | FK | SI | Des Ref PACRoomType |
| PAY_SameDayCPayorCode | varchar |  |  | SI | SameDayCPayorCode |
| PAY_SameDayD1PayorCode | varchar |  |  | SI | SameDayD1PayorCode |
| PAY_SameDayD2PayorCode | varchar |  |  | SI | SameDayD2PayorCode |
| PAY_SameDayD3PayorCode | varchar |  |  | SI | SameDayD3PayorCode |
| PAY_SameDayD4PayorCode | varchar |  |  | SI | SameDayD4PayorCode |
| PAY_SameDayPICCPayorCode | varchar |  |  | SI | SameDayPICCPayorCode |
| PAY_SameDayRoomChargeDesc1 | varchar |  |  | SI | SameDayRoomChargeDesc1 |
| PAY_SameDayRoomChargeDesc2 | varchar |  |  | SI | SameDayRoomChargeDesc2 |
| PAY_SameDayRoomChargeDesc3 | varchar |  |  | SI | SameDayRoomChargeDesc3 |
| PAY_SameDayRoomChargeDesc4 | varchar |  |  | SI | SameDayRoomChargeDesc4 |
| PAY_SameDayRoomChargeDescC | varchar |  |  | SI | SameDayRoomChargeDescC |
| PAY_SameDayRoomChargeDescPICC | varchar |  |  | SI | SameDayRoomChargeDesc PICC Line  |
| PAY_SameDayTypeC | varchar |  |  | SI | SameDayTypeC |
| PAY_SameDayTypeCEpis | varchar |  |  | SI | Same Day Type C Episode |
| PAY_SameDayTypePICC | varchar |  |  | SI | Same Day Type PICC Line  |
| PAY_ServTaxOINotConfigured_DR | bigint |  | FK | SI | Des Ref to ARCST Service tax to apply if order ite... |
| PAY_ServTax_DR | bigint |  | FK | SI | Des Ref to ARCST |
| PAY_SingleApprBatchEMEpisode | varchar |  |  | SI | Single Approval batch for Emergency Episode |
| PAY_SingleApprBatchIPEpisode | varchar |  |  | SI | Single Approval batch for Inpatient Episode |
| PAY_SingleApprBatchOPEpisode | varchar |  |  | SI | Single Approval batch for Outpatient Episode |
| PAY_Text1 | varchar |  |  | SI | Text1 |
| PAY_Text2 | varchar |  |  | SI | Text2 |
| PAY_Text3 | varchar |  |  | SI | Text3 |
| PAY_Text4 | varchar |  |  | SI | Text4 |
| PAY_Text5 | varchar |  |  | SI | Text5 |
| PAY_Time1 | time |  |  | SI | Time1 |
| PAY_Time2 | time |  |  | SI | Time2 |
| PAY_UpdatedDate | date |  |  | SI | Updated Date |
| PAY_UpdatedTime | time |  |  | SI | Updated Time |
| PAY_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PAY_YesNo1 | varchar |  |  | SI | YesNo1 |
| PAY_YesNo2 | varchar |  |  | SI | YesNo2 |
| PAY_YesNo3 | varchar |  |  | SI | YesNo3 |
| PAY_YesNo4 | varchar |  |  | SI | YesNo4 |
| PAY_YesNo5 | varchar |  |  | SI | YesNo5 |
| PAY_YesNo6 | varchar |  |  | SI | YesNo6 |
| PAY_YesNo7 | varchar |  |  | SI | YesNo7 |
| Q01 | - |  |  | SI | Fecha de Registro |
| Q02 | - |  |  | SI | Hora de Registro |
| Q03 | - |  |  | SI | Sesión N° |
| Q04 | - |  |  | SI | 1.  Me llevo bien con otros |
| Q05 | - |  |  | SI | 2.  Me canso rápidamente |
| Q06 | - |  |  | SI | 3.  Nada me interesa |
| Q07 | - |  |  | SI | 4.  Me siento presionado (estresado) en el trabajo... |
| Q08 | - |  |  | SI | 5.  Me siento culpable |
| Q09 | - |  |  | SI | 6.  Me siento irritado, molesto |
| Q10 | - |  |  | SI | 7.  Me siento contento con mi matrimonio/pareja |
| Q11 | - |  |  | SI | 8.  Pienso en quitarme la vida |
| Q12 | - |  |  | SI | 9.  Me siento débil |
| Q13 | - |  |  | SI | 10. Me siento atemorizado |
| Q14 | - |  |  | SI | 11.Necesito tomar bebidas alcohólicas en la mañana... |
| Q15 | - |  |  | SI | 12. Encuentro satisfacción en mi trabajo/ escuela |
| Q16 | - |  |  | SI | 13. Soy una persona feliz |
| Q17 | - |  |  | SI | 14. Trabajo/estudio excesivamente (mas de la cuent... |
| Q18 | - |  |  | SI | 15. Me siento inútil |
| Q19 | - |  |  | SI | 16. Me abruman (angustian) los problemas de mi fam... |
| Q20 | - |  |  | SI | 17. Mi vida sexual me llena |
| Q21 | - |  |  | SI | 18. Me siento solo |
| Q22 | - |  |  | SI | 19. Discuto frecuentemente |
| Q23 | - |  |  | SI | 20. Me siento querido y que me necesitan |
| Q24 | - |  |  | SI | 21. Disfruto mi tiempo libre |
| Q25 | - |  |  | SI | 22. Tengo dificultades para concentrarme |
| Q26 | - |  |  | SI | 23. Me siento sin esperanza  en el futuro |
| Q27 | - |  |  | SI | 24. Estoy contento conmigo mismo |
| Q28 | - |  |  | SI | 25. Me perturban o molestan pensamientos de los qu... |
| Q29 | - |  |  | SI | 26. Me molesta que me critiquen porque tomo o me d... |
| Q30 | - |  |  | SI | 27. Tengo malestares estomacales |
| Q31 | - |  |  | SI | 28. Trabajo/estudio tan bien como lo hacía antes |
| Q32 | - |  |  | SI | 29. Mi corazón palpita demasiado |
| Q33 | - |  |  | SI | 30. Tengo dificultades para llevarme bien con mis ... |
| Q34 | - |  |  | SI | 31. Estoy satisfecho con mi vida |
| Q35 | - |  |  | SI | 32. Tengo problemas en el trabajo/escuela debido a... |
| Q36 | - |  |  | SI | 33. Siento que algo malo va a ocurrir |
| Q37 | - |  |  | SI | 34. Tengo los músculos adoloridos |
| Q38 | - |  |  | SI | 35. Me atemorizan los espacios abiertos, el maneja... |
| Q39 | - |  |  | SI | 36. Me siento nervioso |
| Q40 | - |  |  | SI | 37. Me satisfacen mis relaciones con mis seres que... |
| Q41 | - |  |  | SI | 38. Siento que  me va bien en el trabajo/escuela |
| Q42 | - |  |  | SI | 39. Tengo muchas discusiones en el trabajo/escuela |
| Q43 | - |  |  | SI | 40. Siento que algo anda mal con mi mente |
| Q44 | - |  |  | SI | 41. Tengo dificultades para dormir, o no me puedo ... |
| Q45 | - |  |  | SI | 42. Me siento triste |
| Q46 | - |  |  | SI | 43. Mis relaciones con otros me satisfacen |
| Q47 | - |  |  | SI | 44. Me enojo tanto en el trabajo/escuela que puedo... |
| Q48 | - |  |  | SI | 45. Me dan dolores de cabeza |
| Q49 | - |  |  | SI | SD |
| Q50 | - |  |  | SI | IR |
| Q51 | - |  |  | SI | SR |
| Q52 | - |  |  | SI | Sintomatología (SD): PC = 43 ICC = 12 |
| Q53 | - |  |  | SI | Un puntaje alto indica principalmente la presencia... |
| Q54 | - |  |  | SI | Un puntaje bajo indica la ausencia o la negación d... |
| Q55 | - |  |  | SI | Relaciones interpersonales (RI): PC = 16 ICC = 9 |
| Q56 | - |  |  | SI | Un puntaje alto indica dificultades en sus relacio... |
| Q57 | - |  |  | SI | Un puntaje bajo indica la ausencia de problemas in... |
| Q58 | - |  |  | SI | Rol social (RS): PC = 14 ICC = 8 |
| Q59 | - |  |  | SI | Un puntaje alto señala dificultades en el ajuste d... |
| Q60 | - |  |  | SI | Un puntaje bajo indica un adecuado ajuste al rol s... |
| Q61 | - |  |  | SI | donde el cliente podría contestar arbitrariamente ... |
| Q62 | - |  |  | SI | Puntaje Total: |
| Q63 | - |  |  | SI | Un puntaje alto indica que el cliente admite un el... |
| Q64 | - |  |  | SI | en tanto que un puntaje bajo sugiere que el client... |
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