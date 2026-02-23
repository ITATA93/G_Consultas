# TCBI_Cubes_PAEnquiryContact.Fact

**Schema:** TCBI_Cubes_PAEnquiryContact
**Columnas:** 53
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| DxAge | bigint |  |  | SI | Dimension: DxAge
Expression: %cube.CalculateAge(%... |
| DxAgeGroup | bigint |  |  | SI | Dimension: DxAgeGroup
Expression: %cube.Calculate... |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider<br/>
Source: ENQCTCPDR.... |
| DxContactDayOfWeek | bigint |  |  | SI | Dimension: DxContactDayOfWeek
Expression: $system... |
| DxContactMethod | bigint |  |  | SI | Dimension: DxContactMethod<br/>
Source: ENQContMe... |
| DxContactMode | bigint |  |  | SI | Dimension: DxContactMode
Expression: %cube.GetCon... |
| DxContactOutcome | bigint |  |  | SI | Dimension: DxContactOutcome<br/>
Source: ENQContO... |
| DxContactTimeRange | bigint |  |  | SI | Dimension: DxContactTimeRange
Expression: %source... |
| DxContactType | bigint |  |  | SI | Dimension: DxContactType<br/>
Source: ENQRequestT... |
| DxENQDate | date |  |  | SI | Dimension: DxENQDate<br/>
Source: ENQDate |
| DxENQDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxENQDateFxDayMonthYear<br/>
Source: E... |
| DxENQDateFxMonthNumber | varchar |  |  | SI | Dimension: DxENQDateFxMonthNumber<br/>
Source: EN... |
| DxENQDateFxMonthYear | varchar |  |  | SI | Dimension: DxENQDateFxMonthYear<br/>
Source: ENQD... |
| DxENQDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxENQDateFxQuarterNumber<br/>
Source: ... |
| DxENQDateFxQuarterYear | varchar |  |  | SI | Dimension: DxENQDateFxQuarterYear<br/>
Source: EN... |
| DxENQDateFxYear | varchar |  |  | SI | Dimension: DxENQDateFxYear<br/>
Source: ENQDate |
| DxFundingCategory | bigint |  |  | SI | Dimension: DxFundingCategory<br/>
Source: ENQGove... |
| DxFundingDepartment | bigint |  |  | SI | Dimension: DxFundingDepartment<br/>
Source: ENQGo... |
| DxGender | bigint |  |  | SI | Dimension: DxGender<br/>
Source: ENQSexDR.CTSEXDe... |
| DxInterpreterType | bigint |  |  | SI | Dimension: DxInterpreterType<br/>
Source: ENQCont... |
| DxInterventions | varchar |  |  | SI | Dimension: DxInterventions
Expression: %cube.GetI... |
| DxLocalGoal | bigint |  |  | SI | Dimension: DxLocalGoal<br/>
Source: ENQContLocalG... |
| DxLocalPriority | varchar |  |  | SI | Dimension: DxLocalPriority
Expression: %cube.GetL... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: ENQCityAreaDR.... |
| DxOrganisation | bigint |  |  | SI | Dimension: DxOrganisation<br/>
Source: ENQNonGovO... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: ENQPAPERDR.PA... |
| DxPayor | bigint |  |  | SI | Dimension: DxPayor<br/>
Source: ENQInsTypeDR.INST... |
| DxPlan | bigint |  |  | SI | Dimension: DxPlan<br/>
Source: ENQAuxInsTypeDR.AU... |
| DxPopulationGroup | bigint |  |  | SI | Dimension: DxPopulationGroup<br/>
Source: ENQSour... |
| DxPresentingIssue | varchar |  |  | SI | Dimension: DxPresentingIssue
Expression: %cube.Ge... |
| DxProgram | bigint |  |  | SI | Dimension: DxProgram<br/>
Source: ENQGovernDepart... |
| DxProgramPriority | bigint |  |  | SI | Dimension: DxProgramPriority<br/>
Source: ENQCons... |
| DxReferralTo | varchar |  |  | SI | Dimension: DxReferralTo
Expression: %cube.GetRefe... |
| DxRequestStatus | bigint |  |  | SI | Dimension: DxRequestStatus<br/>
Source: ENQReques... |
| DxSTONumber | bigint |  |  | SI | Dimension: DxSTONumber<br/>
Source: ENQText1 |
| DxService | bigint |  |  | SI | Dimension: DxService<br/>
Source: ENQHospitalDR.H... |
| DxServiceType | bigint |  |  | SI | Dimension: DxServiceType<br/>
Source: ENQItemCatD... |
| DxServicesProvidedBy | varchar |  |  | SI | Dimension: DxServicesProvidedBy
Expression: %cube... |
| DxServicesReceivedBy | varchar |  |  | SI | Dimension: DxServicesReceivedBy
Expression: %cube... |
| DxSuburb | bigint |  |  | SI | Dimension: DxSuburb<br/>
Source: ENQCityDR.CTCITD... |
| DxTeam | bigint |  |  | SI | Dimension: DxTeam<br/>
Source: ENQLocationDR.CTLO... |
| DxVenue | bigint |  |  | SI | Dimension: DxVenue<br/>
Source: ENQContVenueDR.CO... |
| DxWorkerType | bigint |  |  | SI | Dimension: DxWorkerType<br/>
Source: ENQContWorke... |
| MxDirectTime | double |  |  | SI | Measure: MxDirectTime
Expression: %source.ENQDura... |
| MxIndirectTime | double |  |  | SI | Measure: MxIndirectTime
Expression: %source.ENQIn... |
| MxInterpretingTime | double |  |  | SI | Measure: MxInterpretingTime
Expression: %source.E... |
| MxTravelTime | double |  |  | SI | Measure: MxTravelTime
Expression: %source.ENQTrav... |
| RxIDViaENQOEOrdItemDR | bigint |  | FK | SI | Relationship: RxIDViaENQOEOrdItemDR<br/>
Source: ... |
| RxIDViaENQPAPERDR | bigint |  | FK | SI | Relationship: RxIDViaENQPAPERDR<br/>
Source: ENQP... |
| RxIDViaENQRBEventTimesDR | bigint |  | FK | SI | Relationship: RxIDViaENQRBEventTimesDR<br/>
Sourc... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*