# SQLUser.PA_WaitingListScore

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SC_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| SC_Assessor_DR | varchar |  | FK | SI | Des Ref CT Care Provider |
| SC_AssignmentDate | date |  |  | SI | AssignmentDate |
| SC_AssignmentTime | time |  |  | SI | AssignmentTime |
| SC_Childsub | double |  |  | NO | Childsub |
| SC_ClinOverReason_DR | bigint |  | FK | SI | Des Ref PACClinicalOverrideReason |
| SC_DeleteDate | date |  |  | SI | DeleteDate |
| SC_RowId | varchar |  |  | NO | - |
| SC_Score | varchar |  |  | SI | Score |
| SC_ScoringSystemIdentifier_DR | bigint |  | FK | SI | Des Ref Scoring System  |
| SC_UpdateDate | date |  |  | SI | UpdateDate |
| SC_UpdateTime | time |  |  | SI | UpdateTime |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*