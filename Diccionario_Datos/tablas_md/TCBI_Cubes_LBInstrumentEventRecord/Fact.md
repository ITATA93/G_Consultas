# TCBI_Cubes_LBInstrumentEventRecord.Fact

**Schema:** TCBI_Cubes_LBInstrumentEventRecord
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1735385215 | bigint |  |  | SI | Dimension: Dx1735385215<br/>
Source: LBIERECEvent... |
| DxLBIERECValue | bigint |  |  | SI | Dimension: DxLBIERECValue<br/>
Source: LBIERECVal... |
| RxLBIERECParRef | bigint |  |  | SI | Relationship: RxLBIERECParRef<br/>
Source: LBIERE... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*