# Tools_DrugUpload.Classification

**Schema:** Tools_DrugUpload
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Comment | varchar |  |  | SI | Comment |
| DMDLevel | varchar |  |  | NO | TrakType that declaires which Type, can be e.g. AM... |
| ICD | varchar |  |  | SI | ICD    		= ICD Code |
| ItemCode | varchar |  |  | NO | Code depending on Type |
| RefCode | varchar |  |  | NO | Code        = Classification Ref Code       |
| RefDesc | varchar |  |  | SI | Desc        = Classification Ref Desc          |
| RefSystem | varchar |  |  | NO | System      = Classification CodeSystem   (SNOMED-... |
| Snomed | varchar |  |  | SI | Snomed    	= Snomed Code |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*