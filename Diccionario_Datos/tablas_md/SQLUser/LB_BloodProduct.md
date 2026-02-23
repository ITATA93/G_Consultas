# SQLUser.LB_BloodProduct

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBBP_RowID | bigint | PK |  | NO | - |
| ChildQ35DR | - |  |  | SI | Child Reference: Pulmonar |
| LBBP_AssignmentDate | date |  |  | SI | Patient Assignment Date <br />
The date that the ... |
| LBBP_AssignmentMode | varchar |  |  | SI | Patient Assignment mode |
| LBBP_AssignmentPAPerson_DR | bigint |  | FK | SI | Patient Assignment Person
The banking of red cell... |
| LBBP_AssignmentTime | time |  |  | SI | Patient Assignment Time <br />
The time that the ... |
| LBBP_BTSReferenceNumber | varchar |  |  | SI | BTS Reference Number |
| LBBP_BatchIndex | integer |  |  | SI | Batch Index |
| LBBP_BatchNumber | varchar |  |  | SI | Batch Number |
| LBBP_BloodGroup_DR | bigint |  | FK | SI | Blood Group |
| LBBP_BloodProduct_DR | bigint |  | FK | NO | Product Code |
| LBBP_CMVStatus | varchar |  |  | SI | CMV Status |
| LBBP_Comment | varchar |  |  | SI | Comment |
| LBBP_Cost | numeric |  |  | SI | Cost |
| LBBP_DispatchDate | date |  |  | SI | Dispatch Date |
| LBBP_DispatchTime | time |  |  | SI | Dispatch Time |
| LBBP_DisposalCode_DR | bigint |  | FK | SI | Disposal Code |
| LBBP_DisposalLocation_DR | bigint |  | FK | SI | Disposal Location |
| LBBP_DonationDate | date |  |  | SI | Donation Date |
| LBBP_DonationTime | time |  |  | SI | Donation Time |
| LBBP_EDNDestinationID | varchar |  |  | SI | Electronic Delivery Note Destination ID |
| LBBP_EDNOrderNumber | varchar |  |  | SI | Electronic Delivery Note Order Number |
| LBBP_EntryDate | date |  |  | SI | Entry Date |
| LBBP_EntryMode_DR | bigint |  | FK | SI | Mode of Entry |
| LBBP_EntryTime | time |  |  | SI | Entry Time |
| LBBP_ExpiryDate | date |  |  | NO | Expiry Date |
| LBBP_ExpiryTime | time |  |  | NO | Expiry Time |
| LBBP_ExpiryUpdated | varchar |  |  | SI | Expiry Time Updated |
| LBBP_FateDate | date |  |  | SI | Fate Date |
| LBBP_FateTime | time |  |  | SI | Fate Time |
| LBBP_GroupCheckCompleted | varchar |  |  | SI | Group check completed |
| LBBP_HLAFlag | varchar |  |  | SI | HLA Flag |
| LBBP_HbSStatus | varchar |  |  | SI | HbS status |
| LBBP_HepatitisE | varchar |  |  | SI | Hepatitis E |
| LBBP_HighTitreHaemolysinsStatus | varchar |  |  | SI | High Titre Haemolysins Status |
| LBBP_Irradiated | varchar |  |  | SI | Irradiated |
| LBBP_IssueDate | date |  |  | SI | Issue Date |
| LBBP_IssueTemperature | varchar |  |  | SI | Temperature on Issue |
| LBBP_IssueTime | time |  |  | SI | Issue Time |
| LBBP_LastUpdateFunction | varchar |  |  | SI | Last Update Function |
| LBBP_Manufacturer_DR | bigint |  | FK | SI | Manufacturer |
| LBBP_OrderedDate | date |  |  | SI | Ordered Date |
| LBBP_OrderedTime | time |  |  | SI | Ordered Time |
| LBBP_ProcessControl_DR | bigint |  | FK | SI | Process Control
ISBT 128 DIN Flag Type 1 and 2  |
| LBBP_Quantity | numeric |  |  | SI | Quantity |
| LBBP_Source_DR | bigint |  | FK | NO | Source |
| LBBP_Storage_DR | bigint |  | FK | SI | Storage |
| LBBP_SuitableForIssueVerified | varchar |  |  | SI | Suitable for Issue Verified on Blood Issue Compone... |
| LBBP_ThawEndDate | date |  |  | SI | Thaw End Date |
| LBBP_ThawEndTime | time |  |  | SI | Thaw End Time |
| LBBP_ThawStartDate | date |  |  | SI | Thaw Start Date |
| LBBP_ThawStartTime | time |  |  | SI | Thaw Start Time |
| LBBP_TransferCode_DR | bigint |  | FK | SI | Transfer Reason |
| LBBP_TransferHospital_DR | bigint |  | FK | SI | Transfer Hospital |
| LBBP_TransferLocation_DR | bigint |  | FK | SI | Transfer Location in the hospital |
| LBBP_TransportMode_DR | bigint |  | FK | SI | Mode of Transport |
| LBBP_UOM_DR | bigint |  | FK | SI | Unit of Measure |
| LBBP_UnitFate_DR | bigint |  | FK | SI | Unit Fate
Only set if unit status = fated |
| LBBP_UnitNumber | varchar |  |  | NO | Unit / Donation Number |
| LBBP_UnitStatus_DR | bigint |  | FK | SI | Unit Status |
| LBBP_UpdatedExpiryDate | date |  |  | SI | Updated Expiry Date |
| LBBP_UpdatedExpiryTime | time |  |  | SI | UpdatedExpiry Time |
| LBBP_UserCollectingUnit | varchar |  |  | SI | User Collecting Unit For Issue |
| Q82Q1 | - |  |  | SI | Hallazgo |
| Q82Q2 | - |  |  | SI | Ubicación |
| Q82Q3 | - |  |  | SI | Sensibilidad |
| Q82Q4 | - |  |  | SI | Descripción |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*