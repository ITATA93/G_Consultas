# TCBI_Cubes_PAWaitingList.Fact

**Schema:** TCBI_Cubes_PAWaitingList
**Columnas:** 169
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1132850327 | bigint |  |  | SI | Dimension: Dx1132850327<br/>
Source: WLTriageOutc... |
| Dx1152751999 | date |  |  | SI | Dimension: Dx1152751999
Expression: $lg(%expressi... |
| Dx1157802194 | bigint |  |  | SI | Dimension: Dx1157802194<br/>
Source: WLTriageOutc... |
| Dx1235315800 | varchar |  |  | SI | Dimension: Dx1235315800<br/>
Source: WLDateConsul... |
| Dx1288684916 | varchar |  |  | SI | Dimension: Dx1288684916<br/>
Source: WLRefExpiryD... |
| Dx1345562005 | varchar |  |  | SI | Dimension: Dx1345562005<br/>
Source: WLDateOfList |
| Dx1399563897 | varchar |  |  | SI | Dimension: Dx1399563897<br/>
Source: WLEffectiveR... |
| Dx1455667706 | varchar |  |  | SI | Dimension: Dx1455667706 |
| Dx1500247417 | date |  |  | SI | Dimension: Dx1500247417
Expression: %cube.GetAppt... |
| Dx1556069108 | varchar |  |  | SI | Dimension: Dx1556069108<br/>
Source: WLEffectiveR... |
| Dx1649232475 | varchar |  |  | SI | Dimension: Dx1649232475 |
| Dx1687348115 | bigint |  |  | SI | Dimension: Dx1687348115<br/>
Source: WLWaitListSt... |
| Dx1727649123 | varchar |  |  | SI | Dimension: Dx1727649123<br/>
Source: WLDateGuaran... |
| Dx1875305062 | varchar |  |  | SI | Dimension: Dx1875305062<br/>
Source: WLRefExpiryD... |
| Dx1917815152 | varchar |  |  | SI | Dimension: Dx1917815152<br/>
Source: WLTreatmentS... |
| Dx2014766243 | varchar |  |  | SI | Dimension: Dx2014766243<br/>
Source: WLEffectiveR... |
| Dx2064767730 | varchar |  |  | SI | Dimension: Dx2064767730 |
| Dx2178739610 | varchar |  |  | SI | Dimension: Dx2178739610<br/>
Source: WLDateOfList |
| Dx2189430315 | varchar |  |  | SI | Dimension: Dx2189430315<br/>
Source: WLTreatmentS... |
| Dx2192197738 | varchar |  |  | SI | Dimension: Dx2192197738<br/>
Source: WLTriageDate |
| Dx2316318512 | varchar |  |  | SI | Dimension: Dx2316318512<br/>
Source: WLDateGuaran... |
| Dx2364655645 | varchar |  |  | SI | Dimension: Dx2364655645<br/>
Source: WLDateConsul... |
| Dx2393155592 | varchar |  |  | SI | Dimension: Dx2393155592 |
| Dx2499741424 | varchar |  |  | SI | Dimension: Dx2499741424<br/>
Source: WLEffectiveR... |
| Dx2565641542 | varchar |  |  | SI | Dimension: Dx2565641542 |
| Dx2686854951 | varchar |  |  | SI | Dimension: Dx2686854951<br/>
Source: WLRefExpiryD... |
| Dx270482839 | varchar |  |  | SI | Dimension: Dx270482839<br/>
Source: WLTreatmentSt... |
| Dx2727605620 | date |  |  | SI | Dimension: Dx2727605620
Expression: $lg(%expressi... |
| Dx2772995595 | varchar |  |  | SI | Dimension: Dx2772995595<br/>
Source: WLDateConsul... |
| Dx2778807016 | bigint |  |  | SI | Dimension: Dx2778807016<br/>
Source: WLTriageOutc... |
| Dx2824879496 | varchar |  |  | SI | Dimension: Dx2824879496<br/>
Source: WLDateGuaran... |
| Dx283119232 | varchar |  |  | SI | Dimension: Dx283119232 |
| Dx2838194850 | varchar |  |  | SI | Dimension: Dx2838194850 |
| Dx2841659947 | varchar |  |  | SI | Dimension: Dx2841659947<br/>
Source: WLRecallDate |
| Dx2871516330 | varchar |  |  | SI | Dimension: Dx2871516330<br/>
Source: WLTreatmentS... |
| Dx2968164679 | varchar |  |  | SI | Dimension: Dx2968164679<br/>
Source: WLDateGuaran... |
| Dx2973694542 | varchar |  |  | SI | Dimension: Dx2973694542 |
| Dx304363825 | varchar |  |  | SI | Dimension: Dx304363825 |
| Dx3089499856 | varchar |  |  | SI | Dimension: Dx3089499856 |
| Dx3106866782 | varchar |  |  | SI | Dimension: Dx3106866782<br/>
Source: WLDateReceiv... |
| Dx3114110204 | bigint |  |  | SI | Dimension: Dx3114110204<br/>
Source: WLSourceAtte... |
| Dx3233585828 | varchar |  |  | SI | Dimension: Dx3233585828<br/>
Source: WLDateReceiv... |
| Dx3248341820 | varchar |  |  | SI | Dimension: Dx3248341820<br/>
Source: WLRefExpiryD... |
| Dx329286088 | varchar |  |  | SI | Dimension: Dx329286088 |
| Dx3346374111 | varchar |  |  | SI | Dimension: Dx3346374111 |
| Dx337003999 | varchar |  |  | SI | Dimension: Dx337003999<br/>
Source: WLTreatmentSt... |
| Dx3422703831 | varchar |  |  | SI | Dimension: Dx3422703831<br/>
Source: WLDateReceiv... |
| Dx355133295 | varchar |  |  | SI | Dimension: Dx355133295<br/>
Source: WLDateReceive... |
| Dx364179388 | varchar |  |  | SI | Dimension: Dx364179388<br/>
Source: WLTriageDate |
| Dx3642645866 | varchar |  |  | SI | Dimension: Dx3642645866<br/>
Source: WLEffectiveR... |
| Dx3746499346 | varchar |  |  | SI | Dimension: Dx3746499346 |
| Dx3771236616 | varchar |  |  | SI | Dimension: Dx3771236616 |
| Dx3838454253 | varchar |  |  | SI | Dimension: Dx3838454253<br/>
Source: WLDateGuaran... |
| Dx3967654440 | varchar |  |  | SI | Dimension: Dx3967654440<br/>
Source: WLRecallDate |
| Dx3985657403 | varchar |  |  | SI | Dimension: Dx3985657403 |
| Dx3990263097 | varchar |  |  | SI | Dimension: Dx3990263097<br/>
Source: WLEffectiveR... |
| Dx4081107318 | varchar |  |  | SI | Dimension: Dx4081107318<br/>
Source: WLDateConsul... |
| Dx4177504140 | varchar |  |  | SI | Dimension: Dx4177504140<br/>
Source: WLTreatmentS... |
| Dx4190307644 | varchar |  |  | SI | Dimension: Dx4190307644<br/>
Source: WLDateReceiv... |
| Dx4194146282 | varchar |  |  | SI | Dimension: Dx4194146282<br/>
Source: WLDateConsul... |
| Dx4228508883 | varchar |  |  | SI | Dimension: Dx4228508883 |
| Dx4274903906 | varchar |  |  | SI | Dimension: Dx4274903906 |
| Dx4277909367 | varchar |  |  | SI | Dimension: Dx4277909367 |
| Dx432597130 | varchar |  |  | SI | Dimension: Dx432597130<br/>
Source: WLRefExpiryDa... |
| Dx510094225 | varchar |  |  | SI | Dimension: Dx510094225<br/>
Source: WLDateConsult... |
| DxAdmissionCategory | bigint |  |  | SI | Dimension: DxAdmissionCategory<br/>
Source: WLAdm... |
| DxAssignedUser | bigint |  |  | SI | Dimension: DxAssignedUser<br/>
Source: WLAssigned... |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider<br/>
Source: WLDoctorDR... |
| DxCareProviderType | bigint |  |  | SI | Dimension: DxCareProviderType<br/>
Source: WLDoct... |
| DxDaysOnListRange | bigint |  |  | SI | Dimension: DxDaysOnListRange<br/>
Source: WLDaysO... |
| DxDaysWaiting | bigint |  |  | SI | Dimension: DxDaysWaiting<br/>
Source: WLDaysWaiti... |
| DxDepartment | bigint |  |  | SI | Dimension: DxDepartment<br/>
Source: WLCTLOCDR.CT... |
| DxDepartmentCode | bigint |  |  | SI | Dimension: DxDepartmentCode<br/>
Source: WLCTLOCD... |
| DxEpisodeSubType | bigint |  |  | SI | Dimension: DxEpisodeSubType<br/>
Source: WLEpisSu... |
| DxEpisodeSubTypeCode | bigint |  |  | SI | Dimension: DxEpisodeSubTypeCode<br/>
Source: WLEp... |
| DxFundingCategoryDepartment | bigint |  |  | SI | Dimension: DxFundingCategoryDepartment<br/>
Sourc... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: WLHospitalDR.H... |
| DxHospitalCode | bigint |  |  | SI | Dimension: DxHospitalCode<br/>
Source: WLHospital... |
| DxIntendedOperation | bigint |  |  | SI | Dimension: DxIntendedOperation<br/>
Source: WLOpe... |
| DxIntendedProcedure | bigint |  |  | SI | Dimension: DxIntendedProcedure<br/>
Source: WLSta... |
| DxLinkedCareProvider | bigint |  |  | SI | Dimension: DxLinkedCareProvider<br/>
Source: WLDo... |
| DxLinkedCareProviderType | bigint |  |  | SI | Dimension: DxLinkedCareProviderType<br/>
Source: ... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: WLCTLOCDR.CTLO... |
| DxLocationCode | bigint |  |  | SI | Dimension: DxLocationCode<br/>
Source: WLCTLOCDR.... |
| DxNationalProcedureCode | bigint |  |  | SI | Dimension: DxNationalProcedureCode<br/>
Source: W... |
| DxNationalProcedureDesc | bigint |  |  | SI | Dimension: DxNationalProcedureDesc<br/>
Source: W... |
| DxNewWaysFlag | bigint |  |  | SI | Dimension: DxNewWaysFlag
Expression: %cube.GetNew... |
| DxOrderingOfficer | bigint |  |  | SI | Dimension: DxOrderingOfficer<br/>
Source: WLOrder... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: WLPAPMIDR.%ID |
| DxPrimaryWaitingList | bigint |  |  | SI | Dimension: DxPrimaryWaitingList
Expression: %cube... |
| DxRefStatusReason | bigint |  |  | SI | Dimension: DxRefStatusReason<br/>
Source: WLRefSt... |
| DxReferralDepartment | bigint |  |  | SI | Dimension: DxReferralDepartment<br/>
Source: WLRe... |
| DxReferralHospital | bigint |  |  | SI | Dimension: DxReferralHospital<br/>
Source: WLRefD... |
| DxReferralPriority | bigint |  |  | SI | Dimension: DxReferralPriority<br/>
Source: WLRefe... |
| DxReferralReason | bigint |  |  | SI | Dimension: DxReferralReason<br/>
Source: WLReferr... |
| DxReferralType | bigint |  |  | SI | Dimension: DxReferralType<br/>
Source: WLReferral... |
| DxReferralUniqueID | bigint |  |  | SI | Dimension: DxReferralUniqueID<br/>
Source: WLRefe... |
| DxReferredByClinic | bigint |  |  | SI | Dimension: DxReferredByClinic<br/>
Source: WLRefD... |
| DxReferredByDoctor | bigint |  |  | SI | Dimension: DxReferredByDoctor<br/>
Source: WLRefD... |
| DxReferredByHospital | bigint |  |  | SI | Dimension: DxReferredByHospital<br/>
Source: WLRe... |
| DxReferredByInternalCareProvider | bigint |  |  | SI | Dimension: DxReferredByInternalCareProvider<br/>
... |
| DxRemovalReason | bigint |  |  | SI | Dimension: DxRemovalReason
Expression: $lg(%expre... |
| DxRemovalReasonCode | bigint |  |  | SI | Dimension: DxRemovalReasonCode
Expression: $lg(%e... |
| DxReportableFlag | bigint |  |  | SI | Dimension: DxReportableFlag
Expression: %cube.Rep... |
| DxReviewStatus | varchar |  |  | SI | Dimension: DxReviewStatus
Expression: %cube.GetRe... |
| DxSourceOfAddition | bigint |  |  | SI | Dimension: DxSourceOfAddition<br/>
Source: WLSour... |
| DxSourceOfAttendance | bigint |  |  | SI | Dimension: DxSourceOfAttendance<br/>
Source: WLSo... |
| DxStopPathway | bigint |  |  | SI | Dimension: DxStopPathway
Expression: %cube.StopPa... |
| DxSurgeon | bigint |  |  | SI | Dimension: DxSurgeon<br/>
Source: WLSurgeonDR.CTP... |
| DxTrust | bigint |  |  | SI | Dimension: DxTrust<br/>
Source: WLTrustDR.TRUSTDe... |
| DxTrustCode | bigint |  |  | SI | Dimension: DxTrustCode<br/>
Source: WLTrustDR.TRU... |
| DxWLApptDate | date |  |  | SI | Dimension: DxWLApptDate<br/>
Source: WLApptDate |
| DxWLApptDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxWLApptDateFxDayMonthYear<br/>
Source... |
| DxWLApptDateFxMonthNumber | varchar |  |  | SI | Dimension: DxWLApptDateFxMonthNumber<br/>
Source:... |
| DxWLApptDateFxMonthYear | varchar |  |  | SI | Dimension: DxWLApptDateFxMonthYear<br/>
Source: W... |
| DxWLApptDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxWLApptDateFxQuarterNumber<br/>
Sourc... |
| DxWLApptDateFxQuarterYear | varchar |  |  | SI | Dimension: DxWLApptDateFxQuarterYear<br/>
Source:... |
| DxWLApptDateFxYear | varchar |  |  | SI | Dimension: DxWLApptDateFxYear<br/>
Source: WLAppt... |
| DxWLDate | date |  |  | SI | Dimension: DxWLDate<br/>
Source: WLDate |
| DxWLDateConsultRequestSent | date |  |  | SI | Dimension: DxWLDateConsultRequestSent<br/>
Source... |
| DxWLDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxWLDateFxDayMonthYear<br/>
Source: WL... |
| DxWLDateFxMonthNumber | varchar |  |  | SI | Dimension: DxWLDateFxMonthNumber<br/>
Source: WLD... |
| DxWLDateFxMonthYear | varchar |  |  | SI | Dimension: DxWLDateFxMonthYear<br/>
Source: WLDat... |
| DxWLDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxWLDateFxQuarterNumber<br/>
Source: W... |
| DxWLDateFxQuarterYear | varchar |  |  | SI | Dimension: DxWLDateFxQuarterYear<br/>
Source: WLD... |
| DxWLDateFxYear | varchar |  |  | SI | Dimension: DxWLDateFxYear<br/>
Source: WLDate |
| DxWLDateGuaranteed | date |  |  | SI | Dimension: DxWLDateGuaranteed<br/>
Source: WLDate... |
| DxWLDateGuaranteedFxYear | varchar |  |  | SI | Dimension: DxWLDateGuaranteedFxYear<br/>
Source: ... |
| DxWLDateOfList | date |  |  | SI | Dimension: DxWLDateOfList<br/>
Source: WLDateOfLi... |
| DxWLDateOfListFxMonthNumber | varchar |  |  | SI | Dimension: DxWLDateOfListFxMonthNumber<br/>
Sourc... |
| DxWLDateOfListFxMonthYear | varchar |  |  | SI | Dimension: DxWLDateOfListFxMonthYear<br/>
Source:... |
| DxWLDateOfListFxQuarterYear | varchar |  |  | SI | Dimension: DxWLDateOfListFxQuarterYear<br/>
Sourc... |
| DxWLDateOfListFxYear | varchar |  |  | SI | Dimension: DxWLDateOfListFxYear<br/>
Source: WLDa... |
| DxWLDateReceivedBack | date |  |  | SI | Dimension: DxWLDateReceivedBack<br/>
Source: WLDa... |
| DxWLDateReceivedBackFxYear | varchar |  |  | SI | Dimension: DxWLDateReceivedBackFxYear<br/>
Source... |
| DxWLEffectiveRemovalDate | date |  |  | SI | Dimension: DxWLEffectiveRemovalDate<br/>
Source: ... |
| DxWLRecallDate | date |  |  | SI | Dimension: DxWLRecallDate<br/>
Source: WLRecallDa... |
| DxWLRecallDateFxMonthNumber | varchar |  |  | SI | Dimension: DxWLRecallDateFxMonthNumber<br/>
Sourc... |
| DxWLRecallDateFxMonthYear | varchar |  |  | SI | Dimension: DxWLRecallDateFxMonthYear<br/>
Source:... |
| DxWLRecallDateFxQuarterYear | varchar |  |  | SI | Dimension: DxWLRecallDateFxQuarterYear<br/>
Sourc... |
| DxWLRecallDateFxYear | varchar |  |  | SI | Dimension: DxWLRecallDateFxYear<br/>
Source: WLRe... |
| DxWLRefExpiryDate | date |  |  | SI | Dimension: DxWLRefExpiryDate<br/>
Source: WLRefEx... |
| DxWLRefExpiryDateFxYear | varchar |  |  | SI | Dimension: DxWLRefExpiryDateFxYear<br/>
Source: W... |
| DxWLTreatmentStartDate | date |  |  | SI | Dimension: DxWLTreatmentStartDate<br/>
Source: WL... |
| DxWLTriageDate | date |  |  | SI | Dimension: DxWLTriageDate<br/>
Source: WLTriageDa... |
| DxWLTriageDateFxMonthNumber | varchar |  |  | SI | Dimension: DxWLTriageDateFxMonthNumber<br/>
Sourc... |
| DxWLTriageDateFxMonthYear | varchar |  |  | SI | Dimension: DxWLTriageDateFxMonthYear<br/>
Source:... |
| DxWLTriageDateFxQuarterYear | varchar |  |  | SI | Dimension: DxWLTriageDateFxQuarterYear<br/>
Sourc... |
| DxWLTriageDateFxYear | varchar |  |  | SI | Dimension: DxWLTriageDateFxYear<br/>
Source: WLTr... |
| DxWaitingListAccountClass | bigint |  |  | SI | Dimension: DxWaitingListAccountClass<br/>
Source:... |
| DxWaitingListCode | bigint |  |  | SI | Dimension: DxWaitingListCode<br/>
Source: WLWaitL... |
| DxWaitingListDescription | bigint |  |  | SI | Dimension: DxWaitingListDescription<br/>
Source: ... |
| DxWaitingListInsuranceCategory | bigint |  |  | SI | Dimension: DxWaitingListInsuranceCategory<br/>
So... |
| DxWaitingListPackageCover | bigint |  |  | SI | Dimension: DxWaitingListPackageCover
Expression: ... |
| DxWaitingListPayor | bigint |  |  | SI | Dimension: DxWaitingListPayor<br/>
Source: WLInsT... |
| DxWaitingListPayorCode | bigint |  |  | SI | Dimension: DxWaitingListPayorCode<br/>
Source: WL... |
| DxWaitingListPlan | bigint |  |  | SI | Dimension: DxWaitingListPlan<br/>
Source: WLAuxil... |
| DxWaitingListPlanCode | bigint |  |  | SI | Dimension: DxWaitingListPlanCode<br/>
Source: WLA... |
| DxWaitingListPriority | bigint |  |  | SI | Dimension: DxWaitingListPriority<br/>
Source: WLW... |
| DxWaitingListReasonForList | bigint |  |  | SI | Dimension: DxWaitingListReasonForList<br/>
Source... |
| DxWaitingListReasonForListCode | bigint |  |  | SI | Dimension: DxWaitingListReasonForListCode<br/>
So... |
| DxWaitingListStatus | bigint |  |  | SI | Dimension: DxWaitingListStatus<br/>
Source: WLWai... |
| DxWaitingListType | bigint |  |  | SI | Dimension: DxWaitingListType<br/>
Source: WLWaitL... |
| DxWeeksWaiting | bigint |  |  | SI | Dimension: DxWeeksWaiting
Expression: ##class(TCB... |
| MxTotalDaysOnList | double |  |  | SI | Measure: MxTotalDaysOnList<br/>
Source: WLDaysOnL... |
| RxPAPMIRowIdViaWLPAPMIDR | bigint |  | FK | SI | Relationship: RxPAPMIRowIdViaWLPAPMIDR<br/>
Sourc... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*