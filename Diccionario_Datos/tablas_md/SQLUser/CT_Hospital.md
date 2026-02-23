# SQLUser.CT_Hospital

**Schema:** SQLUser
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Catalogo de **Hospitales/Establecimientos**.
Define los centros de salud del sistema.
Campo clave para multi-hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSP_RowId | bigint | PK |  | NO | - |
| HOSP_AccrualsControl | varchar |  |  | SI | Accruals Control  |
| HOSP_Address | varchar |  |  | SI | Address |
| HOSP_ApplyDRGOutlierCalc | varchar |  |  | SI | Apply DRG Outlier Calculation |
| HOSP_ApplyVCFees | varchar |  |  | SI | Apply VC Fees |
| HOSP_AssignedGroupCategory | varchar |  |  | SI | Hospital Assigned Group Category |
| HOSP_BankAccount | varchar |  |  | SI | BankAccount |
| HOSP_BankAccount1 | varchar |  |  | SI | Bank Account  |
| HOSP_BillAddress | varchar |  |  | SI | Billing Address |
| HOSP_BillNo_DR | bigint |  | FK | SI | Des Ref Counter Type |
| HOSP_CPGroupAffiliations | varchar |  |  | SI | Affilations as List of Care Provider Groups |
| HOSP_CareTypes | varchar |  |  | SI | Care Types |
| HOSP_City | bigint |  |  | SI | City |
| HOSP_ClaimTypeCode | varchar |  |  | SI | Claim Type Code
Medicare code for the ECLISPSE In... |
| HOSP_Code | varchar |  |  | NO | Code |
| HOSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HOSP_CodeTranslated | varchar |  |  | SI | Code Translated |
| HOSP_Country_DR | bigint |  | FK | SI | Des Ref CTCountry |
| HOSP_CountyParish_DR | bigint |  | FK | SI | Des Ref CTCountyParish |
| HOSP_CreatedDate | date |  |  | SI | Created Date |
| HOSP_CreatedTime | time |  |  | SI | Created Time |
| HOSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOSP_CreditNoteNo_DR | bigint |  | FK | SI | Des Ref Counter TypeCredit Note No |
| HOSP_DateFrom | date |  |  | SI | DateFrom |
| HOSP_DateTo | date |  |  | SI | Date To |
| HOSP_DaysForOPDOffer | double |  |  | SI | DaysForOPDOffer |
| HOSP_DaysForOPLetterResponse | double |  |  | SI | DaysForOPLetterResponse |
| HOSP_DaysOfferOutcomeChange | double |  |  | SI | DaysOfferOutcomeChange |
| HOSP_DebtorControl | varchar |  |  | SI | Debtor Control  |
| HOSP_Desc | varchar |  |  | NO | Description |
| HOSP_DescTranslated | varchar |  |  | SI | Desc Translated |
| HOSP_Email | varchar |  |  | SI | Email |
| HOSP_Email1 | varchar |  |  | SI | Email1 |
| HOSP_EpTypeMedDisBeforeFinDis | varchar |  |  | SI | Episode Types for Medical Discharge before Financi... |
| HOSP_FacilityId | varchar |  |  | SI | FacilityId
Medicare provider number used by the h... |
| HOSP_FacilityType_DR | bigint |  | FK | SI | Des Ref FacilityType |
| HOSP_Fax | varchar |  |  | SI | Fax |
| HOSP_FaxServerEmail | varchar |  |  | SI | FaxServerEmail |
| HOSP_GuarantorGroup_DR | bigint |  | FK | SI | Des Ref ARCGuarantorGroup |
| HOSP_HospDRGCateg_DR | bigint |  | FK | SI | Des Ref HospDRGCateg |
| HOSP_InsuranceType_DR | bigint |  | FK | SI | Des Ref ARCInsuranceType |
| HOSP_Island | varchar |  |  | SI | Island |
| HOSP_Logo | varchar |  |  | SI | Logo |
| HOSP_MHACT_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by mental health module in Tr... |
| HOSP_MandatoryRefHospital | varchar |  |  | SI | Mandatory Ref Hospital |
| HOSP_MedicalDirector | varchar |  |  | SI | Medical Director |
| HOSP_NationalCode | varchar |  |  | SI | National Code |
| HOSP_NewWays | varchar |  |  | SI | NewWays |
| HOSP_OffersBeforeIP_OPWaitReset | double |  |  | SI | OffersBeforeIP OPWaitReset |
| HOSP_OrganizationID | varchar |  |  | SI | OrganizationID (HPI-O) |
| HOSP_Owner | varchar |  |  | SI | Owner |
| HOSP_PBSDispensingRuleList | varchar |  |  | SI | The list of PBS dispensing rules that apply to thi... |
| HOSP_PBSFacilityNumber | varchar |  |  | SI | The PBS-assigned unique identifier for this hospit... |
| HOSP_POSessionCounter_DR | bigint |  | FK | SI | PO Session Counter Des Ref Counter Type |
| HOSP_PayorApprovalReq | varchar |  |  | SI | Payor Approval Required |
| HOSP_Phone | varchar |  |  | SI | Phone |
| HOSP_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| HOSP_ProcAnaestheticOrders | varchar |  |  | SI | Procedure Anaesthetic Orders  |
| HOSP_Province_DR | bigint |  | FK | SI | Des Ref Province |
| HOSP_Region_DR | bigint |  | FK | SI | Region  |
| HOSP_SHowAppWTimeViolation | varchar |  |  | SI | Show Appointment Waiting Time Violation |
| HOSP_State | bigint |  |  | SI | State |
| HOSP_SubRegion_DR | bigint |  | FK | SI | Des Ref CTSubRegion |
| HOSP_Tariff_DR | bigint |  | FK | SI | Des Ref Tariff |
| HOSP_TimeZone | varchar |  |  | SI | Time Zone  |
| HOSP_Trust_DR | bigint |  | FK | SI | Des Ref Trust |
| HOSP_UnallocPayment | varchar |  |  | SI | Unallocated Payment  |
| HOSP_UpdatedDate | date |  |  | SI | Updated Date |
| HOSP_UpdatedTime | time |  |  | SI | Updated Time |
| HOSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| HOSP_UseSameCounter | varchar |  |  | SI | Use Same Counter for Bill/Refund |
| HOSP_WarnSameServiceWnXDays | double |  |  | SI | Warn if Same Service within X Days |
| HOSP_WeeksSuspensionReview | double |  |  | SI | WeeksSuspensionReview |
| HOSP_ZipDR | bigint |  | FK | SI | Zip des ref |
| Q01 | - |  |  | SI | Bloods taken |
| Q02 | - |  |  | SI | Blood group |
| Q03 | - |  |  | SI | RH factor |
| Q04 | - |  |  | SI | Antibodies |
| Q05 | - |  |  | SI | Full blood count |
| Q06 | - |  |  | SI | Platelets |
| Q07 | - |  |  | SI | Blood cultures |
| Q08 | - |  |  | SI | Bile acid |
| Q09 | - |  |  | SI | Clotting studies |
| Q10 | - |  |  | SI | Cross match |
| Q11 | - |  |  | SI | CP |
| Q12 | - |  |  | SI | Group and save |
| Q13 | - |  |  | SI | HbA1c |
| Q14 | - |  |  | SI | Kleihauer |
| Q15 | - |  |  | SI | Liver function tests |
| Q16 | - |  |  | SI | Maternal serum |
| Q17 | - |  |  | SI | Rhesus antibodies |
| Q18 | - |  |  | SI | Thyroid function tests |
| Q19 | - |  |  | SI | TORCH screen |
| Q20 | - |  |  | SI | Toxoplasmosis |
| Q21 | - |  |  | SI | Urates |
| Q22 | - |  |  | SI | Urea and electrolytes |
| Q23 | - |  |  | SI | Other |
| Q24 | - |  |  | SI | Details |
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