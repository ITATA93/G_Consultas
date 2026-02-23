# SQLUser.CF_SM

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SMCF_RowId1 | double | PK |  | NO | - |
| Q15Q1 | - |  |  | SI | Procedimiento a Realizar |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SMCF_AllowDeletionFromCodeTables | varchar |  |  | SI | Allow Deletion From Code Tables |
| SMCF_AuditUserLogin | varchar |  |  | SI | Audit User Login |
| SMCF_BillingVersion | varchar |  |  | SI | Billing Version |
| SMCF_BiometricsInUse | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| SMCF_CSPPath | varchar |  |  | SI | CSPPath |
| SMCF_CTNamespace | varchar |  |  | SI | CTNamespace |
| SMCF_City_DR | bigint |  | FK | SI | Des Ref City |
| SMCF_CloseAllFormsOnExit | varchar |  |  | SI | Close All Forms On Exit |
| SMCF_CreateWebIndexes | varchar |  |  | SI | CreateWebIndexes |
| SMCF_CrystRepPassword | varchar |  |  | SI | Password |
| SMCF_CrystalRepDSN | varchar |  |  | SI | DSN |
| SMCF_CrystalRepUserID | varchar |  |  | SI | User ID |
| SMCF_DICOMArchivePrefix | varchar |  |  | SI | DICOM Archive Prefix |
| SMCF_DICOMArciveCounter | double |  |  | SI | DICOM Arcive Counter |
| SMCF_DICOMCounter | double |  |  | SI | DICOM Counter |
| SMCF_DefDateFormat | varchar |  |  | SI | Default Date Format |
| SMCF_DefNumberFormat | varchar |  |  | SI | Default Number Format |
| SMCF_DisableAudit | varchar |  |  | SI | Disable Audit |
| SMCF_DoNotAuditHL7AtomicResults | varchar |  |  | SI | SMCFDoNotAuditHL7AtomicResults |
| SMCF_DoNotDeleteGrouperFile | varchar |  |  | SI | DoNotDeleteGrouperFile |
| SMCF_DocumentCounter | double |  |  | SI | Document Counter |
| SMCF_EnableAccessNTLogon | varchar |  |  | SI | Enable Access NT Logon |
| SMCF_EnableSystemCT | varchar |  |  | SI | Enable System CT |
| SMCF_EnableTrakAssist | varchar |  |  | SI | Enable Trak Assist - Deprecated in TC-391548 |
| SMCF_EnvType | varchar |  |  | SI | Environment type |
| SMCF_ErrorFileCounter | double |  |  | SI | Error File Counter |
| SMCF_ExplorePath | varchar |  |  | SI | Explore Path |
| SMCF_HCA_DR | bigint |  | FK | SI | Des Ref HCA |
| SMCF_HL7QueryTimeoutInSecs | double |  |  | SI | HL7QueryTimeoutInSecs |
| SMCF_HRGVersion | varchar |  |  | SI | HRGVersion |
| SMCF_IEPathName | varchar |  |  | SI | IEPathName |
| SMCF_ImageCounter | double |  |  | SI | Image Counter |
| SMCF_InactivityTimeout | double |  |  | SI | Inactivity Timeout (mins) |
| SMCF_InvalidLoginAttempts | varchar |  |  | SI | Invalid Login Attempts |
| SMCF_InvokeUserCacheAuditDLL | varchar |  |  | SI | InvokeUserCacheAuditDLL |
| SMCF_LabtrakUserID | varchar |  |  | SI | Labtrak User ID |
| SMCF_LabtrakUserPassword | varchar |  |  | SI | Labtrak User Password |
| SMCF_LanguageCode | double |  |  | SI | Default Language Number |
| SMCF_LicenseExpires | date |  |  | SI | License Expiry Date |
| SMCF_LicenseKey | varchar |  |  | SI | License Key |
| SMCF_LicenseSiteID | varchar |  |  | SI | License Site ID |
| SMCF_LicenseUsersCurrent | varchar |  |  | SI | Current Number of Users |
| SMCF_LicenseUsersMax | varchar |  |  | SI | Licensed Number of Users |
| SMCF_LinkExtLab | varchar |  |  | SI | Link to External Lab system |
| SMCF_MainDatabaseServer | varchar |  |  | SI | Main Database Server |
| SMCF_MedTrakVersion | varchar |  |  | SI | Version of MedTrak |
| SMCF_Name1 | varchar |  |  | SI | System Name |
| SMCF_Name2 | varchar |  |  | SI | System Name 2 |
| SMCF_NewLabTrak | varchar |  |  | SI | Use New LabTrak |
| SMCF_NoRestrictUserSameGroupOE | varchar |  |  | SI | NoRestrictUserSameGroupOE |
| SMCF_NowNominator | varchar |  |  | SI | Now Nominator |
| SMCF_ObservationBufferInUse | varchar |  |  | SI | Observation Buffer In Use |
| SMCF_OrgCode | varchar |  |  | SI | Organisation Code (Used for SPINE authentication) |
| SMCF_Owner | varchar |  |  | SI | - |
| SMCF_PDSInUse | varchar |  |  | SI | SMCFPSDSInUse |
| SMCF_PasswContainULSNChars | varchar |  |  | SI | Passw to Contain Up,Low,Spec,Num Chars |
| SMCF_PasswordDaysToExpire | double |  |  | SI | Password Days To Expire |
| SMCF_PasswordMinLength | double |  |  | SI | Password Min Length |
| SMCF_PathToCrystalReportServer | varchar |  |  | SI | Path To Crystal Report Server |
| SMCF_PathToDICOMArchive | varchar |  |  | SI | Path To DICOM Archive |
| SMCF_PathToDICOMCache | varchar |  |  | SI | Path To DICOM Cache |
| SMCF_PathToDICOMServer | varchar |  |  | SI | Path To DICOM Server |
| SMCF_PathToDRGGrouper | varchar |  |  | SI | Path To DRG Grouper |
| SMCF_PathToDocumentServer | varchar |  |  | SI | Path for Document Server |
| SMCF_PathToErrorFileServer | varchar |  |  | SI | Path To Error File Server |
| SMCF_PathToImagesServer | varchar |  |  | SI | Path to Images Server |
| SMCF_PathToTemplateServer | varchar |  |  | SI | Path To Template Server |
| SMCF_PathToUnixGrouper | varchar |  |  | SI | Path To Unix Grouper |
| SMCF_PathToVoiceFileServer | varchar |  |  | SI | Path To Voice File Server |
| SMCF_Province_DR | bigint |  | FK | SI | Des Ref Province |
| SMCF_RestrictUserSameGroup | varchar |  |  | SI | RestrictUserSameGroup |
| SMCF_RowId | double |  |  | NO | SMCF Row ID |
| SMCF_SigFigs | integer |  |  | SI | Significant Figures for Calculations |
| SMCF_SingleLogonPerUser | varchar |  |  | SI | SMCFSingleLogonPerUser |
| SMCF_TodayNominator | varchar |  |  | SI | Today Nominator |
| SMCF_TrakCareURL | varchar |  |  | SI | TrakCareURL |
| SMCF_UploadDocMaxSize | double |  |  | SI | Upload Documents MAx Filesize (KB) |
| SMCF_VoiceFileCounter | double |  |  | SI | Voice File Counter |
| SMCF_WordVersion | varchar |  |  | SI | Version of Word |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*