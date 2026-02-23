# TCBI_CodeTables_PHCDrgMast.Fact

**Schema:** TCBI_CodeTables_PHCDrgMast
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| DxAdminRoute | bigint |  |  | SI | Dimension: DxAdminRoute
Expression: %cube.GetRout... |
| DxDrugName | bigint |  |  | SI | Dimension: DxDrugName<br/>
Source: PHCDName |
| DxFormulary | bigint |  |  | SI | Dimension: DxFormulary
Expression: %cube.GetFormu... |
| DxGenericDrug | bigint |  |  | SI | Dimension: DxGenericDrug<br/>
Source: PHCDGeneric... |
| DxPharmacyCategory | bigint |  |  | SI | Dimension: DxPharmacyCategory<br/>
Source: PHCDPH... |
| DxPharmacySubCategory | bigint |  |  | SI | Dimension: DxPharmacySubCategory<br/>
Source: PHC... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*