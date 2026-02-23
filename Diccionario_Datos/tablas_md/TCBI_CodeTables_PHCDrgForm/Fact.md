# TCBI_CodeTables_PHCDrgForm.Fact

**Schema:** TCBI_CodeTables_PHCDrgForm
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxAdministrationRoute | bigint |  |  | SI | Dimension: DxAdministrationRoute<br/>
Source: PHC... |
| DxBaseUOM | bigint |  |  | SI | Dimension: DxBaseUOM<br/>
Source: PHCDFCTUOMDR.CT... |
| DxDateFrom | varchar |  |  | SI | Dimension: DxDateFrom<br/>
Source: PHCDFDateFrom |
| DxDateTo | varchar |  |  | SI | Dimension: DxDateTo<br/>
Source: PHCDFDateTo |
| DxDeductPartially | bigint |  |  | SI | Dimension: DxDeductPartially<br/>
Source: PHCDFDe... |
| DxDrugCode | bigint |  |  | SI | Dimension: DxDrugCode<br/>
Source: PHCDFPHCDParRe... |
| DxDrugName | bigint |  |  | SI | Dimension: DxDrugName<br/>
Source: PHCDFPHCDParRe... |
| DxDuration | bigint |  |  | SI | Dimension: DxDuration<br/>
Source: PHCDFPHCDUDR.P... |
| DxForm | bigint |  |  | SI | Dimension: DxForm<br/>
Source: PHCDFGenRtFormDR.R... |
| DxFormulary | bigint |  |  | SI | Dimension: DxFormulary<br/>
Source: PHCDFFormular... |
| DxFrequency | bigint |  |  | SI | Dimension: DxFrequency<br/>
Source: PHCDFPHCFRDR.... |
| DxGenericName | bigint |  |  | SI | Dimension: DxGenericName<br/>
Source: PHCDFPHCDPa... |
| DxInpatientDuration | bigint |  |  | SI | Dimension: DxInpatientDuration<br/>
Source: PHCDF... |
| DxPHCDFDateFrom | date |  |  | SI | Dimension: DxPHCDFDateFrom<br/>
Source: PHCDFDate... |
| DxPHCDFDateTo | date |  |  | SI | Dimension: DxPHCDFDateTo<br/>
Source: PHCDFDateTo |
| DxPreferred | bigint |  |  | SI | Dimension: DxPreferred<br/>
Source: PHCDFPreferre... |
| DxRoute | bigint |  |  | SI | Dimension: DxRoute<br/>
Source: PHCDFGenRtFormDR.... |
| DxStrength | bigint |  |  | SI | Dimension: DxStrength<br/>
Source: PHCDFGenRtForm... |
| DxVolume | bigint |  |  | SI | Dimension: DxVolume<br/>
Source: PHCDFVolume |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*