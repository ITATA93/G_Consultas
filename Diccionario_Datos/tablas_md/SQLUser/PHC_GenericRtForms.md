# SQLUser.PHC_GenericRtForms

**Schema:** SQLUser
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTF_ParRef | bigint | PK |  | NO | PHC_Generic Parent Reference |
| RTF_AdminAfterSkinTest | varchar |  |  | SI | AdminAfterSkinTest |
| RTF_AdminRoute_DR | bigint |  | FK | SI | Des Ref AdminRoute |
| RTF_AllowOngoingE | varchar |  |  | SI | AllowOngoingE   |
| RTF_AllowOngoingIP | varchar |  |  | SI | AllowOngoingIP   |
| RTF_AllowPRNWithoutFreq | varchar |  |  | SI | Allow PRN orders with no frequency |
| RTF_Childsub | double |  |  | NO | Childsub |
| RTF_CreatedDate | date |  |  | SI | Created Date |
| RTF_CreatedTime | time |  |  | SI | Created Time |
| RTF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RTF_DaysAfterMedsInterActive | double |  |  | SI | DaysAfterMedsInterActive |
| RTF_Form_DR | bigint |  | FK | SI | Des Ref Form |
| RTF_IVExpiry | double |  |  | SI | IVExpiry |
| RTF_IVFluidType | varchar |  |  | SI | IVFluidType  |
| RTF_Ident | varchar |  |  | SI | Ident |
| RTF_Instruc_DR | bigint |  | FK | SI | Des Ref PHCInstruc |
| RTF_MaxDurDaysDischED | integer |  |  | SI | Max Duration Days (Emergency Discharge) |
| RTF_MaxDurDaysDischIP | integer |  |  | SI | Max Duration Days (Inpatient Discharge) |
| RTF_MaxDurDaysDischOP | integer |  |  | SI | Max Duration Days (Outpatient Discharge) |
| RTF_MaxDurDisch | double |  |  | SI | Max Duration Days (Default Discharge) |
| RTF_MaxDurE | double |  |  | SI | MaxDurE |
| RTF_MaxDurIP | double |  |  | SI | MaxDurIP |
| RTF_MaxDurOP | double |  |  | SI | MaxDurOP |
| RTF_RoundFactor | double |  |  | SI | Divisibility Factor for strength incremental round... |
| RTF_RoundMethod | varchar |  |  | SI | Rounding Method |
| RTF_Route_DR | bigint |  | FK | SI | Des Ref Route |
| RTF_RowId | varchar |  |  | NO | - |
| RTF_SigFigs | integer |  |  | SI | Number for rounding to Significant Figures (RoundM... |
| RTF_Strength_DR | bigint |  | FK | SI | Des Ref Strength |
| RTF_SubCat_DR | varchar |  | FK | SI | Des Ref SubCat |
| RTF_UpdatedDate | date |  |  | SI | Updated Date |
| RTF_UpdatedTime | time |  |  | SI | Updated Time |
| RTF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*