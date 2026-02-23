# SQLUser.MR_Diagnos

**Schema:** SQLUser
**Columnas:** 170
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Registro de **Diagnosticos** del paciente.

Diagnosticos por episodio de atencion:
- CIE-10 principal y secundarios
- Fecha de diagnostico
- Medico responsable

**Campos clave:**
- MRDIA_ParRef: Referencia al episodio
- MRDIA_ICDCode_DR: Codigo CIE-10
- MRDIA_Date: Fecha diagnostico
- MRDIA_Type: Tipo (principal, secundario)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRDIA_MRADM_ParRef | bigint | PK |  | NO | MR_AdmLink Parent Reference |
| MRDIA_AccidentDate | varchar |  |  | SI | AccidentDate |
| MRDIA_Active | varchar |  |  | SI | Active |
| MRDIA_AdditionalDignosis | varchar |  |  | SI | AdditionalDignosis |
| MRDIA_AdminCategory_DR | bigint |  | FK | SI | Des Ref AccountClass |
| MRDIA_AliasDiagText | varchar |  |  | SI | AliasDiagText |
| MRDIA_Approximate | varchar |  |  | SI | Approximate |
| MRDIA_AutoAssignedFlg | varchar |  |  | SI | Auto Assigned Flag |
| MRDIA_AuxInsType_DR | bigint |  | FK | SI | Des Ref to AuxInsType |
| MRDIA_BodySite_DR | bigint |  | FK | SI | Des Ref BodySite |
| MRDIA_Childsub | numeric |  |  | NO | MRDIA_Childsub |
| MRDIA_CommReportedDate | date |  |  | SI | Commissioning Reported Date |
| MRDIA_ComorbidCode | varchar |  |  | SI | Code - if Comorbid Condition Terminology link was ... |
| MRDIA_ComorbidDesc | varchar |  |  | SI | Description - if Comorbid Condition Terminology li... |
| MRDIA_ComorbidSelected | varchar |  |  | SI | Selected Description - if Comorbid Condition Termi... |
| MRDIA_ConditionAdmission_DR | bigint |  | FK | SI | Des Ref to MRCConditionAdmission |
| MRDIA_Consult_DR | varchar |  | FK | SI | Des Ref Consult |
| MRDIA_ContractFlag_DR | bigint |  | FK | SI | Des Ref ContractFlag |
| MRDIA_CopyToEpisode_DR | bigint |  | FK | SI | Des Ref to PAAdm - Copied To Linked Episode |
| MRDIA_CopyToHistory | varchar |  |  | SI | Copy To History - Used in web.Msg.MRDiagnos |
| MRDIA_Cosmetic | varchar |  |  | SI | Cosmetic Flag |
| MRDIA_DRGOrder | varchar |  |  | SI | DRG Order |
| MRDIA_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| MRDIA_DaggerAster | varchar |  |  | SI | Dagger Aster |
| MRDIA_Date | date |  |  | SI | Date |
| MRDIA_DateDetect | date |  |  | SI | Date Detected |
| MRDIA_DateDiagnosisIdentif | date |  |  | SI | DateDiagnosisIdentified |
| MRDIA_DeletionReason_DR | bigint |  | FK | SI | Des Ref DeletionReason |
| MRDIA_Desc | varchar |  |  | SI | Description |
| MRDIA_DiagStat_DR | bigint |  | FK | SI | Des Ref to MRC_DiagStat |
| MRDIA_DiagnosisGroup1_DR | bigint |  | FK | SI | Des Ref DiagnosisGroup1 |
| MRDIA_DiagnosisGroup2_DR | bigint |  | FK | SI | Des Ref DiagnosisGroup2 |
| MRDIA_DiagnosisID | varchar |  |  | SI | Diagnosis ID - Used in web.Msg.MRDiagnos |
| MRDIA_DiagnosisType_DR | bigint |  | FK | SI | Diagnosis Type - Used in web.Msg.MRDiagnos |
| MRDIA_DistalMet_DR | bigint |  | FK | SI | Des REf DistalMet |
| MRDIA_DocCode_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| MRDIA_DurationNum | varchar |  |  | SI | DurationNum |
| MRDIA_DurationUnit | varchar |  |  | SI | DurationUnit |
| MRDIA_EndDate | date |  |  | SI | EndDate |
| MRDIA_EndTime | time |  |  | SI | EndTime |
| MRDIA_EnteredAs | varchar |  |  | SI | Entered As - if Terminology link was used |
| MRDIA_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| MRDIA_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| MRDIA_ExcludeFromClaim | varchar |  |  | SI | Exclude from Claim |
| MRDIA_ExtCauseDateOccurrence | date |  |  | SI | External Cause Date of Occurrence |
| MRDIA_ExternalId | varchar |  |  | SI | A reference to external systems |
| MRDIA_FirstInset | varchar |  |  | SI | First Inset |
| MRDIA_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| MRDIA_ICDStatus_DR | bigint |  | FK | SI | Des Ref to MRCIS |
| MRDIA_ICDSup_DR | bigint |  | FK | SI | Des Ref to MRCSI |
| MRDIA_InsType_DR | bigint |  | FK | SI | Des Ref to InsType |
| MRDIA_IsActive | varchar |  |  | SI | Active CALCULATED Property - used for more conplex... |
| MRDIA_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| MRDIA_LinkedExternalId | varchar |  |  | SI | External Id of the linked diagnosis
Used by Healt... |
| MRDIA_LymphInvas_DR | bigint |  | FK | SI | Des Ref LymphInvas |
| MRDIA_LymphNode_DR | bigint |  | FK | SI | Des Ref LymphNode |
| MRDIA_MRDIA_DR | varchar |  | FK | SI | Des Ref MRDIA |
| MRDIA_MalGrade_DR | bigint |  | FK | SI | Des Ref MalGrade |
| MRDIA_MappedICD_DR | bigint |  | FK | SI | Des Ref MappedICD |
| MRDIA_ORAnaOp_DR | varchar |  | FK | SI | Des Ref to ORAnaestOperation |
| MRDIA_OnsetDate | date |  |  | SI | OnsetDate |
| MRDIA_OnsetTime | time |  |  | SI | OnsetTime |
| MRDIA_OriginalDiagnos_DR | varchar |  | FK | SI | Des Ref to MRDiagnos |
| MRDIA_PayByResult | varchar |  |  | SI | Payment By Result |
| MRDIA_Prefix | varchar |  |  | SI | Prefix |
| MRDIA_PresentOnAdmission_DR | bigint |  | FK | SI | Des Ref to PACPresentOnAdmission |
| MRDIA_PrimaryTumourSite_DR | bigint |  | FK | SI | Des Ref PrimaryTumourSite |
| MRDIA_Principle | varchar |  |  | SI | Principle |
| MRDIA_Questionnaire | varchar |  |  | SI | Questionnaire |
| MRDIA_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref - Reason For Correction |
| MRDIA_ResTum_DR | bigint |  | FK | SI | Des Ref ResTum_DR |
| MRDIA_RiskEvaluation_DR | varchar |  | FK | SI | Des Ref RiskEvaluation |
| MRDIA_RowId | varchar |  |  | NO | - |
| MRDIA_Severity_DR | bigint |  | FK | SI | Des Ref Severity |
| MRDIA_SignSym_DR | bigint |  | FK | SI | Des Ref SignSym |
| MRDIA_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| MRDIA_StageClas_DR | bigint |  | FK | SI | Des Ref StageClas |
| MRDIA_Stages_DR | bigint |  | FK | SI | Des Ref Stages_DR |
| MRDIA_Suspicion | varchar |  |  | SI | Suspicion |
| MRDIA_TerminologyCode | varchar |  |  | SI | Code - if Terminology link was used (e.g. ECDS Cod... |
| MRDIA_TerminologyDesc | varchar |  |  | SI | Description - if Terminology link was used (e.g. E... |
| MRDIA_TerminologySelected | varchar |  |  | SI | Selected Description - if Diagnose Terminology lin... |
| MRDIA_Time | time |  |  | SI | Time |
| MRDIA_TimeDiagnosisIdentif | time |  |  | SI | TimeDiagnosisIdentif |
| MRDIA_TumourNotes | varchar |  |  | SI | TumourNotes |
| MRDIA_TumourSize | varchar |  |  | SI | TumourSize |
| MRDIA_TumourUpdateDate | date |  |  | SI | TumourUpdateDate |
| MRDIA_TumourUpdateHospitalDR | bigint |  | FK | SI | Des Ref TumourUpdateHospitalDR |
| MRDIA_TumourUpdateTime | time |  |  | SI | TumourUpdateTime |
| MRDIA_TumourUpdateUser_DR | bigint |  | FK | SI | Des Ref TumourUpdateUser |
| MRDIA_Tumour_DR | bigint |  | FK | SI | Des Ref Tumour |
| MRDIA_UpdateDate | date |  |  | SI | UpdateDate |
| MRDIA_UpdateHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| MRDIA_UpdateTime | time |  |  | SI | UpdateTime |
| MRDIA_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| MRDIA_UserCreated_DR | bigint |  | FK | SI | Des Ref UserCreated |
| MRDIA_VenInvasion_DR | bigint |  | FK | SI | Des Ref VenInvasion |
| MRDIA_WorkRelated | varchar |  |  | SI | Work Related |
| Q07 | - |  |  | SI | Altura de Rodilla |
| Q07ObsDR | - |  |  | SI | Altura de Rodilla DR |
| Q08 | - |  |  | SI | Circunferencia Braquial |
| Q08ObsDR | - |  |  | SI | Circunferencia Braquial DR |
| Q09 | - |  |  | SI | Pliegue Tricipital |
| Q10 | - |  |  | SI | Pliegue Subescapular |
| Q11 | - |  |  | SI | Pliegue Suprailiaco |
| Q12 | - |  |  | SI | Pliegue Braquial |
| Q13 | - |  |  | SI | Sumatoria 4 Pliegues |
| Q26 | - |  |  | SI | Circunferencia Abdominal |
| Q26ObsDR | - |  |  | SI | Circunferencia Abdominal DR |
| Q27 | - |  |  | SI | Circunferencia Pantorrillas |
| Q28 | - |  |  | SI | Dinamometría |
| Q29 | - |  |  | SI | Unidad Medida (Dinamometría) |
| QAB | - |  |  | SI | AB |
| QAGB | - |  |  | SI | AGB |
| QAMB | - |  |  | SI | AMB |
| QCMB | - |  |  | SI | CMB |
| QEDAD | - |  |  | SI | Edad |
| QPH0 | - |  |  | SI | Peso Hombre 6-18 años |
| QPH1 | - |  |  | SI | Peso Hombre 19-59 años |
| QPH2 | - |  |  | SI | Peso Hombre 60-80 años |
| QPM0 | - |  |  | SI | Peso Mujer 6-18 años |
| QPM1 | - |  |  | SI | Peso Mujer 19-59 años |
| QPM2 | - |  |  | SI | Peso Mujer 60-80 años |
| QRGETAREO | - |  |  | SI | Rango Etareo |
| QTH0 | - |  |  | SI | Talla Hombre 6-18 años |
| QTH1 | - |  |  | SI | Talla Hombre 19-59 años |
| QTH2 | - |  |  | SI | Talla Hombre 60-80 años |
| QTM0 | - |  |  | SI | Talla Mujer 6-18 años |
| QTM1 | - |  |  | SI | Talla Mujer 19-59 años |
| QTM2 | - |  |  | SI | Talla Mujer 60-80 años |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*