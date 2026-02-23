# websys_UDFExt.TrakClassEvent

**Schema:** websys_UDFExt
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| EntryPoint | varchar |  |  | SI | - |
| EventName | varchar |  |  | NO | - |
| EventSequence | integer |  |  | NO | - |
| FeaturesRequired | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LastUpdateDate | date |  |  | SI | - |
| LastUpdateTime | time |  |  | SI | - |
| MatchCondition | varchar |  |  | SI | - |
| RegisteredBy | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*