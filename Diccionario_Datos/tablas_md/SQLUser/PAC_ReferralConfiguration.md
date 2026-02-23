# SQLUser.PAC_ReferralConfiguration

**Schema:** SQLUser
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFCONF_RowId | bigint | PK |  | NO | - |
| ChildQ31DR | - |  |  | SI | Child Reference: Dexterity |
| Q30Q1 | - |  |  | SI | Strength assessment for |
| Q30Q2 | - |  |  | SI | Able to lift 2 litre bags |
| Q30Q3 | - |  |  | SI | Able to lift 6 litre bags |
| Q30Q4 | - |  |  | SI | Able to open packaging |
| Q30Q5 | - |  |  | SI | Able to hang bags |
| Q30Q6 | - |  |  | SI | Able to dispose of rubbish |
| Q30Q7 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFCONF_CTSex_DR | bigint |  | FK | SI | Des Ref CTSex |
| REFCONF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFCONF_CounterType_DR | bigint |  | FK | SI | Des Ref CounterType |
| REFCONF_CreatedDate | date |  |  | SI | Created Date |
| REFCONF_CreatedTime | time |  |  | SI | Created Time |
| REFCONF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFCONF_DateFrom | date |  |  | SI | Date From |
| REFCONF_DateTo | date |  |  | SI | Date To |
| REFCONF_InsuranceType_DR | bigint |  | FK | SI | Des Ref InsuranceType |
| REFCONF_NumberAuthorised | double |  |  | SI | NumberAuthorised  |
| REFCONF_NumberFree | double |  |  | SI | NumberFree  |
| REFCONF_NumberInUse | double |  |  | SI | Number in Use  |
| REFCONF_Owner | varchar |  |  | SI | Owner |
| REFCONF_ParamGoingBack | double |  |  | SI | Parameter for going back  |
| REFCONF_RefAssessLevel_DR | bigint |  | FK | SI | Des Ref ReferralAssessmentLevel |
| REFCONF_RefAssessType_DR | bigint |  | FK | SI | Des Ref ReferralAssessmentType |
| REFCONF_UpdatedDate | date |  |  | SI | Updated Date |
| REFCONF_UpdatedTime | time |  |  | SI | Updated Time |
| REFCONF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| REFCONF_WaitListType_DR | bigint |  | FK | SI | Des Ref PACWaitingListType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*