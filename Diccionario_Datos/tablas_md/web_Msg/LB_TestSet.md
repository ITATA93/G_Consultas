# web_Msg.LB_TestSet

**Schema:** web_Msg
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| BloodProductEmergencyIssue | varchar |  |  | SI | Flag to Indicate if test set is in emergency issue... |
| CollectionSpecimenContainers | varchar |  |  | SI | Specimen collections associated with this test set |
| DefaultCollectionAndReceive | bit |  |  | SI | Determine whether the Collection and Receive Date ... |
| DefaultCollectionCentre | bit |  |  | SI | Determine whether the Collection Center from patie... |
| DefaultCollectionForOrderItem_DR | varchar |  | FK | SI | The default specimen containers collection for ord... |
| DoNotAddNewSpecimenContainers | varchar |  |  | SI | Flag to Indicate if Test Set was pre(LBRequest) bu... |
| HTMLComments | longvarchar |  |  | SI | Temporary stream that stores the comment text unti... |
| HTMLStaffNotes | longvarchar |  |  | SI | Temporary stream that stores the staff note text u... |
| ID | varchar |  |  | NO | - |
| LBCQ_RestrictResultEntry | varchar |  |  | SI | Restrict Result Entry
Current Verification Queue ... |
| LBCQ_TestItemRestrictions | varchar |  |  | SI | Test Item Restriction
Current Verification Queue ... |
| LBCSuperset_DR | bigint |  | FK | SI | Link to the superset that triggered the test set t... |
| LBEPGTS_RowID | varchar |  |  | SI | The LBEpisodeGroupTestSet Row ID
Not committed to... |
| LBEP_ClinicalConditions | varchar |  |  | SI | Clinical Condition
A list of any clinical conditi... |
| LBRQTS_RowID | varchar |  |  | SI | - |
| LBRQTS_SpecimenContainers | varchar |  |  | SI | Specimen Container(s) from a request
This propert... |
| LBRequestDR | bigint |  | FK | SI | - |
| LBTS_Accreditations | varchar |  |  | SI | Accreditations - a list of accreditations with the... |
| LBTS_AddingMode | varchar |  |  | SI | Adding Mode |
| LBTS_AuthoriseDate | date |  |  | SI | Status of Results
Date of (last) Authorisation |
| LBTS_AuthoriseTime | time |  |  | SI | Time of (last) Authorisation |
| LBTS_AuthorisedBy_DR | bigint |  | FK | SI | User who (last) Authorised |
| LBTS_BPNumberOfUnits | integer |  |  | SI | Number of units requested
For unit (non-dose) bas... |
| LBTS_BPQuantity | numeric |  |  | SI | Quantity requested
For dose based products |
| LBTS_BPRecentTransfusionPregnancy | varchar |  |  | SI | Patient has had recent transfusion or pregnancy
F... |
| LBTS_BPRequiredByDate | date |  |  | SI | Required by date |
| LBTS_BPRequiredByTime | time |  |  | SI | Required by time |
| LBTS_BPReservationPeriod | integer |  |  | SI | Reservation period |
| LBTS_BPReservationPeriodUnit | varchar |  |  | SI | Reservation period unit |
| LBTS_BillAcknowledgeDate | date |  |  | SI | Date of (last) Billing Acknowledgement |
| LBTS_BillAcknowledgeTime | time |  |  | SI | Time of (last) Billing Acknowledgement |
| LBTS_BillAcknowledged | varchar |  |  | SI | Billing Acknowledged |
| LBTS_BillAcknowledgedBy_DR | bigint |  | FK | SI | User who (last) Billing Acknowledgement |
| LBTS_BillComplexityLevel | integer |  |  | SI | Billing Complexity Level |
| LBTS_BillTariff_DR | varchar |  | FK | SI | Billing Schedule Tariff |
| LBTS_BloodProductGroup_DR | bigint |  | FK | SI | Requested Blood Product Group |
| LBTS_BloodProduct_DR | bigint |  | FK | SI | Blood product requested |
| LBTS_CancellationBy_DR | bigint |  | FK | SI | User who Cancelled the Test Set |
| LBTS_CancellationDate | date |  |  | SI | Status of Results
Date of Cancellation |
| LBTS_CancellationTime | time |  |  | SI | Time of Cancellation |
| LBTS_ClinicalReviewFlag | bit |  |  | SI | Clinical Review Flag
can not be set via UI |
| LBTS_CollectedBy_DR | bigint |  | FK | SI | User who Collected the Test Set |
| LBTS_CollectedDate | date |  |  | SI | Date when Test Set Status was set to Collected |
| LBTS_CollectedTime | time |  |  | SI | Time when Test Set Status was set to Collected |
| LBTS_Comments_DR | bigint |  | FK | SI | Link to a websys.Document that stores the formated... |
| LBTS_Confidential | varchar |  |  | SI | Confidential
Note: This overrides LBEPConfidentia... |
| LBTS_CreatedDate | date |  |  | SI | The date the test set record was created. Set to n... |
| LBTS_CreatedTime | time |  |  | SI | The time the test set record was created. Set to n... |
| LBTS_CustomProfileApplied | bit |  |  | SI | Custom profile is applied (instead of defined regi... |
| LBTS_DeauthorisationBy_DR | bigint |  | FK | SI | User who (last) Deauthorise |
| LBTS_DeauthorisationDate | date |  |  | SI | The date the test set record was deauthorised. Set... |
| LBTS_DeauthorisationNotes | varchar |  |  | SI | Deauthorisation Notes |
| LBTS_DeauthorisationTime | time |  |  | SI | The time the test set record was deauthorised. Set... |
| LBTS_Department_DR | bigint |  | FK | SI | Department associated with the Test Set Revision. ... |
| LBTS_DiffCounter_DR | bigint |  | FK | SI | Differential Counter |
| LBTS_EnteredBy_DR | bigint |  | FK | SI | User who Entered the Test Set |
| LBTS_EnteredDate | date |  |  | SI | Date when Test Set Status was set to Entered |
| LBTS_EnteredTime | time |  |  | SI | Time when Test Set Status was set to Entered |
| LBTS_Episode_DR | bigint |  | FK | SI | LBEpisode Reference
Required by User.LBTestSet. |
| LBTS_ExcludeFromPatientMean | varchar |  |  | SI | Exclude From Patient Mean |
| LBTS_FinalDestination | varchar |  |  | SI | If there are transfers for this test set, the prop... |
| LBTS_LabSite_DR | bigint |  | FK | SI | The (initial) receiving location for the TestSet |
| LBTS_LinkTestSets | varchar |  |  | SI | Linking Test Sets
These are the slaves of this Te... |
| LBTS_MaterialLabSites | varchar |  |  | SI | The lab sites which hold materials of the test set... |
| LBTS_MaternalAddBGDisplay | varchar |  |  | SI | The displayed maternal additional blood groups at ... |
| LBTS_MaternalAntibodyDisplay | varchar |  |  | SI | The displayed maternal antibody at the time of aut... |
| LBTS_MaternalAssocDefaulted | varchar |  |  | SI | Indicate that the mother associated with the patie... |
| LBTS_MaternalBGDisplay | varchar |  |  | SI | The displayed maternal blood group at the time of ... |
| LBTS_MaternalDOB | date |  |  | SI | The displayed maternal DOB at the time of authoris... |
| LBTS_MaternalName | varchar |  |  | SI | The displayed maternal name at the time of authori... |
| LBTS_MaternalName2 | varchar |  |  | SI | The displayed maternal name2 at the time of author... |
| LBTS_MaternalSuitableSpecDisp | varchar |  |  | SI | The displayed description of the maternal suitable... |
| LBTS_MaternalSuitableSpec_DR | bigint |  | FK | SI | The maternal specimen container nominated as this ... |
| LBTS_MotherPAPerson_DR | bigint |  | FK | SI | Mother
The maternal reference necessary for neona... |
| LBTS_NeonatalCrossmatchMode | varchar |  |  | SI | Indicate whether associated blood products should ... |
| LBTS_OrdItem_DR | varchar |  | FK | SI | OrderItem Reference |
| LBTS_OrderBy_DR | bigint |  | FK | SI | User who Ordered the Test Set |
| LBTS_OrderDate | date |  |  | SI | Date when Test Set Status was set to Ordered |
| LBTS_OrderTime | time |  |  | SI | Time when Test Set Status was set to Ordered |
| LBTS_PathogensIdentified | varchar |  |  | SI | Summary of Identified organisms |
| LBTS_PaymentAgreement_DR | bigint |  | FK | SI | Payment Agreement |
| LBTS_PerformedAtRefLab_DR | bigint |  | FK | SI | Performed at (Reference Laboratory)  |
| LBTS_PreliminaryBy_DR | bigint |  | FK | SI | User who made the Test Set Preliminary |
| LBTS_PreliminaryDate | date |  |  | SI | Date when Test Set Status was set to Preliminary |
| LBTS_PreliminaryTime | time |  |  | SI | Time when Test Set Status was set to Preliminary |
| LBTS_Reagents | varchar |  |  | SI | Reagents used for this test set |
| LBTS_ReasonForDeauthorisation_DR | bigint |  | FK | SI | Reason for Deauthorisation  |
| LBTS_ReasonNotPerformed_DR | bigint |  | FK | SI | If test could not be performed this dr links a cod... |
| LBTS_ReceivedBy_DR | bigint |  | FK | SI | User who Received the Test Set |
| LBTS_ReceivedDate | date |  |  | SI | Date when Test Set Status was set to Received |
| LBTS_ReceivedTime | time |  |  | SI | Time when Test Set Status was set to Received |
| LBTS_ReferralLab_DR | bigint |  | FK | SI | Referral Lab (as when in LabTransfers) |
| LBTS_Reportable | varchar |  |  | SI | Flag to indicate if test set is reportable
Defaul... |
| LBTS_RequestTestSet_DR | bigint |  | FK | SI | Differential Counter Request Test Set DR |
| LBTS_ResultGraphPref | bigint |  |  | SI | Result Graph Preferences |
| LBTS_ReusableForOtherLocations | bit |  |  | SI | // Indicates if the specimen container can be reus... |
| LBTS_RowID | varchar |  |  | SI | - |
| LBTS_Rule3ExemptInd | varchar |  |  | SI | Rule3ExemptInd |
| LBTS_S4B3ExemptInd | varchar |  |  | SI | S3b3ExemptInd |
| LBTS_SharedResultTestSets | varchar |  |  | SI | Link to all test set of the same episode and speci... |
| LBTS_SignificantResult | varchar |  |  | SI | Significant Result |
| LBTS_SpecialHandling_DR | bigint |  | FK | SI | Special Handling Instructions |
| LBTS_SpecimenContainerAllocationByTestSetItem | varchar |  |  | SI | SpecimenContainerAllocationByTestSetItem
Flag to ... |
| LBTS_SpecimenContainers | varchar |  |  | SI | Specimen Container(s) |
| LBTS_SpecimenValidityExceeded | numeric |  |  | SI | Specimen Validity Exceeded
Set at test set author... |
| LBTS_SpecimenValidityStatus | varchar |  |  | SI | Specimen Validity Status
Set at test set authoris... |
| LBTS_StaffNotes_DR | bigint |  | FK | SI | Link to a websys.Document that stores the formated... |
| LBTS_StatusBilling | varchar |  |  | SI | Status Billing |
| LBTS_StatusResult | varchar |  |  | SI | Status of Results  (see LB.INC  $$$OrderEReceived,... |
| LBTS_SubjectOrdItem_DR | bigint |  | FK | SI | OrderItem Reference |
| LBTS_Superset_DR | bigint |  | FK | SI | Super Set |
| LBTS_TestSetItemProfile_DR | varchar |  | FK | SI | Current test set item registration profile (can be... |
| LBTS_TestSetSeq | integer |  |  | SI | Instance number of an LBCTestSetRevision within an... |
| LBTS_TestSet_DR | bigint |  | FK | SI | TestSet CodeTable Reference
Required by User.LBTe... |
| LBTS_TriggerTestSet_DR | bigint |  | FK | SI | Differential Counter Trigger Test Set DR |
| LBTS_TurnaroundTimeConfig | varchar |  |  | SI | Turnaround Time Config  |
| LBTS_TurnaroundTimeElapsed | integer |  |  | SI | Turnaround Time Elapsed |
| LBTS_TurnaroundTimeFlag | varchar |  |  | SI | Turnaround Time Flag
Standard Type=LabTestSetTurn... |
| LBTS_ValidityExtensionReason_DR | bigint |  | FK | SI | Specimen Validity Extension Reason |
| LinkingCriteriaUsed | varchar |  |  | SI | Referance to Test Set Linking row used |
| OEORI_ItmMast_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| OEORI_Priority_DR | bigint |  | FK | SI | Des Ref to OECPR |
| PAPersonDR | bigint |  | FK | SI | Temporary PAPerson reference (User.PAPerson) for t... |
| PreviousTestSets | varchar |  |  | SI | - |
| PreviousTestSetsEpisodeViewable | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| RequestTestSetMsg_DR | varchar |  | FK | SI | - |
| SessionId | varchar |  |  | SI | - |
| SpecimenContainers | varchar |  |  | SI | Specimen container message objects associated with... |
| TotalNumberOfPreviousEpisodes | integer |  |  | SI | Total number of previous episodes for cumulative v... |
| TriggerTestSetMsg_DR | varchar |  | FK | SI | - |
| UseTestSetCollectionsDefault | varchar |  |  | SI | Flag to Indicate if Order Item  will use Test Set ... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*