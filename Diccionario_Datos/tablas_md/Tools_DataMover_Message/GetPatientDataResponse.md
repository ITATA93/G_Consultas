# Tools_DataMover_Message.GetPatientDataResponse

**Schema:** Tools_DataMover_Message
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ErrorMessage | varchar |  |  | SI | - |
| IsMaternityReference | bit |  |  | SI | - |
| IsNOKReference | bit |  |  | SI | - |
| MaternityReferenceGUID | varchar |  |  | SI | - |
| NOKReferenceGUID | varchar |  |  | SI | - |
| PatientData | longvarbinary |  |  | SI | - |
| PatientNumber | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*