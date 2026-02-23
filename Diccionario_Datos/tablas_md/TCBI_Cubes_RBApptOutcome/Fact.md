# TCBI_Cubes_RBApptOutcome.Fact

**Schema:** TCBI_Cubes_RBApptOutcome
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxCreatePathway | bigint |  |  | SI | Dimension: DxCreatePathway<br/>
Source: OUTCApOut... |
| DxCreateWL | bigint |  |  | SI | Dimension: DxCreateWL<br/>
Source: OUTCApOutcomeD... |
| DxDischargeFlag | bigint |  |  | SI | Dimension: DxDischargeFlag<br/>
Source: OUTCApOut... |
| DxOutcomeApptId | bigint |  |  | SI | Dimension: DxOutcomeApptId<br/>
Source: OUTCParRe... |
| DxOutcomeCode | bigint |  |  | SI | Dimension: DxOutcomeCode<br/>
Source: OUTCApOutco... |
| DxOutcomeDate | bigint |  |  | SI | Dimension: DxOutcomeDate<br/>
Source: OUTCDate |
| DxOutcomeDescription | bigint |  |  | SI | Dimension: DxOutcomeDescription<br/>
Source: OUTC... |
| DxOutcomeTime | bigint |  |  | SI | Dimension: DxOutcomeTime<br/>
Source: OUTCTime |
| DxRTTCode | bigint |  |  | SI | Dimension: DxRTTCode<br/>
Source: OUTCApOutcomeDR... |
| DxRTTDesc | bigint |  |  | SI | Dimension: DxRTTDesc<br/>
Source: OUTCApOutcomeDR... |
| DxRTTNationalCode | bigint |  |  | SI | Dimension: DxRTTNationalCode<br/>
Source: OUTCApO... |
| DxRTTRank | bigint |  |  | SI | Dimension: DxRTTRank<br/>
Source: OUTCApOutcomeDR... |
| DxRemoveWL | bigint |  |  | SI | Dimension: DxRemoveWL<br/>
Source: OUTCApOutcomeD... |
| DxStopPathway | bigint |  |  | SI | Dimension: DxStopPathway<br/>
Source: OUTCApOutco... |
| RxIDViaOUTCParRef | bigint |  |  | SI | Relationship: RxIDViaOUTCParRef<br/>
Source: OUTC... |
| RxIDViaOUTCWaitingListDR | bigint |  | FK | SI | Relationship: RxIDViaOUTCWaitingListDR<br/>
Sourc... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*