# SQLUser.PA_PersonPackage

**Schema:** SQLUser
**Columnas:** 40
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACK_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| PACK_AuxInsType_DR | bigint |  | FK | SI | Des Ref ARCAuxilInsurType |
| PACK_Childsub | double |  |  | NO | Childsub |
| PACK_Comments | varchar |  |  | SI | Comments |
| PACK_DateFrom | date |  |  | SI | Date From |
| PACK_DateTo | date |  |  | SI | Date To |
| PACK_Desc | varchar |  |  | SI | Desc |
| PACK_EffectiveDateFrom | date |  |  | SI | EffectiveDateFrom |
| PACK_EffectiveDateTo | date |  |  | SI | EffectiveDateTo |
| PACK_ExclFromPriceCalc | varchar |  |  | SI | Exclude from Price Calculation |
| PACK_FixedPrice | double |  |  | SI | FixedPrice |
| PACK_FreeText | varchar |  |  | SI | Free Text |
| PACK_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| PACK_IncludeOptional | varchar |  |  | SI | IncludeOptional |
| PACK_InsType_DR | bigint |  | FK | SI | Des Ref ARCInsuranceType |
| PACK_MainOrderTariffPrice | varchar |  |  | SI | Main Order Tariff Price |
| PACK_Method | varchar |  |  | SI | Package Method |
| PACK_MultipleEpisode | varchar |  |  | SI | MultipleEpisode |
| PACK_NoPriceCalc | varchar |  |  | SI | Do Not Recalculate Package Price |
| PACK_Number | varchar |  |  | SI | Number |
| PACK_NumberOfDays | double |  |  | SI | NumberOfDays |
| PACK_NumberOfVisits | double |  |  | SI | NumberOfVisits |
| PACK_OrigFixedPackagePrice | double |  |  | SI | Original Fixed Package Price |
| PACK_OriginalItemPrice | double |  |  | SI | Original Item Price |
| PACK_PackDisconPackOIPrice | varchar |  |  | SI | Package Discontinue – Package Order Item Price |
| PACK_PackDisconTariffPrice | varchar |  |  | SI | Package Discontinue – Tariff Price |
| PACK_PackageGroupNumber | varchar |  |  | SI | Package Group Number |
| PACK_PackageGroupPrice | double |  |  | SI | Package Group Price |
| PACK_PackageGroup_DR | bigint |  | FK | SI | Package Group |
| PACK_PackagePrice | double |  |  | SI | Package Price |
| PACK_PackageRank | double |  |  | SI | Package Rank |
| PACK_PackageSubGroupPrice | double |  |  | SI | Package SubGroup Price |
| PACK_PackageSubGroup_DR | bigint |  | FK | SI | Package SubGroup |
| PACK_PrefMethPayment_DR | varchar |  | FK | SI | PrefMethPayment  |
| PACK_Reason_DR | bigint |  | FK | SI | Package Reason  |
| PACK_Repeat | varchar |  |  | SI | Repeat |
| PACK_RowId | varchar |  |  | NO | - |
| PACK_SelectionMethod | varchar |  |  | SI | Selection Method |
| PACK_Status_DR | bigint |  | FK | SI | Package Status |
| PACK_Template_DR | bigint |  | FK | SI | Template  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*