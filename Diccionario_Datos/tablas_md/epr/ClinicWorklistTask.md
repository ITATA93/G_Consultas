# epr.ClinicWorklistTask

**Schema:** epr
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| TASKAdminRoute | varchar |  |  | SI | Admin Route |
| TASKAdminRouteExclude | varchar |  |  | SI | Admin Route excluded flag |
| TASKDefault | varchar |  |  | SI | Default |
| TASKDesc | varchar |  |  | SI | Description |
| TASKDispOneIconPerAdm | varchar |  |  | SI | Display One Icon Per Administration (RUI only) |
| TASKDispRateChgDisc | varchar |  |  | SI | Display IV Rate Change, Modifications and Disconti... |
| TASKDoseIsConditional | varchar |  |  | SI | Filter on Order Execution Nodes OEOREIsConditional |
| TASKExclPRN | varchar |  |  | SI | Exclude PRN |
| TASKIcon | varchar |  |  | SI | Icon definition |
| TASKIconSVG | varchar |  |  | SI | Icon SVG definition |
| TASKInfoPaneSize | integer |  |  | SI | Info Pane Size |
| TASKNeedsReview | varchar |  |  | SI | Order Needs Review |
| TASKOrdCat | varchar |  |  | SI | Order cagtegories |
| TASKOrdPrio | varchar |  |  | SI | Order priorities |
| TASKOrdSubCat | varchar |  |  | SI | Order sub cagtegories |
| TASKOrdSubCatExclude | varchar |  |  | SI | Order sub cagtegories excluded flag |
| TASKOrdType | varchar |  |  | SI | Order type |
| TASKOverDueIcon | varchar |  |  | SI | Overdue Icon |
| TASKOwner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| TASKPRN | varchar |  |  | SI | PRN Only |
| TASKSequence | integer |  |  | SI | Sequence |
| TASKShowInfoPane | varchar |  |  | SI | Link to Infopane |
| TASKTooltip | varchar |  |  | SI | Tooltip |
| TASKWorkflow | varchar |  |  | SI | Link workflow |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*