# TCBI_Cubes_LBTestSet.Fact

**Schema:** TCBI_Cubes_LBTestSet
**Columnas:** 145
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1003733195 | varchar |  |  | SI | Dimension: Dx1003733195<br/>
Source: LBTSCollecte... |
| Dx1019034337 | varchar |  |  | SI | Dimension: Dx1019034337<br/>
Source: LBTSDeauthor... |
| Dx1033026164 | varchar |  |  | SI | Dimension: Dx1033026164<br/>
Source: LBTSEnteredD... |
| Dx1105495296 | bigint |  |  | SI | Dimension: Dx1105495296
Expression: ##class(web.L... |
| Dx1150885799 | varchar |  |  | SI | Dimension: Dx1150885799<br/>
Source: LBTSOrderDat... |
| Dx1150936988 | bigint |  |  | SI | Dimension: Dx1150936988
Expression: ##class(TCBI.... |
| Dx1217015244 | bigint |  |  | SI | Dimension: Dx1217015244
Expression: %source.LBTSP... |
| Dx1221024580 | bigint |  |  | SI | Dimension: Dx1221024580
Expression: ##class(web.L... |
| Dx1237898957 | bigint |  |  | SI | Dimension: Dx1237898957
Expression: ##class(web.L... |
| Dx1256134610 | varchar |  |  | SI | Dimension: Dx1256134610<br/>
Source: LBTSAuthoris... |
| Dx1360174243 | varchar |  |  | SI | Dimension: Dx1360174243<br/>
Source: LBTSCancella... |
| Dx1362573462 | bigint |  |  | SI | Dimension: Dx1362573462
Expression: $ztime(%sourc... |
| Dx1521201648 | varchar |  |  | SI | Dimension: Dx1521201648<br/>
Source: LBTSPrelimin... |
| Dx1535119998 | bigint |  |  | SI | Dimension: Dx1535119998
Expression: %source.LBTSO... |
| Dx1608623968 | varchar |  |  | SI | Dimension: Dx1608623968<br/>
Source: LBTSCancella... |
| Dx1635862466 | bigint |  |  | SI | Dimension: Dx1635862466
Expression: ##class(TCBI.... |
| Dx1647546171 | bigint |  |  | SI | Dimension: Dx1647546171
Expression: $ztime(%sourc... |
| Dx1665499426 | bigint |  |  | SI | Dimension: Dx1665499426
Expression: ##class(TCBI.... |
| Dx1698725650 | bigint |  |  | SI | Dimension: Dx1698725650
Expression: %source.LBTSR... |
| Dx1732320360 | varchar |  |  | SI | Dimension: Dx1732320360<br/>
Source: LBTSPrelimin... |
| Dx1997383642 | bigint |  |  | SI | Dimension: Dx1997383642
Expression: $ztime(%sourc... |
| Dx2085037580 | varchar |  |  | SI | Dimension: Dx2085037580<br/>
Source: LBTSOrderDat... |
| Dx2096223106 | varchar |  |  | SI | Dimension: Dx2096223106<br/>
Source: LBTSCollecte... |
| Dx213537805 | varchar |  |  | SI | Dimension: Dx213537805<br/>
Source: LBTSReceivedD... |
| Dx2159249995 | varchar |  |  | SI | Dimension: Dx2159249995<br/>
Source: LBTSEnteredD... |
| Dx2244174759 | bigint |  |  | SI | Dimension: Dx2244174759
Expression: ##class(web.L... |
| Dx2308660708 | varchar |  |  | SI | Dimension: Dx2308660708<br/>
Source: LBTSReceived... |
| Dx2367953216 | bigint |  |  | SI | Dimension: Dx2367953216
Expression: %source.LBTSD... |
| Dx2378256004 | bigint |  |  | SI | Dimension: Dx2378256004
Expression: %source.LBTSC... |
| Dx2439013100 | varchar |  |  | SI | Dimension: Dx2439013100<br/>
Source: LBTSDeauthor... |
| Dx2587128100 | varchar |  |  | SI | Dimension: Dx2587128100<br/>
Source: LBTSCollecte... |
| Dx2825977332 | varchar |  |  | SI | Dimension: Dx2825977332<br/>
Source: LBTSOrderDat... |
| Dx294175862 | bigint |  |  | SI | Dimension: Dx294175862
Expression: $ztime(%source... |
| Dx2944204694 | varchar |  |  | SI | Dimension: Dx2944204694<br/>
Source: LBTSEnteredD... |
| Dx3003531172 | varchar |  |  | SI | Dimension: Dx3003531172<br/>
Source: LBTSDeauthor... |
| Dx3003663667 | varchar |  |  | SI | Dimension: Dx3003663667<br/>
Source: LBTSCancella... |
| Dx3016082642 | varchar |  |  | SI | Dimension: Dx3016082642<br/>
Source: LBTSAuthoris... |
| Dx3042388019 | bigint |  |  | SI | Dimension: Dx3042388019
Expression: ##class(TCBI.... |
| Dx3057800099 | varchar |  |  | SI | Dimension: Dx3057800099<br/>
Source: LBTSPrelimin... |
| Dx3154985501 | bigint |  |  | SI | Dimension: Dx3154985501
Expression: ##class(TCBI.... |
| Dx3253509699 | varchar |  |  | SI | Dimension: Dx3253509699<br/>
Source: LBTSEnteredD... |
| Dx330280626 | varchar |  |  | SI | Dimension: Dx330280626<br/>
Source: LBTSAuthorise... |
| Dx339491288 | bigint |  |  | SI | Dimension: Dx339491288
Expression: ##class(web.LB... |
| Dx3454441423 | bigint |  |  | SI | Dimension: Dx3454441423
Expression: ##class(TCBI.... |
| Dx3476298439 | varchar |  |  | SI | Dimension: Dx3476298439<br/>
Source: LBTSPrelimin... |
| Dx3492394822 | varchar |  |  | SI | Dimension: Dx3492394822<br/>
Source: LBTSDeauthor... |
| Dx3495221426 | varchar |  |  | SI | Dimension: Dx3495221426<br/>
Source: LBTSDeauthor... |
| Dx3514521639 | varchar |  |  | SI | Dimension: Dx3514521639<br/>
Source: LBTSEnteredD... |
| Dx3610911384 | varchar |  |  | SI | Dimension: Dx3610911384<br/>
Source: LBTSCollecte... |
| Dx3679729955 | varchar |  |  | SI | Dimension: Dx3679729955<br/>
Source: LBTSCancella... |
| Dx372491134 | varchar |  |  | SI | Dimension: Dx372491134<br/>
Source: LBTSReceivedD... |
| Dx3763582558 | varchar |  |  | SI | Dimension: Dx3763582558<br/>
Source: LBTSReceived... |
| Dx3805554281 | varchar |  |  | SI | Dimension: Dx3805554281<br/>
Source: LBTSCancella... |
| Dx3892608821 | varchar |  |  | SI | Dimension: Dx3892608821<br/>
Source: LBTSReceived... |
| Dx3946904357 | bigint |  |  | SI | Dimension: Dx3946904357
Expression: ##class(TCBI.... |
| Dx4019690329 | bigint |  |  | SI | Dimension: Dx4019690329<br/>
Source: LBTSSpecimen... |
| Dx4035084220 | bigint |  |  | SI | Dimension: Dx4035084220
Expression: $ztime(%sourc... |
| Dx4051126809 | varchar |  |  | SI | Dimension: Dx4051126809<br/>
Source: LBTSDeauthor... |
| Dx4245293132 | bigint |  |  | SI | Dimension: Dx4245293132
Expression: %source.LBTSA... |
| Dx4282797281 | varchar |  |  | SI | Dimension: Dx4282797281<br/>
Source: LBTSAuthoris... |
| Dx456057886 | bigint |  |  | SI | Dimension: Dx456057886
Expression: $ztime(%source... |
| Dx623491154 | bigint |  |  | SI | Dimension: Dx623491154
Expression: $ztime(%source... |
| Dx671511838 | varchar |  |  | SI | Dimension: Dx671511838<br/>
Source: LBTSAuthorise... |
| Dx673128691 | bigint |  |  | SI | Dimension: Dx673128691
Expression: $ztime(%source... |
| Dx703519714 | varchar |  |  | SI | Dimension: Dx703519714<br/>
Source: LBTSCancellat... |
| Dx727638129 | varchar |  |  | SI | Dimension: Dx727638129<br/>
Source: LBTSPrelimina... |
| Dx733867592 | bigint |  |  | SI | Dimension: Dx733867592
Expression: %source.LBTSCo... |
| Dx750911268 | varchar |  |  | SI | Dimension: Dx750911268<br/>
Source: LBTSOrderDate |
| Dx759468767 | varchar |  |  | SI | Dimension: Dx759468767<br/>
Source: LBTSCollected... |
| Dx867210296 | bigint |  |  | SI | Dimension: Dx867210296
Expression: ##class(web.LB... |
| Dx957326199 | bigint |  |  | SI | Dimension: Dx957326199
Expression: %source.LBTSEn... |
| Dx971617506 | bigint |  |  | SI | Dimension: Dx971617506
Expression: ##class(web.LB... |
| DxAuthDayOfWeek | bigint |  |  | SI | Dimension: DxAuthDayOfWeek
Expression: ##class(TC... |
| DxCTLOCDescViaLBTSLabSiteDR | bigint |  | FK | SI | Dimension: DxCTLOCDescViaLBTSLabSiteDR<br/>
Sourc... |
| DxCancellationDayOfWeek | bigint |  |  | SI | Dimension: DxCancellationDayOfWeek
Expression: ##... |
| DxCancellationSecurityGroup | bigint |  |  | SI | Dimension: DxCancellationSecurityGroup<br/>
Sourc... |
| DxCancellationUserName | bigint |  |  | SI | Dimension: DxCancellationUserName<br/>
Source: LB... |
| DxClinicalReview | bigint |  |  | SI | Dimension: DxClinicalReview
Expression: %expressi... |
| DxCollectedDayOfWeek | bigint |  |  | SI | Dimension: DxCollectedDayOfWeek
Expression: ##cla... |
| DxCollectingSecurityGroup | bigint |  |  | SI | Dimension: DxCollectingSecurityGroup<br/>
Source:... |
| DxCollectingUserName | bigint |  |  | SI | Dimension: DxCollectingUserName<br/>
Source: LBTS... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBTSEpis... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: %ID |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBTSEpisod... |
| DxDeauthorisationDayOfWeek | bigint |  |  | SI | Dimension: DxDeauthorisationDayOfWeek
Expression:... |
| DxDeauthorisationSecurityGroup | bigint |  |  | SI | Dimension: DxDeauthorisationSecurityGroup<br/>
So... |
| DxDeauthorisationUserName | bigint |  |  | SI | Dimension: DxDeauthorisationUserName<br/>
Source:... |
| DxDepartment | bigint |  |  | SI | Dimension: DxDepartment<br/>
Source: LBTSTestSetD... |
| DxEnteredDayOfWeek | bigint |  |  | SI | Dimension: DxEnteredDayOfWeek
Expression: ##class... |
| DxEnteringSecurityGroup | bigint |  |  | SI | Dimension: DxEnteringSecurityGroup<br/>
Source: L... |
| DxEnteringUserName | bigint |  |  | SI | Dimension: DxEnteringUserName<br/>
Source: LBTSEn... |
| DxExtendedValidity | bigint |  |  | SI | Dimension: DxExtendedValidity
Expression: %expres... |
| DxInvalidAtReceive | bigint |  |  | SI | Dimension: DxInvalidAtReceive
Expression: %expres... |
| DxLBTSAuthoriseDate | date |  |  | SI | Dimension: DxLBTSAuthoriseDate<br/>
Source: LBTSA... |
| DxLBTSAuthoriseDateFxYear | varchar |  |  | SI | Dimension: DxLBTSAuthoriseDateFxYear<br/>
Source:... |
| DxLBTSCancellationDate | date |  |  | SI | Dimension: DxLBTSCancellationDate<br/>
Source: LB... |
| DxLBTSCollectedDate | date |  |  | SI | Dimension: DxLBTSCollectedDate<br/>
Source: LBTSC... |
| DxLBTSCollectedDateFxYear | varchar |  |  | SI | Dimension: DxLBTSCollectedDateFxYear<br/>
Source:... |
| DxLBTSDeauthorisationDate | date |  |  | SI | Dimension: DxLBTSDeauthorisationDate<br/>
Source:... |
| DxLBTSEnteredDate | date |  |  | SI | Dimension: DxLBTSEnteredDate<br/>
Source: LBTSEnt... |
| DxLBTSEnteredDateFxYear | varchar |  |  | SI | Dimension: DxLBTSEnteredDateFxYear<br/>
Source: L... |
| DxLBTSOrderDate | date |  |  | SI | Dimension: DxLBTSOrderDate<br/>
Source: LBTSOrder... |
| DxLBTSOrderDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBTSOrderDateFxMonthYear<br/>
Source... |
| DxLBTSOrderDateFxYear | varchar |  |  | SI | Dimension: DxLBTSOrderDateFxYear<br/>
Source: LBT... |
| DxLBTSPreliminaryDate | date |  |  | SI | Dimension: DxLBTSPreliminaryDate<br/>
Source: LBT... |
| DxLBTSPreliminaryDateFxYear | varchar |  |  | SI | Dimension: DxLBTSPreliminaryDateFxYear<br/>
Sourc... |
| DxLBTSReagent | varchar |  |  | SI | Dimension: DxLBTSReagent
Expression: %expression.... |
| DxLBTSReagentBatchNumber | varchar |  |  | SI | Dimension: DxLBTSReagentBatchNumber
Expression: %... |
| DxLBTSReceivedDate | date |  |  | SI | Dimension: DxLBTSReceivedDate<br/>
Source: LBTSRe... |
| DxLBTSReceivedDateFxYear | varchar |  |  | SI | Dimension: DxLBTSReceivedDateFxYear<br/>
Source: ... |
| DxLBTSValidityExtensionReason | bigint |  |  | SI | Dimension: DxLBTSValidityExtensionReason<br/>
Sou... |
| DxOrderDayOfWeek | bigint |  |  | SI | Dimension: DxOrderDayOfWeek
Expression: ##class(T... |
| DxOrderingSecurityGroup | bigint |  |  | SI | Dimension: DxOrderingSecurityGroup<br/>
Source: L... |
| DxOrderingUserName | bigint |  |  | SI | Dimension: DxOrderingUserName<br/>
Source: LBTSOr... |
| DxPreliminaryDayOfWeek | bigint |  |  | SI | Dimension: DxPreliminaryDayOfWeek
Expression: ##c... |
| DxPreliminarySecurityGroup | bigint |  |  | SI | Dimension: DxPreliminarySecurityGroup<br/>
Source... |
| DxPreliminaryUserName | bigint |  |  | SI | Dimension: DxPreliminaryUserName<br/>
Source: LBT... |
| DxPriority | bigint |  |  | SI | Dimension: DxPriority<br/>
Source: LBTSPriorityDR... |
| DxReasonNotPerformed | bigint |  |  | SI | Dimension: DxReasonNotPerformed<br/>
Source: LBTS... |
| DxReceivedDayOfWeek | bigint |  |  | SI | Dimension: DxReceivedDayOfWeek
Expression: ##clas... |
| DxReceivingSecurityGroup | bigint |  |  | SI | Dimension: DxReceivingSecurityGroup<br/>
Source: ... |
| DxReceivingUserName | bigint |  |  | SI | Dimension: DxReceivingUserName<br/>
Source: LBTSR... |
| DxReferralLab | bigint |  |  | SI | Dimension: DxReferralLab<br/>
Source: LBTSReferra... |
| DxSecurityGroup | bigint |  |  | SI | Dimension: DxSecurityGroup<br/>
Source: LBTSAutho... |
| DxSpecimenValidityExceeded | bigint |  |  | SI | Dimension: DxSpecimenValidityExceeded
Expression:... |
| DxSpecimenValidityExceededSlot | bigint |  |  | SI | Dimension: DxSpecimenValidityExceededSlot
Express... |
| DxStatusResult | bigint |  |  | SI | Dimension: DxStatusResult
Expression: %expression... |
| DxTestSet | bigint |  |  | SI | Dimension: DxTestSet<br/>
Source: LBTSTestSetDR.L... |
| DxTurnaroundTime | bigint |  |  | SI | Dimension: DxTurnaroundTime<br/>
Source: LBTSTurn... |
| DxTurnaroundTimeFail | bigint |  |  | SI | Dimension: DxTurnaroundTimeFail
Expression: %expr... |
| DxTurnaroundTimeFlag | bigint |  |  | SI | Dimension: DxTurnaroundTimeFlag
Expression: %expr... |
| DxTurnaroundTimeSlot | bigint |  |  | SI | Dimension: DxTurnaroundTimeSlot
Expression: ##cla... |
| DxUserName | bigint |  |  | SI | Dimension: DxUserName<br/>
Source: LBTSAuthorised... |
| DxWithinValidityPeriod | bigint |  |  | SI | Dimension: DxWithinValidityPeriod
Expression: %ex... |
| MxNumberIT | double |  |  | SI | Measure: MxNumberIT
Expression: %source.LBTSTurna... |
| MxNumberTTFail | double |  |  | SI | Measure: MxNumberTTFail
Expression: (%source.LBTS... |
| NumberClinicalReviewMx | double |  |  | SI | Measure: NumberClinicalReviewMx
Expression: %sour... |
| NumberExtendedMx | double |  |  | SI | Measure: NumberExtendedMx
Expression: %expression... |
| NumberInvalidMx | double |  |  | SI | Measure: NumberInvalidMx
Expression: %expression.... |
| NumberValidMx | double |  |  | SI | Measure: NumberValidMx
Expression: %expression.Wi... |
| RxLBTSEpisodeDR | bigint |  | FK | SI | Relationship: RxLBTSEpisodeDR<br/>
Source: LBTSEp... |
| RxLBTSOrdItemDR | bigint |  | FK | SI | Relationship: RxLBTSOrdItemDR<br/>
Source: LBTSOr... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*