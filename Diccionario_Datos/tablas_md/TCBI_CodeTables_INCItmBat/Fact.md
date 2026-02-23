# TCBI_CodeTables_INCItmBat.Fact

**Schema:** TCBI_CodeTables_INCItmBat
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxDay | varchar |  |  | SI | Dimension: DxDay<br/>
Source: INCIBExpDate |
| DxINCIBExpDate | date |  |  | SI | Dimension: DxINCIBExpDate<br/>
Source: INCIBExpDa... |
| DxINCIBNo | bigint |  |  | SI | Dimension: DxINCIBNo<br/>
Source: INCIBNo |
| DxMonth | varchar |  |  | SI | Dimension: DxMonth<br/>
Source: INCIBExpDate |
| DxYear | varchar |  |  | SI | Dimension: DxYear<br/>
Source: INCIBExpDate |
| RxIDViaINCIBINCIParRef | bigint |  |  | SI | Relationship: RxIDViaINCIBINCIParRef<br/>
Source:... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*