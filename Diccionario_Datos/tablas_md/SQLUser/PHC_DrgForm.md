# SQLUser.PHC_DrgForm

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCDF_PHCD_ParRef | bigint | PK |  | NO | PHCD Parent Reference (Drug master) |
| PHCDF_ATCBin | varchar |  |  | SI | ATC Bin |
| PHCDF_AdminRoute_DR | bigint |  | FK | SI | Des Ref AdminRoute |
| PHCDF_AdvReaction | varchar |  |  | SI | Adverse Reaction (info) |
| PHCDF_AllowOngoingEventDurED | varchar |  |  | SI | Allow Ongoing/Event duration For Emergency Episode |
| PHCDF_AllowOngoingEventDurIP | varchar |  |  | SI | Allow Ongoing/Event duration For Inpatient Episode |
| PHCDF_AllowOngoingEventDurOP | varchar |  |  | SI | Allow Ongoing/Event duration For Outpatient Episod... |
| PHCDF_BaseQty | double |  |  | SI | Base Qty |
| PHCDF_CTUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| PHCDF_ChildSub | double |  |  | NO | PHCDF ChildSub (New Key) |
| PHCDF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCDF_ContraInd | varchar |  |  | SI | Contra Indication (info) |
| PHCDF_ConvAdmQtyToBaseUOM | varchar |  |  | SI | ConvAdmQtyToBaseUOM |
| PHCDF_CreatedDate | date |  |  | SI | Created Date |
| PHCDF_CreatedTime | time |  |  | SI | Created Time |
| PHCDF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCDF_DateFrom | date |  |  | SI | Date From |
| PHCDF_DateTo | date |  |  | SI | Date To |
| PHCDF_DeductPartially | varchar |  |  | SI | Deduct Partially |
| PHCDF_Description | varchar |  |  | SI | Description |
| PHCDF_DilutionVolume | double |  |  | SI | Dilution Volume (mL) |
| PHCDF_DisplacementVolume | double |  |  | SI | Displacement Volume (mL) |
| PHCDF_DrugRegister | varchar |  |  | SI | Drug Register |
| PHCDF_DurationUnit | varchar |  |  | SI |  DurationUnit |
| PHCDF_DurationValue | double |  |  | SI | DurationValue |
| PHCDF_ExpiryAfterOpeningDays | integer |  |  | SI | Vial Expiry Period After Opening At Manufacture - ... |
| PHCDF_ExpiryAfterOpeningHours | integer |  |  | SI | Vial Expiry Period After Opening At Manufacture - ... |
| PHCDF_ExpiryAfterOpeningMinutes | integer |  |  | SI | Vial Expiry Period After Opening At Manufacture - ... |
| PHCDF_ExternalData | varchar |  |  | SI | ExternalData |
| PHCDF_ExtraDetails | varchar |  |  | SI | ExtraDetails |
| PHCDF_Formulary | varchar |  |  | SI | Formulary |
| PHCDF_GenRtForm_DR | varchar |  | FK | SI | Des Ref GenRtForm |
| PHCDF_IVExpiry | double |  |  | SI | IV Expiry |
| PHCDF_InPatDurationUnit | varchar |  |  | SI |  InPat DurationUnit |
| PHCDF_InPatDurationValue | double |  |  | SI | InPat DurationValue |
| PHCDF_InPatDuration_DR | bigint |  | FK | SI | Des Ref PHCDU |
| PHCDF_Indication | varchar |  |  | SI | Indication (info) |
| PHCDF_Interaction | varchar |  |  | SI | Interaction |
| PHCDF_MIMSno | varchar |  |  | SI | MIMS number |
| PHCDF_MaxDurDaysDischED | integer |  |  | SI | Max Duration Days (Emergency Discharge) |
| PHCDF_MaxDurDaysDischIP | integer |  |  | SI | Max Duration Days (Inpatient Discharge) |
| PHCDF_MaxDurDaysDischOP | integer |  |  | SI | Max Duration Days (Outpatient Discharge) |
| PHCDF_MaxDurDaysDischarge | double |  |  | SI | Max Duration Days (Default Discharge) |
| PHCDF_MaxDurDaysEmergency | double |  |  | SI | MaxDurDaysEmergency |
| PHCDF_MaxDurDaysInpatient | double |  |  | SI | MaxDurDaysInpatient |
| PHCDF_MaxDurDaysOutpatient | double |  |  | SI | MaxDurDaysOutpatient |
| PHCDF_MaxNumberRepeats | double |  |  | SI | Max Number of Repeats |
| PHCDF_Modified | varchar |  |  | SI | Modified |
| PHCDF_Monograph | varchar |  |  | SI | Monograph |
| PHCDF_NeverCalculateQty | varchar |  |  | SI | NeverCalculateQty |
| PHCDF_NotAllowPrescBaseUOM | varchar |  |  | SI | Not Allowed to Prescribe in unit of use (Base UOM) |
| PHCDF_OfficialCode | varchar |  |  | SI | Official Code |
| PHCDF_Overfill | double |  |  | SI | Overfill (mL) |
| PHCDF_PBSQuan | double |  |  | SI | PBS Quan |
| PHCDF_PHCDO_DR | bigint |  | FK | SI | Des Ref to PHCDO (Dosage) |
| PHCDF_PHCDU_DR | bigint |  | FK | SI | Des Ref to PHCDU  (Duartion) |
| PHCDF_PHCFR_DR | bigint |  | FK | SI | Des Ref to PHCFR (Frequency) |
| PHCDF_PHCF_DR | bigint |  | FK | NO | Des Ref to PHCF (Form Code) |
| PHCDF_PHCIN_DR | bigint |  | FK | SI | Des Ref to PHCIN (Instruction) |
| PHCDF_PHCPA_DR | bigint |  | FK | SI | Des Ref to PHCPA (Packing) |
| PHCDF_PHCP_DR | bigint |  | FK | SI | Des Ref to PHCP (Per) |
| PHCDF_PHCS_DR | bigint |  | FK | SI | Des Ref to PHCS (Strength) |
| PHCDF_PackageSizeQty | double |  |  | SI | PackageSize Quantity (HealthShare) |
| PHCDF_PictureFile | varchar |  |  | SI | Drug Vendors Picture File Name (External Monograph... |
| PHCDF_Poison_DR | bigint |  | FK | SI | Des Ref Poison |
| PHCDF_Precaution | varchar |  |  | SI | Special Precautions (info) |
| PHCDF_Preferred | varchar |  |  | SI | Preferred |
| PHCDF_Price1 | double |  |  | SI | Price 1 - MIMS (info) |
| PHCDF_Price2 | double |  |  | SI | Price 2 - MIMS (info) |
| PHCDF_RegionCodeFDB | varchar |  |  | SI | RegionCodeFDB |
| PHCDF_RoundIndivAdmin | varchar |  |  | SI | RoundIndivAdmin |
| PHCDF_Route_DR | bigint |  | FK | SI | Des Ref Route |
| PHCDF_RowId | varchar |  |  | NO | - |
| PHCDF_ScheduleClass_DR | bigint |  | FK | SI | Des Ref Scheduled Drug Classification |
| PHCDF_UpdateDate | date |  |  | SI | Update Date |
| PHCDF_UpdateTime | time |  |  | SI | Update Time |
| PHCDF_UpdateUser | bigint |  |  | SI | Update User |
| PHCDF_UpdatedDate | date |  |  | SI | Updated Date |
| PHCDF_UpdatedTime | time |  |  | SI | Updated Time |
| PHCDF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PHCDF_Volume | double |  |  | SI | Volume |
| PHCDF_Warning | varchar |  |  | SI | Warning |
| PHCDF_WithdrawableVolume | double |  |  | SI | Withdrawable Volume (mL) |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*