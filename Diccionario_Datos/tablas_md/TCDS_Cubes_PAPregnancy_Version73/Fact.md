# TCDS_Cubes_PAPregnancy_Version73.Fact

**Schema:** TCDS_Cubes_PAPregnancy_Version73
**Columnas:** 28
**Actualizado:** 2026-01-30 15:31:50

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

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
| Dx2381767253 | varchar |  |  | SI | Dimension: Dx2381767253<br/>
Source: PREGEdcAgree... |
| Dx3529181439 | varchar |  |  | SI | Dimension: Dx3529181439<br/>
Source: PREGEdcAgree... |
| DxAntenatal | varchar |  |  | SI | Dimension: DxAntenatal
Expression: %cube.GetAnteN... |
| DxAntenatalCare | bigint |  |  | SI | Dimension: DxAntenatalCare<br/>
Source: PREGAnten... |
| DxAntenatalCode | varchar |  |  | SI | Dimension: DxAntenatalCode
Expression: %cube.GetA... |
| DxBookingChangePlace | bigint |  |  | SI | Dimension: DxBookingChangePlace
Expression: "sour... |
| DxBookingGestation | bigint |  |  | SI | Dimension: DxBookingGestation<br/>
Source: PREGBo... |
| DxConsultingCareProvider | bigint |  |  | SI | Dimension: DxConsultingCareProvider<br/>
Source: ... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: PREGPerson... |
| DxDeliveryPlanManagement | bigint |  |  | SI | Dimension: DxDeliveryPlanManagement<br/>
Source: ... |
| DxFoetusThisPregnancy | bigint |  |  | SI | Dimension: DxFoetusThisPregnancy<br/>
Source: PRE... |
| DxGravida | bigint |  |  | SI | Dimension: DxGravida<br/>
Source: PREGPersonDR.PA... |
| DxIntendedPlaceOfDelivery | bigint |  |  | SI | Dimension: DxIntendedPlaceOfDelivery<br/>
Source:... |
| DxIsRegularCycle | bigint |  |  | SI | Dimension: DxIsRegularCycle
Expression: "sourceIs... |
| DxMenstruationHistory | bigint |  |  | SI | Dimension: DxMenstruationHistory
Expression: "sou... |
| DxMidwifeTeam | bigint |  |  | SI | Dimension: DxMidwifeTeam<br/>
Source: PREGMidComm... |
| DxOriginalBooking | bigint |  |  | SI | Dimension: DxOriginalBooking<br/>
Source: PREGOri... |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*