# SQLUser.PAC_Ward

**Schema:** SQLUser
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WARD_RowID | bigint | PK |  | NO | - |
| ChildQ21DR | - |  |  | SI | Child Reference: Manoeuvres / Actions performed |
| Q10Q1 | - |  |  | SI | Name |
| Q10Q2 | - |  |  | SI | Role |
| Q10Q3 | - |  |  | SI | Presence |
| Q10Q4 | - |  |  | SI | Arrival time |
| Q10Q5 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| WARD_Active | varchar |  |  | SI | Active Flag |
| WARD_Code | varchar |  |  | NO | Ward Code  |
| WARD_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| WARD_CreatedDate | date |  |  | SI | Created Date |
| WARD_CreatedTime | time |  |  | SI | Created Time |
| WARD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WARD_Desc | varchar |  |  | NO | Ward Description |
| WARD_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| WARD_IgnoreTempLoc | varchar |  |  | SI | IgnoreTempLoc  |
| WARD_InactiveDateFrom | date |  |  | SI | Inactive Date From |
| WARD_InactiveDateTo | date |  |  | SI | Inactive Date To |
| WARD_InactiveTimeFrom | time |  |  | SI | Inactive Time From |
| WARD_InactiveTimeTo | time |  |  | SI | Inactive Time To |
| WARD_LocationDR | bigint |  | FK | SI | Location |
| WARD_RoomDR | bigint |  | FK | SI | Ward_RoomDR |
| WARD_SingleRoom | varchar |  |  | NO | Single Room |
| WARD_UpdatedDate | date |  |  | SI | Updated Date |
| WARD_UpdatedTime | time |  |  | SI | Updated Time |
| WARD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WARD_ViewLinkedRooms | varchar |  |  | SI | View Linked Rooms |
| WARD_ViewNextMostUrgent | varchar |  |  | SI | View Next Most Urgent |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*