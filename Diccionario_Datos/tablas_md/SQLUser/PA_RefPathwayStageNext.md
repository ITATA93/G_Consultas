# SQLUser.PA_RefPathwayStageNext

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencia/Derivación**. Traslados entre servicios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NX_ParRef | varchar | PK |  | NO | PA_RefPathway Parent Reference |
| NX_Childsub | double |  |  | NO | Childsub |
| NX_RowId | varchar |  |  | NO | - |
| NX_Stage_DR | varchar |  | FK | SI | Des Ref PARefPathwayStage |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*