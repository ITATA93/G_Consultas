# SQLUser.SS_Profile

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSP_RowID | bigint | PK |  | NO | - |
| SSP_ACNChartDR | bigint |  | FK | SI | Active Clinical Notes Chart |
| SSP_ACNSummaryChartBookDR | bigint |  | FK | SI | ACN Summary Chart Book |
| SSP_AllocateAnyPatientType | varchar |  |  | SI | Allocate Any Patient Type |
| SSP_AllowDoseRecalculationAtPointOfAdmin | varchar |  |  | SI | Medication administration - Allow Dose Re-calculat... |
| SSP_AllowEditModeOPPlanner | varchar |  |  | SI | Allow Edit Mode for OP Planner |
| SSP_AllowEditModeOTPlanner | varchar |  |  | SI | Allow Edit Mode for OT Planner |
| SSP_AllowMergeDiscrepantTM | varchar |  |  | SI | Allow Patient Merge of Discrepant Blood Transfusio... |
| SSP_AllowedToSendForPatAndAck | varchar |  |  | SI | OT - Allowed to Send for Patient and Acknowledge |
| SSP_AllowedTransferSendForArrived | varchar |  |  | SI | OT - Allowed to Transfer Sent For/Arrived Bookings |
| SSP_BulkAdminOffsetFutureMinutes | integer |  |  | SI | Bulk Administration Default Time Configuration: Of... |
| SSP_BulkAdminOffsetPastMinutes | integer |  |  | SI | Bulk Administration Default Time Configuration: Of... |
| SSP_CPTreatmentLocList_DR | bigint |  | FK | SI | Care Provider Treatment Location List |
| SSP_CanEditClosedAss | bit |  |  | SI | Able to edit Authorised Questionnaires |
| SSP_CanEditResQues | bit |  |  | SI | Able to edit authorised Result Questionnaires |
| SSP_ClinicalSpecialty_DR | bigint |  | FK | SI | Clinical Specialty. Only applicable if the profile... |
| SSP_Code | varchar |  |  | NO | Code	 |
| SSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSP_DFLocList_DR | bigint |  | FK | SI | Departmental Functions Default Location List |
| SSP_DateFrom | date |  |  | SI | Effective date for the record |
| SSP_DateTo | date |  |  | SI | Last day the record is active  |
| SSP_DefaultEntryType_DR | bigint |  | FK | SI | Default Entry Type |
| SSP_DefaultLabHistoryView | varchar |  |  | SI | Default Lab History View  |
| SSP_Desc | varchar |  |  | NO | Description  |
| SSP_DisSumDocTp | varchar |  |  | SI | Discharge Summary Document Type - comma-separated ... |
| SSP_DisSumEPRChartBook_DR | bigint |  | FK | SI | Discharge Summary EPR ChartBook |
| SSP_DisableDigitalSigning | varchar |  |  | SI | Disable Digital Signing of Reports |
| SSP_DisplayObsComments | varchar |  |  | SI | Display Observation Comments |
| SSP_DisplayQuestInCPSum | bit |  |  | SI | Display Questionnaire in Care Plan Summary |
| SSP_EmergencyLocList_DR | bigint |  | FK | SI | Emergency Location List |
| SSP_EncounterRecordPatientSummaryChart_DR | bigint |  | FK | SI | Encounter Record Patient Summary Chart |
| SSP_EnforcePositivePacking | varchar |  |  | SI | Lab - Enforce Positive Packing |
| SSP_ExcludeNullPatientTypes | varchar |  |  | SI | Exclude null Patient Types |
| SSP_HDR_DR | bigint |  | FK | SI | Flowsheet config |
| SSP_HandoverMenuEntryType_DR | bigint |  | FK | SI | Handover Menu Entry Type |
| SSP_HealthPromLocList_DR | bigint |  | FK | SI | Health Promotion - Community |
| SSP_InPatLocList_DR | bigint |  | FK | SI | Inpatient Location List |
| SSP_InPatTransferList_DR | bigint |  | FK | SI | Inpatient Transfer Location List |
| SSP_JBGroup_DR | bigint |  | FK | SI | Des Ref to PACJourneyBoardGroup |
| SSP_LabAllowAccessStaffNote | varchar |  |  | SI | Lab - Can Access Staff Notes |
| SSP_LabAllowEnquireNonFinalResults | varchar |  |  | SI | Lab - Enquire on non-final results |
| SSP_MainChartBookDR | bigint |  | FK | SI | Main Chart Book |
| SSP_MainChartDR | bigint |  | FK | SI | Main Chart |
| SSP_MedAdminPrivileges | varchar |  |  | SI | Medication Administration Privileges |
| SSP_MortuaryAccess | varchar |  |  | SI | Has Mortuary Access |
| SSP_OnlyInpatUnitsForMyHospital | varchar |  |  | SI | Only Inpatient Units For My Hospital |
| SSP_OnlyOutpatUnitsForMyHospital | varchar |  |  | SI | Only Outpatient Units For My Hospital |
| SSP_OutPatLocList_DR | bigint |  | FK | SI | Outpatient Location List |
| SSP_Owner | varchar |  |  | SI | Owner |
| SSP_PCManageEnrollment | varchar |  |  | SI | Allow Access to HealthShare Community Patient Port... |
| SSP_PatTypeRestrictOPD | varchar |  |  | SI | Apply Patient Type Restrictions to Appointment Boo... |
| SSP_PatTypeRestrictPF | varchar |  |  | SI | Apply Patient Type Restrictions to Patient Find |
| SSP_PatTypeRestrictWL | varchar |  |  | SI | Apply Patient Type Restrictions to Waiting Lists |
| SSP_PatientSummaryChart_DR | bigint |  | FK | SI | Patient Summary Chart |
| SSP_PatientTypeInclusiveExclusive | varchar |  |  | SI | Patient Type in search - Inclusive/Exclusive  |
| SSP_PrevEpisChartDR | bigint |  | FK | SI | Previous Episode Chart |
| SSP_RadLocList_DR | bigint |  | FK | SI | Radiology Location List |
| SSP_SetupComplete | varchar |  |  | SI | OT - Setup Complete |
| SSP_TempPatLocList_DR | bigint |  | FK | SI | Temporary Location List |
| SSP_ToDoListChart_DR | bigint |  | FK | SI | To-Do List Chart |
| SSP_UDWAdminAccess | bit |  |  | SI | Has access to edit the setup of Restricted Control... |
| SSP_WLNotTriageLocList_DR | bigint |  | FK | SI | Waiting List Not Triage Location List |
| SSP_WLStatusList_DR | bigint |  | FK | SI | Waiting List Status List |
| SSP_WaitListLocList_DR | bigint |  | FK | SI | Waiting List Location List |
| SSP_WardPlaceLocList_DR | bigint |  | FK | SI | List of Wards Allowed to Place Patient Within |
| SSP_WardViewLocList_DR | bigint |  | FK | SI | List of Wards Allowed to View |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*