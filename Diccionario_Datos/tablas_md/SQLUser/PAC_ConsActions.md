# SQLUser.PAC_ConsActions

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONSACT_RowId | bigint | PK |  | NO | - |
| CONSACT_Code | varchar |  |  | NO | Code |
| CONSACT_CreatedDate | date |  |  | SI | Created Date |
| CONSACT_CreatedTime | time |  |  | SI | Created Time |
| CONSACT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONSACT_Desc | varchar |  |  | NO | Description |
| CONSACT_URL | varchar |  |  | SI | URL |
| CONSACT_UpdatedDate | date |  |  | SI | Updated Date |
| CONSACT_UpdatedTime | time |  |  | SI | Updated Time |
| CONSACT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q10Q1 | - |  |  | SI | Review date |
| Q10Q2 | - |  |  | SI | Screening status |
| Q10Q3 | - |  |  | SI | Review notes |
| Q10Q4 | - |  |  | SI | Reviewed by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*