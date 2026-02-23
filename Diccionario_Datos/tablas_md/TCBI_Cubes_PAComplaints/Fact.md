# TCBI_Cubes_PAComplaints.Fact

**Schema:** TCBI_Cubes_PAComplaints
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1022551629 | varchar |  |  | SI | Dimension: Dx1022551629<br/>
Source: PACMDateComp... |
| Dx234010592 | varchar |  |  | SI | Dimension: Dx234010592<br/>
Source: PACMDateCompl... |
| Dx2442601847 | varchar |  |  | SI | Dimension: Dx2442601847<br/>
Source: PACMDateNext... |
| Dx2563807764 | varchar |  |  | SI | Dimension: Dx2563807764<br/>
Source: PACMDateReso... |
| Dx2865177546 | varchar |  |  | SI | Dimension: Dx2865177546<br/>
Source: PACMDateNext... |
| Dx3274010259 | varchar |  |  | SI | Dimension: Dx3274010259<br/>
Source: PACMDateComp... |
| Dx4058976699 | varchar |  |  | SI | Dimension: Dx4058976699<br/>
Source: PACMDateReso... |
| Dx4120413478 | varchar |  |  | SI | Dimension: Dx4120413478<br/>
Source: PACMDateNext... |
| Dx590145774 | bigint |  |  | SI | Dimension: Dx590145774<br/>
Source: PACMComplaint... |
| Dx765570476 | bigint |  |  | SI | Dimension: Dx765570476<br/>
Source: PACMPriorityD... |
| Dx947246437 | varchar |  |  | SI | Dimension: Dx947246437<br/>
Source: PACMDateResol... |
| DxCMCDescViaPACMCategoryDR | bigint |  | FK | SI | Dimension: DxCMCDescViaPACMCategoryDR<br/>
Source... |
| DxCMSDescViaPACMStatusDR | bigint |  | FK | SI | Dimension: DxCMSDescViaPACMStatusDR<br/>
Source: ... |
| DxComplaintDayOfWeek | bigint |  |  | SI | Dimension: DxComplaintDayOfWeek
Expression: ##cla... |
| DxNextActionDayOfWeek | bigint |  |  | SI | Dimension: DxNextActionDayOfWeek
Expression: ##cl... |
| DxPACMDateComplaint | date |  |  | SI | Dimension: DxPACMDateComplaint<br/>
Source: PACMD... |
| DxPACMDateComplaintFxYear | varchar |  |  | SI | Dimension: DxPACMDateComplaintFxYear<br/>
Source:... |
| DxPACMDateNextAction | date |  |  | SI | Dimension: DxPACMDateNextAction<br/>
Source: PACM... |
| DxPACMDateNextActionFxYear | varchar |  |  | SI | Dimension: DxPACMDateNextActionFxYear<br/>
Source... |
| DxPACMDateResolved | date |  |  | SI | Dimension: DxPACMDateResolved<br/>
Source: PACMDa... |
| DxPACMDateResolvedFxYear | varchar |  |  | SI | Dimension: DxPACMDateResolvedFxYear<br/>
Source: ... |
| DxPACMReportedBy | bigint |  |  | SI | Dimension: DxPACMReportedBy<br/>
Source: PACMRepo... |
| DxPACMType | bigint |  |  | SI | Dimension: DxPACMType<br/>
Source: PACMType |
| DxResolvedDayOfWeek | bigint |  |  | SI | Dimension: DxResolvedDayOfWeek
Expression: ##clas... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*