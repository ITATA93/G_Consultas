# SQLUser.RB_Referral

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REF_RowId | bigint | PK |  | NO | - |
| REF_Address | varchar |  |  | SI | Address |
| REF_Admission_DR | bigint |  | FK | SI | - |
| REF_Appoint_DR | varchar |  | FK | SI | Des Ref Appoint |
| REF_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| REF_Comments | varchar |  |  | SI | Comments |
| REF_Consultant_DR | varchar |  | FK | SI | Des Ref Consultant |
| REF_CreateDate | date |  |  | SI | CreateDate |
| REF_CreateTime | time |  |  | SI | CreateTime |
| REF_CreateUser_DR | bigint |  | FK | SI | Des Ref CreateUser |
| REF_DOB | date |  |  | SI | Date of Birth |
| REF_DiagCode | varchar |  |  | SI | DiagCode   |
| REF_DiagDesc | varchar |  |  | SI | DiagDesc |
| REF_Email | varchar |  |  | SI | Email   |
| REF_ErefStyleSheet | varchar |  |  | SI | ErefStyleSheet |
| REF_ExternalNumber | varchar |  |  | SI | ExternalNumber |
| REF_ExternalNumberType | varchar |  |  | SI | ExternalNumberType |
| REF_Forename | varchar |  |  | SI | Forename |
| REF_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| REF_InterpreterLanguage | varchar |  |  | SI | Interpreter Language |
| REF_InterpreterRequired | varchar |  |  | SI | Interpreter Required |
| REF_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| REF_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| REF_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| REF_Name2 | varchar |  |  | SI | Name2 |
| REF_OtherInformation | varchar |  |  | SI | Other Information |
| REF_PAPMI_DR | bigint |  | FK | SI | Des Ref  PAPMI |
| REF_PhoneH | varchar |  |  | SI | PhoneH |
| REF_PhoneM | varchar |  |  | SI | PhoneM |
| REF_PhoneW | varchar |  |  | SI | PhoneW |
| REF_PrefCareProvGenderDR | bigint |  | FK | SI | Preferred Care Provider Gender Des Ref Sex |
| REF_PrimDoc | varchar |  |  | SI | REFPrimDoc |
| REF_PrimDocAddress | varchar |  |  | SI | PrimDocAddress |
| REF_PrimDocClinic | varchar |  |  | SI | PrimDocClinic |
| REF_PrimDocEmail | varchar |  |  | SI | PrimDocEmail   |
| REF_PrimDocPhoneH | varchar |  |  | SI | PrimDocPhoneH |
| REF_PrimDocPhoneM | varchar |  |  | SI | PrimDocPhoneM |
| REF_PrimDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| REF_Priority_DR | bigint |  | FK | SI | Des Ref Priority |
| REF_ReceivedDate | date |  |  | SI | ReceivedDate |
| REF_ReceivedTime | time |  |  | SI | ReceivedTime |
| REF_RefCSId | varchar |  |  | SI | Referral Clinical Summary rowid |
| REF_RefCSReferralID | varchar |  |  | SI | Referral id |
| REF_RefDoc | varchar |  |  | SI | RefDoc |
| REF_RefDocAddress | varchar |  |  | SI | RefDocAddress |
| REF_RefDocClinic | varchar |  |  | SI | RefDocClinic |
| REF_RefDocEmail | varchar |  |  | SI | RefDocEmail   |
| REF_RefDocPhoneH | varchar |  |  | SI | RefDocPhoneH   |
| REF_RefDocPhoneM | varchar |  |  | SI | RefDocPhoneM   |
| REF_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| REF_RefLetterDate | date |  |  | SI | RefLetterDate |
| REF_RefNumber | varchar |  |  | SI | Referral Number |
| REF_RefStatus | varchar |  |  | SI | Referral status |
| REF_RefToProvider | varchar |  |  | SI | Referring to Provider |
| REF_RequestItem | varchar |  |  | SI | - |
| REF_RequestReason | varchar |  |  | SI | - |
| REF_SendingFacility | varchar |  |  | SI | Sending Facility |
| REF_SensoryImpairment | varchar |  |  | SI | Sensory Impairment |
| REF_Service_DR | bigint |  | FK | SI | Des Ref Service |
| REF_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| REF_SourceOfAddit_DR | bigint |  | FK | SI | Des Ref SourceOfAddition |
| REF_Status | varchar |  |  | SI | Status |
| REF_Surname | varchar |  |  | SI | Surname |
| REF_TreatmentID | varchar |  |  | SI | TreatmentID |
| REF_UBRN | varchar |  |  | SI | UBRN |
| REF_USRN | varchar |  |  | SI | USRN |
| REF_UpdatedExternal | varchar |  |  | SI | UpdatedExternal |
| REF_WLPriority_DR | bigint |  | FK | SI | Des Ref WLPriority |
| REF_WLReason_DR | bigint |  | FK | SI | Des Ref WLReason for List |
| REF_WaitListType_DR | bigint |  | FK | SI | Des Ref WaitListType |
| REF_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |
| REF_WrittenCommFormat | varchar |  |  | SI | Written Communication Format |
| REF_Zip | varchar |  |  | SI | Zip |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*