# epr.CTGraphItemDefinition

**Schema:** epr
**Columnas:** 44
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CTGIAdmRouteDR | bigint |  | FK | SI | - |
| CTGIColour | varchar |  |  | SI | - |
| CTGIDateFrom | date |  |  | SI | - |
| CTGIDateTo | date |  |  | SI | - |
| CTGIDefaultShow | bit |  |  | SI | Default show
shows by default in graph. if false ... |
| CTGIDisplayGraphOnly | varchar |  |  | SI | - |
| CTGIFontCapitalisation | varchar |  |  | SI | Font Capitalisation - Upper Case, Lower Case, Titl... |
| CTGIFontSize | integer |  |  | SI | - |
| CTGIGenericDR | bigint |  | FK | SI | - |
| CTGIGenericType | varchar |  |  | SI | Generic Graph Type
Determines if Generic items wi... |
| CTGIGraphDR | bigint |  | FK | SI | - |
| CTGIHeight | integer |  |  | SI | - |
| CTGIHideForCTL | varchar |  |  | SI | Hide Item For Clinical Timelines |
| CTGIIVCalcMethod | varchar |  |  | SI | Calculation Method
Used to normalize the denomina... |
| CTGILBCTestItemDR | bigint |  | FK | SI | - |
| CTGILabItemDR | varchar |  | FK | SI | this is NOT strictly a DR we can use.
It is simpl... |
| CTGILegendSequence | varchar |  |  | SI | - |
| CTGILinkedGraphItemDR | varchar |  | FK | SI | - |
| CTGILinkedLabItemDR | varchar |  | FK | SI | - |
| CTGILinkedObsItemDR | bigint |  | FK | SI | - |
| CTGILinkedOrderItemDR | varchar |  | FK | SI | - |
| CTGILowerPregnancyRange | varchar |  |  | SI | - |
| CTGILowerRange | varchar |  |  | SI | - |
| CTGIMarker | varchar |  |  | SI | - |
| CTGIMarkerSize | varchar |  |  | SI | - |
| CTGINonLinearRefRanges | varchar |  |  | SI | - |
| CTGINormalLineType | varchar |  |  | SI | - |
| CTGIObsItemDR | bigint |  | FK | SI | - |
| CTGIObsOnly | varchar |  |  | SI | Observation item only |
| CTGIOrderItemDR | varchar |  | FK | SI | - |
| CTGIOwner | varchar |  |  | SI | - |
| CTGIPartogramSequence | varchar |  |  | SI | - |
| CTGIRefLineColour | varchar |  |  | SI | - |
| CTGIUomDR | bigint |  | FK | SI | - |
| CTGIUpperPregnancyRange | varchar |  |  | SI | - |
| CTGIUpperRange | varchar |  |  | SI | - |
| CTGIVariableLineType | varchar |  |  | SI | - |
| CTGIVerticalTitle | varchar |  |  | SI | Vertical Title |
| CTGIY1AxisMax | varchar |  |  | SI | - |
| CTGIY1AxisMin | varchar |  |  | SI | - |
| CTGIY1AxisStep | varchar |  |  | SI | - |
| CTGIYAxis | varchar |  |  | SI | - |
| CTGItemType | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*