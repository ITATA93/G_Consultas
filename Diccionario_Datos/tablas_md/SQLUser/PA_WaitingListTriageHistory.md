# SQLUser.PA_WaitingListTriageHistory

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRIHIS_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| TRIHIS_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| TRIHIS_Childsub | double |  |  | NO | Childsub |
| TRIHIS_RowId | varchar |  |  | NO | - |
| TRIHIS_TriageDate | date |  |  | SI | TriageDate |
| TRIHIS_TriageNotes | varchar |  |  | SI | TriageNote |
| TRIHIS_TriageTime | time |  |  | SI | TriageTime |
| TRIHIS_UpdateDate | date |  |  | SI | UpdateDate |
| TRIHIS_UpdateTime | time |  |  | SI | UpdateTime |
| TRIHIS_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| TRIHIS_WLTriageOutcome_DR | bigint |  | FK | SI | Des Ref PACWLTriageOutcome  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*