# TCBI_Cubes_PAPregnancy.Fact

**Schema:** TCBI_Cubes_PAPregnancy
**Columnas:** 38
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1051912876 | varchar |  |  | SI | Dimension: Dx1051912876<br/>
Source: PREGEdcAgree... |
| Dx1239934197 | varchar |  |  | SI | Dimension: Dx1239934197<br/>
Source: PREGEdcAgree... |
| Dx1372507958 | varchar |  |  | SI | Dimension: Dx1372507958<br/>
Source: PREGDateOfBo... |
| Dx2381767253 | varchar |  |  | SI | Dimension: Dx2381767253<br/>
Source: PREGEdcAgree... |
| Dx2462997204 | varchar |  |  | SI | Dimension: Dx2462997204<br/>
Source: PREGDateOfBo... |
| Dx276818094 | varchar |  |  | SI | Dimension: Dx276818094<br/>
Source: PREGDateOfBoo... |
| Dx2883324710 | varchar |  |  | SI | Dimension: Dx2883324710<br/>
Source: PREGDateOfBo... |
| Dx3173461349 | varchar |  |  | SI | Dimension: Dx3173461349<br/>
Source: PREGDateOfBo... |
| Dx3529181439 | varchar |  |  | SI | Dimension: Dx3529181439<br/>
Source: PREGEdcAgree... |
| Dx751380782 | bigint |  |  | SI | Dimension: Dx751380782<br/>
Source: PREGFeedInten... |
| DxAntenatal | varchar |  |  | SI | Dimension: DxAntenatal
Expression: %cube.GetAnteN... |
| DxAntenatalCare | bigint |  |  | SI | Dimension: DxAntenatalCare<br/>
Source: PREGAnten... |
| DxAntenatalCode | varchar |  |  | SI | Dimension: DxAntenatalCode
Expression: %cube.GetA... |
| DxBookingChangePlace | bigint |  |  | SI | Dimension: DxBookingChangePlace<br/>
Source: PREG... |
| DxBookingGestation | bigint |  |  | SI | Dimension: DxBookingGestation<br/>
Source: PREGBo... |
| DxChorionicity | bigint |  |  | SI | Dimension: DxChorionicity<br/>
Source: PREGChorio... |
| DxConsultingCareProvider | bigint |  |  | SI | Dimension: DxConsultingCareProvider<br/>
Source: ... |
| DxDeliveryPlanManagement | bigint |  |  | SI | Dimension: DxDeliveryPlanManagement<br/>
Source: ... |
| DxFirst | bigint |  |  | SI | Dimension: DxFirst<br/>
Source: PREGFirstPregnanc... |
| DxFoetusThisPregnancy | bigint |  |  | SI | Dimension: DxFoetusThisPregnancy<br/>
Source: PRE... |
| DxGravida | bigint |  |  | SI | Dimension: DxGravida<br/>
Source: PREGPersonDR.PA... |
| DxIntendedPlaceOfDelivery | bigint |  |  | SI | Dimension: DxIntendedPlaceOfDelivery<br/>
Source:... |
| DxIsRegularCycle | bigint |  |  | SI | Dimension: DxIsRegularCycle
Expression: %cube.IsR... |
| DxMenstruationHistory | varchar |  |  | SI | Dimension: DxMenstruationHistory
Expression: %cub... |
| DxMidwifeTeam | bigint |  |  | SI | Dimension: DxMidwifeTeam<br/>
Source: PREGMidComm... |
| DxOriginalBooking | bigint |  |  | SI | Dimension: DxOriginalBooking<br/>
Source: PREGOri... |
| DxPREGDateOfBooking | date |  |  | SI | Dimension: DxPREGDateOfBooking<br/>
Source: PREGD... |
| DxPREGDateOfBookingFxYear | varchar |  |  | SI | Dimension: DxPREGDateOfBookingFxYear<br/>
Source:... |
| DxPREGEdcAgreed | date |  |  | SI | Dimension: DxPREGEdcAgreed<br/>
Source: PREGEdcAg... |
| DxPREGEdcAgreedFxMonthYear | varchar |  |  | SI | Dimension: DxPREGEdcAgreedFxMonthYear<br/>
Source... |
| DxPREGEdcAgreedFxYear | varchar |  |  | SI | Dimension: DxPREGEdcAgreedFxYear<br/>
Source: PRE... |
| DxParity | bigint |  |  | SI | Dimension: DxParity<br/>
Source: PREGPersonDR.PAP... |
| DxPlannedFeedingType | bigint |  |  | SI | Dimension: DxPlannedFeedingType<br/>
Source: PREG... |
| DxPregnancyStatus | bigint |  |  | SI | Dimension: DxPregnancyStatus<br/>
Source: PREGSta... |
| Rx1230204054 | bigint |  |  | SI | Relationship: Rx1230204054<br/>
Source: PREGPerso... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*