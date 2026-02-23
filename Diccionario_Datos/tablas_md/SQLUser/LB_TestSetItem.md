# SQLUser.LB_TestSetItem

**Schema:** SQLUser
**Columnas:** 146
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTSI_ParRef | bigint | PK |  | NO | Parent TestSet DR |
| LBTSI_Accreditations | varchar |  |  | SI | Accreditations - a list of accreditations with the... |
| LBTSI_AdditionalBloodGroup_DR | bigint |  | FK | SI | Reference to the additional blood group result |
| LBTSI_Antibody_DR | bigint |  | FK | SI | Reference to the antibody result |
| LBTSI_Antigen_DR | bigint |  | FK | SI | Reference to the antigen result |
| LBTSI_AuthoriseDate | date |  |  | SI | Date the result was las authorised |
| LBTSI_AuthoriseTime | time |  |  | SI | Time the result was last authorised |
| LBTSI_AuthorisedBy_DR | bigint |  | FK | SI | User who (last) Authorised |
| LBTSI_AutoCommentsExecuted | varchar |  |  | SI | Stores Rules executed |
| LBTSI_Billable | varchar |  |  | SI | Test Set Item is Billable/Non-Billable.
This prop... |
| LBTSI_BloodGroup_DR | bigint |  | FK | SI | Reference to the blood group result |
| LBTSI_ClinicalReviewFlag | bit |  |  | SI | Clinical Review Flag
can not be set via UI |
| LBTSI_CodedResultList | varchar |  |  | SI | Coded Result value list for Coded Result Multiple ... |
| LBTSI_CodedResult_DR | bigint |  | FK | SI | Stores a coded result referenence  |
| LBTSI_Comments_DR | bigint |  | FK | SI | Link to a websys.Document that stores the formated... |
| LBTSI_Date | date |  |  | SI | Date result, comment, reportable or status was las... |
| LBTSI_DeltaCheckIndicator | varchar |  |  | SI | Delta Check Indicator |
| LBTSI_Diluted | varchar |  |  | SI | Flag that indicates that the sample the test was p... |
| LBTSI_DilutionFactor | numeric |  |  | SI | Dilution factor of the sample the test was perform... |
| LBTSI_EnteredDate | date |  |  | SI | Date the result was entered |
| LBTSI_EnteredTime | time |  |  | SI | Time the result was entered |
| LBTSI_EnteredUser_DR | bigint |  | FK | SI | User who entered the result |
| LBTSI_ExcludeFromPatientMean | varchar |  |  | SI | Exclude From Patient Mean |
| LBTSI_Hidden | varchar |  |  | SI | Hide Result - Used on Test Set Internal Profiles t... |
| LBTSI_InstrumentFlags | varchar |  |  | SI | Translated Instrument flags transmitted for this r... |
| LBTSI_InstrumentPerformedDate | date |  |  | SI | Date the test on the instrument was performed - DE... |
| LBTSI_InstrumentPerformedTime | time |  |  | SI | Time the test on the instrument was performed - DE... |
| LBTSI_Instrument_DR | bigint |  | FK | SI | Intrument the test item result was received from |
| LBTSI_InterpretationReportable | varchar |  |  | SI | Clinical Interpretation is Reportable/Non-Reportab... |
| LBTSI_InterpretationSourceType | varchar |  |  | SI | Interpretation Source |
| LBTSI_InterpretationText_DR | bigint |  | FK | SI | Link to a websys.Document that stores the formated... |
| LBTSI_Interpretation_DR | bigint |  | FK | SI | Clinical Interpretation
Only stores the first ran... |
| LBTSI_ManualInstrumentSchedule | varchar |  |  | SI | Manual Instrument Schedule
Do not schedule this t... |
| LBTSI_NotPerformed | varchar |  |  | SI | Test Set Item Not Performed
Default: N, can be se... |
| LBTSI_NotPerformedDate | date |  |  | SI | - |
| LBTSI_NotPerformedTime | time |  |  | SI | - |
| LBTSI_NotPerformedUser | bigint |  |  | SI | - |
| LBTSI_OriginalInstrumentFlags | varchar |  |  | SI | Original Instrument flags transmitted for this res... |
| LBTSI_PathGroupPathRule_DR | varchar |  | FK | SI | Pathogen Group Pathogenicity Rule |
| LBTSI_PathogenAssignAntibioticPanel | varchar |  |  | SI | Apply Antibiotic Rules |
| LBTSI_PathogenConfirmed | varchar |  |  | SI | Pathogen is Confirmed/Interim |
| LBTSI_PathogenDuplicate | varchar |  |  | SI | Pathogen is Duplicate/Original |
| LBTSI_PathogenGrowthQualifierCode | varchar |  |  | SI | Growth Qualifier Code of Pathogen 
Growth Qualifi... |
| LBTSI_PathogenGrowthQualifierDesc | varchar |  |  | SI | Growth Qualifier Description of Pathogen 
Growth ... |
| LBTSI_PathogenGrowthQualifier_DR | bigint |  | FK | SI | Growth Qualifier of Pathogen |
| LBTSI_PathogenPathogenicityRule_DR | varchar |  | FK | SI | Pathogen Pathogenicity Rule |
| LBTSI_PathogenSequence | numeric |  |  | SI | Pathogen sequence |
| LBTSI_PathogenSignificant | varchar |  |  | SI | Pathogen is Significant/Normal. |
| LBTSI_PathogenSubTypeCode | varchar |  |  | SI | Sub Type Code of Pathogen 
Sub Type code as of au... |
| LBTSI_PathogenSubTypeDesc | varchar |  |  | SI | Sub Type Description of Pathogen 
Sub Type descri... |
| LBTSI_PathogenSubTypeGroupCode | varchar |  |  | SI | Sub Type Group Code of Pathogen 
Sub Type Group c... |
| LBTSI_PathogenSubTypeGroupDesc | varchar |  |  | SI | Sub Type Group Description of Pathogen 
Sub Type ... |
| LBTSI_PathogenSubTypeGroup_DR | bigint |  | FK | SI | Sub Type Group of Pathogen |
| LBTSI_PathogenSubType_DR | varchar |  | FK | SI | Sub Type of Pathogen |
| LBTSI_PathogenType | varchar |  |  | SI | Pathogen type |
| LBTSI_Pathogen_DR | bigint |  | FK | SI | Test Set Item is a Micro Pathogen.  The reference ... |
| LBTSI_PerformedAtLabSite_DR | bigint |  | FK | SI | Lab Site the result was entered or performed |
| LBTSI_PerformedDate | date |  |  | SI | Date the test on the instrument was performed |
| LBTSI_PerformedTime | time |  |  | SI | Time the test on the instrument was performed |
| LBTSI_PlannedSpecimenContainers | varchar |  |  | SI | Original specimen container plan
Do not modify af... |
| LBTSI_ProfileOmitted | varchar |  |  | SI | Flag to indicate if the test set item is active
U... |
| LBTSI_Reaction_DR | bigint |  | FK | SI | Reference to the reaction result |
| LBTSI_ReadOnly | varchar |  |  | SI | Read Only - Used on Test Set Internal Profiles to ... |
| LBTSI_RepeatNumber | numeric |  |  | SI | Repeat number
At the moment only set for results ... |
| LBTSI_Reportable | varchar |  |  | SI | Test Set Item is Reportable/Non-Reportable.
This ... |
| LBTSI_Required | varchar |  |  | SI | Test Set Item is Required/Non-Required.
Overrides... |
| LBTSI_ResultAbnormalFlag | varchar |  |  | SI | Calculated abnormal (external) flag for the result... |
| LBTSI_ResultClassName | varchar |  |  | SI | In case the result is coded this property stores t... |
| LBTSI_ResultCode | varchar |  |  | SI | Result Code 
Stores code for coded result as of a... |
| LBTSI_ResultDesc | varchar |  |  | SI | Result Desc
Stores the formated result value (or ... |
| LBTSI_ResultInterpretationRule_DR | varchar |  | FK | SI | Result Interpretion |
| LBTSI_ResultInterpretationValue | varchar |  |  | SI | Result value set by a result interpretion |
| LBTSI_ResultNormalRange | varchar |  |  | SI | Result Range
Stores Range as of authorisation dat... |
| LBTSI_ResultRangeFlag | varchar |  |  | SI | Internal result flag
Used for workflow evaluation... |
| LBTSI_ResultTestItemCodedResult_DR | varchar |  | FK | SI | Stores a Test Item Comment reference |
| LBTSI_ResultUom | varchar |  |  | SI | Result Uom
Stores Units of measure (Desc) for res... |
| LBTSI_RowID | varchar |  |  | NO | - |
| LBTSI_SharedResultTestSetItems | varchar |  |  | SI | Link to all test set items of the same episode and... |
| LBTSI_SignificantResult | varchar |  |  | SI | Significant Result |
| LBTSI_SpecimenContainers | varchar |  |  | SI | Specimen Container(s) |
| LBTSI_SpecimenValidityExceeded | numeric |  |  | SI | Specimen Validity Exceeded
Set at test set author... |
| LBTSI_SpecimenValidityStatus | varchar |  |  | SI | Specimen Validity Status
Set at test set authoris... |
| LBTSI_StaffNotes_DR | bigint |  | FK | SI | Link to a websys.Document that stores the formated... |
| LBTSI_Status | varchar |  |  | SI | Result Status |
| LBTSI_StoredValue | varchar |  |  | SI | In case the result is a standard type this propery... |
| LBTSI_TestMethod_DR | bigint |  | FK | SI | Test Method
A record of the Test Method calculate... |
| LBTSI_TestSetBloodProduct_DR | varchar |  | FK | SI | Blood product which is tested by this test set ite... |
| LBTSI_TestSetItem_DR | varchar |  | FK | SI | Reference to LBCTestSetRevisionItem code table |
| LBTSI_TextResult_DR | bigint |  | FK | SI | Stores a text result in HTML Rich Text as a websys... |
| LBTSI_Time | time |  |  | SI | Time result, comment, reportable or status was las... |
| LBTSI_User_DR | bigint |  | FK | SI | User last modified result, comment, reportable or ... |
| LBTSI_ValidityExtensionReason_DR | bigint |  | FK | SI | Specimen Validity Extension Reason |
| LBTSI_Value | varchar |  |  | SI | Result value 
Note: for Pathogens, this is the Co... |
| Q01 | - |  |  | SI | Espacio de trabajo y entrenamiento del paciente li... |
| Q02 | - |  |  | SI | Piso limpio, seco y no recientemente encerado |
| Q03 | - |  |  | SI | Posicionamiento adecuado del paciente en camillas,... |
| Q04 | - |  |  | SI | Lavado de manos, antes y despues de la atención de... |
| Q05 | - |  |  | SI | Posicionamiento en alturas bajas con referencia al... |
| Q06 | - |  |  | SI | Adecuada eliminación de residuos en basureros |
| Q07 | - |  |  | SI | Cronómetro para el tiempo de aplicación de element... |
| Q08 | - |  |  | SI | Descartar patologías de trastornos sensibilidad su... |
| Q09 | - |  |  | SI | Descartar alteraciones de equilibrio y control de ... |
| Q10 | - |  |  | SI | Adecuada base de sustentación en entrenamientos de... |
| Q11 | - |  |  | SI | Paciente sin contraindicaciones según procedimient... |
| Q12 | - |  |  | SI | Chequeo de variables hemodinámicas |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*