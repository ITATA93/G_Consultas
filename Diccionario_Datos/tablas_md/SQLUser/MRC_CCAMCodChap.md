# SQLUser.MRC_CCAMCodChap

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CHAP_RowId | bigint | PK |  | NO | - |
| CHAP_Code | varchar |  |  | NO | Code |
| CHAP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CHAP_CreatedDate | date |  |  | SI | Created Date |
| CHAP_CreatedTime | time |  |  | SI | Created Time |
| CHAP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CHAP_DateFrom | date |  |  | SI | Date From |
| CHAP_DateTo | date |  |  | SI | Date To |
| CHAP_Desc | varchar |  |  | NO | Description |
| CHAP_Owner | varchar |  |  | SI | Owner |
| CHAP_UpdatedDate | date |  |  | SI | Updated Date |
| CHAP_UpdatedTime | time |  |  | SI | Updated Time |
| CHAP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ32DR | - |  |  | SI | Child Reference: Tipo de aborto |
| Q171Q1 | - |  |  | SI | Hallazgo |
| Q171Q2 | - |  |  | SI | Ubicación |
| Q171Q3 | - |  |  | SI | Sensibilidad |
| Q171Q4 | - |  |  | SI | Descripción |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*