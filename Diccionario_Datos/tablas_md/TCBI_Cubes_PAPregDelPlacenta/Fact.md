# TCBI_Cubes_PAPregDelPlacenta.Fact

**Schema:** TCBI_Cubes_PAPregDelPlacenta
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxMembraneCondition | bigint |  |  | SI | Dimension: DxMembraneCondition<br/>
Source: PLACM... |
| DxMotherID | bigint |  |  | SI | Dimension: DxMotherID<br/>
Source: PLACParRef.DEL... |
| DxPLACDelTypeDR | bigint |  | FK | SI | Dimension: DxPLACDelTypeDR<br/>
Source: PLACDelTy... |
| DxPLACExpulsionComplicDR | bigint |  | FK | SI | Dimension: DxPLACExpulsionComplicDR<br/>
Source: ... |
| DxPlacentaAnomaly | bigint |  |  | SI | Dimension: DxPlacentaAnomaly<br/>
Source: PLACOth... |
| DxPlacentaChoronicity | bigint |  |  | SI | Dimension: DxPlacentaChoronicity<br/>
Source: PLA... |
| DxPlacentaCondition | bigint |  |  | SI | Dimension: DxPlacentaCondition<br/>
Source: PLACP... |
| DxPlacentaWeight | bigint |  |  | SI | Dimension: DxPlacentaWeight<br/>
Source: PLACPlac... |
| DxReasontoSendPlacenta | bigint |  |  | SI | Dimension: DxReasontoSendPlacenta<br/>
Source: PL... |
| DxSenttoPathology | bigint |  |  | SI | Dimension: DxSenttoPathology<br/>
Source: PLACSen... |
| DxTherapyforComplication | bigint |  |  | SI | Dimension: DxTherapyforComplication<br/>
Source: ... |
| RxIDViaPLACParRef | bigint |  |  | SI | Relationship: RxIDViaPLACParRef<br/>
Source: PLAC... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*