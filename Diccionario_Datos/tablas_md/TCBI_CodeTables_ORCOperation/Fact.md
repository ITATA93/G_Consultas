# TCBI_CodeTables_ORCOperation.Fact

**Schema:** TCBI_CodeTables_ORCOperation
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx3474779830 | bigint |  |  | SI | Dimension: Dx3474779830
Expression: %cube.DaySurg... |
| DxActiveDateToDay | varchar |  |  | SI | Dimension: DxActiveDateToDay<br/>
Source: OPERAct... |
| DxActiveDateToMonth | varchar |  |  | SI | Dimension: DxActiveDateToMonth<br/>
Source: OPERA... |
| DxActiveDateToYear | varchar |  |  | SI | Dimension: DxActiveDateToYear<br/>
Source: OPERAc... |
| DxAgeFrom | bigint |  |  | SI | Dimension: DxAgeFrom<br/>
Source: OPERAgeFrom |
| DxCTSEXDescViaOPERSexDR | bigint |  | FK | SI | Dimension: DxCTSEXDescViaOPERSexDR<br/>
Source: O... |
| DxDateActiveFromDay | varchar |  |  | SI | Dimension: DxDateActiveFromDay<br/>
Source: OPERD... |
| DxDateActiveFromMonth | varchar |  |  | SI | Dimension: DxDateActiveFromMonth<br/>
Source: OPE... |
| DxDateActiveFromYear | varchar |  |  | SI | Dimension: DxDateActiveFromYear<br/>
Source: OPER... |
| DxLengthOfStay | bigint |  |  | SI | Dimension: DxLengthOfStay<br/>
Source: OPERLength... |
| DxLongDescription | bigint |  |  | SI | Dimension: DxLongDescription<br/>
Source: OPERLon... |
| DxNationalCode | bigint |  |  | SI | Dimension: DxNationalCode<br/>
Source: OPERNation... |
| DxOPERActiveDateTo | date |  |  | SI | Dimension: DxOPERActiveDateTo<br/>
Source: OPERAc... |
| DxOPERAgeTo | bigint |  |  | SI | Dimension: DxOPERAgeTo<br/>
Source: OPERAgeTo |
| DxOPERCode | bigint |  |  | SI | Dimension: DxOPERCode<br/>
Source: OPERCode |
| DxOPERDateActiveFrom | date |  |  | SI | Dimension: DxOPERDateActiveFrom<br/>
Source: OPER... |
| DxOPERICD10 | bigint |  |  | SI | Dimension: DxOPERICD10<br/>
Source: OPERICD10 |
| DxOperationDescription | bigint |  |  | SI | Dimension: DxOperationDescription<br/>
Source: OP... |
| RxIDViaOPERARCIMDR | bigint |  | FK | SI | Relationship: RxIDViaOPERARCIMDR<br/>
Source: OPE... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*