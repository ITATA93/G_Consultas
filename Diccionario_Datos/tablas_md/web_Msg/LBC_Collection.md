# web_Msg.LBC_Collection

**Schema:** web_Msg
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCCOL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCOL_Comments | varchar |  |  | SI | Comments |
| LBCCOL_CreatedDate | date |  |  | SI | Created Date |
| LBCCOL_CreatedTime | time |  |  | SI | Created Time |
| LBCCOL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCOL_Owner | varchar |  |  | SI | Owner |
| LBCCOL_Priority | double |  |  | SI | Priority - the lowest value will be the default Sp... |
| LBCCOL_RowID | varchar |  |  | SI | - |
| LBCCOL_TestItem_DR | bigint |  | FK | SI | TestItem DR |
| LBCCOL_TestSetItem_DR | varchar |  | FK | SI | TestSetItem DR |
| LBCCOL_TestSet_DR | bigint |  | FK | SI | TestSet DR |
| LBCCOL_Type | varchar |  |  | SI | Type
Note: TS is TestSetRevision, TSI is TestSetR... |
| LBCCOL_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCOL_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCOL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*