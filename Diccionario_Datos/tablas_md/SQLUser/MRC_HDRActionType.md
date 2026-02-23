# SQLUser.MRC_HDRActionType

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HDRAT_RowId | bigint | PK |  | NO | - |
| HDRAT_Code | varchar |  |  | SI | Code |
| HDRAT_CreatedDate | date |  |  | SI | Created Date |
| HDRAT_CreatedTime | time |  |  | SI | Created Time |
| HDRAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HDRAT_DateField | varchar |  |  | SI | Date Field |
| HDRAT_DefaultWorkFlow_DR | bigint |  | FK | SI | Default Workflow ID |
| HDRAT_Desc | varchar |  |  | SI | Description |
| HDRAT_JS | varchar |  |  | SI | URL |
| HDRAT_TimeField | varchar |  |  | SI | Time Field |
| HDRAT_URL | varchar |  |  | SI | URL |
| HDRAT_UpdatedDate | date |  |  | SI | Updated Date |
| HDRAT_UpdatedTime | time |  |  | SI | Updated Time |
| HDRAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q11Q1 | - |  |  | SI | Lugar del Dolor |
| Q11Q2 | - |  |  | SI | Cronología: Duración/Temporalidad |
| Q11Q3 | - |  |  | SI | Topografía: Localización |
| Q11Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*