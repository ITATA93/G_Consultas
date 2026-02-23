# SQLUser.PA_PathwayItemEpType

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATHIE_ParRef | varchar | PK |  | NO | Parent Reference |
| PATHIE_Childsub | double |  |  | NO | Childsub |
| PATHIE_EpisodeType | varchar |  |  | SI | Episode Type |
| PATHIE_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*