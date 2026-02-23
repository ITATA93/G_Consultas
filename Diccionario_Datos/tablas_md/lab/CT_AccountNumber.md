# lab.CT_AccountNumber

**Schema:** lab
**Columnas:** 38
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTAN_RowID | varchar | PK |  | NO | - |
| CTAN_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTAN_BillAddress1 | varchar |  |  | SI | Bill Address1 |
| CTAN_BillAddress2 | varchar |  |  | SI | Bill Address2 |
| CTAN_BillAddress3_Suburb | varchar |  |  | SI | Bill Suburb |
| CTAN_BillAddress4_State | varchar |  |  | SI | Bill State |
| CTAN_BillAddress5_PostCode | varchar |  |  | SI | Bill Post Code |
| CTAN_Code | varchar |  |  | NO | Code |
| CTAN_CustomerType_DR | varchar |  | FK | SI | Customer Type |
| CTAN_Description | varchar |  |  | SI | Description |
| CTAN_Email | varchar |  |  | SI | Email |
| CTAN_Fax | varchar |  |  | SI | Fax |
| CTAN_Flag1 | varchar |  |  | SI | Flag 1 |
| CTAN_Flag2 | varchar |  |  | SI | Flag 2 |
| CTAN_Flag3 | varchar |  |  | SI | Flag 3 |
| CTAN_FundDependant | varchar |  |  | SI | Health Fund Dependant Counter |
| CTAN_FundNumber | varchar |  |  | SI | Health Fund Number |
| CTAN_GivenName | varchar |  |  | SI | Given Name |
| CTAN_HealthFund_DR | varchar |  | FK | SI | Health Fund DR |
| CTAN_LastModifiedDate | date |  |  | SI | Last Modified Date |
| CTAN_LastModifiedTime | time |  |  | SI | Last Modified Time |
| CTAN_LastModifiedUser_DR | varchar |  | FK | SI | Last Modified User DR |
| CTAN_NationalID | varchar |  |  | SI | NationalID |
| CTAN_NationalIDType_DR | varchar |  | FK | SI | National ID Type DR |
| CTAN_PaymentCode_DR | varchar |  | FK | SI | Payment Code DR |
| CTAN_PhoneHome | varchar |  |  | SI | Phone Home |
| CTAN_PhoneMobile | varchar |  |  | SI | Phone Mobile |
| CTAN_PhoneWork | varchar |  |  | SI | Phone Work |
| CTAN_RegionCode | varchar |  |  | SI | Region Code |
| CTAN_ResidentialAddress1 | varchar |  |  | SI | Residential Address1 |
| CTAN_ResidentialAddress2 | varchar |  |  | SI | Residential Address2 |
| CTAN_ResidentialAddress3_Suburb | varchar |  |  | SI | Residential Suburb |
| CTAN_ResidentialAddress4_State | varchar |  |  | SI | Residential State |
| CTAN_ResidentialAddress5_PostCode | varchar |  |  | SI | Residential Post Code |
| CTAN_Surname | varchar |  |  | SI | Surname |
| CTAN_Title_DR | varchar |  | FK | SI | Des Ref Title |
| CTAN_Type | varchar |  |  | SI | Type |
| CTAN_UserSite_DR | varchar |  | FK | SI | User Site |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*