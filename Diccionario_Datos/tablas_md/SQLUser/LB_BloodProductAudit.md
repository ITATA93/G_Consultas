# SQLUser.LB_BloodProductAudit

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBBPAU_ParRef | bigint | PK |  | NO | Parent Blood Product |
| ChildQ45DR | - |  |  | SI | Child Reference: Extremidades |
| LBBPAU_Action | varchar |  |  | SI | Action |
| LBBPAU_AntigenReactions | varchar |  |  | SI | Antigen reactions
Antigens and antigen reactions ... |
| LBBPAU_Antigens | varchar |  |  | SI | Antigens |
| LBBPAU_AssignmentDOB | date |  |  | SI | Assigned Patient Date of Birth |
| LBBPAU_AssignmentDate | date |  |  | SI | Patient Assignment Date |
| LBBPAU_AssignmentFirstName | varchar |  |  | SI | Assigned Patient Firstname |
| LBBPAU_AssignmentMode | varchar |  |  | SI | Patient Assignment mode |
| LBBPAU_AssignmentPAPerson_DR | bigint |  | FK | SI | Patient Assignment Person
The banking of red cell... |
| LBBPAU_AssignmentRegistrationNo | varchar |  |  | SI | Assigned Patient Registration No (URN) |
| LBBPAU_AssignmentSurname | varchar |  |  | SI | Assigned Patient Surname |
| LBBPAU_AssignmentTime | time |  |  | SI | Patient Assignment Time |
| LBBPAU_AuthoriseDate | date |  |  | SI | Date of Authorisation |
| LBBPAU_AuthoriseTime | time |  |  | SI | Time of Authorisation |
| LBBPAU_BTSReferenceNumber | varchar |  |  | SI | BTS Reference Number |
| LBBPAU_BatchIndex | integer |  |  | SI | Batch Index |
| LBBPAU_BatchNumber | varchar |  |  | SI | Batch Number |
| LBBPAU_BloodGroup_DR | bigint |  | FK | SI | Blood Group |
| LBBPAU_BloodProduct_DR | bigint |  | FK | SI | Blood Product |
| LBBPAU_CMVStatus | varchar |  |  | SI | CMV Status |
| LBBPAU_Changes | varchar |  |  | SI | - |
| LBBPAU_Comment | varchar |  |  | SI | Comment |
| LBBPAU_Compatibility | varchar |  |  | SI | Compatibility |
| LBBPAU_Cost | numeric |  |  | SI | Cost |
| LBBPAU_DOB | date |  |  | SI | Date of Birth |
| LBBPAU_Date | date |  |  | NO | Date of the Audit Event |
| LBBPAU_DispatchDate | date |  |  | SI | Dispatch Date |
| LBBPAU_DispatchTime | time |  |  | SI | Dispatch Time |
| LBBPAU_DisposalCode_DR | bigint |  | FK | SI | Disposal Code |
| LBBPAU_DisposalLocation_DR | bigint |  | FK | SI | Disposal Location |
| LBBPAU_DonationDate | date |  |  | SI | Donation Date |
| LBBPAU_DonationTime | time |  |  | SI | Donation Time |
| LBBPAU_EDNOrderNumber | varchar |  |  | SI | Electronic Delivery Note Order Number |
| LBBPAU_EntryDate | date |  |  | SI | Date of Entry |
| LBBPAU_EntryMode_DR | bigint |  | FK | SI | Mode of Entry |
| LBBPAU_EntryTime | time |  |  | SI | Time of Entry |
| LBBPAU_EpisodeNumber | varchar |  |  | SI | Lab Episode Number  |
| LBBPAU_Episode_DR | bigint |  | FK | SI | LBEpisode Reference |
| LBBPAU_ExpiryDate | date |  |  | SI | Date of Expiry |
| LBBPAU_ExpiryTime | time |  |  | SI | Time of Expiry |
| LBBPAU_FateDate | date |  |  | SI | Date of Fate |
| LBBPAU_FateTime | time |  |  | SI | Time of Fate |
| LBBPAU_FirstName | varchar |  |  | SI | Patient Firstname |
| LBBPAU_GroupCheckBloodGroup_DR | bigint |  | FK | SI | Unit Group Check Blood group |
| LBBPAU_HLAFlag | varchar |  |  | SI | HLA Flag |
| LBBPAU_HbSStatus | varchar |  |  | SI | HbS status |
| LBBPAU_HepatitisE | varchar |  |  | SI | Hepatitis E |
| LBBPAU_HighTitreHaemolysinsPresent | varchar |  |  | SI | High Titre Haemolysins Present (deprecated propert... |
| LBBPAU_HighTitreHaemolysinsStatus | varchar |  |  | SI | High Titre Haemolysins Status |
| LBBPAU_Irradiated | varchar |  |  | SI | Irradiated |
| LBBPAU_IssueDate | date |  |  | SI | Issue Date |
| LBBPAU_IssueTemperature | varchar |  |  | SI | Temperature on Issue |
| LBBPAU_IssueTime | time |  |  | SI | Issue Time |
| LBBPAU_LastUpdateFunction | varchar |  |  | SI | Last Update Function |
| LBBPAU_MRN | varchar |  |  | SI | MRN |
| LBBPAU_Manufacturer_DR | bigint |  | FK | SI | Manufacturer |
| LBBPAU_OrderedDate | date |  |  | SI | Ordered Date |
| LBBPAU_OrderedTime | time |  |  | SI | Ordered Time |
| LBBPAU_PAPERID | varchar |  |  | SI | National ID
NHS Number in UK |
| LBBPAU_Quantity | numeric |  |  | SI | Quantity |
| LBBPAU_RegistrationNumber | varchar |  |  | SI | Registration Number |
| LBBPAU_RequiredByDate | date |  |  | SI | Required by date |
| LBBPAU_RequiredByTime | time |  |  | SI | Required by time |
| LBBPAU_ReservationPeriod | integer |  |  | SI | Reservation period |
| LBBPAU_ReservationPeriodUnit | varchar |  |  | SI | Reservation period unit |
| LBBPAU_RowID | varchar |  |  | NO | - |
| LBBPAU_Sex_DR | bigint |  | FK | SI | Sex |
| LBBPAU_Source_DR | bigint |  | FK | SI | Source |
| LBBPAU_StorageOld_DR | bigint |  | FK | SI | Storage Old |
| LBBPAU_Storage_DR | bigint |  | FK | SI | Storage |
| LBBPAU_Suitability | varchar |  |  | SI | Suitability |
| LBBPAU_SuitableForIssueVerified | varchar |  |  | SI | Suitable for Issue Verified on Blood Issue Compone... |
| LBBPAU_Surname | varchar |  |  | SI | Patient Surname |
| LBBPAU_TestSet_DR | bigint |  | FK | SI | Test Set  |
| LBBPAU_ThawEndDate | date |  |  | SI | Thaw End Date |
| LBBPAU_ThawEndTime | time |  |  | SI | Thaw End Time |
| LBBPAU_ThawStartDate | date |  |  | SI | Thaw Start Date |
| LBBPAU_ThawStartTime | time |  |  | SI | Thaw Start Time |
| LBBPAU_Time | time |  |  | NO | Time of the Audit Event |
| LBBPAU_TransferCode_DR | bigint |  | FK | SI | Transfer Reason |
| LBBPAU_TransferHospital_DR | bigint |  | FK | SI | Transfer Hospital |
| LBBPAU_TransferLocation_DR | bigint |  | FK | SI | Transfer Location in the Hospital |
| LBBPAU_TransportMode_DR | bigint |  | FK | SI | Mode of Transport |
| LBBPAU_Type | varchar |  |  | NO | Type of the Audit Event |
| LBBPAU_UOM_DR | bigint |  | FK | SI | Unit of Measure |
| LBBPAU_UnitFate_DR | bigint |  | FK | SI | Unit Fate |
| LBBPAU_UnitNumber | varchar |  |  | SI | Unit Number |
| LBBPAU_UnitStatus_DR | bigint |  | FK | SI | Unit Status |
| LBBPAU_UpdatedExpiryDate | date |  |  | SI | [DEPRECATED]Unnecessary Property[/DEPRECATED] Upda... |
| LBBPAU_UpdatedExpiryTime | time |  |  | SI | [DEPRECATED]Unnecessary Property[/DEPRECATED] Upda... |
| LBBPAU_UserCollectingUnit | varchar |  |  | SI | User Collecting Unit For Issue |
| LBBPAU_User_DR | bigint |  | FK | SI | User |
| Q39Q1 | - |  |  | SI | Palpación |
| Q39Q2 | - |  |  | SI | Percusión |
| Q39Q3 | - |  |  | SI | Auscultación |
| Q39Q4 | - |  |  | SI | Localización |
| Q39Q5 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*