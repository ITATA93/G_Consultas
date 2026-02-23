# TCBI_Cubes_LBInstrument.Fact

**Schema:** TCBI_Cubes_LBInstrument
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1276093255 | bigint |  |  | SI | Dimension: Dx1276093255<br/>
Source: LBIEInstrume... |
| Dx2452736604 | bigint |  |  | SI | Dimension: Dx2452736604<br/>
Source: LBIEInstrume... |
| Dx2879783836 | varchar |  |  | SI | Dimension: Dx2879783836<br/>
Source: LBIEStartDat... |
| Dx3111400002 | bigint |  |  | SI | Dimension: Dx3111400002<br/>
Source: LBIEInstrume... |
| Dx549219144 | bigint |  |  | SI | Dimension: Dx549219144<br/>
Source: LBIEInstrumen... |
| Dx734426422 | varchar |  |  | SI | Dimension: Dx734426422<br/>
Source: LBIEStartDate |
| DxLBCIETDescViaLBIETypeDR | bigint |  | FK | SI | Dimension: DxLBCIETDescViaLBIETypeDR<br/>
Source:... |
| DxLBCIETNotesViaLBIETypeDR | bigint |  | FK | SI | Dimension: DxLBCIETNotesViaLBIETypeDR<br/>
Source... |
| DxLBIEStartDate | date |  |  | SI | Dimension: DxLBIEStartDate<br/>
Source: LBIEStart... |
| DxLBIEStartDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBIEStartDateFxMonthYear<br/>
Source... |
| DxLBIEStartDateFxYear | varchar |  |  | SI | Dimension: DxLBIEStartDateFxYear<br/>
Source: LBI... |
| DxSSUSRNameViaLBIEUserDR | bigint |  | FK | SI | Dimension: DxSSUSRNameViaLBIEUserDR<br/>
Source: ... |
| DxStartDayOfWeek | bigint |  |  | SI | Dimension: DxStartDayOfWeek
Expression: ##class(T... |
| DxStartTime | bigint |  |  | SI | Dimension: DxStartTime
Expression: $ztime(%source... |
| DxStartTimeRange | bigint |  |  | SI | Dimension: DxStartTimeRange
Expression: %source.L... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*