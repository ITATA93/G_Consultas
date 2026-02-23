# TCBI_Cubes_PACPathway.Fact

**Schema:** TCBI_Cubes_PACPathway
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx2076791104 | bigint |  |  | SI | Dimension: Dx2076791104<br/>
Source: PACPOriginal... |
| Dx2222245353 | date |  |  | SI | Dimension: Dx2222245353<br/>
Source: PACPOriginal... |
| DxCTSEXDesc | bigint |  |  | SI | Dimension: DxCTSEXDesc<br/>
Source: PACPSexDR.CTS... |
| DxDateFromDay | varchar |  |  | SI | Dimension: DxDateFromDay<br/>
Source: PACPOrigina... |
| DxDateFromMonth | varchar |  |  | SI | Dimension: DxDateFromMonth<br/>
Source: PACPOrigi... |
| DxDateFromMonthOfYear | varchar |  |  | SI | Dimension: DxDateFromMonthOfYear<br/>
Source: PAC... |
| DxDateFromQuarter | varchar |  |  | SI | Dimension: DxDateFromQuarter<br/>
Source: PACPOri... |
| DxDateFromYear | varchar |  |  | SI | Dimension: DxDateFromYear<br/>
Source: PACPOrigin... |
| DxDayOfWeek | bigint |  |  | SI | Dimension: DxDayOfWeek
Expression: ##class(TCBI.U... |
| DxPACPAgeFrom | bigint |  |  | SI | Dimension: DxPACPAgeFrom
Expression: ##Class(web.... |
| DxPACPAgeTo | bigint |  |  | SI | Dimension: DxPACPAgeTo
Expression: ##Class(web.PA... |
| DxPACPOriginalProtocolDR | bigint |  | FK | SI | Dimension: DxPACPOriginalProtocolDR<br/>
Source: ... |
| DxPACPathwayHosp | varchar |  |  | SI | Dimension: DxPACPathwayHosp
Expression: ##Class(w... |
| DxPACPathwayLoc | varchar |  |  | SI | Dimension: DxPACPathwayLoc
Expression: ##Class(we... |
| DxPACPathwayProblem | varchar |  |  | SI | Dimension: DxPACPathwayProblem
Expression: ##Clas... |
| DxPACPathwayRole | varchar |  |  | SI | Dimension: DxPACPathwayRole
Expression: ##Class(w... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*