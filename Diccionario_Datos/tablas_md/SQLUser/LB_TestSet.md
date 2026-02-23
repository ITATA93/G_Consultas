# SQLUser.LB_TestSet

**Schema:** SQLUser
**Columnas:** 243
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Solicitudes de Laboratorio**.

Agrupa examenes solicitados:
- Panel de examenes
- Muestras asociadas
- Estado del proceso

**Campos clave:**
- LBTS_RowId: ID unico
- LBTS_Order_DR: FK a orden
- LBTS_CollectDate: Fecha de toma de muestra
- LBTS_Status: Estado del proceso

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTS_RowID | bigint | PK |  | NO | - |
| ChildQExaDR | - |  |  | SI | Child Reference: Exámenes |
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
| LBTS_Episode_DR | bigint |  | FK | NO | LBEpisode Reference |
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
| LBTS_Priority_DR | bigint |  | FK | SI | Calculated Test Set Priority - Do not index and do... |
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
| LBTS_TestSetSeq | integer |  |  | NO | Instance number of an LBCTestSetRevision within an... |
| LBTS_TestSet_DR | bigint |  | FK | NO | TestSet CodeTable Reference |
| LBTS_TriggerTestSet_DR | bigint |  | FK | SI | Differential Counter Trigger Test Set DR |
| LBTS_TurnaroundTimeConfig | varchar |  |  | SI | Turnaround Time Config  |
| LBTS_TurnaroundTimeElapsed | integer |  |  | SI | Turnaround Time Elapsed |
| LBTS_TurnaroundTimeFlag | varchar |  |  | SI | Turnaround Time Flag
Standard Type=LabTestSetTurn... |
| LBTS_ValidityExtensionReason_DR | bigint |  | FK | SI | Specimen Validity Extension Reason |
| Q30 | - |  |  | SI | Escolaridad |
| Q31 | - |  |  | SI | Resultado Riesgo Morir de Bronconeumonía |
| Q35 | - |  |  | SI | FI Síndrome Bronquial Obstructivo Recurrente Leve |
| Q36 | - |  |  | SI | FE Síndrome Bronquial Obstructivo Recurrente Leve |
| Q37 | - |  |  | SI | FI Síndrome Bronquial Obstructivo Recurrente Moder... |
| Q38 | - |  |  | SI | FE Síndrome Bronquial Obstructivo Recurrente Moder... |
| Q39 | - |  |  | SI | FI Síndrome Bronquial Obstructivo Recurrente Sever... |
| Q40 | - |  |  | SI | FE Síndrome Bronquial Obstructivo Recurrente Sever... |
| Q41 | - |  |  | SI | FI Asma Bronquial Leve |
| Q42 | - |  |  | SI | FE Asma Bronquial Leve |
| Q43 | - |  |  | SI | FI Asma Bronquial Moderado |
| Q44 | - |  |  | SI | FE Asma Bronquial Moderado |
| Q45 | - |  |  | SI | FI Asma Bronquial Severo |
| Q46 | - |  |  | SI | FE Asma Bronquial Severo |
| Q47 | - |  |  | SI | FI Enfermedad Pulmonar Obstructiva Crónica A |
| Q48 | - |  |  | SI | FE Enfermedad Pulmonar Obstructiva Crónica A |
| Q49 | - |  |  | SI | FI Enfermedad Pulmonar Obstructiva Crónica B |
| Q50 | - |  |  | SI | FE Enfermedad Pulmonar Obstructiva Crónica B |
| Q51 | - |  |  | SI | FI Bronquitis Obstructiva |
| Q52 | - |  |  | SI | FE Bronquitis Obstructiva |
| Q53 | - |  |  | SI | FE Otras Iras Bajas |
| Q54 | - |  |  | SI | FI Otras Iras Bajas |
| Q55 | - |  |  | SI | E Síndrome Bronquial Obstructivo Recurrente Leve |
| Q56 | - |  |  | SI | E Síndrome Bronquial Obstructivo Recurrente Modera... |
| Q57 | - |  |  | SI | E Síndrome Bronquial Obstructivo Recurrente Severo |
| Q58 | - |  |  | SI | E Asma Bronquial Leve |
| Q59 | - |  |  | SI | E Asma Bronquial Moderado |
| Q60 | - |  |  | SI | E Asma Bronquial Severo |
| Q61 | - |  |  | SI | E Enfermedad Pulmonar Obstructiva Crónica A |
| Q62 | - |  |  | SI | E Enfermedad Pulmonar Obstructiva Crónica B |
| Q63 | - |  |  | SI | E Bronquitis Obstructiva |
| Q64 | - |  |  | SI | E Otras Iras Bajas |
| Q65 | - |  |  | SI | Si ya aplicó encuesta de calidad de vida hace un a... |
| Q66 | - |  |  | SI | FI IRA Alta |
| Q67 | - |  |  | SI | FE IRA Alta |
| Q68 | - |  |  | SI | E IRA Alta |
| Q69 | - |  |  | SI | FI Influenza |
| Q70 | - |  |  | SI | FE Influenza |
| Q71 | - |  |  | SI | E Influenza |
| Q72 | - |  |  | SI | FI Neumonía |
| Q73 | - |  |  | SI | FE Neumonía |
| Q74 | - |  |  | SI | E Neumonía |
| Q75 | - |  |  | SI | FI Coqueluche |
| Q76 | - |  |  | SI | FE Coqueluche |
| Q77 | - |  |  | SI | E Coqueluche |
| Q78 | - |  |  | SI | FI Fibrosis Quística |
| Q79 | - |  |  | SI | FE Fibrosis Quística |
| Q80 | - |  |  | SI | E Fibrosis Quísitca |
| Q81 | - |  |  | SI | FI Displasia Broncopulmonar |
| Q82 | - |  |  | SI | FE Displasia Broncopulmonar |
| Q83 | - |  |  | SI | E Displasia Broncopulmonar |
| Q84 | - |  |  | SI | FI Otras Respiratorias Crónicas |
| Q85 | - |  |  | SI | FE Otras Respiratorias Crónicas |
| Q86 | - |  |  | SI | E Otras Respiratorias Crónicas |
| Q87 | - |  |  | SI | ¿El ingreso / Re-Ingreso es por exacerbación de al... |
| Q88 | - |  |  | SI | Cuáles (Selecciones según el número de la patologí... |
| Q89 | - |  |  | SI | FI Oxigeno Dependiente |
| Q90 | - |  |  | SI | FE Oxígeno Dependente |
| Q91 | - |  |  | SI | E Oxígeno Dependiente |
| Q92 | - |  |  | SI | FI Asistencia Ventilatoria No Invasiva o Invasiva |
| Q93 | - |  |  | SI | FE Asistencia Ventilatoria No Invasiva o Invasiva |
| Q94 | - |  |  | SI | E Asistencia Ventilatoria No Invasiva o Invasiva |
| QComuna | - |  |  | SI | Comuna |
| QConsultorio | - |  |  | SI | Consultorio |
| QDerivadar | - |  |  | SI | Derivar a consejería |
| QDestino | - |  |  | SI | Destino |
| QDestinoObsDR | - |  |  | SI | Destino DR |
| QDomic | - |  |  | SI | Domicilio |
| QECVC | - |  |  | SI | Encuesta Calidad de Vida de Control |
| QECVI | - |  |  | SI | Encuesta Calidad de Vida al Ingreso |
| QESU | - |  |  | SI | Encuenta Satisfacción Usuaria |
| QEdu | - |  |  | SI | Educación en Box (Técnica inhalatoria, manejo ambi... |
| QExamen | - |  |  | SI | Exámen |
| QFechaControl | - |  |  | SI | Fecha próximo Control |
| QFechaReg | - |  |  | SI | Fecha Registro |
| QHoraReg | - |  |  | SI | Hora Registro |
| QNFam | - |  |  | SI | Número Familia |
| QOrigen | - |  |  | SI | Origen |
| QOrigenObsDR | - |  |  | SI | Origen DR |
| QPaciente | - |  |  | SI | Paciente |
| QPrev | - |  |  | SI | Previsión |
| QProxCont | - |  |  | SI | Próximo Control |
| QRegion | - |  |  | SI | Región |
| QRiesgoLab | - |  |  | SI | Riesgo Laboral |
| QRiesgoLabObsDR | - |  |  | SI | Riesgo Laboral DR |
| QRut | - |  |  | SI | Rut |
| QServicio | - |  |  | SI | Servicio de Salud |
| QTab1 | - |  |  | SI | Años Fumando |
| QTab1ObsDR | - |  |  | SI | Años Fumando DR |
| QTab2 | - |  |  | SI | Cigarros al Día |
| QTab2ObsDR | - |  |  | SI | Cigarros al Día DR |
| QTab3 | - |  |  | SI | Paquetes al Año |
| QTab3ObsDR | - |  |  | SI | Paquetes al Año DR |
| QTelef | - |  |  | SI | Teléfono |
| QTest6m | - |  |  | SI | A Test de 6 minutos |
| QTipoProf | - |  |  | SI | Tipo Profesional |
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
| QViveCon | - |  |  | SI | Vive con |
| QViveConObsDR | - |  |  | SI | Vive con  DR |
| Qvacun | - |  |  | SI | A Vacunación |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*