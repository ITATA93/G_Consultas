# SQLUser.RBC_OutcomeOfAppointStage

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STOPST_ParRef | bigint | PK |  | NO | RBC_OutcomeOfAppoint Parent Reference |
| STOPST_Childsub | double |  |  | NO | Childsub |
| STOPST_CreatedDate | date |  |  | SI | Created Date |
| STOPST_CreatedTime | time |  |  | SI | Created Time |
| STOPST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STOPST_RowId | varchar |  |  | NO | - |
| STOPST_StageStop_DR | bigint |  | FK | SI | Des Ref PACRefTemplateStageType |
| STOPST_UpdatedDate | date |  |  | SI | Updated Date |
| STOPST_UpdatedTime | time |  |  | SI | Updated Time |
| STOPST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*