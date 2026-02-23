# TCBI_CodeTables_SSUser.Fact

**Schema:** TCBI_CodeTables_SSUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1214662674 | bigint |  |  | SI | Dimension: Dx1214662674<br/>
Source: SSUSRCarePro... |
| Dx1318432593 | bigint |  |  | SI | Dimension: Dx1318432593<br/>
Source: SSUSRDefault... |
| Dx3676805571 | bigint |  |  | SI | Dimension: Dx3676805571<br/>
Source: SSUSRAllowWe... |
| Dx647429738 | bigint |  |  | SI | Dimension: Dx647429738<br/>
Source: SSUSRHospital... |
| DxAllowWebLayoutManager | bigint |  |  | SI | Dimension: DxAllowWebLayoutManager<br/>
Source: S... |
| DxDateFrom | varchar |  |  | SI | Dimension: DxDateFrom<br/>
Source: SSUSRDateFrom |
| DxDateTo | varchar |  |  | SI | Dimension: DxDateTo<br/>
Source: SSUSRDateTo |
| DxLanguage | bigint |  |  | SI | Dimension: DxLanguage<br/>
Source: SSUSRCTLANDR.C... |
| DxSSGRPDescViaSSUSRGroup | bigint |  |  | SI | Dimension: DxSSGRPDescViaSSUSRGroup<br/>
Source: ... |
| DxSSUSRActive | bigint |  |  | SI | Dimension: DxSSUSRActive<br/>
Source: SSUSRActive |
| DxSSUSRDateFrom | date |  |  | SI | Dimension: DxSSUSRDateFrom<br/>
Source: SSUSRDate... |
| DxSSUSRDateTo | date |  |  | SI | Dimension: DxSSUSRDateTo<br/>
Source: SSUSRDateTo |
| DxUserID | bigint |  |  | SI | Dimension: DxUserID<br/>
Source: SSUSRInitials |
| DxUserName | bigint |  |  | SI | Dimension: DxUserName<br/>
Source: SSUSRName |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*