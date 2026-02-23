# lab.SS_User

**Schema:** lab
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSUSR_RowId | varchar | PK |  | NO | - |
| SSUSR_ALPHAUPName | varchar |  |  | NO | ALPHAUP Name |
| SSUSR_Active | varchar |  |  | NO | Active |
| SSUSR_ChangePIN | varchar |  |  | SI | Change PIN |
| SSUSR_ChangePassword | varchar |  |  | SI | Change Password |
| SSUSR_CompetencyExpiryDate | date |  |  | SI | Competency Expiry Date |
| SSUSR_Competency_DR | varchar |  | FK | SI | Competency  |
| SSUSR_DBLaboratory_DR | varchar |  | FK | SI | DB Laboratory DR |
| SSUSR_DBSiteOfOrigin | varchar |  |  | SI | Site of Origin |
| SSUSR_DateOfLastLogon | date |  |  | SI | Date Of Last Logon |
| SSUSR_DateOfLastPINChange | date |  |  | SI | Date Of Last PIN Change |
| SSUSR_DateOfLastPasswordChange | date |  |  | SI | Date Of Last Password Change |
| SSUSR_Department_DR | varchar |  | FK | SI | Department DR |
| SSUSR_Destination_DR | varchar |  | FK | SI | Des Ref Destination |
| SSUSR_EMailName | varchar |  |  | SI | Name on EMail system |
| SSUSR_Group | bigint |  |  | SI | Security Group |
| SSUSR_Initials | varchar |  |  | NO | Initials (Short Name) |
| SSUSR_Language_DR | bigint |  | FK | SI | Language DR |
| SSUSR_ManualPairedSera | varchar |  |  | SI | Manual Paired Sera Management |
| SSUSR_Name | varchar |  |  | NO | Name |
| SSUSR_NumberOfFailedLogins | double |  |  | SI | Number Of Failed Logins |
| SSUSR_PEPLPrefix | varchar |  |  | SI | PE PL prefix |
| SSUSR_PETable | varchar |  |  | SI | PE Table |
| SSUSR_PIN | varchar |  |  | SI | PIN |
| SSUSR_Password | varchar |  |  | SI | Password |
| SSUSR_PersonnelType_DR | varchar |  | FK | SI | Des Ref Personnel Type |
| SSUSR_PracticeSecurityType | varchar |  |  | SI | Practice Security Type |
| SSUSR_Provider | varchar |  |  | SI | Provider number |
| SSUSR_Qualifications | varchar |  |  | SI | Qualifications |
| SSUSR_Supervisor | varchar |  |  | SI | Supervisor |
| SSUSR_SupervisorForAP | varchar |  |  | SI | Supervisor For AP |
| SSUSR_SupervisorForBB | varchar |  |  | SI | Supervisor For BB |
| SSUSR_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*