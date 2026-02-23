# SQLUser.ARC_DepTypeByRoom

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROOM_ParRef | bigint | PK |  | NO | ARC_DepType Parent Reference |
| Q46Q1 | - |  |  | SI | Pulso |
| Q46Q2 | - |  |  | SI | lateralidad |
| Q46Q3 | - |  |  | SI | Hallazgos |
| Q46Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| ROOM_Childsub | double |  |  | NO | Childsub |
| ROOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ROOM_CreatedDate | date |  |  | SI | Created Date |
| ROOM_CreatedTime | time |  |  | SI | Created Time |
| ROOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROOM_DateFrom | date |  |  | NO | Date From |
| ROOM_DateTo | date |  |  | SI | Date To |
| ROOM_DefDepositAmt | double |  |  | SI | DefDepositAmt |
| ROOM_RoomType_DR | bigint |  | FK | SI | Des Ref PACRoomType |
| ROOM_RowId | varchar |  |  | NO | - |
| ROOM_UpdatedDate | date |  |  | SI | Updated Date |
| ROOM_UpdatedTime | time |  |  | SI | Updated Time |
| ROOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*