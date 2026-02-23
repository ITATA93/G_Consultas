# SQLUser.LB_EpisodeEvent

**Schema:** SQLUser
**Columnas:** 159
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEPE_RowID | bigint | PK |  | NO | - |
| LBEPETS_MaternalAddBGDisplay | varchar |  |  | SI | The displayed maternal additional blood groups at ... |
| LBEPETS_MaternalAntibodyDisplay | varchar |  |  | SI | The displayed maternal antibody at the time of aut... |
| LBEPETS_MaternalBGDisplay | varchar |  |  | SI | The displayed maternal blood group at the time of ... |
| LBEPETS_MaternalSuitableSpecDisp | varchar |  |  | SI | The displayed description of the maternal suitable... |
| LBEPETS_MaternalSuitableSpec_DR | bigint |  | FK | SI | The maternal specimen container nominated as this ... |
| LBEPE_AcknowledgedBy_DR | bigint |  | FK | SI | Acknowledged By User for transfer logistics |
| LBEPE_ActivatedTestItemValues | varchar |  |  | SI | List of Activated Test Item values |
| LBEPE_ActivatedTestItems | varchar |  |  | SI | Activated Test Items in Test Set |
| LBEPE_Age | double |  |  | SI | Age |
| LBEPE_AntibioticChangeDetails | varchar |  |  | SI | Antibiotic Changes  |
| LBEPE_AttachToEPR | bit |  |  | SI | Attachment Attached to EPR |
| LBEPE_AttachmentComments | varchar |  |  | SI | Attachment Comment |
| LBEPE_AttachmentFileName | varchar |  |  | SI | Attachment File Name |
| LBEPE_BatchType | varchar |  |  | SI | Batch Type - Report Generation Method |
| LBEPE_BloodProducts | varchar |  |  | SI | The blood products |
| LBEPE_Changes | varchar |  |  | SI | A list of the changes represented by a single audi... |
| LBEPE_Clinic_DR | bigint |  | FK | SI | Clinic for Referring Doctor for the report |
| LBEPE_Comments | varchar |  |  | SI | Free text comments |
| LBEPE_Confidential | varchar |  |  | SI | Confidential |
| LBEPE_CurrentObservation | varchar |  |  | SI | LBCObservation Current Reference |
| LBEPE_CurrentTestSetItem | varchar |  |  | SI | Test Set Item Current Reference |
| LBEPE_CustomProfile | bit |  |  | SI | Custom Test Set Profile in use |
| LBEPE_DOB | date |  |  | SI | Date of Birth (as known at Time of Collection) |
| LBEPE_DRBatchID | varchar |  |  | SI | Doctors Report Batch ID (not a database reference ... |
| LBEPE_Date | date |  |  | SI | Date of the event |
| LBEPE_DeactivatedTestItemValues | varchar |  |  | SI | List of Deactivated Test Item values |
| LBEPE_DeactivatedTestItems | varchar |  |  | SI | Deactivated Test Items in Test Set |
| LBEPE_DecisionSupportEvent_DR | bigint |  | FK | SI | List of New Report Recipient Types |
| LBEPE_DecisionSupportEvents | varchar |  |  | SI | List of DSS event IDs in event |
| LBEPE_EpisodeAttachment_DR | varchar |  | FK | SI | Attachment for Lab Episode |
| LBEPE_Episode_DR | bigint |  | FK | NO | Lab Episode |
| LBEPE_ErrorMessage | varchar |  |  | SI | Error Message from Printing Production |
| LBEPE_EstDOB | varchar |  |  | SI | Estimated Date of Birth (as known at Time of Colle... |
| LBEPE_ExternalLinkComment | varchar |  |  | SI | External Link Comment |
| LBEPE_ExternalLinkTitle | varchar |  |  | SI | External Link Title |
| LBEPE_ExternalLinkURL | varchar |  |  | SI | External Link URL |
| LBEPE_ExternalLink_DR | bigint |  | FK | SI | External Link |
| LBEPE_FirstName | varchar |  |  | SI | Patient Firstname (as known at Time of Collection) |
| LBEPE_FromWorkArea_DR | bigint |  | FK | SI | Destination Work Area |
| LBEPE_Group_DR | bigint |  | FK | SI | Security Group |
| LBEPE_IndigStatDesc | varchar |  |  | SI | Ethnicity Description |
| LBEPE_IndigStat_DR | bigint |  | FK | SI | Ethnicity |
| LBEPE_InstrumentDetails | varchar |  |  | SI | Instrument results |
| LBEPE_InstrumentSchProcedures | varchar |  |  | SI | Instrument Schedule Procedures  |
| LBEPE_InstrumentSchTestItems | varchar |  |  | SI | Instrument Schedule Test Items  |
| LBEPE_InstrumentScheduleStatus | varchar |  |  | SI | Instrument Schedule Status |
| LBEPE_InstrumentSchedule_DR | bigint |  | FK | SI | Instrument Schedule |
| LBEPE_Instrument_DR | bigint |  | FK | SI | Instrument the results arrived from |
| LBEPE_InterpretationReportable | varchar |  |  | SI | Test Set Item Interpretation Reportable |
| LBEPE_LBCTestSets | varchar |  |  | SI | List of LBCTestSets in event |
| LBEPE_LabProtocolDesc | varchar |  |  | SI | Lab Protocol Description |
| LBEPE_LabSiteFrom_DR | bigint |  | FK | SI | From Lab Site |
| LBEPE_LabSiteTo_DR | bigint |  | FK | SI | To Lab Site |
| LBEPE_LinkedLBCTestSets | varchar |  |  | SI | List of Linked LBCTestSets in event |
| LBEPE_LinkedTestSets | varchar |  |  | SI | List of Linked Test Sets |
| LBEPE_MRN | varchar |  |  | SI | MRN (in use at Time of Collection) |
| LBEPE_ModifiedComments_DR | bigint |  | FK | SI | Modified Document  |
| LBEPE_NewContainer | varchar |  |  | SI | New Container |
| LBEPE_NewSpcAnatomSite | varchar |  |  | SI | New Anatomical Site |
| LBEPE_NewSpcAnatomSiteQualifier | varchar |  |  | SI | New Anatomical Site Qualifier |
| LBEPE_NewSpcLesion | varchar |  |  | SI | New Lesion |
| LBEPE_NewSpecimen | varchar |  |  | SI | New Specimen |
| LBEPE_NewSpecimenContainerComments | varchar |  |  | SI | List of New Comments for Specimen Container |
| LBEPE_NewTSSpecialHandlings | varchar |  |  | SI | List of New Special Handlings for Test Set |
| LBEPE_OLDComments | varchar |  |  | SI | Free text comments |
| LBEPE_OldContainer | varchar |  |  | SI | Old Container |
| LBEPE_OldSpcAnatomSite | varchar |  |  | SI | Old Anatomical Site |
| LBEPE_OldSpcAnatomSiteQualifier | varchar |  |  | SI | Old Anatomical Site Qualifier |
| LBEPE_OldSpcLesion | varchar |  |  | SI | Old Lesion |
| LBEPE_OldSpecimen | varchar |  |  | SI | Old Specimen |
| LBEPE_OldSpecimenContainerComments | varchar |  |  | SI | List of Old Comments for Specimen Container |
| LBEPE_OldSpecimenNumber | varchar |  |  | SI | Old Specimen Number |
| LBEPE_OldTSSpecialHandlings | varchar |  |  | SI | List of Old Special Handlings for Test Set |
| LBEPE_OriginalComments_DR | bigint |  | FK | SI | Original Document  |
| LBEPE_OriginalLabSiteTo_DR | bigint |  | FK | SI | The Original To Lab Site before Transfer destinati... |
| LBEPE_OriginalReferralLab_DR | bigint |  | FK | SI | The Original Referral Lab before Transfer destinat... |
| LBEPE_OverrideFreeText | varchar |  |  | SI | User-entered Override Free Text |
| LBEPE_OverrideReason_DR | bigint |  | FK | SI | Override Reason |
| LBEPE_OverrideText | varchar |  |  | SI | Override Text |
| LBEPE_PAPERID | varchar |  |  | SI | National ID 
NHS Number in UK |
| LBEPE_PatTypeDesc | varchar |  |  | SI | Patient Type Description |
| LBEPE_PatType_DR | bigint |  | FK | SI | Patient Type |
| LBEPE_PhoneNumber | varchar |  |  | SI | Phone number for the phone log |
| LBEPE_PreviousObservation | varchar |  |  | SI | LBCObservation Previous Reference |
| LBEPE_PreviousTestSetItem | varchar |  |  | SI | Test Set Item Previous Reference |
| LBEPE_ProtocolMaterial_DR | varchar |  | FK | SI | Protocol Material |
| LBEPE_ProtocolMaterials | varchar |  |  | SI | List of ProtocolMaterials in event |
| LBEPE_ProtocolObservation_DR | varchar |  | FK | SI | Protocol Observation |
| LBEPE_ProtocolProcedure_DR | varchar |  | FK | SI | Protocol Procedure |
| LBEPE_Protocol_DR | bigint |  | FK | SI | Lab Protocol |
| LBEPE_Queue_DR | bigint |  | FK | SI | Lab Queue |
| LBEPE_ReasonNotPerformed_DR | bigint |  | FK | SI | Reason not be performed |
| LBEPE_RecepientType | varchar |  |  | SI | The type of recipient for the report
If LBEPEReci... |
| LBEPE_RecipientID | varchar |  |  | SI | The Recipient (ID of User.CTCareProv, User.CTLoc, ... |
| LBEPE_ReferralLab_DR | bigint |  | FK | SI | Referral Lab where specime container is transfered |
| LBEPE_Report | varchar |  |  | SI | Report used for printing |
| LBEPE_ReportClasses | varchar |  |  | SI | Report Classes |
| LBEPE_ReportMode | varchar |  |  | SI | Report Mode (e.g., Printed, Electronic, SMS) |
| LBEPE_ReportPages | varchar |  |  | SI | Report Pages |
| LBEPE_ReportType | varchar |  |  | SI | Report Type (e.g., Finals Only, Interim, Prelimina... |
| LBEPE_RequestEvent_DR | bigint |  | FK | SI | Reference to LBRequestEvent that was used to popul... |
| LBEPE_ReservationPeriod | varchar |  |  | SI | New Blood Unit Reservation Period |
| LBEPE_ReservationPeriodUnit | varchar |  |  | SI | New Blood Unit Reservation Period Unit |
| LBEPE_ResultChangeDetails | varchar |  |  | SI | Change of Results
1 Previous Code
2 Previous Des... |
| LBEPE_SNOMEDData | varchar |  |  | SI | A list of the SNOMED Snap shot |
| LBEPE_SexDesc | varchar |  |  | SI | Sex (as known at Time of Collection) Description |
| LBEPE_Sex_DR | bigint |  | FK | SI | Sex (as known at Time of Collection) |
| LBEPE_ShipmentContainerNumber | varchar |  |  | SI | Shipment Container Number |
| LBEPE_SpeciesDesc | varchar |  |  | SI | Species Description |
| LBEPE_Species_DR | bigint |  | FK | SI | Species |
| LBEPE_SpecimenCollectDate | date |  |  | SI | Test set item date collected |
| LBEPE_SpecimenCollectTime | time |  |  | SI | Test set item time collected |
| LBEPE_SpecimenContainerDateTimes | varchar |  |  | SI | Specimen Container Date Time List |
| LBEPE_SpecimenContainerDetails | varchar |  |  | SI | Specimen Detail List |
| LBEPE_SpecimenContainerNewVolume | varchar |  |  | SI | Specimen Container New Volume |
| LBEPE_SpecimenContainerOldVolume | varchar |  |  | SI | Specimen Container Old Volume |
| LBEPE_SpecimenContainers | varchar |  |  | SI | List of SpecimenContainer in event |
| LBEPE_StorageContainer_DR | bigint |  | FK | SI | Storage Container |
| LBEPE_StorageDetails | varchar |  |  | SI | Storage Details as at the time of insert
1  Stora... |
| LBEPE_Surname | varchar |  |  | SI | Patient Surname (as known at Time of Collection) |
| LBEPE_TSMotherDOB | date |  |  | SI | The DOB of the mother |
| LBEPE_TSMotherFirstName | varchar |  |  | SI | The First Name of the mother |
| LBEPE_TSMotherPAPerson_DR | bigint |  | FK | SI | The person object of the mother |
| LBEPE_TSMotherSurname | varchar |  |  | SI | The Surname of the mother |
| LBEPE_TSMotherURN | varchar |  |  | SI | The URN of the mother |
| LBEPE_TestItem_DR | bigint |  | FK | SI | Test Item that has result changed |
| LBEPE_TestSetAttachment_DR | varchar |  | FK | SI | Attachment for Test Set |
| LBEPE_TestSetAuthorisedBy_DR | bigint |  | FK | SI | Authorise user of the test set |
| LBEPE_TestSetDeAuthorisedBy_DR | bigint |  | FK | SI | De-Authorise user of the test set |
| LBEPE_TestSetDeAuthorisedNotes | varchar |  |  | SI | De-Authorise Notes of the test set |
| LBEPE_TestSetItemBillable | varchar |  |  | SI | Test Set Item Billable |
| LBEPE_TestSetItemDatePerformed | date |  |  | SI | Test set item date performed |
| LBEPE_TestSetItemEnteredDate | date |  |  | SI | Test set item date entered |
| LBEPE_TestSetItemEnteredTime | time |  |  | SI | Test set item time entered |
| LBEPE_TestSetItemReportable | varchar |  |  | SI | Test Set Item Reportable |
| LBEPE_TestSetItemResult | varchar |  |  | SI | LBTestSetItemResult  
needed as we use same test ... |
| LBEPE_TestSetItemTimePerformed | time |  |  | SI | Test set item time performed |
| LBEPE_TestSetItemValidTilDate | date |  |  | SI | Test set item date valid until |
| LBEPE_TestSetItemValidTilTime | time |  |  | SI | Test set item time valid unti |
| LBEPE_TestSetItem_DR | varchar |  | FK | SI | Link to the test set item (for indexing) |
| LBEPE_TestSetProfileID | varchar |  |  | SI | Test Set Profile  |
| LBEPE_TestSetResultStatus | varchar |  |  | SI | New Test Set Status |
| LBEPE_TestSets | varchar |  |  | SI | List of affected Test Sets |
| LBEPE_Time | time |  |  | SI | Time of the event |
| LBEPE_ToWorkArea_DR | bigint |  | FK | SI | Origin Work Area |
| LBEPE_TransferAutomaticSendAway | varchar |  |  | SI | Transfer is an automatic send away |
| LBEPE_TransferDestinationChangeReason_DR | bigint |  | FK | SI | Record the reason why a transfer would have their ... |
| LBEPE_Type_DR | bigint |  | FK | SI | Type of the event  |
| LBEPE_User_DR | bigint |  | FK | SI | User |
| LBEPE_ValidityExtensionReason_DR | bigint |  | FK | SI | Specimen Validity Extension Reason |
| LBEPE_Worksheet_DR | bigint |  | FK | SI | Affected Worksheet |
| LBEPR_ActionCode_DR | bigint |  | FK | SI | Action Code |
| Q224Q1 | - |  |  | SI | Hallazgo |
| Q224Q2 | - |  |  | SI | Ubicación |
| Q224Q3 | - |  |  | SI | Sensibilidad |
| Q224Q4 | - |  |  | SI | Descripción |
| Q224Q5 | - |  |  | SI | Ispección Texto |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*