# SQLUser.RTC_MRecordType

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TYP_RowId | bigint | PK |  | NO | - |
| TYP_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| TYP_Code | varchar |  |  | NO | Code |
| TYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TYP_Counter | double |  |  | SI | Counter |
| TYP_CreatedDate | date |  |  | SI | Created Date |
| TYP_CreatedTime | time |  |  | SI | Created Time |
| TYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TYP_DateFrom | date |  |  | SI | Date From |
| TYP_DateTo | date |  |  | SI | Date To |
| TYP_Desc | varchar |  |  | NO | Description |
| TYP_Length | double |  |  | SI | Length |
| TYP_MRNoPolicy | varchar |  |  | SI | MR No Policy |
| TYP_NotCreateVolume | varchar |  |  | SI | Do Not Create Volume |
| TYP_Owner | varchar |  |  | SI | Owner |
| TYP_Pref | varchar |  |  | SI | Prefix |
| TYP_Suf | varchar |  |  | SI | Suffix |
| TYP_UpdatedDate | date |  |  | SI | Updated Date |
| TYP_UpdatedTime | time |  |  | SI | Updated Time |
| TYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| TYP_VolumeType | varchar |  |  | SI | Volume Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*