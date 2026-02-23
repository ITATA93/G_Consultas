# lab.CF_SystemDefaults

**Schema:** lab
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFSM_RowId | bigint | PK |  | NO | - |
| CFSM_AnalyticalPort | varchar |  |  | SI | Analytical Port |
| CFSM_AnalyticalServer | varchar |  |  | SI | Analytical Server |
| CFSM_AnalyticsIndexing | varchar |  |  | SI | Analytics Indexing |
| CFSM_AutoPatMerge | varchar |  |  | SI | Automatic Patient Merging |
| CFSM_CentralSite_DR | varchar |  | FK | SI | Central Site DR |
| CFSM_ClientCode | varchar |  |  | SI | Client Code |
| CFSM_CloseAllFormsOnExit | varchar |  |  | SI | Close All Forms On Exit |
| CFSM_CurrentSite_DR | varchar |  | FK | SI | Current Site DR |
| CFSM_DateFormat | varchar |  |  | SI | Date format |
| CFSM_DecimalSymbol | varchar |  |  | SI | Decimal symbol |
| CFSM_DefaultDestination_DR | varchar |  | FK | SI | Des Ref Default Destination |
| CFSM_DisallowPreviousPasswords | varchar |  |  | SI | Disallow Use Previous Passwords |
| CFSM_InactivityTimeOut | double |  |  | SI | Inactivity Time Out |
| CFSM_InactivityTimeOutWord | double |  |  | SI | Inactivity Time Out Word |
| CFSM_InterfacesDatabaseServer | varchar |  |  | SI | Interfaces Database Server |
| CFSM_LDAPIsWindowsAD | varchar |  |  | SI | Is Windows Active Directory |
| CFSM_LDAPSecureCertFile | varchar |  |  | SI | Secure Certificate File |
| CFSM_LDAPSecureConnection | varchar |  |  | SI | Secure Connection |
| CFSM_LDAPServer | varchar |  |  | SI | LDAP Server |
| CFSM_LDAPUNIXAdminDN | varchar |  |  | SI | UNIX AdminDN |
| CFSM_LDAPUNIXAdminPassword | varchar |  |  | SI | UNIX Administrator Password |
| CFSM_LDAPUNIXBaseDN | varchar |  |  | SI | UNIX Base DN |
| CFSM_LDAPUNIXUniqueIdentifier | varchar |  |  | SI | UNIX Unique Identifier |
| CFSM_LDAPWinAdminDN | varchar |  |  | SI | Windows AdminDN |
| CFSM_LDAPWinAdminName | varchar |  |  | SI | Windows Administrator Name |
| CFSM_LDAPWinAdminPassword | varchar |  |  | SI | Windows Administrator Password |
| CFSM_LDAPWinBaseDN | varchar |  |  | SI | Windows Base DN |
| CFSM_LDAPWinDomain | varchar |  |  | SI | Windows Domain |
| CFSM_LDAPWinUniqueIdentifier | varchar |  |  | SI | Windows Unique Identifier |
| CFSM_LanguageCode | double |  |  | SI | Default Language Number |
| CFSM_LicenseExpires | date |  |  | SI | License Expiry Date |
| CFSM_LicenseKey | varchar |  |  | SI | License Key |
| CFSM_LicenseSiteID | varchar |  |  | SI | License Site ID |
| CFSM_LicenseUsersCurrent | varchar |  |  | SI | License Users Current |
| CFSM_LicenseUsersMax | varchar |  |  | SI | License Users Max |
| CFSM_LincolnPDFServer | varchar |  |  | SI | Lincoln PDF Server Name |
| CFSM_MainDatabaseServer | varchar |  |  | SI | Main Database Server |
| CFSM_MaxNumberOfUsers | numeric |  |  | SI | Maximum number of concurrent users |
| CFSM_MultiDBModel | varchar |  |  | SI | Multi DB model |
| CFSM_Name1 | varchar |  |  | SI | System Name |
| CFSM_Name2 | varchar |  |  | SI | System Name 2 |
| CFSM_NoTimeNominator | varchar |  |  | SI | No Time Nominator |
| CFSM_NowNominator | varchar |  |  | SI | Now Nominator |
| CFSM_NumberOfLoginTries | double |  |  | SI | Number Of Login Tries |
| CFSM_PackEntryFieldOrder | varchar |  |  | SI | Pack Entry Field Order |
| CFSM_PasswordExpiryPeriod | varchar |  |  | SI | Password expiry period |
| CFSM_PasswordMinLength | varchar |  |  | SI | Password Minimum Length |
| CFSM_PasswordMixed | varchar |  |  | SI | Password Mixed |
| CFSM_PasswordNumberLimit | double |  |  | SI | Password Number Limit |
| CFSM_PathToEDIFilesIn | varchar |  |  | SI | Path To EDI Files In |
| CFSM_PathToEDIFilesOut | varchar |  |  | SI | Path To EDI Files Out |
| CFSM_PathToErrorFileServer | varchar |  |  | SI | Path to Error File Server |
| CFSM_PathToImagesServer | varchar |  |  | SI | Path to Images Server |
| CFSM_PathToImagesServerCache | varchar |  |  | SI | Path to Images Server Cache |
| CFSM_PathToImportEpisodes | varchar |  |  | SI | Path To Import Episodes |
| CFSM_PathToLincolnPDF | varchar |  |  | SI | Path to Lincoln PDF |
| CFSM_PathToQCReport | varchar |  |  | SI | Path To QC Report |
| CFSM_PathToReportsFax | varchar |  |  | SI | Path to Reports Fax |
| CFSM_PathToReportsFaxCache | varchar |  |  | SI | Path to Reports Fax Cache |
| CFSM_PathToReportsLocal | varchar |  |  | SI | Path to Reports Local |
| CFSM_PathToReportsLocalCache | varchar |  |  | SI | Path to Reports Local Cache |
| CFSM_PathToTemplateCache | varchar |  |  | SI | Path to Template Server Cache |
| CFSM_PathToTemplateServer | varchar |  |  | SI | Path to Template Server |
| CFSM_PathToVoiceFileServer | varchar |  |  | SI | Path to Voice File Server |
| CFSM_PathtoDocumentServer | varchar |  |  | SI | Path to Document Server |
| CFSM_PathtoDocumentServerCache | varchar |  |  | SI | Path to Document Server Cache |
| CFSM_ShadowServerIP | varchar |  |  | SI | Shadow Server IP |
| CFSM_SleepTime | varchar |  |  | SI | Sleep Time for pcl2pdf Server |
| CFSM_TimeFormat | varchar |  |  | SI | Time format |
| CFSM_TimeOutSingle | double |  |  | SI | Patient search - Time Out Single |
| CFSM_TimeOutTotal | double |  |  | SI | Patient search - Time Out Total |
| CFSM_TodayNominator | varchar |  |  | SI | Today Nominator |
| CFSM_TwoTierSetup | varchar |  |  | SI | Two Tier Setup |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*