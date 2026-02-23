# SQLUser.LBC_Altitude

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCALT_RowID | bigint | PK |  | NO | - |
| LBCALT_Code | varchar |  |  | NO | Code |
| LBCALT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCALT_CreatedDate | date |  |  | SI | Created Date |
| LBCALT_CreatedTime | time |  |  | SI | Created Time |
| LBCALT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCALT_DateFrom | date |  |  | SI | From Date |
| LBCALT_DateTo | date |  |  | SI | To Date |
| LBCALT_Desc | varchar |  |  | NO | Description |
| LBCALT_Owner | varchar |  |  | SI | Owner |
| LBCALT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCALT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCALT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q11Q1 | - |  |  | SI | Temas Prioritarios |
| Q11Q2 | - |  |  | SI | Registro de la Actividad |
| Q11Q3 | - |  |  | SI | Registrado por |
| Q11Q4 | - |  |  | SI | Fecha |
| Q11Q5 | - |  |  | SI | Hora |
| Q11Q6 | - |  |  | SI | CESFAM |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*