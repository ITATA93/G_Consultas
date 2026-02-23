# SQLUser.PHC_ScheduledDrugClass

**Schema:** SQLUser
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCSDC_RowId | bigint | PK |  | NO | - |
| PHCSDC_BrandSubsFlag | varchar |  |  | NO | Allow Brand Substitutions Flag |
| PHCSDC_CSDrugAdmFlag | varchar |  |  | NO | Counter Sign Drug Administration Flag |
| PHCSDC_CSOrderFlag | varchar |  |  | NO | Counter Sign Order Flag |
| PHCSDC_Code | varchar |  |  | NO | Scheduled Drug Classification Code |
| PHCSDC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCSDC_CreatedDate | date |  |  | SI | Created Date |
| PHCSDC_CreatedTime | time |  |  | SI | Created Time |
| PHCSDC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCSDC_DateFrom | date |  |  | SI | DateFrom |
| PHCSDC_DateTo | date |  |  | SI | DateTo |
| PHCSDC_Desc | varchar |  |  | NO | Description |
| PHCSDC_DisallowPhoneOrd | varchar |  |  | SI | Not Allowed via Phone Order |
| PHCSDC_DisposalFlag | varchar |  |  | NO | Require Disposal Flag |
| PHCSDC_DisposalReason_DR | bigint |  | FK | SI | Des Ref Disposal Reason |
| PHCSDC_DrugRegister | varchar |  |  | SI | Drug Register |
| PHCSDC_Icon | varchar |  |  | SI | Icon |
| PHCSDC_LongDesc | varchar |  |  | SI | Long Description |
| PHCSDC_OEMsgFlag | varchar |  |  | NO | Display OE Message Flag |
| PHCSDC_OrdPhysFlag | varchar |  |  | NO | Prescription Changed by Ordering Physician Only Fl... |
| PHCSDC_Owner | varchar |  |  | SI | Owner |
| PHCSDC_PrescDetailsFlag | varchar |  |  | NO | Display Prescription Details Flag |
| PHCSDC_PrescFlag1 | varchar |  |  | NO | Prescription Flag: Generate Presc for Each Drug |
| PHCSDC_PrescFlag2 | varchar |  |  | NO | Prescription Flag: Generate Presc for Each Schedul... |
| PHCSDC_PrescValPeriod | double |  |  | SI | Prescription Validity Period |
| PHCSDC_Rank | double |  |  | SI | Rank |
| PHCSDC_RepeatsFlag | varchar |  |  | NO | Repeats Allowed Flag |
| PHCSDC_ReqDispQtyForDisMedOrOP | varchar |  |  | SI | Require Dispense Quantity for Discharge/Outpatient... |
| PHCSDC_RestrPharmFlag | varchar |  |  | NO | Restricted Pharmacy Flag |
| PHCSDC_ReturnsFlag | varchar |  |  | NO | Allow Auto Returns Flag |
| PHCSDC_StorageBinStatus | varchar |  |  | SI | StorageBinStatus |
| PHCSDC_UpdatedDate | date |  |  | SI | Updated Date |
| PHCSDC_UpdatedTime | time |  |  | SI | Updated Time |
| PHCSDC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*