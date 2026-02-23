# SQLUser.IKDocument

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ConceptList | varchar |  |  | SI | - |
| EpisodeID | varchar |  |  | SI | PA_Adm |
| HighLevelConceptList | varchar |  |  | SI | - |
| IKnowSourceID | varchar |  |  | SI | - |
| ParseDate | date |  |  | SI | - |
| ParseTime | time |  |  | SI | - |
| PatientID | varchar |  |  | SI | PA_Person  / PA_PatMas |
| SourceClassName | varchar |  |  | SI | TrakCare Source ClassName |
| SourceID | varchar |  |  | SI | TrakCare Source ID |
| StoreDate | date |  |  | SI | - |
| StoreTime | time |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*