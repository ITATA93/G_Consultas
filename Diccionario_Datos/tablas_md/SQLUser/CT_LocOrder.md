# SQLUser.CT_LocOrder

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORDER_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| ChildQ88DR | - |  |  | SI | Child Reference: Femostop Deflation |
| ORDER_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| ORDER_Childsub | double |  |  | NO | Childsub |
| ORDER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORDER_CreatedDate | date |  |  | SI | Created Date |
| ORDER_CreatedTime | time |  |  | SI | Created Time |
| ORDER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORDER_DateFrom | date |  |  | SI | Date  From |
| ORDER_DateTo | date |  |  | SI | Date To |
| ORDER_EpisodeType | varchar |  |  | SI | Episode Type |
| ORDER_RowId | varchar |  |  | NO | - |
| ORDER_TriggerEvent | varchar |  |  | SI | Trigger Event |
| ORDER_UpdatedDate | date |  |  | SI | Updated Date |
| ORDER_UpdatedTime | time |  |  | SI | Updated Time |
| ORDER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q85Q1 | - |  |  | SI | Time |
| Q85Q2 | - |  |  | SI | mls |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*