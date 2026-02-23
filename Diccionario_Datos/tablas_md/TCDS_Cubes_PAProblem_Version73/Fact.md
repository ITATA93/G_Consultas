# TCDS_Cubes_PAProblem_Version73.Fact

**Schema:** TCDS_Cubes_PAProblem_Version73
**Columnas:** 32
**Actualizado:** 2026-01-30 15:31:52

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1270110534 | bigint |  |  | SI | Dimension: Dx1270110534<br/>
Source: PROBICPC2Cod... |
| Dx1577460993 | bigint |  |  | SI | Dimension: Dx1577460993<br/>
Source: PROBSnomedTe... |
| Dx4283355078 | bigint |  |  | SI | Dimension: Dx4283355078<br/>
Source: PROBSnomedCo... |
| Dx928107184 | varchar |  |  | SI | Dimension: Dx928107184<br/>
Source: PROBOnsetDate |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider
Expression: "sourceCare... |
| DxCategory | bigint |  |  | SI | Dimension: DxCategory
Expression: "sourceCategory... |
| DxCategoryCode | bigint |  |  | SI | Dimension: DxCategoryCode
Expression: "sourceCate... |
| DxCauseOfDeath | bigint |  |  | SI | Dimension: DxCauseOfDeath
Expression: "sourceCaus... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: PROBParRef... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation
Expression: "sourceLocation... |
| DxMRCIDDescViaPROBICDCodeDR | bigint |  | FK | SI | Dimension: DxMRCIDDescViaPROBICDCodeDR<br/>
Sourc... |
| DxPROBEndDate | date |  |  | SI | Dimension: DxPROBEndDate<br/>
Source: PROBEndDate |
| DxPROBEndDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxPROBEndDateFxDayMonthYear<br/>
Sourc... |
| DxPROBEndDateFxMonthYear | varchar |  |  | SI | Dimension: DxPROBEndDateFxMonthYear<br/>
Source: ... |
| DxPROBEndDateFxYear | varchar |  |  | SI | Dimension: DxPROBEndDateFxYear<br/>
Source: PROBE... |
| DxPROBMainEpisDiagnos | bigint |  |  | SI | Dimension: DxPROBMainEpisDiagnos<br/>
Source: PRO... |
| DxPROBOnsetDate | date |  |  | SI | Dimension: DxPROBOnsetDate<br/>
Source: PROBOnset... |
| DxPROBOnsetDateFxMonthYear | varchar |  |  | SI | Dimension: DxPROBOnsetDateFxMonthYear<br/>
Source... |
| DxPROBOnsetDateFxYear | varchar |  |  | SI | Dimension: DxPROBOnsetDateFxYear<br/>
Source: PRO... |
| DxPROBProvisionalDiagnos | bigint |  |  | SI | Dimension: DxPROBProvisionalDiagnos<br/>
Source: ... |
| DxPROBUpdateDate | date |  |  | SI | Dimension: DxPROBUpdateDate<br/>
Source: PROBUpda... |
| DxSEVDescViaPROBSeverityDR | bigint |  | FK | SI | Dimension: DxSEVDescViaPROBSeverityDR<br/>
Source... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus
Expression: "sourceStatusDesc... |
| DxStatusCode | bigint |  |  | SI | Dimension: DxStatusCode
Expression: "StatusCode" |
| DxUpdateDateTime | bigint |  |  | SI | Dimension: DxUpdateDateTime
Expression: %cube.Dat... |
| DxUpdateDay | varchar |  |  | SI | Dimension: DxUpdateDay<br/>
Source: PROBUpdateDat... |
| DxUpdateMonth | varchar |  |  | SI | Dimension: DxUpdateMonth<br/>
Source: PROBUpdateD... |
| DxUpdateQuarter | varchar |  |  | SI | Dimension: DxUpdateQuarter<br/>
Source: PROBUpdat... |
| DxUpdateYear | varchar |  |  | SI | Dimension: DxUpdateYear<br/>
Source: PROBUpdateDa... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*