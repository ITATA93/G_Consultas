# SQLUser.PAC_Room

**Schema:** SQLUser
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROOM_RowID | bigint | PK |  | NO | - |
| Q03Q1 | - |  |  | SI | Source(s) |
| Q03Q2 | - |  |  | SI | Confirmed by |
| Q03Q3 | - |  |  | SI | Date |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| ROOM_Code | varchar |  |  | NO | Room Code |
| ROOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ROOM_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| ROOM_CreatedDate | date |  |  | SI | Created Date |
| ROOM_CreatedTime | time |  |  | SI | Created Time |
| ROOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROOM_DateFrom | date |  |  | SI | Date From |
| ROOM_DateTo | date |  |  | SI | Date To |
| ROOM_Desc | varchar |  |  | NO | Room Description |
| ROOM_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| ROOM_DifferentSexPatients | varchar |  |  | SI | Different Sex Patients in Room |
| ROOM_Incompletes | varchar |  |  | SI | Incompletes |
| ROOM_NoOfRows | varchar |  |  | SI | No Of Rows |
| ROOM_OTAgeFrom | double |  |  | SI | OT Location Age Restriction From |
| ROOM_OTAgeTo | double |  |  | SI | OT Location Age Restriction To |
| ROOM_OTSex | varchar |  |  | SI | OT Location Sex Restriction  |
| ROOM_OrderByCalcRankPriority | varchar |  |  | SI | Order By Calculated Rank Priority |
| ROOM_OrderByPriority | varchar |  |  | SI | Order By Priority |
| ROOM_Owner | varchar |  |  | SI | Owner |
| ROOM_Query | varchar |  |  | SI | Query |
| ROOM_RoomType_DR | bigint |  | FK | NO | Room Type des ref |
| ROOM_SinglePatient | varchar |  |  | SI | Single Patient Only |
| ROOM_TotalNotInBed | varchar |  |  | SI | TotalNotInBed |
| ROOM_UpdatedDate | date |  |  | SI | Updated Date |
| ROOM_UpdatedTime | time |  |  | SI | Updated Time |
| ROOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*