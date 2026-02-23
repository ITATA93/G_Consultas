# TCBI_Cubes_PAAdm2DischargeSummary.Fact

**Schema:** TCBI_Cubes_PAAdm2DischargeSummary
**Columnas:** 48
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1174131329 | varchar |  |  | SI | Dimension: Dx1174131329<br/>
Source: DISPADischar... |
| Dx1280491897 | varchar |  |  | SI | Dimension: Dx1280491897<br/>
Source: DISPADischar... |
| Dx1287784998 | varchar |  |  | SI | Dimension: Dx1287784998<br/>
Source: DISPADischar... |
| Dx1302514473 | varchar |  |  | SI | Dimension: Dx1302514473<br/>
Source: DISPADischar... |
| Dx1629844864 | varchar |  |  | SI | Dimension: Dx1629844864<br/>
Source: DISPADischar... |
| Dx2021016628 | varchar |  |  | SI | Dimension: Dx2021016628<br/>
Source: DISPADischar... |
| Dx2493490791 | varchar |  |  | SI | Dimension: Dx2493490791<br/>
Source: DISPADischar... |
| Dx2597836549 | date |  |  | SI | Dimension: Dx2597836549<br/>
Source: DISPADischar... |
| Dx2640453405 | varchar |  |  | SI | Dimension: Dx2640453405<br/>
Source: DISPADischar... |
| Dx2683514956 | varchar |  |  | SI | Dimension: Dx2683514956<br/>
Source: DISPADischar... |
| Dx2696618794 | varchar |  |  | SI | Dimension: Dx2696618794<br/>
Source: DISPADischar... |
| Dx2854792271 | date |  |  | SI | Dimension: Dx2854792271<br/>
Source: DISPADischar... |
| Dx3085335783 | date |  |  | SI | Dimension: Dx3085335783<br/>
Source: DISPADischar... |
| Dx3121506836 | varchar |  |  | SI | Dimension: Dx3121506836<br/>
Source: DISPADischar... |
| Dx3146411573 | varchar |  |  | SI | Dimension: Dx3146411573<br/>
Source: DISPADischar... |
| Dx3260598827 | varchar |  |  | SI | Dimension: Dx3260598827<br/>
Source: DISPADischar... |
| Dx3260690683 | varchar |  |  | SI | Dimension: Dx3260690683<br/>
Source: DISPADischar... |
| Dx3401192631 | date |  |  | SI | Dimension: Dx3401192631<br/>
Source: DISPADischar... |
| Dx3667020614 | varchar |  |  | SI | Dimension: Dx3667020614<br/>
Source: DISPADischar... |
| Dx3888992046 | varchar |  |  | SI | Dimension: Dx3888992046<br/>
Source: DISPADischar... |
| Dx3968860828 | varchar |  |  | SI | Dimension: Dx3968860828<br/>
Source: DISPADischar... |
| Dx43465093 | varchar |  |  | SI | Dimension: Dx43465093<br/>
Source: DISPADischarge... |
| Dx547876339 | varchar |  |  | SI | Dimension: Dx547876339<br/>
Source: DISPADischarg... |
| Dx603131364 | varchar |  |  | SI | Dimension: Dx603131364<br/>
Source: DISPADischarg... |
| Dx783362168 | varchar |  |  | SI | Dimension: Dx783362168<br/>
Source: DISPADischarg... |
| Dx7987407 | varchar |  |  | SI | Dimension: Dx7987407<br/>
Source: DISPADischargeS... |
| Dx958022256 | varchar |  |  | SI | Dimension: Dx958022256<br/>
Source: DISPADischarg... |
| Dx986126422 | varchar |  |  | SI | Dimension: Dx986126422<br/>
Source: DISPADischarg... |
| DxDischargeSummaryCareProvider | bigint |  |  | SI | Dimension: DxDischargeSummaryCareProvider<br/>
So... |
| DxDischargeSummaryLocation | bigint |  |  | SI | Dimension: DxDischargeSummaryLocation<br/>
Source... |
| DxDischargeToCreateDays | bigint |  |  | SI | Dimension: DxDischargeToCreateDays
Expression: ##... |
| DxDischargeToCreateRange | bigint |  |  | SI | Dimension: DxDischargeToCreateRange
Expression: #... |
| DxInternalStatus | bigint |  |  | SI | Dimension: DxInternalStatus<br/>
Source: DISPADis... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: DISParRef.PAA... |
| DxReferralCareProvider | bigint |  |  | SI | Dimension: DxReferralCareProvider<br/>
Source: DI... |
| DxReferralCategory | bigint |  |  | SI | Dimension: DxReferralCategory<br/>
Source: DISPAD... |
| DxReferralDoctor | bigint |  |  | SI | Dimension: DxReferralDoctor<br/>
Source: DISPADis... |
| DxReferralHospital | bigint |  |  | SI | Dimension: DxReferralHospital<br/>
Source: DISPAD... |
| DxReferralLocation | bigint |  |  | SI | Dimension: DxReferralLocation<br/>
Source: DISPAD... |
| DxReferralPriority | bigint |  |  | SI | Dimension: DxReferralPriority<br/>
Source: DISPAD... |
| DxReferralReason | bigint |  |  | SI | Dimension: DxReferralReason<br/>
Source: DISPADis... |
| DxReviewStatus | bigint |  |  | SI | Dimension: DxReviewStatus<br/>
Source: DISPADisch... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus
Expression: %cube.GetDischarg... |
| DxType | bigint |  |  | SI | Dimension: DxType<br/>
Source: DISPADischargeSumm... |
| Rx2272900870 | bigint |  |  | SI | Relationship: Rx2272900870<br/>
Source: DISParRef... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*