# TCBI_Cubes_MRNursingNotes.Fact

**Schema:** TCBI_Cubes_MRNursingNotes
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx3089946601 | varchar |  |  | SI | Dimension: Dx3089946601<br/>
Source: NOTDateAuth |
| DxCareProviderEntered | bigint |  |  | SI | Dimension: DxCareProviderEntered<br/>
Source: NOT... |
| DxCareProviderGroup | bigint |  |  | SI | Dimension: DxCareProviderGroup<br/>
Source: NOTNu... |
| DxCareProviderType | bigint |  |  | SI | Dimension: DxCareProviderType<br/>
Source: NOTCPT... |
| DxLocationEntered | bigint |  |  | SI | Dimension: DxLocationEntered<br/>
Source: NOTEnte... |
| DxNOTDate | date |  |  | SI | Dimension: DxNOTDate<br/>
Source: NOTDate |
| DxNOTDateAuth | date |  |  | SI | Dimension: DxNOTDateAuth<br/>
Source: NOTDateAuth |
| DxNOTDateAuthFxDayMonthYear | varchar |  |  | SI | Dimension: DxNOTDateAuthFxDayMonthYear<br/>
Sourc... |
| DxNOTDateAuthFxMonthNumber | varchar |  |  | SI | Dimension: DxNOTDateAuthFxMonthNumber<br/>
Source... |
| DxNOTDateAuthFxMonthYear | varchar |  |  | SI | Dimension: DxNOTDateAuthFxMonthYear<br/>
Source: ... |
| DxNOTDateAuthFxQuarterYear | varchar |  |  | SI | Dimension: DxNOTDateAuthFxQuarterYear<br/>
Source... |
| DxNOTDateAuthFxYear | varchar |  |  | SI | Dimension: DxNOTDateAuthFxYear<br/>
Source: NOTDa... |
| DxNOTDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxNOTDateFxDayMonthYear<br/>
Source: N... |
| DxNOTDateFxMonthNumber | varchar |  |  | SI | Dimension: DxNOTDateFxMonthNumber<br/>
Source: NO... |
| DxNOTDateFxMonthYear | varchar |  |  | SI | Dimension: DxNOTDateFxMonthYear<br/>
Source: NOTD... |
| DxNOTDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxNOTDateFxQuarterNumber<br/>
Source: ... |
| DxNOTDateFxQuarterYear | varchar |  |  | SI | Dimension: DxNOTDateFxQuarterYear<br/>
Source: NO... |
| DxNOTDateFxYear | varchar |  |  | SI | Dimension: DxNOTDateFxYear<br/>
Source: NOTDate |
| DxNoteStatus | bigint |  |  | SI | Dimension: DxNoteStatus<br/>
Source: NOTStatusDR.... |
| DxNoteType | bigint |  |  | SI | Dimension: DxNoteType<br/>
Source: NOTClinNotesTy... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: NOTParRef.MRA... |
| Rx3506920373 | bigint |  |  | SI | Relationship: Rx3506920373<br/>
Source: NOTParRef... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*