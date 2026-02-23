# websys.Configuration

> TrakCare System Configuration

**Schema:** websys
**Columnas:** 140
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

*Descripción original:* TrakCare System Configuration

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AlwaysResolveComputerNameOnPrint | bit |  |  | SI | If enabled forces reverse DNS lookup for client IP... |
| CGIVarClientIP | varchar |  |  | SI | Log 73942 - specifies the CGI variable used to der... |
| ChartFXURL | varchar |  |  | SI | - |
| CheckJSPercentServerCalls | bit |  |  | SI | [DEPRECATED]Not used anymore as checking of percen... |
| CrystalPreviewMode | varchar |  |  | SI | Crystal Preview Mode for V10 |
| CrystalPrintLocalVersion | varchar |  |  | SI | - |
| CrystalRptLicenses | integer |  |  | SI | Total number of Crystal Reports licenses for the O... |
| CrystalViewerType | varchar |  |  | SI | Crystal Viewer Type |
| CustomListRowExpression | varchar |  |  | SI | 85568 Expression that is executed on display of a ... |
| DBCredentials | varchar |  |  | SI | Ensemble credentials JReports will use to connect ... |
| DSN | varchar |  |  | SI | This property has been for a long time but as far ... |
| DataNamespace | varchar |  |  | SI | Data NameSpace |
| DateCenturyWindow | varchar |  |  | SI | - |
| DateFormat | varchar |  |  | SI | - |
| DateMaxAdditionDays | integer |  |  | SI | - |
| DateMonthCharacter | varchar |  |  | SI | - |
| DateSeparator | varchar |  |  | SI | - |
| DateTodayCharacter | varchar |  |  | SI | - |
| DateWeekCharacter | varchar |  |  | SI | - |
| DateYearCharacter | varchar |  |  | SI | - |
| DecimalPlaces | integer |  |  | SI | Number of decimal places used by currency conversi... |
| DecimalSymbol | varchar |  |  | SI | Decimal symbol |
| DefaultEmailFrom | varchar |  |  | SI | dah 15.02.2008 66325 - add default email from for ... |
| DefaultLetterReport | bigint |  |  | SI | Default Report for editable letters that dont have... |
| DigitalSignClient | bit |  |  | SI | - |
| DigitalSignClientApplet | bit |  |  | SI | - |
| DigitalSignClientDll | varchar |  |  | SI | - |
| DigitalSignClientNotUsePwd | bit |  |  | SI | - |
| DigitalSignClientScript | varchar |  |  | SI | - |
| DisablePrinterInUseCheck | bit |  |  | SI | Maximise printing throughput by diabling printer i... |
| DoNotCache | bit |  |  | SI | If this property is true then all %response object... |
| DocObjectBaseURL | varchar |  |  | SI | Base URL for Online Help Documentation |
| EnableAnalyticsIndexing | bit |  |  | SI | 84019 Enable Analytics Indexing |
| EnableCaching | bit |  |  | SI | Enable patient data caching (patient data caching ... |
| EnableCodeTableUpdates | bit |  |  | SI | - |
| EnableEditionOptions | bit |  |  | SI | - |
| EnableHelp | bit |  |  | SI | Enable Online Help |
| EnableMsgNotif | bit |  |  | SI | - |
| EnablePrintOptions | bit |  |  | SI | - |
| EnableSecureDocViewer | bit |  |  | SI | Enable Secure Document Viewer |
| EnableTRAKOptions | bit |  |  | SI | - |
| EnableVisualRulesIndexing | bit |  |  | SI | Enable VisualRules Indexing |
| ExternalAuthLogoutURL | varchar |  |  | SI | URL to redirect to on logout when external authent... |
| FeaturesFrameworkDisabled | bit |  |  | SI | [DEPRECATED]Replaced by FeaturesFrameworkEnabled i... |
| FeaturesFrameworkEnabled | bit |  |  | SI | Features Framework Enabled |
| HSViewerLinkURL | varchar |  |  | SI | HealthShare Viewer Dynamic Link URL
Used to launc... |
| HideDebugInfo | bit |  |  | SI | Hide Debug Information 75676 |
| InstallationCode | varchar |  |  | SI | - |
| JReportEncoding | varchar |  |  | SI | [DEPRECATED]Deprecated by new Logi Report configur... |
| JReportFilesVersion | varchar |  |  | SI | [DEPRECATED]Deprecated by new Logi Report configur... |
| JReportResourcePrefix | varchar |  |  | SI | [DEPRECATED]Deprecated by new Logi Report configur... |
| JReportServerVersion | varchar |  |  | SI | [DEPRECATED]Deprecated by new Logi Report configur... |
| LDAPAdminName | varchar |  |  | SI | User that has search privileges on the LDAP server... |
| LDAPAdminPassword | varchar |  |  | SI | Password of User that has search privileges on the... |
| LDAPBaseDN | varchar |  |  | SI | Define the Base distinguished name (DN) of where t... |
| LDAPEnableFailback | bit |  |  | SI | When used with Override Authentication, if externa... |
| LDAPEnabled | bit |  |  | SI | Set to true to enable user authentication to check... |
| LDAPIsWindowsAD | bit |  |  | SI | This needs to be defined if the LDAP server is a W... |
| LDAPSecureCertFile | varchar |  |  | SI | For a Unix Cache client, specify where the certifi... |
| LDAPSecureConnection | bit |  |  | SI | Set to true to use a secure TSL/SSL connection for... |
| LDAPServer | varchar |  |  | SI | Define the LDAP primary server address. This shoul... |
| LDAPServer2 | varchar |  |  | SI | Define the LDAP secondary server address. This sho... |
| LDAPServer3 | varchar |  |  | SI | Define the LDAP tertiary server address. This shou... |
| LDAPUniqueIdentifier | varchar |  |  | SI | Define the unique identifier attribute in the user... |
| LabDataNamespace | varchar |  |  | SI | - |
| LabTrakURL | varchar |  |  | SI | LabTrak URL |
| LabWorksheetReport | bigint |  |  | SI | Default Report for printing Lab Worksheets |
| LanguageApp | varchar |  |  | SI | Stores rowid from SSLanguage table.
Uses this lan... |
| LayoutManager | varchar |  |  | SI | Connection string to the Trak Web Edit Layout mana... |
| LookupKey | varchar |  |  | SI | ab 12.03.08 65772 |
| NATServer | bit |  |  | SI | Specifies if NAT Server is being used. When enable... |
| OverrideAuthentication | bit |  |  | SI | Override TrakCare authentication. Should only be e... |
| PathToApp | varchar |  |  | SI | The path from top level on web server to applicati... |
| PathToCDLs | varchar |  |  | SI | Path used to import CDLs, views, and to export vie... |
| PathToDSFiles | varchar |  |  | SI | Path of the folder that will store all Discharge S... |
| PathToHelpText | varchar |  |  | SI | [DEPRECATED]Deprecated in favour of Documentation ... |
| PathToJReports | varchar |  |  | SI | Path to JReportsFolder |
| PathToReports | varchar |  |  | SI | The path to reports folder.
Used by the TPS when ... |
| PathToReportsUnix | varchar |  |  | SI | The Unix path to reports folder.
Used for the Rep... |
| PathToScripts | varchar |  |  | SI | The path on the server for generated scripts to be... |
| PathToTemporaryFiles | varchar |  |  | SI | Used by Mail and Fax services as common place to p... |
| PathToTemporaryFilesUnix | varchar |  |  | SI | For unix boxes only this is the local path of the ... |
| PathToVBFileServerRoot | varchar |  |  | SI | UNC path to Patches folder. There should only one ... |
| PathToVBPatches | varchar |  |  | SI | UNC path to Patches folder. There should only one ... |
| PathToWebPatches | varchar |  |  | SI | UNC path to Patches folder. There should only one ... |
| PathsToWebServers | varchar |  |  | SI | A ; delimitted list of Web Server paths. There may... |
| PerformanceStatisticsCapture | bit |  |  | SI | - |
| PerformanceStatisticsCaptureMemoryUsage | bit |  |  | SI | Enable capturing of memory usage to page load perf... |
| PerformanceStatisticsCaptureVerbose | bit |  |  | SI | - |
| PerformanceStatisticsDisplay | bit |  |  | SI | - |
| PerformanceStatisticsIconCapture | bit |  |  | SI | - |
| PrintServiceEnabled | bit |  |  | SI | Enables/Disables Crystal reports license monitorin... |
| PushAPIPath | varchar |  |  | SI | Path of the Push Notification API |
| PushEnable | bit |  |  | SI | Enable Push Notifications |
| PushPassword | varchar |  |  | SI | Password for push server connection |
| PushSSLProfile | varchar |  |  | SI | Push SSL Configuration defined in managment portal |
| PushSecure | bit |  |  | SI | Enable secure connection (HTTPS) to push server |
| PushServer | varchar |  |  | SI | DNS Name or IP address of Push Notification Server |
| PushServerPort | varchar |  |  | SI | Port for push server connection |
| PushServerTimeout | integer |  |  | SI | Timeout for push server connection |
| PushUserName | varchar |  |  | SI | Username for push server connection |
| QuesSignPadClass | varchar |  |  | SI | SiganturePad  Class  used to open signature pad in... |
| Region | varchar |  |  | SI | ab 1.06.07 63290 - region is a higher level than s... |
| ReportPreviewUserRestrict | bit |  |  | SI | 87515 Enable single user instance restriction for ... |
| ReportPrinterSelectionLogic | bit |  |  | SI | Report Printer Selection Logic (o=old,1=new)
0 = ... |
| SMTPServer | varchar |  |  | SI | DNS Name or IP address of SMTP (Simple Mail Transp... |
| SSOAuthorisationClass | varchar |  |  | SI | SSO Authorisation Class |
| SSOIdentityManagerLocation | varchar |  |  | SI | SSO Identity Manager Location |
| SSOOAuth2ClientName | varchar |  |  | SI | Placeholder for custom OAuth2 Client Name used by ... |
| SecureDocViewerRedirectPath | varchar |  |  | SI | Path used to configure TrakCare web server to redi... |
| SiteCode | varchar |  |  | SI | A code to identify the site |
| SortMaxRows | varchar |  |  | SI | The maximum number of rows to be returned and sort... |
| SpeedMinerRTS | bit |  |  | SI | ab 65888 - speedminer global setting |
| SpineAuthentication | bit |  |  | SI | ab 15.12.08 66574 -spine authentication flag |
| Style | varchar |  |  | SI | System wide style setting, selected from StandardT... |
| TimeAMSymbol | varchar |  |  | SI | - |
| TimeFormat | varchar |  |  | SI | - |
| TimeLockSession | varchar |  |  | SI | LockSession TimeOut in minutes |
| TimeNowCharacter | varchar |  |  | SI | - |
| TimeOut | varchar |  |  | SI | Application TimeOut in minutes |
| TimePMSymbol | varchar |  |  | SI | - |
| TimeSeparator | varchar |  |  | SI | - |
| TimeZone | varchar |  |  | SI | Server Time Zone |
| URLToAnalytics | varchar |  |  | SI | URL to the Analytics server 83651
For example, "h... |
| URLToCrystalReports | varchar |  |  | SI | - |
| URLToJReportServer | varchar |  |  | SI | [DEPRECATED]Deprecated by new Logi Report configur... |
| URLToSecureDocServer | varchar |  |  | SI | URL to Secure Document Server |
| URLToSecureDocViewer | varchar |  |  | SI | URL to Secure Document Viewer |
| URLToZENReports | varchar |  |  | SI | yc 19/01/2009 70694 - URL to run ZEN reports from |
| UseChartFX | bit |  |  | SI | dah 23.01.08 65056 - add config checkbox to force ... |
| UseEPRMenuScroll | bit |  |  | SI | true to use system scroll buttons on epr menu head... |
| VBFolderNameActiveX | varchar |  |  | SI | UNC path to Patches folder. There should only one ... |
| VBFolderNameActiveXWinSys | varchar |  |  | SI | UNC path to Patches folder. There should only one ... |
| VBFolderNameExecutables | varchar |  |  | SI | UNC path to Patches folder. There should only one ... |
| WebServer | varchar |  |  | SI | Address (IP Address or Name of web server).
Used ... |
| WebServerPassword | varchar |  |  | SI | - |
| WebServerUsername | varchar |  |  | SI | - |
| XMLUnixPath | varchar |  |  | SI | cjb 22/08/2005 54693 |
| XMLWindowsPath | varchar |  |  | SI | cjb 22/08/2005 54693 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*