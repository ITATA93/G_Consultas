# web_Msg.LB_SpecimenContainer

**Schema:** web_Msg
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Muestras de Laboratorio**. Gestión de especímenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AnatomicalSiteMandatory | bit |  |  | SI | - |
| AnatomicalSiteQualifierMandatory | bit |  |  | SI | - |
| AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site  |
| Container_DR | bigint |  | FK | SI | Container |
| DefaultAliquotSelected | varchar |  |  | SI | Selected Default Aliquot |
| DisableMerge | bit |  |  | SI | Disable merge for use in Specimen Receive |
| FinanceDescription | varchar |  |  | SI | Based on finance condition and resolution.  
The ... |
| FinanceOverrideAllowed | bit |  |  | SI | Based on access profile settings, lab site and dep... |
| FinanceResolved | varchar |  |  | SI | Message class storage of financial precondition as... |
| ID | varchar |  |  | NO | - |
| LBCTestSetRevisionDefaultAliquot_DR | varchar |  | FK | SI | Link to the default aliquot |
| LBEPGSPC_RowID | varchar |  |  | SI | The LBEpisodeGroupSpecimenContainer Row ID
Not co... |
| LBRQSPC_RowID | varchar |  |  | SI | LBRequestSpecimenContainer ID used if we save to L... |
| LBRequestDR | bigint |  | FK | SI | LBRequest ID used if we save to LBRequest rather t... |
| LBSPC_AlternateNumberLabelToBePrinted | bit |  |  | SI | A flag to indicate an specimen alternate number sh... |
| LBSPC_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBSPC_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBSPC_Collected | varchar |  |  | SI | Specimen Collected |
| LBSPC_CollectedBy_DR | bigint |  | FK | SI | User Who Collected the Specimen Container  |
| LBSPC_CollectionCentre_DR | bigint |  | FK | SI | Collection Centre |
| LBSPC_CollectionDate | date |  |  | SI | Date Of Collection of the sample |
| LBSPC_CollectionSpecimenContainers | varchar |  |  | SI | List of collections that initiated the creation of... |
| LBSPC_CollectionTime | time |  |  | SI | Time Of Collection of the sample |
| LBSPC_Comments | varchar |  |  | SI | Comments |
| LBSPC_ContainerNumber | varchar |  |  | SI | Container Number (from manufacturer) |
| LBSPC_Container_DR | bigint |  | FK | SI | Container Type |
| LBSPC_CrossDepartment | bit |  |  | SI | Indicates if specimen container can be used by mul... |
| LBSPC_DepartmentIndicator | varchar |  |  | SI | Specimen Container Department Indicator
Used for ... |
| LBSPC_Disposed | bit |  |  | SI | Disposed Flag |
| LBSPC_Episode_DR | bigint |  | FK | SI | Lab Episode
Required by User.LBSpecimenContainer. |
| LBSPC_FinalDestination | varchar |  |  | SI | If there are transfers for this specimen container... |
| LBSPC_Initiation_DR | bigint |  | FK | SI | Initiation |
| LBSPC_InvalidSpecimenAuto | varchar |  |  | SI | Flag to indicate if specimen has been marked as in... |
| LBSPC_InvalidSpecimenDate | date |  |  | SI | Invalid Specimen Date |
| LBSPC_InvalidSpecimenForFuture | varchar |  |  | SI | Invalid for future flag |
| LBSPC_InvalidSpecimenInvalidForAll | varchar |  |  | SI | Invalid for all flag |
| LBSPC_InvalidSpecimenReason_DR | bigint |  | FK | SI | Reason Specimen Invalid |
| LBSPC_InvalidSpecimenReplacement_DR | bigint |  | FK | SI | Invalid Specimen Replacement Container (for single... |
| LBSPC_InvalidSpecimenReplacements | varchar |  |  | SI | Invalid Specimen Replacement Containers (for multi... |
| LBSPC_InvalidSpecimenTestSets | varchar |  |  | SI | Test Sets |
| LBSPC_InvalidSpecimenTime | time |  |  | SI | Invalid Specimen Time |
| LBSPC_InvalidSpecimenType | varchar |  |  | SI | Type of the Reason Specimen Invalid E.g. use befor... |
| LBSPC_InvalidSpecimenUser_DR | bigint |  | FK | SI | Invalid Specimen User |
| LBSPC_LabSite_DR | bigint |  | FK | SI | From site of the specimen container (can include n... |
| LBSPC_LabelToBePrinted | bit |  |  | SI | A flag to indicate the specimen number label shoul... |
| LBSPC_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBSPC_ManualSelected | varchar |  |  | SI | Flag to indicate row has been selected for manual ... |
| LBSPC_ManualSpecimenEntry | varchar |  |  | SI | Manual Specimen Entry |
| LBSPC_ReceivedBy_DR | bigint |  | FK | SI | User Who Received the Specimen Container  |
| LBSPC_ReceivedDate | date |  |  | SI | Date Of Receiving |
| LBSPC_ReceivedTime | time |  |  | SI | Time Of Receiving |
| LBSPC_ReferralLab_DR | bigint |  | FK | SI | Referral Lab where specimen container is transferr... |
| LBSPC_ReusableForOtherLocations | bit |  |  | SI | Indicates if the specimen container can be reused ... |
| LBSPC_RowID | varchar |  |  | SI | - |
| LBSPC_SourceDefaultAliquot_DR | varchar |  | FK | SI | Link to the source default aliquot |
| LBSPC_SourceMaterial_DR | varchar |  | FK | SI | Source Protocol Material used for material convers... |
| LBSPC_SourceSpecimenContainers | varchar |  |  | SI | Source Specimen Containers used for aliquots and p... |
| LBSPC_SourceType | varchar |  |  | SI | Specimen container source type
	A = Created as Al... |
| LBSPC_SpecimenNumber | varchar |  |  | SI | Specimen Number |
| LBSPC_Specimen_DR | bigint |  | FK | SI | Specimen Type |
| LBSPC_StorageDate | date |  |  | SI | Date Of Storage Change (Stored/Disposed/Not in Sto... |
| LBSPC_StorageTime | time |  |  | SI | Time Of Storage Change (Stored/Disposed/Not in Sto... |
| LBSPC_StoredBy_DR | bigint |  | FK | SI | User Who done Storage Change |
| LBSPC_SuitabilityExtensionDate | date |  |  | SI | Date the user performed the suitability extension |
| LBSPC_SuitabilityExtensionPeriod | integer |  |  | SI | The period to extend the suitability validity peri... |
| LBSPC_SuitabilityExtensionTime | time |  |  | SI | Time the user performed the suitability extension |
| LBSPC_SuitabilityExtensionUser_DR | bigint |  | FK | SI | User that performed the suitability extension |
| LBSPC_SuitabilityPeriodOverrideReason_DR | bigint |  | FK | SI | The reason for overriding the suitability extensio... |
| LBSPC_VolumeCollected | double |  |  | SI | Actual volume collected in the Container |
| LBSPC_VolumeCurrently | double |  |  | SI | Current volume remaining in the Container |
| LBSPC_VolumeNeeded | double |  |  | SI | Original volume needed |
| LBSPC_WorkAreaDateIn | date |  |  | SI | Date the specimen container was received into the ... |
| LBSPC_WorkAreaDateOut | date |  |  | SI | Date the specimen container was removed from  the ... |
| LBSPC_WorkAreaTimeIn | time |  |  | SI | Time the specimen container was received into the ... |
| LBSPC_WorkAreaTimeOut | time |  |  | SI | Time the specimen container was removed from the w... |
| LBSPC_WorkAreaUserIn_DR | bigint |  | FK | SI | Work Area User In
User that received the specimen... |
| LBSPC_WorkAreaUserOut_DR | bigint |  | FK | SI | Work Area User Out
User that removed the specimen... |
| LBSPC_WorkArea_DR | bigint |  | FK | SI | Current work area
Work area into which the specim... |
| LesionMandatory | bit |  |  | SI | - |
| Lesion_DR | bigint |  | FK | SI | Lesion |
| OrdItem_DR | varchar |  | FK | SI | Order Item
For the specimen containers created at... |
| OrderDate | date |  |  | SI | Order Date
For the specimen containers created at... |
| OrderTime | time |  |  | SI | Order Time
For the specimen containers created at... |
| ReadOnly | bit |  |  | SI | - |
| SelectedTestSets | varchar |  |  | SI | Selected Test Sets |
| SessionId | varchar |  |  | SI | - |
| Specimen_DR | bigint |  | FK | SI | Specimen  |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*