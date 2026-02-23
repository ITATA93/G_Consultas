# SQLUser.RBC_Equipment

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EQ_RowId | bigint | PK |  | NO | - |
| EQ_AllowMultipleEventApps | varchar |  |  | SI | Allow multiple event appointments |
| EQ_Bed_DR | varchar |  | FK | SI | Inpatient Episode Bed |
| EQ_Code | varchar |  |  | NO | Code |
| EQ_CreatedDate | date |  |  | SI | Created Date |
| EQ_CreatedTime | time |  |  | SI | Created Time |
| EQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EQ_DateFrom | date |  |  | SI | Date From |
| EQ_DateTo | date |  |  | SI | Date To |
| EQ_Desc | varchar |  |  | NO | Description |
| EQ_EpisodeSubType_DR | bigint |  | FK | SI | Inpatient Episode Subtype |
| EQ_Group_DR | bigint |  | FK | SI | Des Ref Group |
| EQ_Outstation | varchar |  |  | SI | Outstation |
| EQ_UpdatedDate | date |  |  | SI | Updated Date |
| EQ_UpdatedTime | time |  |  | SI | Updated Time |
| EQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| EQ_Ward_DR | bigint |  | FK | SI | Inpatient Episode Ward |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*