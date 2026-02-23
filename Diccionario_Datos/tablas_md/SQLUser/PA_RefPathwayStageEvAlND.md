# SQLUser.PA_RefPathwayStageEvAlND

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencia/Derivación**. Traslados entre servicios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NUMD_ParRef | varchar | PK |  | NO | PA_RefPathway Parent Reference |
| NUMD_Active | varchar |  |  | SI | Active |
| NUMD_AlertFromDate | date |  |  | SI | Alert From Date  |
| NUMD_Childsub | double |  |  | NO | Childsub |
| NUMD_NumberOfDays | double |  |  | SI | NumberOfDays |
| NUMD_RowId | varchar |  |  | NO | - |
| NUMD_State_DR | bigint |  | FK | SI | Des Ref Sate |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*