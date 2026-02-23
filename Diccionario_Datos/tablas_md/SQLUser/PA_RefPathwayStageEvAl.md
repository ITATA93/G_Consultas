# SQLUser.PA_RefPathwayStageEvAl

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencia/Derivación**. Traslados entre servicios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AL_ParRef | varchar | PK |  | NO | PA_RefPathway Parent Reference |
| AL_Childsub | double |  |  | NO | Childsub |
| AL_RowId | varchar |  |  | NO | - |
| AL_StageStatus_DR | bigint |  | FK | SI | Des Ref Stage Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*