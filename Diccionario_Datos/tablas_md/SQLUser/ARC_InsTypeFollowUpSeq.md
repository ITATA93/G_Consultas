# SQLUser.ARC_InsTypeFollowUpSeq

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FOLUPSEQ_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| ChildQ82DR | - |  |  | SI | Child Reference: VULVA |
| FOLUPSEQ_Childsub | double |  |  | NO | Childsub |
| FOLUPSEQ_CreatedDate | date |  |  | SI | Created Date |
| FOLUPSEQ_CreatedTime | time |  |  | SI | Created Time |
| FOLUPSEQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FOLUPSEQ_FollowUpStage_DR | bigint |  | FK | SI | Des Ref FollowUpStage |
| FOLUPSEQ_NumberOfDays | double |  |  | SI | Number of days from the previous stage |
| FOLUPSEQ_ReportText | varchar |  |  | SI | Report Text |
| FOLUPSEQ_RowId | varchar |  |  | NO | - |
| FOLUPSEQ_Sequence | double |  |  | SI | Sequence |
| FOLUPSEQ_TaskAssignedGroup_DR | bigint |  | FK | SI | Des Ref to CTTaskAssignGroup |
| FOLUPSEQ_TaskAssignedUser_DR | bigint |  | FK | SI | Des Ref to SSUser |
| FOLUPSEQ_Task_DR | bigint |  | FK | SI | Des Ref epr.Task |
| FOLUPSEQ_UpdatedDate | date |  |  | SI | Updated Date |
| FOLUPSEQ_UpdatedTime | time |  |  | SI | Updated Time |
| FOLUPSEQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q64Q1 | - |  |  | SI | Edad aproximada (años) |
| Q64Q2 | - |  |  | SI | Tipo de resultado |
| Q64Q3 | - |  |  | SI | Duración aproximada (semanas) |
| Q64Q4 | - |  |  | SI | Resultado Perinatal |
| Q64Q5 | - |  |  | SI | Descripción |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*