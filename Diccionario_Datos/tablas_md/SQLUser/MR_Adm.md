# SQLUser.MR_Adm

**Schema:** SQLUser
**Columnas:** 307
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRADM_RowId | bigint | PK |  | NO | - |
| MRADM_ACAS_DR | bigint |  | FK | SI | ACAS DR |
| MRADM_ADM_DR | bigint |  | FK | SI | Des Ref to PAADM |
| MRADM_ATISWIES | varchar |  |  | SI | ATIS WIES |
| MRADM_AccountClass_DR | bigint |  | FK | SI | Des Ref AccountClass |
| MRADM_Activity_DR | bigint |  | FK | SI | Des Ref Activity |
| MRADM_AdmReadmRehab_DR | bigint |  | FK | SI | Des Ref AdmReadmRehab |
| MRADM_AdmRoute_DR | bigint |  | FK | SI | Des Ref AdmRoute |
| MRADM_AmbulanceCase | varchar |  |  | SI | Ambulance Case |
| MRADM_AutopsyType_DR | bigint |  | FK | SI | Des Ref Autopsy Type |
| MRADM_BPDiastolic | varchar |  |  | SI | Blood Pressure Diastolic |
| MRADM_BPSystolic | varchar |  |  | SI | Blood Pressure Systolic |
| MRADM_BaseWIES | varchar |  |  | SI | Base WIES |
| MRADM_BloodSugarTestResult | varchar |  |  | SI | Blood Sugar Test Result |
| MRADM_BloodType_DR | bigint |  | FK | SI | Des Ref BloodType |
| MRADM_CCUHours | double |  |  | SI | CCU Hours |
| MRADM_CPAPHours | double |  |  | SI | CPAP Hours |
| MRADM_CarePlanEndDate | date |  |  | SI | CarePlanEndDate |
| MRADM_CarePlanReviewDate | date |  |  | SI | CarePlanReviewDate |
| MRADM_CarePlanStartDate | date |  |  | SI | CarePlanStartDate |
| MRADM_CareType_DR | bigint |  | FK | SI | Des Ref CareType |
| MRADM_CarerAvail_DR | bigint |  | FK | SI | Des Ref CarerAvail |
| MRADM_CauseOfDeath_DR | bigint |  | FK | SI | Des Ref CauseOfDeath |
| MRADM_CeasarianSection | varchar |  |  | SI | Ceasarian Section |
| MRADM_Coder_DR | bigint |  | FK | SI | Des Ref Coder |
| MRADM_CodingUpdateDate | date |  |  | SI | Coding Update Date |
| MRADM_CodingUpdateHospital_DR | bigint |  | FK | SI | Des Ref CodingUpdateHospital |
| MRADM_CodingUpdateTime | time |  |  | SI | Coding Update Time |
| MRADM_CodingUpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| MRADM_ConditAtDisch_DR | bigint |  | FK | SI | Condition At Time of Dicsharge |
| MRADM_ConscState_DR | bigint |  | FK | SI | Des Ref ConscState |
| MRADM_ContrSpokeIdentif_DR | bigint |  | FK | SI | Des Ref ContrSpokeIdentif |
| MRADM_ContractRole_DR | bigint |  | FK | SI | Des Ref ContractRole |
| MRADM_ContractType_DR | bigint |  | FK | SI | Des Ref ContractType |
| MRADM_DRGCodingWeight | varchar |  |  | SI | DRG Coding Admission Weight |
| MRADM_DRGCodingWeightUOM_DR | bigint |  | FK | SI | DRG Coding Admission Weight UOM |
| MRADM_DRGFirstDateProcessing | date |  |  | SI | DRG First Date Processing |
| MRADM_DRGFreeText1 | varchar |  |  | SI | Free Text Field |
| MRADM_DRGFreeText2 | varchar |  |  | SI | Free Text Field |
| MRADM_DRGFreeText3 | varchar |  |  | SI | Free Text Field |
| MRADM_DRGFreeText4 | varchar |  |  | SI | Free Text Field |
| MRADM_DRGGenFloat1 | double |  |  | SI | Generic Float Field |
| MRADM_DRGGenFloat2 | double |  |  | SI | Generic Float Field |
| MRADM_DRGGenInteger1 | integer |  |  | SI | Generic Integer Field |
| MRADM_DRGGenInteger2 | integer |  |  | SI | Generic Integer Field |
| MRADM_DRGGenLookup1 | varchar |  |  | SI | Generic Checkbox  - This has changed from a generi... |
| MRADM_DRGGenLookup2 | varchar |  |  | SI | Generic Checkbox  - This has changed from a generi... |
| MRADM_DRGGrouperVersionStatutory_DR | bigint |  | FK | SI | Des Ref DRGGrouperVersion |
| MRADM_DRGGrouperVersion_DR | bigint |  | FK | SI | Des Ref DRGGrouperVersion |
| MRADM_DRGLastDateProcessing | date |  |  | SI | DRG Last Date Processing |
| MRADM_DRGProcessTimes | double |  |  | SI | DRG Process Times |
| MRADM_DRGStatutory_DR | bigint |  | FK | SI | Des Ref DRG |
| MRADM_DRGTariff | double |  |  | SI | DRG Tariff |
| MRADM_DRGWeight | double |  |  | SI | DRG Weight |
| MRADM_DRG_DR | bigint |  | FK | SI | Des Ref DRG |
| MRADM_DRG_Weighting | varchar |  |  | SI | DRG Weighting |
| MRADM_Date | date |  |  | SI | Date |
| MRADM_DateHeight | date |  |  | SI | Date Height |
| MRADM_DateProofPrinted | date |  |  | SI | DateProofPrinted |
| MRADM_DateRangeFrom | varchar |  |  | SI | DateRangeFrom |
| MRADM_DateRangeTo | varchar |  |  | SI | Date Range To |
| MRADM_DateSerumCreatinine | date |  |  | SI | DateSerumCreatinine |
| MRADM_DateWeight | date |  |  | SI | Date Weight |
| MRADM_DegreeProgression_DR | bigint |  | FK | SI | Des Ref to DegreeProgression  |
| MRADM_Deletion | varchar |  |  | SI | Deletion |
| MRADM_DietComments | varchar |  |  | SI | Diet Comments |
| MRADM_DischBedMobility_DR | bigint |  | FK | SI | Des Ref DischBedMobility |
| MRADM_DischClassif_DR | bigint |  | FK | SI | Des Ref Discharge Classif |
| MRADM_DischDestin_DR | bigint |  | FK | SI | Des Ref DischDestin |
| MRADM_DischEating_DR | bigint |  | FK | SI | Des Ref DischEating |
| MRADM_DischPallCare_DR | bigint |  | FK | SI | Des Ref DischPallCare |
| MRADM_DischRUGTotal | double |  |  | SI | Disch RUG Total |
| MRADM_DischReasonBedUnAvail_DR | bigint |  | FK | SI | Des Ref DischReasonBedUnAvail |
| MRADM_DischToileting_DR | bigint |  | FK | SI | Des Ref DischToileting |
| MRADM_DischTransfer_DR | bigint |  | FK | SI | Des Ref DischTransfer |
| MRADM_DischTransport_DR | bigint |  | FK | SI | Des Ref DischTransport |
| MRADM_DischType_DR | bigint |  | FK | SI | Des REf to DischType |
| MRADM_DischargeDate | date |  |  | SI | Discharge Date |
| MRADM_DocDisch_DR | varchar |  | FK | SI | Des Ref CTCP |
| MRADM_DrainTubes_DR | bigint |  | FK | SI | Des Ref DrainTubes_ |
| MRADM_DurationMechVent | double |  |  | SI | Duration of Mechanical Ventilation |
| MRADM_Ectopic | varchar |  |  | SI | Ectopic Beats Per Min |
| MRADM_EpisClinComplexScore | double |  |  | SI | Episode Clinical Complexity Score (ECCS) |
| MRADM_EscortSource_DR | bigint |  | FK | SI | Des Ref EscortSource |
| MRADM_FollowUpReasonFreeText | varchar |  |  | SI | Follow Up Reason Free Text |
| MRADM_FundingArrang_DR | bigint |  | FK | SI | Des Ref FundingArrang |
| MRADM_GPConsent | varchar |  |  | SI | GP Consent |
| MRADM_GlasgowComaScore | double |  |  | SI | GlasgowComaScore |
| MRADM_GrouperStatus_DR | bigint |  | FK | SI | Des Ref GrouperStatus |
| MRADM_HeadCircumference | varchar |  |  | SI | Head Circumference |
| MRADM_HealthSpecCode_DR | varchar |  | FK | SI | Des Ref to CTLocHealthSpecCode |
| MRADM_Height | varchar |  |  | SI | Height |
| MRADM_HeightUOM_DR | bigint |  | FK | SI | Height UOM |
| MRADM_HighOutlierDays | double |  |  | SI | High Outlier Days |
| MRADM_ICUHours | double |  |  | SI | ICU Hours |
| MRADM_IVTherapy_DR | bigint |  | FK | SI | Des Ref IVTherapy |
| MRADM_InfectType_DR | bigint |  | FK | SI | Des Ref InfectType |
| MRADM_InjuryDesc | varchar |  |  | SI | InjuryDesc |
| MRADM_InlierEquivalence | varchar |  |  | SI | InlierEquivalence |
| MRADM_IntentReadmit_DR | bigint |  | FK | SI | Des Ref IntentReadmit |
| MRADM_Isolation_DR | bigint |  | FK | SI | Des Ref Isolation |
| MRADM_KidneyTranspDes | varchar |  |  | SI | KidneyTransplant Desired |
| MRADM_KidneyTransplant | varchar |  |  | SI | Kidney Transplant |
| MRADM_MRAdmMedicationHistory_DR | varchar |  | FK | SI | Des Ref MRAdmMedicationHistory |
| MRADM_MaterType_DR | bigint |  | FK | SI | Des Ref MaterType |
| MRADM_MedicSuffix_DR | bigint |  | FK | SI | Des Ref MedicSuffix |
| MRADM_MedicallyFit | varchar |  |  | SI | MedicallyFit |
| MRADM_MentHealthStat_DR | bigint |  | FK | SI | [DEPRECATED]Replaced by mental health module in Tr... |
| MRADM_MultiVisitingHoursRanges | varchar |  |  | SI | MultiVisitingHoursRanges |
| MRADM_NoStillBirth | varchar |  |  | SI | No of Still Birth |
| MRADM_NumberOfDays | double |  |  | SI | Number Of Days |
| MRADM_NurseDisch_DR | varchar |  | FK | SI | Des Ref to CTCP |
| MRADM_NursingHours | varchar |  |  | SI | NursingHours |
| MRADM_Objective | varchar |  |  | SI | Objective Findings |
| MRADM_OnsetDate | date |  |  | SI | Onset Date |
| MRADM_OtherConditions_DR | bigint |  | FK | SI | Des Ref OtherConditions |
| MRADM_OtherDischType | varchar |  |  | SI | Other Disch Type |
| MRADM_OtherInfectType | varchar |  |  | SI | Other Infection Type |
| MRADM_OtherTransferReason | varchar |  |  | SI | OtherTransferReason |
| MRADM_Overnight_DR | bigint |  | FK | SI | Des Ref Overnight |
| MRADM_OxygenSaturation | varchar |  |  | SI | Oxygen Saturation |
| MRADM_PACSDischargeDate | date |  |  | SI | PACS Discharge Date |
| MRADM_PCCL | double |  |  | SI | Patient Clinical Complexity Level |
| MRADM_PMUpdateDate | date |  |  | SI | PM UpdateDate |
| MRADM_PMUpdateHospital_DR | bigint |  | FK | SI | Des Ref PMUpdateHospital |
| MRADM_PMUpdateTime | time |  |  | SI | PM UpdateTime |
| MRADM_PMUpdateUser_DR | bigint |  | FK | SI | Des Ref PMUpdateUser |
| MRADM_PRS2Status | varchar |  |  | SI | PRS2 Status |
| MRADM_PainRange | varchar |  |  | SI | PainRange |
| MRADM_PainScore | double |  |  | SI | PainScore |
| MRADM_PatCondDate | date |  |  | SI | PatCondDate |
| MRADM_PatCondTime | time |  |  | SI | PatCondTime |
| MRADM_PatCond_DR | bigint |  | FK | SI | Des Ref PatCond |
| MRADM_PatInqUpdUserHosp_DR | bigint |  | FK | SI | Des Ref PatInqUpdUserHosp |
| MRADM_PatInqUpdUser_DR | bigint |  | FK | SI | Des Ref User |
| MRADM_PatInqUpdateDate | date |  |  | SI | PatInqUpdateDate |
| MRADM_PatInqUpdateTime | time |  |  | SI | PatInqUpdateTime |
| MRADM_PatientRequirements | varchar |  |  | SI | PatientRequirements |
| MRADM_PreHospTreatment | varchar |  |  | SI | PreHosp Treatment |
| MRADM_PresentComplaint | varchar |  |  | SI | Present Complaint |
| MRADM_ProgrFundSource_DR | bigint |  | FK | SI | Des Ref Program FundSource |
| MRADM_ProgressDate | date |  |  | SI | Progress Date |
| MRADM_ProgressTime | time |  |  | SI | Progress Time |
| MRADM_Progress_DR | bigint |  | FK | SI | Des Ref Progress |
| MRADM_PulseRate | varchar |  |  | SI | Pulse Rate |
| MRADM_ReasonCritCareTrans_DR | bigint |  | FK | SI | Des Ref ReasonCritCareTransfer |
| MRADM_ReasonForRevFinDisch_DR | bigint |  | FK | SI | Des RefReasonForRevFinDisch |
| MRADM_ReasonTransfer_DR | bigint |  | FK | SI | Des Ref ReasonTransfer |
| MRADM_RecordsToResubmit | varchar |  |  | SI | RecordsToResubmit |
| MRADM_RefBookDate | date |  |  | SI | RefBookDate |
| MRADM_RefClin_DR | bigint |  | FK | SI | Des Ref RefClin |
| MRADM_ReferredTo_DR | bigint |  | FK | SI | Des Ref ReferredTo_DR |
| MRADM_Remarks | varchar |  |  | SI | Remarks |
| MRADM_Resend | varchar |  |  | SI | Resend |
| MRADM_Resp | varchar |  |  | SI | Resp |
| MRADM_RestPeriodFrom | time |  |  | SI | RestPeriodFrom |
| MRADM_RestPeriodTo | time |  |  | SI | RestPeriodTo |
| MRADM_RingWard | varchar |  |  | SI | RingWard |
| MRADM_RiskOfMortality_DR | bigint |  | FK | SI | Des Ref to MRCRiskOfMortality |
| MRADM_SentPRS2 | varchar |  |  | SI | Sent to PRS2 |
| MRADM_SeparationReferral_DR | varchar |  | FK | SI | Text Des Ref SeparationReferral |
| MRADM_SeqNo | varchar |  |  | SI | SeqNo |
| MRADM_SerumCreatinine | double |  |  | SI | SerumCreatinine |
| MRADM_SourceReferralPalCare_DR | bigint |  | FK | SI | Des Ref SourceReferralPalCare |
| MRADM_SpecialInstr | varchar |  |  | SI | Special Instructions |
| MRADM_Subjective | varchar |  |  | SI | Subjective Findings |
| MRADM_TakingCalls | varchar |  |  | SI | Taking Calls |
| MRADM_Temp | varchar |  |  | SI | Temperature |
| MRADM_Time | time |  |  | SI | Time |
| MRADM_TotalWIESPrice | varchar |  |  | SI | Total WIES Price |
| MRADM_TotalWIESScore | varchar |  |  | SI | Total WIES Score |
| MRADM_Traffic_DR | bigint |  | FK | SI | Des Ref  PA Traffic |
| MRADM_TransDest2_DR | bigint |  | FK | SI | Des Ref TransDest2(used as transfer source) |
| MRADM_TransfDest_DR | bigint |  | FK | SI | Des Ref TransfDest |
| MRADM_TransferDateRefCln | date |  |  | SI | Transfer Date from RefCln |
| MRADM_TransferMeans_DR | bigint |  | FK | SI | Des Ref Transfer Means |
| MRADM_TubalLigation | varchar |  |  | SI | Tubal Ligation |
| MRADM_Tumor_DR | bigint |  | FK | SI | Des Ref Tumor |
| MRADM_UnplanReadmission_DR | bigint |  | FK | SI | Des Ref UnplanReadmission |
| MRADM_UrineSugarTestResult | varchar |  |  | SI | Urine Sugar Test Result |
| MRADM_Ventilation_DR | bigint |  | FK | SI | Des Ref Ventilation |
| MRADM_VisionScoreLeft | varchar |  |  | SI | Vision Score Left |
| MRADM_VisionScoreRight | varchar |  |  | SI | Vision Score Right |
| MRADM_VisitHrFrom | time |  |  | SI | VisitHrFrom |
| MRADM_VisitHrTo | time |  |  | SI | VisitHrTo |
| MRADM_VisitType_DR | bigint |  | FK | SI | Des Ref Visit Type |
| MRADM_VisitorStatus_DR | bigint |  | FK | SI | Des Ref Visitor Status |
| MRADM_WaistCircumference | varchar |  |  | SI | Waist Circumference |
| MRADM_Weight | varchar |  |  | SI | Weight |
| MRADM_WeightUOM_DR | bigint |  | FK | SI | Weight UOM |
| MRADM_WorkingDiagnosis_DR | bigint |  | FK | SI | Des Ref WorkingDiagnosis |
| MRADM_WoundType_DR | bigint |  | FK | SI | Des Ref WoundType |
| Q01 | - |  |  | SI | Establecimiento de Salud (código y descripción) |
| Q02 | - |  |  | SI | código establecimiento de salud |
| Q03 | - |  |  | SI | Mes de Atención |
| Q04 | - |  |  | SI | Año de Atención |
| Q05 | - |  |  | SI | Total talleres, comunas comunidades, talleres grup... |
| Q06 | - |  |  | SI | Total talleres, espacios amigables en aps, tallere... |
| Q07 | - |  |  | SI | Total talleres, lugares de trabajo, talleres grupa... |
| Q08 | - |  |  | SI | Total talleres, establecimientos educacion, taller... |
| Q09 | - |  |  | SI | Autoestima y autocuidado, comunas comunidades, tal... |
| Q10 | - |  |  | SI | Autoestima y autocuidado, espacios amigables en ap... |
| Q11 | - |  |  | SI | Autoestima y autocuidado, lugares de trabajo, tall... |
| Q12 | - |  |  | SI | Autoestima y autocuidado, establecimientos educaci... |
| Q13 | - |  |  | SI | mente sana y cuerpo sano, comunas comunidades, tal... |
| Q14 | - |  |  | SI | mente sana y cuerpo sano, espacios amigables en ap... |
| Q15 | - |  |  | SI | mente sana y cuerpo sano, lugares de trabajo, tall... |
| Q16 | - |  |  | SI | mente sana y cuerpo sano, establecimientos educaci... |
| Q17 | - |  |  | SI | comunicacion, comunas comunidades, talleres grupal... |
| Q18 | - |  |  | SI | comunicacion, espacios amigables en aps, talleres ... |
| Q19 | - |  |  | SI | comunicacion, lugares de trabajo, talleres grupale... |
| Q20 | - |  |  | SI | comunicacion, establecimientos educacion, talleres... |
| Q21 | - |  |  | SI | yo me cuido, comunas comunidades, talleres grupale... |
| Q22 | - |  |  | SI | yo me cuido, espacios amigables en aps, talleres g... |
| Q23 | - |  |  | SI | yo me cuido, lugares de trabajo, talleres grupales |
| Q24 | - |  |  | SI | yo me cuido, establecimientos educacion, talleres ... |
| Q25 | - |  |  | SI | control de tabaco, comunas comunidades, talleres g... |
| Q26 | - |  |  | SI | control de tabaco, espacios amigables en aps, tall... |
| Q27 | - |  |  | SI | control de tabaco, lugares de trabajo, talleres gr... |
| Q28 | - |  |  | SI | control de tabaco, establecimientos educacion, tal... |
| Q29 | - |  |  | SI | otros tipos de talleres, comunas comunidades, tall... |
| Q30 | - |  |  | SI | otros tipos de talleres, espacios amigables en aps... |
| Q31 | - |  |  | SI | otros tipos de talleres, lugares de trabajo, talle... |
| Q32 | - |  |  | SI | otros tipos de talleres, establecimientos educacio... |
| Q33 | - |  |  | SI | Total Actividades, comunas comunidades, actividade... |
| Q34 | - |  |  | SI | Total Actividades, espacios amigables en aps, acti... |
| Q35 | - |  |  | SI | Total Actividades, lugares de trabajo, actividades... |
| Q36 | - |  |  | SI | Total Actividades, establecimientos educacion, act... |
| Q37 | - |  |  | SI | Total Actividades, oficina intercultural, activida... |
| Q38 | - |  |  | SI | Total Actividades, otros, actividades gestion |
| Q39 | - |  |  | SI | reuniones de gestion, comunas comunidades, activid... |
| Q40 | - |  |  | SI | reuniones de gestion, espacios amigables en aps, a... |
| Q41 | - |  |  | SI | reuniones de gestion, lugares de trabajo, activida... |
| Q42 | - |  |  | SI | reuniones de gestion, establecimientos educacion, ... |
| Q43 | - |  |  | SI | reuniones de gestion, oficina intercultural, activ... |
| Q44 | - |  |  | SI | reuniones de gestion, otros, actividades gestion |
| Q45 | - |  |  | SI | reuniones masivas de gestion, comunas comunidades,... |
| Q46 | - |  |  | SI | reuniones masivas de gestion, espacios amigables e... |
| Q47 | - |  |  | SI | reuniones masivas de gestion, lugares de trabajo, ... |
| Q48 | - |  |  | SI | reuniones masivas de gestion, establecimientos edu... |
| Q49 | - |  |  | SI | reuniones masivas de gestion, oficina intercultura... |
| Q50 | - |  |  | SI | reuniones masivas de gestion, otros, actividades g... |
| Q51 | - |  |  | SI | acciones de comunicacion y difusion, comunas comun... |
| Q52 | - |  |  | SI | acciones de comunicacion y difusion, espacios amig... |
| Q53 | - |  |  | SI | acciones de comunicacion y difusion, lugares de tr... |
| Q54 | - |  |  | SI | acciones de comunicacion y difusion, establecimien... |
| Q55 | - |  |  | SI | acciones de comunicacion y difusion, oficina inter... |
| Q56 | - |  |  | SI | acciones de comunicacion y difusion, otros, activi... |
| Q57 | - |  |  | SI | preparacion acciones educativas, comunas comunidad... |
| Q58 | - |  |  | SI | preparacion acciones educativas, espacios amigable... |
| Q59 | - |  |  | SI | preparacion acciones educativas, lugares de trabaj... |
| Q60 | - |  |  | SI | preparacion acciones educativas, establecimientos ... |
| Q61 | - |  |  | SI | preparacion acciones educativas, oficina intercult... |
| Q62 | - |  |  | SI | preparacion acciones educativas, otros, actividade... |
| Q63 | - |  |  | SI | entrevistas, comunas comunidades, actividades gest... |
| Q64 | - |  |  | SI | entrevistas, espacios amigables en aps, actividade... |
| Q65 | - |  |  | SI | entrevistas, lugares de trabajo, actividades gesti... |
| Q66 | - |  |  | SI | entrevistas, establecimientos educacion, actividad... |
| Q67 | - |  |  | SI | entrevistas, oficina intercultural, actividades ge... |
| Q68 | - |  |  | SI | entrevistas, otros, actividades gestion |
| Q69 | - |  |  | SI | investigacion y capacitacion de RRHH, comunas comu... |
| Q70 | - |  |  | SI | investigacion y capacitacion de RRHH, espacios ami... |
| Q71 | - |  |  | SI | investigacion y capacitacion de RRHH, lugares de t... |
| Q72 | - |  |  | SI | investigacion y capacitacion de RRHH, establecimie... |
| Q73 | - |  |  | SI | investigacion y capacitacion de RRHH, oficina inte... |
| Q74 | - |  |  | SI | investigacion y capacitacion de RRHH, otros, activ... |
| QHR | - |  |  | SI | Establecimiento de Salud |
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