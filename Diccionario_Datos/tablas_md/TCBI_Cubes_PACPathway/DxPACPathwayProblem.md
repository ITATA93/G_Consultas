# TCBI_Cubes_PACPathway.DxPACPathwayProblem

**Schema:** TCBI_Cubes_PACPathway
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DxPACPathwayProblem | varchar |  |  | NO | Dimension property: DxPACPathwayProblem<br/>
Sour... |
| PxPACPPDesc | varchar |  |  | SI | Dimension property: PxPACPPDesc<br/>
Source: $pie... |
| PxPACPPICDCodeDR | varchar |  | FK | SI | Dimension property: PxPACPPICDCodeDR<br/>
Source:... |
| PxPACPPICPC2CodesDR | varchar |  | FK | SI | Dimension property: PxPACPPICPC2CodesDR<br/>
Sour... |
| PxPACPPSnomedConceptDR | varchar |  | FK | SI | Dimension property: PxPACPPSnomedConceptDR<br/>
S... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*