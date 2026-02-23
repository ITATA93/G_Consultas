# SQLUser.AR_HICVerifHistory

**Schema:** SQLUser
**Columnas:** 180
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VERH_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Origen de la Licencia |
| Q02 | - |  |  | SI | Fecha de Inicio del reposo |
| Q03 | - |  |  | SI | Número de días |
| Q04 | - |  |  | SI | Fecha de final del Reposo |
| Q05 | - |  |  | SI | Tipo de Reposo |
| Q06 | - |  |  | SI | Jornada |
| Q07 | - |  |  | SI | Lugar de Reposo |
| Q08 | - |  |  | SI | Comuna de Reposo |
| Q09 | - |  |  | SI | Dirección de Reposo |
| Q10 | - |  |  | SI | Teléfono |
| Q11 | - |  |  | SI | Justificación otro Domicilio |
| Q12 | - |  |  | SI | Lugar de Reposo Alternativo |
| Q13 | - |  |  | SI | Comuna de Reposo Alternativo |
| Q14 | - |  |  | SI | Dirección de Reposo Alternativo: |
| Q15 | - |  |  | SI | Teléfono Alternativo |
| Q16 | - |  |  | SI | Otro Domicilio Alternativo |
| Q17 | - |  |  | SI | Tipo de Licencia |
| Q18 | - |  |  | SI | Datos del Hijo |
| Q19 | - |  |  | SI | RUN del Hijo |
| Q20 | - |  |  | SI | DV del Hijo |
| Q21 | - |  |  | SI | Nombre del Hijo |
| Q22 | - |  |  | SI | Apellido Paterno del Hijo |
| Q23 | - |  |  | SI | Apellido Materno del Hijo |
| Q24 | - |  |  | SI | Fecha de Nacimiento del Hijo |
| Q25 | - |  |  | SI | Fecha de Accidente |
| Q26 | - |  |  | SI | Hora de Accidente |
| Q27 | - |  |  | SI | Trayecto |
| Q28 | - |  |  | SI | Subtipo de Licencia |
| Q29 | - |  |  | SI | Fecha Concepción |
| Q30 | - |  |  | SI | Diagnostico principal |
| Q31 | - |  |  | SI | Observaciones Diagnóstico |
| Q32 | - |  |  | SI | Otros Antecedentes médicos |
| Q33 | - |  |  | SI | Diagnóstico Secundario CIE-10 |
| Q34 | - |  |  | SI | Diagnostico Secundario |
| Q35 | - |  |  | SI | Otros Diagnósticos CIE-10 |
| Q36 | - |  |  | SI | Otros Diagnósticos |
| Q37 | - |  |  | SI | Antecedentes Clínicos |
| Q38 | - |  |  | SI | Exámenes de Apoyo |
| Q39 | - |  |  | SI | Código de Proceso |
| Q40 | - |  |  | SI | UrlConexion |
| Q41 | - |  |  | SI | Número Licencia |
| Q42 | - |  |  | SI | Estado Licencia |
| Q43 | - |  |  | SI | Motivo de Licencia |
| Q44 | - |  |  | SI | Inicio Trámite Invalidez |
| Q45 | - |  |  | SI | Correo Electrónico |
| Q46 | - |  |  | SI | Número de empleadores |
| Q47 | - |  |  | SI | Hijo Mortinato |
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
| VERH_AccidentDate | date |  |  | SI | Accident Date |
| VERH_AccidentInd | varchar |  |  | SI | Accident Indicator |
| VERH_AccountReferenceId | varchar |  |  | SI | Account Reference Id  |
| VERH_AdmissionDate | date |  |  | SI | Admission Date |
| VERH_BenefitLimitations | varchar |  |  | SI | Benefit Limitations |
| VERH_ChargeAmount | double |  |  | SI | Charge Amount |
| VERH_ClaimFundAssessmentCde | varchar |  |  | SI | Claim Fund Assessment Code |
| VERH_ClaimFundExplanationCode | varchar |  |  | SI | Claim Fund Explanation Code |
| VERH_ClaimFundExplanationText | varchar |  |  | SI | Claim Fund Explanation Text |
| VERH_CoPaymentAmount | varchar |  |  | SI | Co-Payment Amount |
| VERH_CoPaymentDaysRemaining | varchar |  |  | SI | Co-Payment Days Remaining |
| VERH_CoPaymentDescription | varchar |  |  | SI | Co-Payment Descriptio |
| VERH_CompensationClaimInd | varchar |  |  | SI | Compensation Claim Indicator |
| VERH_ConcessionStatusCode | varchar |  |  | SI | Concession Status Code |
| VERH_ConcessionStatusText | varchar |  |  | SI | Concession Status Text |
| VERH_CurrentPatMedicareCardNum | varchar |  |  | SI | Current Pat Medicare CardNum |
| VERH_CurrentPatientFamilyName | varchar |  |  | SI | Current Patient Family Name |
| VERH_CurrentPatientFirstName | varchar |  |  | SI | Current Patient First Name |
| VERH_CurrentPatientReferenceNum | varchar |  |  | SI | Current Patient Reference Num |
| VERH_CurrentVeteranFileNum | varchar |  |  | SI | Current Veteran FileNum |
| VERH_DVAProcDate | date |  |  | SI | DVA ProcDate |
| VERH_DVAStatusCode | varchar |  |  | SI | DVA Status Code |
| VERH_DVAStatusText | varchar |  |  | SI | DVA Status Text |
| VERH_DateOfService | date |  |  | SI | Date Of Service |
| VERH_DateSent | date |  |  | SI | Date Sent |
| VERH_DischargeDate | date |  |  | SI | Discharge Date |
| VERH_EarliestDateOfService | date |  |  | SI | Earliest Date Of Service |
| VERH_EmergencyAdmissionInd | varchar |  |  | SI | Emergency Admission Indicator |
| VERH_ExcessAmount | varchar |  |  | SI | Excess Amount |
| VERH_ExcessAmountDescription | varchar |  |  | SI | Excess Amount Description |
| VERH_ExcessBonusAmount | varchar |  |  | SI | Excess Bonus Amount |
| VERH_ExclusionDescription | varchar |  |  | SI | Exclusion Description |
| VERH_FacilityId | varchar |  |  | SI | Facility Id |
| VERH_FinancialStatus | varchar |  |  | SI | Financial Status |
| VERH_FundBenefitAmount | double |  |  | SI | Fund Benefit Amount |
| VERH_FundBrandId | varchar |  |  | SI | Fund Brand Id |
| VERH_FundReferenceId | varchar |  |  | SI | Fund Reference Id |
| VERH_FundStatusCode | varchar |  |  | SI | Fund Status Code |
| VERH_FundStatusText | varchar |  |  | SI | Fund Status Text |
| VERH_HealthFundProcDate | date |  |  | SI | Health Fund Processed Date |
| VERH_LengthOfStay | double |  |  | SI | Length Of Stay |
| VERH_MedicareProcDate | date |  |  | SI | Medicare Processed Date |
| VERH_MedicareStatusCode | varchar |  |  | SI | Medicare Status Code |
| VERH_MedicareStatusText | varchar |  |  | SI | Medicare Status Text |
| VERH_OECTypeCde | varchar |  |  | SI | Online Eligibility Check (OEC) Type Code |
| VERH_OPVTypeCode | varchar |  |  | SI | OPV Type Code |
| VERH_PAADM_DR | bigint |  | FK | SI | Episode Number |
| VERH_PAPER_DR | bigint |  | FK | SI | Des Ref PAPER |
| VERH_PEAPotentialInd | varchar |  |  | SI | Potential Previously Existing Ailment Indicator |
| VERH_PEARequestInd | varchar |  |  | SI | PEA Request Indicator |
| VERH_PatientAddressLocality | varchar |  |  | SI | Address Locality |
| VERH_PatientAddressPostcode | varchar |  |  | SI | Postcode |
| VERH_PatientAliasFamilyName | varchar |  |  | SI | Alias Familay Name |
| VERH_PatientAliasFirstName | varchar |  |  | SI | Alias First Name |
| VERH_PatientDOB | date |  |  | SI | Patient DOB |
| VERH_PatientFamilyName | varchar |  |  | SI | Patient Family Name |
| VERH_PatientFirstName | varchar |  |  | SI | Patient First Name |
| VERH_PatientFundMembershipNum | varchar |  |  | SI | Patient Fund Membership Num |
| VERH_PatientFundUPI | varchar |  |  | SI | Patient Fund UPI |
| VERH_PatientGender | varchar |  |  | SI | Patient Gender |
| VERH_PatientMedicareCardNum | varchar |  |  | SI | Patient Medicare CardNum |
| VERH_PatientReferenceNum | varchar |  |  | SI | PatientReferenceNum |
| VERH_PatientSecondInitial | varchar |  |  | SI | Second Initial |
| VERH_PresentingIllnessCode | varchar |  |  | SI | Presenting Illness Code |
| VERH_PresentingIllnessItemNum | varchar |  |  | SI | Presenting Illness Item Number |
| VERH_ProcessStatusCde | varchar |  |  | SI | Process Status Code |
| VERH_ReferenceId | varchar |  |  | SI | Reference Id |
| VERH_ReturnCode | varchar |  |  | SI | ReturnCode |
| VERH_ReturnText | varchar |  |  | SI | Return Text |
| VERH_SameDayInd | varchar |  |  | SI | Same Day Indicator |
| VERH_SenderContactEmail | varchar |  |  | SI | Sender Contact Email |
| VERH_SenderContactPersonName | varchar |  |  | SI | Sender Contact Person Name |
| VERH_SenderContactPersonPhone | varchar |  |  | SI | Sender Contact Person Phone |
| VERH_ServiceCode | varchar |  |  | SI | Service Code |
| VERH_ServiceCodeTypeCode | varchar |  |  | SI | Service Code Type Code |
| VERH_ServiceFundAssessmentCde | varchar |  |  | SI | Service Fund Assessment Code |
| VERH_ServiceFundExplanationCode | varchar |  |  | SI | Service Fund Explanation Code |
| VERH_ServiceFundExplanationText | varchar |  |  | SI | Service Fund Explanation Text |
| VERH_ServiceId | varchar |  |  | SI | Service Id |
| VERH_ServiceProviderNum | varchar |  |  | SI | Service Provider Num |
| VERH_ServiceQuantity | double |  |  | SI | Service Quantity |
| VERH_ServiceRate | double |  |  | SI | Service Rate |
| VERH_ServicingProviderNum | varchar |  |  | SI | ServicingProviderNum |
| VERH_SubmissionAuthorisedInd | varchar |  |  | SI | SubmissionAuthorisedInd |
| VERH_TableDescription | varchar |  |  | SI | Table Description |
| VERH_TableName | varchar |  |  | SI | Table Name |
| VERH_TableScale | varchar |  |  | SI | Table Scale |
| VERH_TimeSent | time |  |  | SI | Time Sent |
| VERH_TransactionID | varchar |  |  | SI | Transaction ID |
| VERH_User_DR | bigint |  | FK | SI | Des Ref User |
| VERH_VeteranEntitlementCode | varchar |  |  | SI | Veteran Entitlement Code |
| VERH_VeteranFileNum | varchar |  |  | SI | Veteran File Num |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*