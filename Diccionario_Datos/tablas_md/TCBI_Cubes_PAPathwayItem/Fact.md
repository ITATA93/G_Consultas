# TCBI_Cubes_PAPathwayItem.Fact

**Schema:** TCBI_Cubes_PAPathwayItem
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DXLinkedOrderDescription | bigint |  |  | SI | Dimension: DXLinkedOrderDescription<br/>
Source: ... |
| DXOrderSetDescription | bigint |  |  | SI | Dimension: DXOrderSetDescription<br/>
Source: PAT... |
| DXPathID | bigint |  |  | SI | Dimension: DXPathID<br/>
Source: PATHIParRef.%ID |
| DXPathwayDesc | bigint |  |  | SI | Dimension: DXPathwayDesc<br/>
Source: PATHIParRef... |
| DXPathwayItemAdhoc | bigint |  |  | SI | Dimension: DXPathwayItemAdhoc
Expression: %cube.G... |
| DXPathwayItemStatus | bigint |  |  | SI | Dimension: DXPathwayItemStatus
Expression: %cube.... |
| DXPathwayItemType | bigint |  |  | SI | Dimension: DXPathwayItemType
Expression: %cube.Ge... |
| DXPathwayOutcome | bigint |  |  | SI | Dimension: DXPathwayOutcome<br/>
Source: PATHIPar... |
| DXPathwayProtocolDesc | bigint |  |  | SI | Dimension: DXPathwayProtocolDesc<br/>
Source: PAT... |
| DXPathwayProtocolItmDesc | bigint |  |  | SI | Dimension: DXPathwayProtocolItmDesc<br/>
Source: ... |
| DXPathwayType | bigint |  |  | SI | Dimension: DXPathwayType<br/>
Source: PATHIParRef... |
| DXProtocolVersion | bigint |  |  | SI | Dimension: DXProtocolVersion<br/>
Source: PATHIPa... |
| Dx1881868468 | varchar |  |  | SI | Dimension: Dx1881868468<br/>
Source: PATHIPlanned... |
| DxPATHIPlannedStartDate | date |  |  | SI | Dimension: DxPATHIPlannedStartDate<br/>
Source: P... |
| DxPathwayItemDesc | bigint |  |  | SI | Dimension: DxPathwayItemDesc<br/>
Source: PATHIDe... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: PATHIParRef.P... |
| MxAdhocItems | double |  |  | SI | Measure: MxAdhocItems<br/>
Source: PATHIIsAdhoc |
| MxLinkedOrderItems | double |  |  | SI | Measure: MxLinkedOrderItems
Expression: $S(%sourc... |
| Rx2952215789 | bigint |  |  | SI | Relationship: Rx2952215789<br/>
Source: PATHIParR... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*