# TCBI_CodeTables_ARCItemCat.Fact

**Schema:** TCBI_CodeTables_ARCItemCat
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx3874306313 | bigint |  |  | SI | Dimension: Dx3874306313<br/>
Source: ARCICExecCat... |
| Dx4116673120 | bigint |  |  | SI | Dimension: Dx4116673120<br/>
Source: ARCICTextRes... |
| DxARCICDateFrom | date |  |  | SI | Dimension: DxARCICDateFrom<br/>
Source: ARCICDate... |
| DxARCICDateTo | date |  |  | SI | Dimension: DxARCICDateTo<br/>
Source: ARCICDateTo |
| DxARCICNurseWorkBench | bigint |  |  | SI | Dimension: DxARCICNurseWorkBench<br/>
Source: ARC... |
| DxDateFrom | varchar |  |  | SI | Dimension: DxDateFrom<br/>
Source: ARCICDateFrom |
| DxDateTo | varchar |  |  | SI | Dimension: DxDateTo<br/>
Source: ARCICDateTo |
| DxDisplyOPWhiteboard | bigint |  |  | SI | Dimension: DxDisplyOPWhiteboard<br/>
Source: ARCI... |
| DxOrderCategory | bigint |  |  | SI | Dimension: DxOrderCategory<br/>
Source: ARCICOrdC... |
| DxOrderSubCat | bigint |  |  | SI | Dimension: DxOrderSubCat<br/>
Source: ARCICDesc |
| DxOrderType | bigint |  |  | SI | Dimension: DxOrderType<br/>
Source: ARCICOrderTyp... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*