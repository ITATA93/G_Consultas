# SQLUser.PA_ProblemMetastaticSite

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROBMETASITE_ParRef | varchar | PK |  | NO | PA_Problem Parent Reference |
| PROBMETASITE_BodyParts_DR | bigint |  | FK | SI | Des Ref MRC_BodyParts |
| PROBMETASITE_Childsub | double |  |  | NO | Childsub |
| PROBMETASITE_Date | date |  |  | SI | Discovery date for metastatic site |
| PROBMETASITE_ICDDx_DR | bigint |  | FK | SI | Des Ref MRC_ICDDx |
| PROBMetastaticSite_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*