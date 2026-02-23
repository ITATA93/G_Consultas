# web_Msg.LB_BloodProductList

**Schema:** web_Msg
**Columnas:** 41
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AssignmentExpired | varchar |  |  | SI | Flag to search for products that are beyond the as... |
| AssignmentModeList | varchar |  |  | SI | A list of Assignment Modes to find |
| DereservationDate | date |  |  | SI | Dereservation Date |
| DereservationTime | time |  |  | SI | Dereservation Time |
| ExpiryDateFrom | date |  |  | SI | - |
| ExpiryDateTo | date |  |  | SI | - |
| FateCode | bigint |  |  | SI | - |
| FatedDateFrom | date |  |  | SI | Fated Date From |
| FatedDateTo | date |  |  | SI | Fated Date To |
| FatedTimeFrom | time |  |  | SI | Fated Time From |
| FatedTimeTo | time |  |  | SI | Fated Time To |
| ID | varchar |  |  | NO | - |
| InCirculation | varchar |  |  | SI | - |
| Irradiated | varchar |  |  | SI | Irradiated Status |
| LBBPAssignmentModeSearch | varchar |  |  | SI | Patient Assignment mode |
| LBBPBTSReferenceNumber | varchar |  |  | SI | BTS Reference Number |
| LBBPBatchNumber | varchar |  |  | SI | - |
| LBBPBloodGroupDR | bigint |  | FK | SI | - |
| LBBPBloodProductDR | bigint |  | FK | SI | - |
| LBBPBloodProductGroupDR | bigint |  | FK | SI | - |
| LBBPCMVStatus | varchar |  |  | SI | - |
| LBBPDisposalCodeDR | bigint |  | FK | SI | - |
| LBBPEDNOrderNumber | varchar |  |  | SI | Electronic Delivery Note Order Number |
| LBBPManufacturerDR | bigint |  | FK | SI | - |
| LBBPSourceDR | bigint |  | FK | SI | - |
| LBBPStorageDR | bigint |  | FK | SI | - |
| LBBPUnitNumber | varchar |  |  | SI | - |
| LBBPUnitStatus | bigint |  |  | SI | - |
| LBCSTStorageGroupDR | bigint |  | FK | SI | Storage Group |
| LabSite | bigint |  |  | SI | - |
| NullNotTestedAntigens | varchar |  |  | SI | Include Null / Not-Tested Antigens |
| OnlyNonAcknowledged | varchar |  |  | SI | Used for Product Acknowledgement 
only return blo... |
| ReadOnly | bit |  |  | SI | - |
| ReceivedDateFrom | date |  |  | SI | - |
| ReceivedDateTo | date |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| hiddenLBBPUnitStatusList | varchar |  |  | SI | - |
| hiddenNegativeAntigenList | varchar |  |  | SI | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*