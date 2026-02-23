# SQLUser.PAC_RefTemplateStageNext

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NX_ParRef | varchar | PK |  | NO | PAC_RefTemplate Parent Reference |
| NX_Childsub | double |  |  | NO | Childsub |
| NX_CreatedDate | date |  |  | SI | Created Date |
| NX_CreatedTime | time |  |  | SI | Created Time |
| NX_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NX_RowId | varchar |  |  | NO | - |
| NX_Stage_DR | varchar |  | FK | SI | Des Ref PACRefTemplateStage |
| NX_UpdatedDate | date |  |  | SI | Updated Date |
| NX_UpdatedTime | time |  |  | SI | Updated Time |
| NX_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q32Q1 | - |  |  | SI | Date |
| Q32Q2 | - |  |  | SI | Time |
| Q32Q3 | - |  |  | SI | Indication for line change |
| Q32Q4 | - |  |  | SI | Other indication for PD line change |
| Q32Q5 | - |  |  | SI | Next line change due |
| Q32Q6 | - |  |  | SI | Line change notes |
| Q32Q7 | - |  |  | SI | Changed by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*