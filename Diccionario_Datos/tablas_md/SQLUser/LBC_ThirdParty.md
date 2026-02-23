# SQLUser.LBC_ThirdParty

**Schema:** SQLUser
**Columnas:** 41
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTP_RowID | bigint | PK |  | NO | - |
| ChildQ83DR | - |  |  | SI | Child Reference: Reflejos Arcaicos Normales |
| LBCTP_Address | varchar |  |  | SI | Street Address |
| LBCTP_City_DR | bigint |  | FK | SI | City |
| LBCTP_Code | varchar |  |  | NO | Code |
| LBCTP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTP_CodeTranslated | varchar |  |  | SI | Code Translated |
| LBCTP_ConfidentialFax | varchar |  |  | SI | Confidential Fax Number |
| LBCTP_Copies | numeric |  |  | SI | Deprecated
The default number of copies to use fo... |
| LBCTP_Courier_DR | bigint |  | FK | SI | Deprecated
The default Courier to use for Lab Doc... |
| LBCTP_CreatedDate | date |  |  | SI | Created Date |
| LBCTP_CreatedTime | time |  |  | SI | Created Time |
| LBCTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTP_CumulativeEpisodes | integer |  |  | SI | Deprecated
Cumulatives Maximum Number of Episodes... |
| LBCTP_CumulativeOrder | varchar |  |  | SI | Deprecated
Doctors Reports Cumulative Order
The ... |
| LBCTP_CumulativePreference | varchar |  |  | SI | Deprecated
Doctors Reports Cumulative Preference... |
| LBCTP_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTP_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTP_Desc | varchar |  |  | NO | Description (Full Name, as to appear on the report... |
| LBCTP_DescTranslated | varchar |  |  | SI | Desc Translated |
| LBCTP_DoctorsReportsDeliverySort | varchar |  |  | SI | Deprecated
Doctors Reports Delivery Sort
The sor... |
| LBCTP_DoctorsReportsType | varchar |  |  | SI | Deprecated
Report Type
The ReportType to use for... |
| LBCTP_ExternalInterfaceQueue_DR | bigint |  | FK | SI | Deprecated
External Interface Queue |
| LBCTP_ExternalReferralSource | varchar |  |  | SI | External Referral Source |
| LBCTP_Fax | varchar |  |  | SI | Fax Number |
| LBCTP_Language_DR | bigint |  | FK | SI | Deprecated
Doctors Reports Language
The language... |
| LBCTP_ManualPrint | varchar |  |  | SI | Deprecated
Manual Print
Flag to show if Doctors ... |
| LBCTP_Owner | varchar |  |  | SI | Owner |
| LBCTP_Phones | varchar |  |  | SI | Phone Numbers |
| LBCTP_Province_DR | bigint |  | FK | SI | State |
| LBCTP_QuickPrint | varchar |  |  | SI | Deprecated
The default Quick-Print flag for Docto... |
| LBCTP_ReportMode | varchar |  |  | SI | Deprecated
Report Mode |
| LBCTP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCTP_Zip_DR | bigint |  | FK | SI | Zip |
| Q70Q1 | - |  |  | SI | Lesión |
| Q70Q2 | - |  |  | SI | Segmento |
| Q70Q3 | - |  |  | SI | Lateralidad |
| Q70Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*