# SQLUser.PA_TempAddress

**Schema:** SQLUser
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADDR_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| ADDR_AddrManualEntry | varchar |  |  | SI | Unvalidated address is manually entered |
| ADDR_AddreSamID | varchar |  |  | SI | Address eSam ID |
| ADDR_AddressType_DR | bigint |  | FK | SI | Des Ref AddressType |
| ADDR_AdmLeave_DR | varchar |  | FK | SI | Des Ref AdmLeave |
| ADDR_BusinessPhone | varchar |  |  | SI | Business Phone |
| ADDR_Childsub | double |  |  | NO | Childsub |
| ADDR_CityArea_DR | bigint |  | FK | SI | Des Ref CityArea |
| ADDR_City_DR | bigint |  | FK | SI | Des Ref City |
| ADDR_Comments | varchar |  |  | SI | Comments |
| ADDR_Country_DR | bigint |  | FK | SI | Country |
| ADDR_DateFrom | date |  |  | SI | Date From |
| ADDR_DateTo | date |  |  | SI | Date To |
| ADDR_DependentLocality | varchar |  |  | SI | DependentLocality |
| ADDR_DomicileCode | varchar |  |  | SI | Domicile Code |
| ADDR_ExternalOID | varchar |  |  | SI | ExternalOID |
| ADDR_ForeignCity | varchar |  |  | SI | Foreign City |
| ADDR_ForeignCountry | varchar |  |  | SI | Foreign Country |
| ADDR_ForeignSuburb | varchar |  |  | SI | Foreign Suburb |
| ADDR_ForeignZip | varchar |  |  | SI | Foreign Zip |
| ADDR_GeoLocationCode | varchar |  |  | SI | Address Geo-location Code |
| ADDR_HCA_DR | bigint |  | FK | SI | Des Ref HCA |
| ADDR_Latitude | varchar |  |  | SI | Address Latitude |
| ADDR_Longitude | varchar |  |  | SI | Address Longitude |
| ADDR_MobilePhone | varchar |  |  | SI | Mobile Phone |
| ADDR_NotValidAddrReason_DR | bigint |  | FK | SI | Not Validated Address Reason - Des Ref to PACNotVa... |
| ADDR_Phone | varchar |  |  | SI | Phone |
| ADDR_Province_DR | bigint |  | FK | SI | Des REf Province |
| ADDR_Region_DR | bigint |  | FK | SI | Des Ref Region |
| ADDR_RowId | varchar |  |  | NO | - |
| ADDR_Street | varchar |  |  | SI | Street |
| ADDR_Street2 | varchar |  |  | SI | Street2 |
| ADDR_Street3 | varchar |  |  | SI | Address 3 |
| ADDR_StreetLine1 | varchar |  |  | SI | StreetLine1 |
| ADDR_UpdateDate | date |  |  | SI | UpdateDate |
| ADDR_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| ADDR_UpdateTime | time |  |  | SI | Update Time |
| ADDR_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| ADDR_Zip_DR | bigint |  | FK | SI | Des REf Zip |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*