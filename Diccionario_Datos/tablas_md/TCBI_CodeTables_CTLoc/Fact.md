# TCBI_CodeTables_CTLoc.Fact

**Schema:** TCBI_CodeTables_CTLoc
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1388436641 | bigint |  |  | SI | Dimension: Dx1388436641<br/>
Source: CTLOCHospita... |
| Dx3011299930 | bigint |  |  | SI | Dimension: Dx3011299930<br/>
Source: CTLOCSignifF... |
| DxCTLOCMRRequestMoveValid | bigint |  |  | SI | Dimension: DxCTLOCMRRequestMoveValid<br/>
Source:... |
| DxCTLOCMedicalRecordActive | bigint |  |  | SI | Dimension: DxCTLOCMedicalRecordActive<br/>
Source... |
| DxCTLOCType | bigint |  |  | SI | Dimension: DxCTLOCType<br/>
Source: CTLOCType |
| DxDepartment | bigint |  |  | SI | Dimension: DxDepartment<br/>
Source: CTLOCDepDR.D... |
| DxLocationCode | bigint |  |  | SI | Dimension: DxLocationCode<br/>
Source: CTLOCCode |
| DxLocationDescription | bigint |  |  | SI | Dimension: DxLocationDescription<br/>
Source: CTL... |
| DxRUDescViaCTLOCRespUnitDR | bigint |  | FK | SI | Dimension: DxRUDescViaCTLOCRespUnitDR<br/>
Source... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*