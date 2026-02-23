# SQLUser.PA_Questionnaire

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUE_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| QUE_Adm_DR | bigint |  | FK | SI | Des Ref Adm |
| QUE_Childsub | double |  |  | NO | Childsub |
| QUE_ComputedScore | varchar |  |  | SI | Computed Score |
| QUE_Date | date |  |  | SI | Date |
| QUE_RowId | varchar |  |  | NO | - |
| QUE_Time | time |  |  | SI | Time |
| QUE_UserWindow_DR | bigint |  | FK | SI | Des REf UserWindow |
| QUE_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*