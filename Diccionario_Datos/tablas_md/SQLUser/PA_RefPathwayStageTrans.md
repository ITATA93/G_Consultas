# SQLUser.PA_RefPathwayStageTrans

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencia/Derivación**. Traslados entre servicios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRANS_ParRef | varchar | PK |  | NO | PA_RefPathway Parent Reference |
| TRANS_ARCIM_DR | varchar |  | FK | SI | ARCItmMast |
| TRANS_Childsub | double |  |  | NO | Childsub |
| TRANS_Consultant_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| TRANS_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| TRANS_NonTriaged | varchar |  |  | SI | NonTriaged |
| TRANS_Priority_DR | bigint |  | FK | SI | Des Ref PACWaitingListPriority |
| TRANS_Procedure_DR | bigint |  | FK | SI | Des Ref PACStatePPP |
| TRANS_RowId | varchar |  |  | NO | - |
| TRANS_Specialty_DR | bigint |  | FK | SI | Des Ref CTLoc |
| TRANS_StageStatus_DR | bigint |  | FK | SI | Des Ref Stage Status |
| TRANS_WaitingList_DR | bigint |  | FK | SI | Des Ref WaitingList |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*