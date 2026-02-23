# TCBI_CodeTables_ARCItmMast.Fact

**Schema:** TCBI_CodeTables_ARCItmMast
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1191850305 | bigint |  |  | SI | Dimension: Dx1191850305<br/>
Source: ARCIMObserva... |
| Dx1266206526 | bigint |  |  | SI | Dimension: Dx1266206526<br/>
Source: ARCIMRMFrequ... |
| Dx1679031825 | bigint |  |  | SI | Dimension: Dx1679031825<br/>
Source: ARCIMPHCDFDR... |
| Dx2092835163 | bigint |  |  | SI | Dimension: Dx2092835163<br/>
Source: ARCIMAllowOr... |
| Dx3352281079 | bigint |  |  | SI | Dimension: Dx3352281079<br/>
Source: ARCIMPHCDFDR... |
| Dx660761216 | bigint |  |  | SI | Dimension: Dx660761216<br/>
Source: ARCIMRMDurati... |
| DxARCIMChargePartial | bigint |  |  | SI | Dimension: DxARCIMChargePartial<br/>
Source: ARCI... |
| DxARCIMOrderOnItsOwn | bigint |  |  | SI | Dimension: DxARCIMOrderOnItsOwn<br/>
Source: ARCI... |
| DxARCIMSensitive | bigint |  |  | SI | Dimension: DxARCIMSensitive<br/>
Source: ARCIMSen... |
| DxARCIMSensitiveOrder | bigint |  |  | SI | Dimension: DxARCIMSensitiveOrder<br/>
Source: ARC... |
| DxBillingGroup | bigint |  |  | SI | Dimension: DxBillingGroup<br/>
Source: ARCIMBillS... |
| DxBillingSubGroup | bigint |  |  | SI | Dimension: DxBillingSubGroup<br/>
Source: ARCIMBi... |
| DxItemCategory | bigint |  |  | SI | Dimension: DxItemCategory<br/>
Source: ARCIMItemC... |
| DxItemCode | bigint |  |  | SI | Dimension: DxItemCode<br/>
Source: ARCIMCode |
| DxItemDescription | bigint |  |  | SI | Dimension: DxItemDescription<br/>
Source: ARCIMDe... |
| DxItemSubCategory | bigint |  |  | SI | Dimension: DxItemSubCategory<br/>
Source: ARCIMIt... |
| DxServiceCategory | bigint |  |  | SI | Dimension: DxServiceCategory<br/>
Source: ARCIMSe... |
| DxServiceGroup | bigint |  |  | SI | Dimension: DxServiceGroup<br/>
Source: ARCIMServi... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*