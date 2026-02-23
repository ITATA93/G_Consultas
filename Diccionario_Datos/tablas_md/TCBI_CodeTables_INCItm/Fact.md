# TCBI_CodeTables_INCItm.Fact

**Schema:** TCBI_CodeTables_INCItm
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| DxBaseUOM | bigint |  |  | SI | Dimension: DxBaseUOM<br/>
Source: INCICTUOMDR.CTU... |
| DxIssTrfFlag | bigint |  |  | SI | Dimension: DxIssTrfFlag<br/>
Source: INCIIsTrfFla... |
| DxMainStore | bigint |  |  | SI | Dimension: DxMainStore<br/>
Source: INCICTLOCDR.C... |
| DxPurchaseType | bigint |  |  | SI | Dimension: DxPurchaseType<br/>
Source: INCIINCPOD... |
| DxPurchaseUOM | bigint |  |  | SI | Dimension: DxPurchaseUOM<br/>
Source: INCICTUOMPu... |
| DxReplenishmentOption | bigint |  |  | SI | Dimension: DxReplenishmentOption<br/>
Source: INC... |
| DxSterileCategory | bigint |  |  | SI | Dimension: DxSterileCategory<br/>
Source: INCISte... |
| DxSterileFlag | bigint |  |  | SI | Dimension: DxSterileFlag<br/>
Source: INCISterile |
| DxStkCat | bigint |  |  | SI | Dimension: DxStkCat<br/>
Source: INCIINCSCDR.INCS... |
| DxStkCode | bigint |  |  | SI | Dimension: DxStkCode<br/>
Source: INCICode |
| DxStkDesc | bigint |  |  | SI | Dimension: DxStkDesc<br/>
Source: INCIDesc |
| DxStkTakeGrp | bigint |  |  | SI | Dimension: DxStkTakeGrp<br/>
Source: INCIINCTGDR.... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*