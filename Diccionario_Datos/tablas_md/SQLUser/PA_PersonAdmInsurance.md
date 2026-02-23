# SQLUser.PA_PersonAdmInsurance

**Schema:** SQLUser
**Columnas:** 32
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAINS_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| PAINS_ApplyGST | varchar |  |  | SI | ApplyGST |
| PAINS_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| PAINS_BenefitPackage_DR | varchar |  | FK | SI | Des Ref ARCAuxilInsurTypeBenefitPackage |
| PAINS_CTLOC_DR | bigint |  | FK | SI | Des Ref CTSpec |
| PAINS_CTPCP_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| PAINS_CTREL_DR | bigint |  | FK | SI | Des Ref CTREL |
| PAINS_CardNo | varchar |  |  | SI | CardNo |
| PAINS_CardType_DR | bigint |  | FK | SI | Des Ref CardType |
| PAINS_CardholderId | varchar |  |  | SI | CardholderId |
| PAINS_CardholderName | varchar |  |  | SI | CardholderName |
| PAINS_Childsub | double |  |  | NO | Childsub |
| PAINS_DateTypeFrom | date |  |  | SI | DateTypeFrom |
| PAINS_DateTypeTo | date |  |  | SI | DateTypeTo |
| PAINS_DateValidFrom | date |  |  | SI | DateValidFrom |
| PAINS_DateValidTo | date |  |  | SI | DateValidTo |
| PAINS_DependentFlag | varchar |  |  | SI | DependentFlag |
| PAINS_Dependent_DR | varchar |  | FK | SI | Des Ref PAPersonInsurance |
| PAINS_EpisSubType_DR | bigint |  | FK | SI | Des Ref PACEpisodeSubType |
| PAINS_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| PAINS_NumOfVisits | double |  |  | SI | NumOfVisits |
| PAINS_NumOfVisitsRemain | double |  |  | SI | NumOfVisitsRemain |
| PAINS_PayorVariationComments | varchar |  |  | SI | PayorVariationComments |
| PAINS_PersonResponsible | varchar |  |  | SI | PersonResponsible |
| PAINS_Rank | varchar |  |  | SI | Rank |
| PAINS_RoomType_DR | bigint |  | FK | SI | Des Ref PACRoomType |
| PAINS_RowId | varchar |  |  | NO | - |
| PAINS_Spec_DR | bigint |  | FK | SI | Des Ref Spec |
| PAINS_UpdateDate | date |  |  | SI | UpdateDate |
| PAINS_UpdateTime | time |  |  | SI | UpdateTime |
| PAINS_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| PAINS_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*