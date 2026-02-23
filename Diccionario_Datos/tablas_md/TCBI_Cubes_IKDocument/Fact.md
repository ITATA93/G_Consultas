# TCBI_Cubes_IKDocument.Fact

**Schema:** TCBI_Cubes_IKDocument
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx2797598302 | bigint |  |  | SI | Dimension: Dx2797598302<br/>
Source: Sentence.Doc... |
| DxHighLevelConcept | bigint |  |  | SI | Dimension: DxHighLevelConcept<br/>
Source: HighLe... |
| DxIndexValue | bigint |  |  | SI | Dimension: DxIndexValue<br/>
Source: IndexValue |
| Rx2684111088 | bigint |  |  | SI | Relationship: Rx2684111088<br/>
Source: Sentence.... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*