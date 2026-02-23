# SQLUser.PHC_PBSPrescribingRuleBenefit

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BEN_ParRef | bigint | PK |  | NO | PHC_PBSPrescribingRule Parent Reference |
| BEN_BenefitType | varchar |  |  | SI | A designation for the circumstances under which a ... |
| BEN_Childsub | double |  |  | NO | Childsub |
| BEN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BEN_CreatedDate | date |  |  | SI | Created Date |
| BEN_CreatedTime | time |  |  | SI | Created Time |
| BEN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BEN_DateFrom | date |  |  | SI | DateFrom |
| BEN_DateTo | date |  |  | SI | DateTo |
| BEN_ProviderList | varchar |  |  | SI | The list of types of providers that this benefit c... |
| BEN_RestrictionList | varchar |  |  | SI | The list of reasons for subsidisation that apply t... |
| BEN_RowId | varchar |  |  | NO | - |
| BEN_UpdatedDate | date |  |  | SI | Updated Date |
| BEN_UpdatedTime | time |  |  | SI | Updated Time |
| BEN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*