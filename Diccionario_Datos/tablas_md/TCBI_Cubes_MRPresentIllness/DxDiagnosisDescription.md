# TCBI_Cubes_MRPresentIllness.DxDiagnosisDescription

**Schema:** TCBI_Cubes_MRPresentIllness
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| DxDiagnosisCode | bigint |  |  | NO | Dimension property: DxDiagnosisCode<br/>
Source: ... |
| DxDiagnosisDescription | varchar |  |  | NO | Dimension property: DxDiagnosisDescription<br/>
S... |
| PxDiagnosisDescription | varchar |  |  | SI | Dimension property: PxDiagnosisDescription<br/>
S... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*