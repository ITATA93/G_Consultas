# SQLUser.ORC_Operation

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPER_RowId | bigint | PK |  | NO | - |
| ChildQ03DR | - |  |  | SI | Child Reference: Wound drainage |
| OPER_ARCIM_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| OPER_ActiveDateTo | date |  |  | SI | Active Date To |
| OPER_AddCodReq_DR | bigint |  | FK | SI | Des Ref Additional Code Requirement |
| OPER_Age2CheckType_DR | bigint |  | FK | SI | Des Ref Age2 Check Type |
| OPER_Age2From | varchar |  |  | SI | Age2From |
| OPER_Age2To | varchar |  |  | SI | Age2 To |
| OPER_AgeCheckType_DR | bigint |  | FK | SI | Des Ref Age Check Type1 |
| OPER_AgeFrom | varchar |  |  | SI | Age From |
| OPER_AgeFrom1 | varchar |  |  | SI | Age From1 |
| OPER_AgeTo | varchar |  |  | SI | Age To |
| OPER_AgeTo1 | varchar |  |  | SI | Age To1 |
| OPER_AreaCodeRestraints_DR | bigint |  | FK | SI | Des Ref Area Code Restraints |
| OPER_BlockNumber | varchar |  |  | SI | Block Number |
| OPER_CCAMCodChapSectBlockCateg_DR | varchar |  | FK | SI | Des Ref MRCCCAMCodChapSectBlockCateg |
| OPER_CCAMCodChapSectBlock_DR | varchar |  | FK | SI | Des Ref MRCCCAMCodChapSectBlock |
| OPER_CCAMCodChapSect_DR | varchar |  | FK | SI | Des Ref MRCCCAMCodChapSect |
| OPER_CCAMCodChap_DR | bigint |  | FK | SI | Des Ref MRCCCAMCodChap |
| OPER_CodPractices_DR | bigint |  | FK | SI | Des Ref Coding Practices |
| OPER_Code | varchar |  |  | NO | ICD Code |
| OPER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OPER_CodeTranslated | varchar |  |  | SI | - |
| OPER_CreatedDate | date |  |  | SI | Created Date |
| OPER_CreatedTime | time |  |  | SI | Created Time |
| OPER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPER_DaggerAsterEdit_DR | bigint |  | FK | SI | Des Ref Dagger and Asterisk Edit |
| OPER_DateActiveFrom | date |  |  | NO | Date Active From |
| OPER_DaySurgery | varchar |  |  | SI | Day Surgery |
| OPER_DaysAdvance | double |  |  | SI | Days in Advance to Admit |
| OPER_DefaultAnaesMeth_DR | bigint |  | FK | SI | Default Anaesthesia Method |
| OPER_DefaultCategory_DR | bigint |  | FK | SI | Des Ref  Oper Category |
| OPER_DefaultEstimTime | varchar |  |  | SI | Default Estimated Time |
| OPER_Desc | varchar |  |  | NO | Operation Description |
| OPER_DescTranslated | varchar |  |  | SI | - |
| OPER_EpisodeTypes | varchar |  |  | SI | Episode Types |
| OPER_ExternalCause | varchar |  |  | SI | External Cause |
| OPER_ICD10 | varchar |  |  | SI | ICD10 |
| OPER_ICD10Map | varchar |  |  | SI | First ICD10 Mapping |
| OPER_ICD9Map | varchar |  |  | SI | ICD9 Mapping |
| OPER_LengthOfStay | varchar |  |  | SI | Length Of Stay |
| OPER_LongDescription | varchar |  |  | SI | Long Description |
| OPER_MechVentilCode | varchar |  |  | SI | Mechanical Ventilation Code |
| OPER_NIV | varchar |  |  | SI | Non-Invasive Ventilation |
| OPER_NationalCode | varchar |  |  | SI | National Code |
| OPER_OperBundle_DR | bigint |  | FK | SI | Des Ref ARCOperationBundle  |
| OPER_Owner | varchar |  |  | SI | Owner |
| OPER_PrevCleanUpTime | double |  |  | SI | Clean up time (minutes) needed after the previous ... |
| OPER_ProcDateMandatory | varchar |  |  | SI | Procedure Date Mandatory Flag |
| OPER_ProcSetupTime | double |  |  | SI | Pre/Set up time (minutes), setup time needed for t... |
| OPER_Purpose | varchar |  |  | SI | Purpose |
| OPER_Recovery | varchar |  |  | SI | Recovery |
| OPER_SexCheckType_DR | bigint |  | FK | SI | Des Ref Sex Check Type |
| OPER_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| OPER_UnacceptablePDx | varchar |  |  | SI | Unacceptable PDx |
| OPER_UpdatedDate | date |  |  | SI | Updated Date |
| OPER_UpdatedTime | time |  |  | SI | Updated Time |
| OPER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| OPER_Valid | varchar |  |  | SI | Valid |
| OPER_WaitingListType_DR | bigint |  | FK | SI | Waiting List Type  |
| Q02Q1 | - |  |  | SI | Dressing type |
| Q02Q2 | - |  |  | SI | Details |
| Q02Q3 | - |  |  | SI | Site |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*