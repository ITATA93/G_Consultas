# TCBI_CodeTables_CTCareProv.Fact

**Schema:** TCBI_CodeTables_CTCareProv
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxActive | bigint |  |  | SI | Dimension: DxActive<br/>
Source: CTPCPActiveFlag |
| DxAnaesthetist | bigint |  |  | SI | Dimension: DxAnaesthetist<br/>
Source: CTPCPAnaes... |
| DxCTPCPAdmittingRights | bigint |  |  | SI | Dimension: DxCTPCPAdmittingRights<br/>
Source: CT... |
| DxCTPCPDateActiveFrom | date |  |  | SI | Dimension: DxCTPCPDateActiveFrom<br/>
Source: CTP... |
| DxCTPCPDateActiveTo | date |  |  | SI | Dimension: DxCTPCPDateActiveTo<br/>
Source: CTPCP... |
| DxCTPCPPractitionerFlag1 | bigint |  |  | SI | Dimension: DxCTPCPPractitionerFlag1<br/>
Source: ... |
| DxCTPCPSpecialistYN | bigint |  |  | SI | Dimension: DxCTPCPSpecialistYN<br/>
Source: CTPCP... |
| DxCTSPCDescViaCTPCPSpecDR | bigint |  | FK | SI | Dimension: DxCTSPCDescViaCTPCPSpecDR<br/>
Source:... |
| DxCareProviderCode | bigint |  |  | SI | Dimension: DxCareProviderCode<br/>
Source: CTPCPC... |
| DxCareProviderDescription | bigint |  |  | SI | Dimension: DxCareProviderDescription<br/>
Source:... |
| DxCareProviderType | bigint |  |  | SI | Dimension: DxCareProviderType<br/>
Source: CTPCPC... |
| DxDateFrom | varchar |  |  | SI | Dimension: DxDateFrom<br/>
Source: CTPCPDateActiv... |
| DxDateTo | varchar |  |  | SI | Dimension: DxDateTo<br/>
Source: CTPCPDateActiveT... |
| DxRadiologist | bigint |  |  | SI | Dimension: DxRadiologist<br/>
Source: CTPCPRadiol... |
| DxSurgeon | bigint |  |  | SI | Dimension: DxSurgeon<br/>
Source: CTPCPSurgeon |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*